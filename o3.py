# Örnek: Sistem saati okunarak;
#       06-11 arası günaydın,
#       12-18 arası iyi günler,
#       19-22 arası iyi akşamlar
#       23-01 arası iyi geceler
#       02-05 arası yat artık
# şeklinde mesaj verecek programı yazınız.

from datetime import datetime

saat = datetime.today().hour
saat = 6

if((saat == 23)or(saat == 1)):
     print('iyi geceler')
elif(saat >= 19):
     print('iyi akşamlar')
elif(saat >= 12):
     print('iyi günler')
elif(saat >= 6):
     print('günaydın')
elif(saat >= 2):
     print('yat artık')

