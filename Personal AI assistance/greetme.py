import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

with open("Alarmtext.txt", "rt") as extractedtime:
    time = extractedtime.read()

def ring(time):
    timeset=str(time)
    timenow=timeset.replace("jarvis","")
    timenow=timenow.replace("set alarm","")
    timenow=timenow.replace(" and ",":")
    timenow=timenow.replace(" ",":")
    Alarmtime= str(timenow)
    print(Alarmtime)
    while True:
        currenttime= datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime==Alarmtime:
            speak("Alarm ringing")
            os.startfile("potcalarm.mp3")
            with open("Alarmtext.txt", "w") as file:
                file.write("")
            break
ring(time)           

         
