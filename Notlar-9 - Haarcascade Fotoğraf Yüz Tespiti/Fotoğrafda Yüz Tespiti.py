import cv2
import numpy as np

img= cv2.imread("yuz.jpg")

yuz_casc=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#yuz_casc diye bir değişkene hardcascade dosyamızı tanıtdık

griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#yüz tespiti gri tonda yapılır bu yüzden cvtColor kullanıp bgr2gray yaptık

yuzler=yuz_casc.detectMultiScale(griton,1.1,4)#yuzler diye bir değişkene detectMultiScale komutu ile hangi resimdeki
                                              #yüzleri bulacağını,%kaç büyüteceğini,kaç kere teyit edeceğini
                                              #söylediğimiz parametreleri  ve bu aynı zamanda birden çok 
                                              #yüz tanımamızı sağladı 
for (x,y,w,h) in yuzler: #for döngüsü ile yüzün etrafında oluşacak karenin konum değişkenlerini girdik ve in yuzler
                         #diyerek konum değişkelerini yuzler değişkeni içerisinde aldık
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)#konum bilgileri girdiik buraya çok kafa yoramadım baya karışık önemlide değil

cv2.imshow("Yuzler",img)#ve kapanış
cv2.waitKey(0)
cv2.destroyAllWindows()