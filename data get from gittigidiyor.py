import bs4 as bs
import urllib.request
kaynak=urllib.request.urlopen("http://www.gittigidiyor.com/").read()
sayfa=bs.BeautifulSoup(kaynak,'lxml')

sonuc=sayfa.findAll('p',{"class":"discount-price"})
toplam=0
for fiyat in sonuc:
    fiyat=fiyat.string
    fiyat=fiyat.replace('TL','')
    fiyat = fiyat.replace('.','')
    fiyat=''.join(fiyat.split())
    fiyat=fiyat[:-3]
    fiyat=int(fiyat)
    toplam=toplam+fiyat

kaynaklar=urllib.request.urlopen("https://www.amazon.com.tr/")
sayfalar=sayfalar=bs.BeautifulSoup(kaynaklar,'lxml')
sonular=sayfalar.findAll("span",{"a-size-medium"})
toplam2=0

for veri in sonular:
    veri=veri.text
    veri=veri.replace('₺','')
    veri=veri.replace('Müşteriler bunları da satın aldı:','')
    veri=veri.replace('5,90 - ','')
    veri = veri.replace('.', '')
    veri = veri.replace(',', '')
    veri=veri[:4]
    veri = veri.replace('0', '')
    veri=int(veri)






    print(veri)












#for div in sayfa.findAll('div'):
 #   print(div)
#print(sayfa.get_text())#sayfadan text çekmeye yarıyo