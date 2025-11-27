import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser

engine = pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def search(query):
    query=query.strip().lower()
    if "google" in query or "search" in query:
        import wikipedia as googleScrap
        query= query.replace("jarvis","")
        query= query.replace("google","")
        query= query.replace("search","")
        speak("this is what i found on google")
        try:
            pywhatkit.search(query)
            result= googleScrap.summary(query,1)
            speak(result)
        except:
            speak("sorry no answer availaable")

    elif "youtube" in query:
        speak("here's your youtube video")
        query= query.replace("youtube","")
        query= query.replace("jarvis","")
        web= "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        speak("its done sir")
        

    elif "wikipedia" in query or "information" in query:
        speak("searching from wikipedia")
        query= query.replace("wikipedia","")
        query= query.replace("search","")
        query= query.replace("jarvis","")
        try:
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")     
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("The topic is too broad. Please be more specific.")
            print(f"DisambiguationError: {e}")
        except wikipedia.exceptions.PageError:
            speak("Sorry, no page found on Wikipedia for this query.")
            print("Page not found.")
        except Exception as e:
            speak("An error occurred while searching Wikipedia.")
            print(f"Error: {e}")
