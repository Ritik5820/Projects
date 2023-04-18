import pyttsx3 

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

voice = engine.setProperty('voice',voices[2].id)


def speak(text): 
    engine.say(text)
    engine.runAndWait()


speak ('Hello')