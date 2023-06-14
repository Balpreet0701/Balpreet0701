import pyttsx3
import pyaudio
import speech_recognition as sr
import nltk

spEng= pyttsx3.init()
spEng.setProperty('rate',100)   #to set the speed of saying

spEng.say('Hi how are you is everything fine')
spEng.runAndWait()

recognizer=sr.Recognizer()

#to record from mike   and will reply by speaking
with sr. Microphone() as mic:
    print('Say:',end=' ')
    audio=recognizer.listen(mic,timeout=1,phrase_time_limit=5)  #phraselimit is used for teh length of speech
    try:
        text=recognizer.recognize_google(audio)
        print(text)
        spEng.say(text)
        spEng.runAndWait()
    except Exception as err:
        print('\n Could not recognize')