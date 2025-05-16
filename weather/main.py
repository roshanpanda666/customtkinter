import customtkinter as ctk
import requests
from bs4 import BeautifulSoup

def get_weather_data():
    city = city_entry.get().strip().lower().replace(" ", "-")
    weather_url = f"https://www.timeanddate.com/weather/india/{city}"
    aqi_url = f"https://aqicn.org/city/india/{city}/"

    try:
        # Weather scraping
        weather_response = requests.get(weather_url)
        soup = BeautifulSoup(weather_response.text, "html.parser")

        temp_div = soup.find("div", class_="h2")
        desc_p = soup.find("p")
        uv_div = soup.find("div", class_="small")

        temp = temp_div.text.strip() if temp_div else "N/A"
        desc = desc_p.text.strip() if desc_p else "N/A"
        uv = uv_div.text.strip() if uv_div else "UV not found"

        # AQI scraping
        aqi_response = requests.get(aqi_url)
        aqi_soup = BeautifulSoup(aqi_response.text, "html.parser")
        aqi_value_div = aqi_soup.find("div", {"id": "aqiwgtvalue"})
        aqi_value = aqi_value_div.text.strip() if aqi_value_div else "N/A"

        # Go-out logic
        uv_index = int(''.join(filter(str.isdigit, uv.split()[0]))) if any(char.isdigit() for char in uv) else 0
        aqi_int = int(aqi_value) if aqi_value.isdigit() else 0

        if aqi_int <= 100 and uv_index <= 5:
            advice = "✅ You can go out safely!"
        else:
            advice = "⚠️ Not safe to go out (Bad air or high UV)"

        # Update UI
        temp_label.configure(text=f"🌡 Temp: {temp}")
        desc_label.configure(text=f"🌥 {desc}")
        uv_label.configure(text=f"🔆 {uv}")
        aqi_label.configure(text=f"🫁 AQI: {aqi_value}")
        advice_label.configure(text=advice)

    except Exception as e:
        temp_label.configure(text="❌ Error")
        desc_label.configure(text="")
        uv_label.configure(text="")
        aqi_label.configure(text="")
        advice_label.configure(text=f"Something went wrong!\n{e}")

# --- GUI Setup ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("600x400")
root.title("Advanced Weather App ☁️🌡🫁")

main_frame = ctk.CTkFrame(root)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Title
title_label = ctk.CTkLabel(main_frame, text="🌤️ Weather & Air Check", font=("Arial", 22))
title_label.pack(pady=10)

# Input
city_entry = ctk.CTkEntry(main_frame, placeholder_text="Enter Indian city (e.g., Bhubaneswar)")
city_entry.pack(pady=10, fill="x", padx=40)

get_button = ctk.CTkButton(main_frame, text="Get Data", command=get_weather_data)
get_button.pack(pady=10)

# Grid for data
data_frame = ctk.CTkFrame(main_frame)
data_frame.pack(pady=20, padx=20, fill="x", expand=True)

# Labels inside the grid
temp_label = ctk.CTkLabel(data_frame, text="", font=("Arial", 16))
desc_label = ctk.CTkLabel(data_frame, text="", font=("Arial", 16))
uv_label = ctk.CTkLabel(data_frame, text="", font=("Arial", 16))
aqi_label = ctk.CTkLabel(data_frame, text="", font=("Arial", 16))
advice_label = ctk.CTkLabel(main_frame, text="", font=("Arial", 18))

# Arrange data side-by-side using grid
temp_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
desc_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
uv_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
aqi_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
advice_label.pack(pady=10)

root.mainloop()
