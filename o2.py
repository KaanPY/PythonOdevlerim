# Örnek: Program; sistem zamanını okuyacak ve haftasonu ise "İyi Tatiller..",
# hafta içi ise "İyi Çalışmalar..." şeklinde mesaj yazacak. 

# Not: weekday fonksiyonunda; Pazartesi 0 ile Pazar 6 arası

from datetime import datetime

zaman = datetime.today()
if(zaman.weekday() == 5 or zaman.weekday() == 6):
    print("İyi Tatiller")
else:
    print("İyi çalışmalar")




    
    
