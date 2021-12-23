import numpy as np
import cv2
import speech_recognition as sr
import time
from gtts import gTTS
from playsound import playsound
import random
import os

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
            speak('kanka sesin gelmiyor')
        except sr.RequestError:
            speak('beynim yandı knk')
        return voice
    
def response(voice):
    if 'hey arkadaşım' in voice:    
        soru = record('efendim knk ha buarada taş kağıt makas oynayalım mı')
        if soru == 'tamam':           
            secenek=["taş","kağıt","makas"]
            tas = secenek[0]
            kagit = secenek[1]
            makas = secenek[2]
            seçim = record('taş mı kağıt mı makas mı unutma seni göremiyorum')
            arkadasin_secimi=random.choice(secenek)
            if seçim == 'taş':
                if arkadasin_secimi == tas:
                    speak('Bende taş demiştim berabere kaldık')
                elif arkadasin_secimi == kagit:
                    speak('ha ha kanka ben kağıt yapmıştım eziyorum seni he')
                elif arkadasin_secimi == makas:
                    speak('vallaha ballı çıktın ben makas yapmışdım') 
            if seçim == 'kağıt':
                if arkadasin_secimi == kagit:
                    speak('Bende kağıt demiştim berabere kaldık')
                elif arkadasin_secimi == makas:
                    speak('ha ha kanka ben makas yapmıştım eziyorum seni he')
                elif arkadasin_secimi == tas:
                    speak('vallaha ballı çıktın ben taş yapmıştım')
            if seçim == 'makas':
                if arkadasin_secimi == makas:
                    speak('Bende makas demiştim berabere kaldık')
                elif arkadasin_secimi == tas:
                    speak('ha ha kanka ben taş yapmıştım eziyorum seni he')
                elif arkadasin_secimi == kagit:
                    speak('vallaha ballı çıktın ben kağıt yapmışdım')
            speak('ben sıkıldım hadi bay bay')
            exit()
        if soru == 'hayır':
            speak('tamamdır')
            
        if 'görüşürüz' in voice:
            speak('görüşürüz kanka')
            exit()


        while 1:
            voice = record()
            print(voice)
            response(voice) 