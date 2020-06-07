import numpy as np
import pandas as pd
usvideo=pd.read_csv('C:/Users/emree/Desktop/verianalizi/usvideos.csv',)
#print(usvideo.head(n=5))
usvideo.drop(["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis=1,inplace=True)
#print(usvideo.columns,usvideo.index)
#print("Begeni ortalaması:",usvideo['likes'].mean(),"\nBegenmeme Ortalaması:",usvideo['dislikes'].mean())
#print(usvideo[usvideo["views"].max()==usvideo["views"]]['title'].iloc[0])#En cok goruntelenme alan
#print(usvideo[usvideo["views"].min()==usvideo["views"]]['title'].iloc[0])#En az goruntulenme alan
#print(usvideo.groupby("category_id").mean()[["comment_count"]])
#print(usvideo['category_id'].value_counts())


#-------------başlık uzunlugunu bulma--------------
def uzunluk(title):
    return len(title)
usvideo["baslik_uzunlugu"]=usvideo["title"].apply(uzunluk)
#print(usvideo)
#--------------etiketin uzulugunu bulma--------------
def tags(tag):
    taglist=tag.split('|')
    return len(taglist)
usvideo['tag_uzunlugu']=usvideo['tags'].apply(tags)
#print(usvideo)
#---------------------------begeni oranı en yüksekden en dusuge dogru sıralama
#print(usvideo)