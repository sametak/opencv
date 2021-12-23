import cv2
import numpy as np

kamera=cv2.VideoCapture("ilgili.mp4")#videomuzu değişkene atadık

while True:
    ret, goruntu=kamera.read()#bi while döngüsü ile görüntüyü aldık ve q tuşunu çıkmak için ayarladık
    cv2.imshow("kamera",goruntu)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()
