import cv2 #Opencv ile işlemlere Başlarken Öncelikle Kütüphanemizi Ekliyoruz.

resim=cv2.imread('insan.jpg') #Resim değişkeni oluşturup tanımlıyoruz. #Eğer başlıkdan sonra , koyup 0 yazarsak resim siyah beyaz olur.
cv2.imshow('insan',resim) #imshow kütüphansi ile resimi gösteriyoruz ve başlık olarak insan yazdırıyoruz.
#cv2.imwrite("gri.jpg",resim) #resmin son halinin çıktısını alır örn: gri ton isimli bir çıktı alacak ve siyah beyaz olacak çıktık-mız.

cv2.waitKey(0) #eğer kullanıcı herhangi bir tuşa bastığında gösterilen fotoğtrafın kapanmasını istiyorsak cv2.waitKey(0) komutunu kullanıyoruz
cv2.destroyAllWindows() #şimdide bir yere dokunulduğunda açılan tüm pencereleri kapatmasını söyüyoruz.