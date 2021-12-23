import cv2
import numpy as np

ressim=cv2.imread("messi.jpg")

print(str(ressim.item(100,100,1))) #.item komutunu kullanarak 100e 100lük kısmındaki yeşil piksellerin kaç tane olduğunu sorguluyoruz 0=mavi 1=yeşil 2=kırmızı
ressim.itemset((100,100,2),255) #.itemset komutu ile resimin 100e 100lük kısmındaki kırmızı olan bölümlerin koyuluğunu fulledik yani 255e çıkardık

print(str(ressim.shape)) #resimin boyutunu kaça kaç olduğunu ve kaç renkden oluştuğunu gösterir

print(str(ressim.size)) #resimin kaç pixel olduğunun bilgisini bu şekilde alabiliyoruz

print(ressim.dtype)#iki resimi aynı anda gösterirken veya iki resmin birkaç verisini toplarken veri tiplerinin aynı olmasına dikkat etmeliyiz

ROI=ressim[50:200,300:500] #resimin kesiceğimiz bölmesinin +y -y ve +x -x olarak konum bilgisini değişkenimize atadık

ressim[50:200,200:400]=ROI #şimdi ise kestiğimiz bölgeyi ressim değişkeninin istediğimiz yerine yapıştırdık

cv2.imshow("kesilmiş bölüm",ROI) #ve şimdii ekrana yansıtıyoruz

ressim[:,:,0]=0 #burada resmin 0 yani mavi bölümlerinin tonunu sıfırlıyoruz.



cv2.imshow("messi",ressim)
cv2.waitKey(0)
cv2.destroyAllWindows()