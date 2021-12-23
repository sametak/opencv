import numpy as np
import cv2
import time
from gtts import gTTS
import random
from playsound import playsound
import os

car_cascade = cv2.CascadeClassifier('cars.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)

def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


        
while(True):
    ret, frame = capture.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayFrame, 1.1, 4)
    arabalar = car_cascade.detectMultiScale(frame,1.3,3)


    if len(arabalar) == 0:
        speak("Hiç Araç Yok")
        time.sleep(5)

    else:
        speak("Tanımlanan Araç Sayısı: " + str(arabalar.shape[0]))
        time.sleep(5)
    if len(faces) == 0:
        speak( "hiç insan yok" ,)
        time.sleep(5)
    else:
        speak("Tanımlanan İnsan Sayısı: " + str(faces.shape[0]))
        time.sleep(3)

        if (cv2.waitKey(1) == 27):
            break


capture.release()
cv2.destroyAllWindows()
speak('hoş geldiniz')