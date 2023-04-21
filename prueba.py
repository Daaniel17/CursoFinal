import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

engine=pyttsx3.init()
for voz in engine.getProperty("voices"):
    print(voz)
