import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    print("how can a help you Aditya, sir")
    speak("how can a help you Aditya, sir")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except sr.UnknownValueError:
        return "Sorry, I cannot understand"
    except sr.RequestError:
        return "Sorry, I cannot understand"
    return query
if __name__ == "__main__":
    while True:
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            print(results)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
            print(strTime)


