import cv2


kamera = cv2.VideoCapture(0)  # kameramızı okutduk
# yuz_casc diye bir değişkene hardcascade dosyamızı tanıtdık
yuzler = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while(1):  # kamera kullandığımız için while döngüsü açdık
    ret, frame = kamera.read()

    griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # gri tonumuzu oluşturduk
    # yuzler diye bir değişkene detectMultiScale komutu ile hangi resimdeki
    yuzler = yuzler.detectMultiScale(griton, 1.1, 4)
    # yüzleri bulacağını,%kaç büyüteceğini,kaç kere teyit edeceğini
    # söylediğimiz parametreleri  ve bu aynı zamanda birden çok
    # yüz tanımamızı sağladı

    for(x, y, w, h) in yuzler:  # for döngüsü ile yüzün etrafında oluşacak karenin konum değişkenlerini girdik ve in yuzler
        # diyerek konum değişkelerini yuzler değişkeni içerisinde aldık
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3)
    cv2.imshow("orjinal", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):  # temel kamera kapatma işlemleri
        break

kamera.release()
cv2.destroyAllWindows()
