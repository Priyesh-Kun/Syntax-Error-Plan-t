from django.shortcuts import render
import speech_recognition as sr
from os import path 

# Create your views here.
def voice_to_text():
    audio_file = path.join(path.dirname(path.realpath('Recording.wav')),'Recording.wav')
    recog = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        input = recog.record(source)
    try:
        text = recog.recognize_google(input,language='en-in')
    except Exception:
        print("Error")
        return 0
    return text