import cv2
import numpy as mp
 
mavi=[255,0,0]#Öncelikle mavi rengini mavi değişkenine atıyorum. 

resim=cv2.imread("resim.jpg")

#şimdi size çerçeve oluşturmanın birden çok yolunu göstericem
replicate=cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_REPLICATE)#1.yol #10,10,10,10 yazdığımız kısım, üst,alt,sağ,sol, uzunluklarıdır
reflect=cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_REFLECT)#2.yol
reflect101=cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_REFLECT101)#3.yol
wrap=cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_WRAP)#4.yol
constant=cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_CONSTANT,value=mavi)#5.yol bu yol kenara temel bir çerçeve çeker.
                                                                #value komutu ile çerçeveyi renklendirebiliriz
cv2.imshow("Orjinal",resim)
cv2.imshow("1.yol",replicate)
cv2.imshow("2.yol",reflect)
cv2.imshow("3.yol",reflect101)
cv2.imshow("4.yol",wrap)
cv2.imshow("5.yol",constant)

cv2.waitKey(0)
cv2.destroyAllWindows()