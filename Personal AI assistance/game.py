import pyttsx3
import random

engine = pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def game():
    myscore=0
    jarscore=0
    i= 0
    while(i<5):
        g=("rock","paper","scr")
        jarchoose= random.choice(g)
        mychoose= input("choose stone paper or scisors:")
        
        if mychoose not in g:
            speak("invalid")
            print("invalid ")
            continue
        elif jarchoose==mychoose:
            print(f"you:{mychoose}   jarvis:{jarchoose}")
            speak("game tie")
            print("game tie") 
            print(f"score:- Me:{myscore}  jar{jarscore}")   

        elif jarchoose=="rock" and mychoose=="scr":
            print(f"you:{mychoose}   jarvis:{jarchoose}")
            speak("jarvis won")
            print("jarvis won")
            jarscore+=1
            print(f"score:- Me:{myscore}  jar{jarscore}")

        elif jarchoose=="paper" and mychoose=="rock":
            print(f"you:{mychoose}   jarvis:{jarchoose}")
            speak("jarvis won")
            print("jarvis won")
            jarscore+=1
            print(f"score:- Me:{myscore}  jar{jarscore}")

        elif jarchoose=="scr" and mychoose=="paper":
            print(f"you:{mychoose}   jarvis:{jarchoose}")
            speak("jarvis won")
            print("jarvis won")
            jarscore+=1
            print(f"score:- Me:{myscore}  jar{jarscore}")

        else:
            print(f"you:{mychoose}   jarvis:{jarchoose}")
            speak("you won")
            print("you won")
            myscore+=1
            print(f"score:- Me:{myscore}  jar{jarscore}")
        
        if i<4:
            print()
        i=i+1
        
    if jarscore>myscore:
        speak("yesss i won the game hehehehehee")
        print("yesss i won the game\n")
    elif myscore>jarscore:
        speak("ohh no you won the game")
        print("you won the game\n")    
    else:
        speak("the game is finally tie")
        print("the game is finally tie\n")

    speak("do you want to play again?say yes or no")
    pagain=input("yes/no:")
    if pagain=="yes":
        game()