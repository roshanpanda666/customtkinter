from playsound import playsound
def play1():
    print("playing sound")
    playsound('cal/sound.wav')

def click():
    print("playing sound click")
    playsound('cal/uiclick.mp3')

def resultsound():
    print("playing sound result")
    playsound('cal/resultt.mp3')

if __name__=="__main__":
    play1(),click(),resultsound()