import speech_recognition as sr 

recognizer = sr.Recognizer()

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