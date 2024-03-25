import pyttsx3
import time


def timer():
    seconds = int(input("Time in seconds: "))
    text = input("Phrase: ")
    if text == "":
        text = "Time to chill!"
    engine = pyttsx3.init()
    engine.say(text)
    while seconds > 0:
        print(f"Time left: {seconds}")
        time.sleep(1)
        seconds -= 1
    print(text)
    engine.runAndWait()


timer()
