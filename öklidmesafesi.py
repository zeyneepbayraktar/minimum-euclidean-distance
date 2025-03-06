#noktaları içeren bir liste
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
#fonksiyon tanımlamak için def kullan
#math.sqrt() fonksiyonunu (karekök almak için) kullanmak için math modülünü ekle
import math
def euclideanDistance(point1, point2):
    x1, y1 = point1 #ilk nokta (x1, y1)
    x2, y2 = point2 #ikinci nokta (x2, y2)
    return math.sqrt((x2-x1)**2+(y2-y1)**2) #öklid mesafesi formülü d = √(x₂-x₁)²+(y₂-y₁)²
distances = [] #mesafenin saklanacağı liste
#tüm nokta çiftleri arasındaki mesafeyi hsaplamak için iç içe iki döngü
for i in range(len(points)): #ilk noktayı seç
    for j in range(i+1, len(points)): # İkinci noktayı seç (kendisiyle karşılaştırmamak için i+1'den başlat)
        distance = euclideanDistance(points[i], points[j])  # Mesafeyi hesapla
        distances.append(distance)  # Listeye ekle
#len() fonksiyonu, bir listenin, stringin veya başka bir veri yapısının uzunluğunu (eleman sayısını) döndüren Python fonksiyonu
print(distances) #çıktı


