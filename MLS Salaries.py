import numpy as np
import pandas as pd
sutunlar=['club','last_name','first_name','position','base_salary','guaranteed_compensation']
mlssalaries=pd.read_csv('C:/Users/emree/Desktop/verianalizi/mls-salaries-2017.csv',header=0)
#print(mlssalaries.head(n=10))# İlk 10 veriyi okuma
#print("Listedeki toplam veri sayısı:",len(mlssalaries.index))
#print("Tüm maaşların ortalaması:",mlssalaries['base_salary'].mean())
#print("En yüksek maaş:",mlssalaries['base_salary'].max())
#print(mlssalaries[ mlssalaries['guaranteed_compensation'].max()==mlssalaries['guaranteed_compensation'])# En yüksek tazminata sahip kişinin index degeri
#print(mlssalaries[mlssalaries['guaranteed_compensation'].max()==mlssalaries['guaranteed_compensation']]['last_name'])
#print(mlssalaries.iloc[401]['last_name'])
#print("Gonzalez Pirez'in oynadıgı mevki :",mlssalaries[mlssalaries['last_name']=="Gonzalez Pirez"]["position"].iloc[0])


#--------------- Mevkilere göre bulma ve gruplama-----------
#print(mlssalaries.groupby('position').mean())#Posizyona göre ortalama maaşlar

#print("Veri setinde ",len(mlssalaries.groupby('position').mean().index)," farklı mevki bulunmaktadır.")-----------------
#print(mlssalaries['position'].nunique()) #bir usttekıyle aynı gorevı goruyor-----------------------

#print(mlssalaries['position'].value_counts())#Her mevkide toplam kaç deger var
#print(mlssalaries['club'].value_counts())#Her takımda kac kısı oynuyor
#--------------- İçinde son gecen oyuncular bulma

def bul(soyad):
    if "son" in soyad.lower():
        return True
    return False
print(mlssalaries[mlssalaries['last_name'].apply(bul)])






