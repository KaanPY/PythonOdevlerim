"""
Örnek: Mail doğruluk kontrolü
Kurallar:

     Mail adresi  15-100 karakter olacak.
     Sadece 1 adet @ işareti olacak.
     Nokta işareti olacak
     En son noktadan sonraki uzantı 2 veya 3 karakter olacak(tr, com gibi)
    
Örnek mailler:

    ali.yilmaz@gmail.com
    ahmetsener@hotmail.com
    iletisim@lezzetlihayaller.com
    ttpendik@k12.meb.gov.tr

"""

mailadresi = "ttpendik@k12.meb.gov.tr"

karaktersayisi = len(mailadresi) # len komutu string'teki karakter sayısını verir.
e_adet = mailadresi.count('@')
nokta = mailadresi.count('.')
ensonnokta = mailadresi.rindex(".") + 1   # yazının sonundan itibaren istenen karakteri ar
enson_uzanti = karaktersayisi - ensonnokta

if(karaktersayisi < 15 or karaktersayisi > 100):
    print("Lütfen doğru bir mail adresi giriniz")
elif(e_adet != 1):
    print("Mail adresinde 1 adet @ işareti bulunması gerekir.")
elif(nokta < 1):
    print("Mail adresinde enaz 1 adet nokta işareti bulunması gerekir.")
elif(enson_uzanti < 2 or enson_uzanti > 3):
    print("Mailin son kısmı(örnek: com gibi) 2 veya 3 karakter olabilir")
else:
    print("Mail adresiniz doğru")















    
    

























