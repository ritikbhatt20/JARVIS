from googletrans import Translator
from app import speak
from core import listen_fn

translator = Translator()

def translate():
    speak("Sure, please say the phrase you want to translate.")
    phrase = listen_fn.listen()
    if phrase:
        try:
            translation = translator.translate(phrase, dest='fr')  # Translate to French (you can change 'fr' to any language code)
            speak(f"The translated phrase is: {translation.text}")
        except Exception as e:
            print("Translation error:", e)
            speak("Sorry, I couldn't translate the phrase.")
    
