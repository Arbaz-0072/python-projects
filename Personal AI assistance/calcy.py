import pyttsx3

engine = pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def calcylator(query):
    query = query.lower()
    query = query.replace("plus", "+").replace("minus", "-")
    query = query.replace("into", "*").replace("multiply", "*").replace("multiplied", "*")
    query = query.replace("divided by", "/").replace("divide", "/")
    query = query.replace("power", "**").replace("^", "**")
    query = query.replace("calculate", "").strip()

    try:
        result = eval(query)
        print("Result:", result)
        speak(f"answer is{result}")
    except Exception as e:
        print("Error:", e)
        speak("Error",e)
        return None
