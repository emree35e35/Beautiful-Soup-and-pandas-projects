from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import numpy as np

site= "https://iibf.deu.edu.tr/wp-courselist.php"
baslik = {'User-Agent': 'Mozilla/5.0'}
istek = Request(site,headers=baslik)
sayfa = urlopen(istek)
sayfaverisi = BeautifulSoup(sayfa)
hocalar = sayfaverisi.find("select",{'name':'hoca'}).find_all("option")
ogretmenler=[]
uzunogretmenler=[]
kısaogretmenler=[]
words = 0
ogretmenad=["emre"]
ogretmensoyad=["emre"]



for ogretmenlistesi in hocalar:

    ogretmenlistesi=ogretmenlistesi['value']
    kelimelistesi=ogretmenlistesi.split()
    kelimeler=len(kelimelistesi)
    if kelimeler>=3:
        uzunogretmenler.append(ogretmenlistesi)
    if kelimeler==2:
        kısaogretmenler.append(ogretmenlistesi)
for i in kısaogretmenler:
    i=i.split()
    ogretmenad.append(i[0])
    ogretmensoyad.append(i[1])
for i in uzunogretmenler:
    i = i.split()
    ogretmenad.append(i[0]+" "+i[1])
    ogretmensoyad.append(i[2])
print(ogretmenad)



df=pd.DataFrame(data=ogretmenad,columns=["ogretmen_ad"])
df["ogretmen_soyad"]=ogretmensoyad
df["ogretmen_yas"]=np.random.randint(25,55,154)
print(df)

df.to_csv('hoca.csv',index="id")




