import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)
def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    print("listening")
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
