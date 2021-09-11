# Örnek: Sistem tarihi okunarak hangi mevsimde olduğumuzu ekrana yazdırınız.

# 12-01-02 kış
# 03-04-05 ilkbahar
# 06-07-08 yaz
# 09-10-11 sonbahar
# 01-12 arası değerler var

from datetime import datetime # python kütüphanesinden datetime(zaman) bilgilerini çekiyoruz

ay = datetime.today().month # Bilgisiyarın ay bilgisini alıyoruz

if((ay >= 12)or(ay == 1)or(ay == 2)):
    print('kış')
elif(ay >= 9):
    print('sonbahar')
elif(ay >= 6):
    print('yaz')
elif(ay >= 3):
    print('ilkbahar')
