import pandas as pd
import matplotlib.pyplot as plt
fifa=pd.read_csv("C:/Users/emree\Desktop/verianalizi/PlayerPersonalData.csv")
#print(fifa[["Name","Value"]])#Birden fazla column yazdırmak icin 2 defa paranteze al
def degistir(degisen):

        degisen = degisen.replace("€", "")
        degisen = degisen.replace("M", "000000")
        degisen = degisen.replace("K", "000")
        degisen = degisen.replace(".", "")
        degisen = int(degisen)
        return degisen
fifa['WageWithoutString']=fifa["Wage"].apply(degistir)#Değeri Hamlastırma fonksiyonu
#fifa['Club'].fillna("Bilinmeyen Club",inplace=True)#Bazı kulüplerin adı yazılmadıgından dolayı bilinnmeyen klub yazdır yada asagıdakini yapabilirsin
fifa.dropna(inplace=True)#Komple içi boş olanları siler
fifaValueTotal=fifa.groupby("Club")["WageWithoutString"].sum()

#print(fifaValueTotal.head(5))#Genel Klublerın MAAŞ Toplamları ilk 5i

#Klubleri ve maaşlarını çizdirme
#lt.plot(fifaValueTotal.head(5),"red")#İlk 5ini yazdırıp onları çizdirme
#plt.show()

enyuksekucret=fifa[fifa["WageWithoutString"].max()==fifa["WageWithoutString"]]['Club'].iloc[0]#En cok Ücret ödeyen klüb
#print(enyuksekucret)
endusukucret=fifa[fifa["WageWithoutString"].min()==fifa["WageWithoutString"]]['Club'].iloc[0]#En az Ücret ödeyen klüb
print(endusukucret)





#-----------Tek takım üzerinden işlem yapma-------------
fifaBarcelonaValueTotal=fifa[fifa['Club']=="FC Barcelona"]["WageWithoutString"].sum()  #Tek takımın maaşlarını toplatma
#print("\nBarcelona'nın Toplam Oyuncu Maaşı:",fifaBarcelonaValueTotal)
