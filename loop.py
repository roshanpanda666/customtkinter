import time
from sound import play
def print_hello_world():
    for i in range(10):
        print("hello world", i)
        time.sleep(0.6)
    print("yaaaaaaaaaaaaaaaaa")
    play()
    

if __name__ == "__main__":
    print_hello_world()