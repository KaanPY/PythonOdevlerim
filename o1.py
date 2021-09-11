'''
from datetime import datetime #datetime sınıfı içe aktarılıyor.

an = datetime.now() #tarih nesnesi oluşturulup now() fonksiyonu ile zaman bilgisi atanıyor.

print("tarih ve saat = ",an) #an nesnesi ekrana yazdırılıyor.

####################################################################################################

from datetime import date #date sınıfı içe aktarılıyor.

bugun = date.today()

print("bugun = ", bugun)

####################################################################################################

'''
from datetime import datetime #datetime sınıfı içe aktarılıyor.

bugun = datetime.today()

print("bugun = ",bugun)

print(bugun.weekday()) #haftanın kaçıncı günü - Pazartesi 0 ile Pazar 6 arası

print(bugun.year) # yıl bilgisi

print(bugun.month) # ay bilgisi

print(bugun.day) # gün bilgisi

print(bugun.hour) # saat bilgisi

print(bugun.minute) # dakika bilgisi

print(bugun.second) # saniye bilgisi

 
 
   
