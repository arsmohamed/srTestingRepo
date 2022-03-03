import os 
import time
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS



def speak(text):
    tts = gTTS(text=text, lang='en') # tranform the text into audioFile
    filename = "testing.wav" 
    tts.save(filename)
    playsound(filename)
speak("lets see")
# playsound('test.mp3')