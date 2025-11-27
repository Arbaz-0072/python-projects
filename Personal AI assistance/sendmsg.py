import pyttsx3
import pywhatkit
import os
import webbrowser
import datetime
from time import sleep
from datetime import datetime,timedelta



engine = pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendmsg():
    speak("which person")
    a= int(input("1-Me\n2-Umair\n3-zeeshan\nenter number:"))
    speak("tell me whats your messege")
    msg= str(input("enter your messege:"))
    
    if a==1:
        speak("sending messege to you")
        pywhatkit.sendwhatmsg_instantly("+918450948009", msg, wait_time=10,tab_close=True)

    elif a==2:
        speak("sending messege to your friend umair")
        pywhatkit.sendwhatmsg_instantly("+917020840184", msg, wait_time=10, tab_close=True)
    
    elif a==3:
        speak("sending messege to zeeshan bhai")
        pywhatkit.sendwhatmsg_instantly("+919920176567", msg, wait_time=10, tab_close=True)
sendmsg()