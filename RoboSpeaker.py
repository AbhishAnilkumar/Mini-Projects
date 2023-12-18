import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        user_input = input("What do you want me to speak: ")
        if user_input == "q":
            break
        speak(user_input)
