from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd

site= "https://iibf.deu.edu.tr/wp-courselist.php"
baslik = {'User-Agent': 'Mozilla/5.0'}
istek = Request(site,headers=baslik)
sayfa = urlopen(istek)
sayfaverisi = BeautifulSoup(sayfa)
dersler = sayfaverisi.find("select",{'name':'ders'}).find_all("option")
ders=[]
for derslistesi in dersler:
    derslistesi=derslistesi['value']
    ders.append(derslistesi)

df=pd.DataFrame(data=ders,columns=["DersAdı"])
df.to_csv('ders.csv',index="id")





