#our main file.

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json

#speech syntesis
engine = pyttsx3.init()


engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()


model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(8192)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
   
        print(text)
        speak(text)