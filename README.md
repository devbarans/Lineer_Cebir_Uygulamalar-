# Linear Algebra Applications with NumPy

Bu çalışmada NumPy kütüphanesi kullanılarak doğrusal cebirin temel kavramları
sayısal olarak incelenmiştir. Çalışma kapsamında doğrusal bağımsızlık,
geren kümeler (span), baz ve boyut kavramları, özvektörlerin baz oluşturma
durumu ile norm, uzaklık ve birim vektör hesaplamaları ele alınmıştır.

---

## Soru 1 – Doğrusal Bağımsızlık / Bağımlılık

Dört vektör bir araya getirilerek oluşturulan matrisin rütbesi (rank)
hesaplanmıştır. Matrisin rank değeri 3 olarak bulunmuştur. Vektör sayısı
4 olmasına rağmen rank değeri 3 olduğu için bu vektörlerin doğrusal
bağımlı olduğu sonucuna varılmıştır. Ayrıca açık bir doğrusal ilişki
bulunmuştur:

v2 = 2 · v1

Bu ilişki, vektör kümesinin doğrusal bağımsız olmadığını doğrudan
göstermektedir.

---

## Soru 2 – Span (Geren Küme) Testi

Üç vektör kullanılarak oluşturulan matris ile verilen b vektörü için
en küçük kareler yöntemi uygulanmıştır. Elde edilen katsayılar ile
matris-vektör çarpımı yapıldığında sonuç b vektörünü verdiğinden,
b vektörünün bu üç vektörün gerdiği uzayda yer aldığı görülmüştür.

Bu sonuç, b vektörünün span{u1, u2, u3} kümesine ait olduğunu göstermektedir.
Ancak yalnızca üç vektör kullanıldığı için bu küme R⁴ uzayının tamamını
değil, bir alt uzayı germektedir.

---

## Soru 3 – Baz ve Boyut

Verilen matrisin rütbesi hesaplanmış ve rank değeri 3 olarak bulunmuştur.
Bu sonuç, matrisin sütun uzayının boyutunun 3 olduğunu göstermektedir.
QR ayrışımı yardımıyla doğrusal bağımsız sütunlar belirlenmiş ve bu
sütunların sütun uzayı için bir baz oluşturduğu sonucuna varılmıştır.

---

## Soru 4 – Özvektörler Baz Oluşturur mu?

Köşegen bir 3x3 matrisin özdeğerleri ve özvektörleri hesaplanmıştır.
Elde edilen özvektörlerden oluşturulan matrisin rank değeri 3 olduğu için
özvektörlerin doğrusal bağımsız olduğu görülmüştür. Bu nedenle söz konusu
özvektörler R³ uzayı için bir baz oluşturmaktadır.

Bu durum, matrisin köşegenlenebilir olmasından kaynaklanmaktadır.
Her 3x3 matrisin özvektörlerinin mutlaka bir baz oluşturmadığı
unutulmamalıdır.

---

## Soru 5 – Norm, Uzaklık ve Birim Vektör

Verilen dört noktanın Öklid normları hesaplanarak her bir vektörün
orijine olan uzaklığı bulunmuştur. Ardından noktalar arasındaki
çiftler için mesafe matrisi oluşturulmuş ve bu matris yardımıyla
en yakın ve en uzak nokta çiftleri belirlenmiştir.

Son aşamada her vektör, kendi normuna bölünerek birim vektör haline
getirilmiştir. Bu işlem sırasında vektörlerin yönleri korunmuş,
yalnızca uzunlukları 1 olacak şekilde normalize edilmiştir.

---

## Kullanılan Teknolojiler

Python programlama dili ve NumPy kütüphanesi kullanılarak doğrusal cebirin
temel kavramları sayısal olarak analiz edilmiştir.

---

## Sonuç

Bu çalışma, doğrusal cebirde sıkça kullanılan kavramların bilgisayar
ortamında nasıl test edilebileceğini ve doğrulanabileceğini göstermektedir.
Teorik bilgilerin NumPy ile desteklenmesi, konuların daha somut ve
anlaşılır hale gelmesini sağlamıştır.
