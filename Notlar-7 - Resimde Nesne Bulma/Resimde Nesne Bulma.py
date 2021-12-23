import cv2
import numpy as np

img_rgb=cv2.imread("ana-resim.jpg")#resmi tanıtdık
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)#gri halini tanıtdık

nesne=cv2.imread("template.jpg",0)#bulunacak nesneyi tanıtdık

w,h=nesne.shape[::-1]#ilk iki parametreyi atlayıp w ve h ye son iki parametresiniz dedik

res=cv2.matchTemplate(img_gray,nesne,cv2.TM_CCOEFF_NORMED)#matchTemplate resmin gri tonunda nesneyi eşleştirmeye çalış anlamında kullanılıyor.
threshold=0.8#yüzde 80 oranla uyuştur dedik

loc=np.where(res>threshold)#nesneyi bulduğu lokasyonları loc diye bir değişkende tut dedik #yani %80 üzerindeki eşleşmeleri loc değişkeninde tut dedik

for n in zip(*loc[::-1]):#bi for döngüsünde n değişkeni yapıp locu n ye atadık
    cv2.rectangle(img_rgb,n,(n[0]+w,n[1]+h),(0,255,255),2)#n ye kare oluşturduk

cv2.imshow("bulunan nesneler",img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
#kendi düşüncemle renk konusunda karışıklık oluşmasın diye bulunacak nesneyi ve resmi gri tonda iken 
#eşleştirdik ve lokasyonunu loc değişkenine loc değişkenine atadık for döngüsü ile loc
# değişkenindeki lokasyona göre rectangle kare oluşturma komutu ile kare oluşturduk