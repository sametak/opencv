import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,150)#kamera.set diyip (cv2.CAP_PROP_FRAME_WIDTH,150) yazınca genişlik
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,150)#150 altda tekrardan işlemi yükseklik için yapıp yüksekliği 150 yaptık

while True:
    ret, goruntu=kamera.read()
    griton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    ret=kamera.set(3,100)#yukarıda yaptığımız işlemin aynısını ret parametresi ile
    ret=kamera.set(4,100)#de yapabiliyoruz.
    cv2.imshow("kamera",goruntu)
    cv2.imshow("griton",griton)
    if cv2.waitKey(25) % 0xFF==ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()

