import speech_recognition as sr 
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        
        except sr.RequestError:
            print("Sorry, I'm having trouble recognizing your speech.")
            return ""
        
def respond(query):
    if "hello" in query:
        speak("Hello! How can I help you today?")

    elif "open google" in query:
        webbrowser.open('https://www.google.com')
        speak("Opening Google.")

    elif "what is the time" in query:
        # You can implement time-related functionality here
        # For example: datetime.datetime.now().strftime("%I:%M %p")
        speak("I'm sorry, I cannot provide the current time.")

    elif "goodbye" in query:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input:
            respond(user_input)
