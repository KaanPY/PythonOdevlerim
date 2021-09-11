import datetime

taksit = int(input("Vade Sayısı: "))
fiyat = float(input("Ürün Fiyatı: "))
ayliktaksit = round(fiyat / taksit,2) # round foksiyonu sayıalrı yuvarlamada kullanılıyor

for sayac in range(1,taksit+1):
    bugun = datetime.date.today()
    vade = bugun + datetime.timedelta(days = 30 * sayac)
    print(str(sayac) + ". Taksit => Tarih: " + str(vade) + " Taksit Tutarı: " + str(ayliktaksit) + " TL")
   
