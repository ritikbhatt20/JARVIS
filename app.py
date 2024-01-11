from core import listen_fn
from core import weather
from core import translate
from core import curr_convertor
import pyttsx3
import webbrowser
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

        
def respond(query):
    if "hello" in query:
        speak("Hello! How can I help you today?")

    elif "open google" in query:
        speak("Opening Google.")
        webbrowser.open('https://www.google.com')

    elif "open youtube" in query:
        speak("Opening Youtube.")
        webbrowser.open('https://www.youtube.com')

    elif "weather" in query or "weather update" in query:
        text = weather.weather_data()
        speak(text)

    elif "translate" in query:
        translate.translate()

    elif "what is the time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")  # Get current time
        speak(f"The current time is {current_time}.")
        
    elif "currency" in query or "convert" in query:  # Adjust the trigger words as needed
        speak("Sure, please provide me the amount you want to convert to.")
        user_input = listen_fn.listen()
    
        if user_input:
            words = user_input.split()
            amount = float(words[1])  # Extracts the amount
        
            converted_amount = curr_convertor.currency_conversion(amount, "USD", "INR")
            speak(f"{amount} US dollars is approximately {converted_amount:.2f} Indian Rupees")

    elif "thank you" in query or "thankyou" in query:
        speak("Your welcome! How can I assist you further?")

    elif "goodbye" in query or "good bye" in query:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    while True:
        user_input = listen_fn.listen()
        if user_input:
            respond(user_input)
