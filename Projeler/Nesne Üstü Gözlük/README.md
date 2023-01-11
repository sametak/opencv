# Nesne Üstü Gözlük;

## Amacı; :
Bu projede, görme yardımcı desteğin tersine görüş gücünün sınırlarını genişletmek amaçlanmaktadır.Görüntü işleyebilen kameralı bir gözlük tasarlanacak ve görüntünün görüntülenebilmesi için küçük bir ekran eklenecek. Cihaz Rasberry Pi ve Rasberry Pi kamera ile çalışacak kendine ayit hoparlorü olacak ve kamera ile arka arkaya olan görüntüleme ekranı raylı bir sisteme sahip olacak ve 5-6 cm uzaklaşip yakinlaşabilecek. Ray kısmı tamamen kapandığında görüntü kesilecek ve gözü rahatsız etmeyecek aynı zamanda enerjiden tasaruf sağlanacak. Arka arkaya olan kamera ve ekran kısmı yukarı doğru menteşeli bir sistemle kalkabilecek ve kullanılmadığı zaman pasif duruma getirilebilecek. Şarz entegresine sahip bir lityum pile sahip olacak ve tasarımı 3D yazıcı cihazından çıkartılacak. Fonksiyonları;

-"BİG Data" yani büyük bir veri yığını databasesine sahip olacak ve bu database içerisinde nesne tespiti sağlamak için dünya üzerindeki objelerin tespit için gerekli onlarca fotoğrafı "xml" formatında barındıracak. Bu sayede nesne tespiti gerçekleşecek ve bu büyük kütüphane hem gelecek için hem şuanki zaman için görme yeteneğine sahip bir yapayzeka sağlayacak.

-İçerisinde kendisiyle canlı olarak haberlesebileceğimiz bir asistan var olacak ve ona sesli olarak "tarih ve saat", "internet araması yapma" "karşısındakı nesneleri algılama" "Yazı Okuma"  "Konum Tespiti" "Yol Takibi" vb. komutlar verilebilecek 

-Ticari olarak kullanımı düşünülürse kategorilere ayrılıp kullanım amacına göre satışı gerçekleşebilir. Örneğin bilgisayar mühendisi bir arkadaşa lehim gibi ince işler yaparken ışık tutma yanık algılama sesli video okuma gibi özellikler eklenebilir. Görme engelli bir arkadasa ekran kısmı çıkarılıp sesli görme yardımcısı olarak kullanılabilir. Duyma engelli bir rkadasa hoparlor kısmı çıkartılıp daha çok görüntü üzerine yazı yazma amaçlı kullanılabilir. Görüntüyü profosyonelce işlemek geleceğin yapay zekasına atılan bir adımdır, bu projede bu adımın ilk örneğidir, geleceği açıktır.

###### -Adım 1 | BackEnd:
Xampp üzerinden kendimize ait PHP bir database oluşturacağız.Bu databaseyi Python ile bağdaştırıp databaseye kameranın otomatik tespit edebileceği nesneleri ekleyeceğiz. Databaseyi herkeze açık yapıp gelişitirinilebilir bi "BIG-Data" haline getirmeyi planliyorum.

Detaylı açıklama proje docx belgesinin içerisinde bulunmaktadır.

###### -Adım 2 | FrontEnd : 
Projenin gözlük tasarımını engelsiz gözlük projesinin tasarımı üzerine çalışarak tasarlayacağım. Raylı sistem ile kamera ve ekran sirt sirta duracak ve ekran ray aracılığıyla gözün 7-8 cm uzağına alınıp görüntü rahat okunulabilir bir hale getirilinecek.

