import os
import pyttsx3
import pyautogui
import webbrowser
from time import sleep

engine = pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp={
    "cmd":"cmd","paint":"paint","word":"winword","excel":"excel","brave":"brave",
    "chrome":"chrome","powerpoint":"powerpoint","roblox":"roblox"
}

def openappweb(query):
    query=query.strip().lower()
    speak("opening")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query= query.replace("open","")
        query= query.replace("jarvis","")
        query= query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys= list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    query= query.lower().strip()
    speak("closing")
    keys=list(dictapp.keys())
    for app in keys:
        if app in query:
            os.system(f"taskkill /f /im {dictapp[app]}.exe")

    






