#our main file.

import speech_recognition as sr

#create a recognizer 
r = sr.Recognizer()

#open the MIC for capture
with sr.Microphone() as source:
    
    audio = r.listen(source) #define mic as a audio font

    print(r.recognize_google(audio, language='pt'))