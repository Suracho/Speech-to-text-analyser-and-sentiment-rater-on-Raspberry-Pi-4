import speech_recognition as sr
from textblob import TextBlob
import time
import Adafruit_CharLCD as lcd

with sr.Microphone() as source:
    try:
        lcd.message("Speak Anything: ")
        print("Speak Anything :")
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source,timeout=20)
        print(audio)
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        a = TextBlob(text)
        m=a.sentiment.polarity
        m+=1
        m*=50
        print(" ",int(m))
    except:
        print("Sorry could not recognize what you said")

