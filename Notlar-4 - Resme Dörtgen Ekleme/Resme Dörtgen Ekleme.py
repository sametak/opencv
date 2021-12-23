import cv2
import numpy as np

resim=cv2.imread("messi.jpg")
cv2.imshow("original",resim)

cv2.rectangle(resim, (300,300),(500,300),(255,0,0),2) #cv2.rectangle komutunun önüne parantez içinde konum,
cv2.imshow("kareli",resim)                           #renk ve karenin kalınlığı bilgilerini yazarak resimde 
                                                     #kare oluştururuz.

cv2.waitKey(0),
cv2.destroyAllWindows()

#ÖNEMLİ : cv2.rectangle(resim,(200,70),(300,130),(255.0.0),(2))
#(200,70 demek sol üstden sağa doğru 200 git aşşağıya doğru 70 git )
#(320,130) demek sol üstden sağa doğru 320 git aşşağıya doğru 130 git demek ve bu şekilde kare oluşur.
#(255.0.0)demek en koyu mavi rengi olsun demektir (0.255.0) yeşil, (0.0.255) kırmızıdır.
#(2) kalınlığı 2 piksel olsun demektir.