import requests
import json
import pyttsx3

city = input()

URL = f"http://api.weatherapi.com/v1/current.json?key=c15b7ec3b7d04fb083433530231112&q={city}"

r = requests.get(URL)
# print(r.text)
Wdict = json.loads(r.text)
w = Wdict["current"]["temp_c"]
s = Wdict["current"]["wind_kph"]

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


sentence = speak(f"The current weather in {city} is {w} and the speed of wind is {s} Kilo Per Hour")
print(sentence)
