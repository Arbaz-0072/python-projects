import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
import os
import datetime
import pyautogui
import random
import time

engine = pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listenning.....")
        r.adjust_for_ambient_noise(source, duration=1)
        audio= r.listen(source,phrase_time_limit=5)
    try:
        query= r.recognize_google(audio,language='eng-in')
        print(f"you said {query}\n")
    except Exception as e:
        print("say again ")
        speak("say again ")
        return "None"
    return query

def alarm(query):
    timehere=open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("greetme.py")

def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<=18:
        speak("good afternoon ")
    else:
        speak("good evening ")
    speak("How can i help?")

if __name__=="__main__":
    greetme()
    while True:
        query= takeCommand().lower()
        if "go to sleep" in query:
            speak("ok sir,you can call me anytime")
            exit()
        elif "hello" in query:
            speak("hello sir ,how are you?")
        elif "how are you" in query:
            speak("i am fine,what about you sir?")
        elif "i am fine" in query:
            speak("that's great hehehehe")
        elif "thank you" in query:
            speak("you are welcome") 
        elif "what is your name" in query or "what's your name" in query:
            speak("my name is jarvis,your AI assistant")
        elif "time" in query:
            timenow = datetime.datetime.now().strftime("%H:%M")   
            speak("now the time is"+timenow)

        elif "close VS code" in query or "close visual studio" in query:
            speak("closing VS code")
            pyautogui.hotkey("alt","f4")
        elif "open" in query or "start" in query:
            from openclose import openappweb
            openappweb(query)
        elif "close" in query:
            from openclose import closeappweb
            closeappweb(query)
        elif "google" in query or "search" in query or "youtube" in query or "wikipedia" in query:
            from search import search
            search(query)    
        
        elif "shutdown" in query or "shut down" in query:
            speak("are you sure to shut down?")
            shut=input("are you sure?Yes/No: ")
            if shut=="yes":
                speak("shuting down")
                os.system("shutdown /s /t 1")
            else:
                break
        
        elif "play game" in query or "play a game" in query or "can you play" in query:
            speak("yess i can play with you")
            speak("lets start the game..")
            from game import game
            game()

        # --------------video-----------------
        elif "pause" in query or "wait" in query or "stop" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "play" in query or "resume" in query or "start" in query:
            pyautogui.press("k")  
            speak("video started")
        elif "mute" in query or "turn of"in query:
            pyautogui.press("m")
            speak("muted")
        elif "volume up" in query or "up" in query:
            for i in range(5):
                pyautogui.press("volumeup")
        elif "volume down" in query or "down" in query:
            for i in range(5):
                pyautogui.press("volumedown")          
        elif "bored" in query or "tired" in query or "feeling bad" in query or "boring" in query or"play for me" in query:
            speak("playing song for you:")
            a= (1,2,3)
            b= random.choice(a)
            if b==1:
                webbrowser.open("https://youtu.be/SDpqVXOINlI?si=wNt5_lU7G08YQcQ3")
            if b==2:
                webbrowser.open("https://youtu.be/8OkpRK2_gVs?si=cKmA5eSZQc0AvuF0")
            if b==3:
                webbrowser.open("https://youtu.be/nAksM2HAAqo?si=8PIq_iRZ8byyt1tp")



        elif "alarm" in query or "set alarm" in query:
            speak("set your alarm")
            alr=input("please tell me the time:")
            alarm(alr)
            speak("its done")
        
        elif "remember that" in query:
            query= query.replace("remember","")
            query= query.replace("that","")
            query= query.replace("jarvis","")
            rmsg=query
            speak("okk i will remember "+rmsg)
            rfile=open("remembermesseges.txt","w")
            rfile.write(rmsg)
            rfile.close()
        elif "what do you remember" in query or "what you remember" in query:
            remmsg= open("remembermesseges.txt","r")
            speak("yess i know that "+remmsg.read())    
        
        elif "calculate" in query:
            from calcy import calcylator
            calcylator(query)

        elif "whatsapp" in query or "whats app" in query or "send message" in query or "send a messege" in query:
            from sendmsg import sendmsg
            sendmsg()

        elif "screenshot" in query or "screen shot" in query:
            speak("taking screenshot")
            scr=pyautogui.screenshot()
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"C:\\Users\\ARBAZ\\Pictures\\Screenshots\\screenshot_{timestamp}.jpg"
            scr.save(filename)

        elif "click my photo" in query or "take my photo" in query or"take photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("smile please")
            pyautogui.press("enter")

                


        
        
                

