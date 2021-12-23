import numpy as np
import cv2
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

car_cascade = cv2.CascadeClassifier('../cars.xml')
face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)

r = sr.Recognizer()

def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.RequestError:
            speak('sistem çalışmıyor')
        return voice
    
def response(voice):
    if 'hey asistan' in voice:    
        if 'insan say' in voice:
            while True:
                ret, image = capture.read()
                grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(grayImage, 1.1, 4)

            
                if len(faces) == 0:
                    speak( "hiç insan yok" ,)
                    time.sleep(5)  
                else:
                    speak("Tanımlanan İnsan Sayısı: " + str(faces.shape[0]))
                    time.sleep(5)


                if (cv2.waitKey(1) == 27):


                        break
            capture.release()
            cv2.destroyAllWindows()
        if 'arac say' in voice:
            while True:
                ret,frame= capture.read()

                arabalar = car_cascade.detectMultiScale(frame,1.3,3)
                
                if len(arabalar) == 0:
                    speak()
                else:
                    speak("Tanımlanan Araç Sayısı: " + str(arabalar.shape[0]))
                    break
        if 'bana bir hikaye anlat' in voice:
            speak('bir varmış bir yokmuş bir adam varmış ölmüş sj')

        if 'saat kaç' in voice:
            speak(datetime.now().strftime('%H:%M:%S'))
        if 'arama yap' in voice:
            search = record('ne aramak istiyorsun')
            url = 'https://google.com/search?q='+search
            webbrowser.get().open(url)
            speak(search + 'için bulduklarım')
        if 'tamamdır' in voice:
            speak('görüşürüz')
            exit()
        
speak('nasıl yardımcı olabilirim')

while 1:
    voice = record()
    print(voice)
    response(voice)