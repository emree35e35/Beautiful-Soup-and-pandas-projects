import numpy as np
import pandas as pd
import re
df=pd.read_csv("C:/Users/emree/Desktop/movie_metadata.csv",sep="," ,header=0)
df.sort_values(by=['imdb_score'],inplace=True,ascending=0)
df2=(df[['movie_title','imdb_score','actor_1_name','actor_2_name','actor_3_name','country','title_year','budget','genres','duration','director_name','director_facebook_likes','actor_3_facebook_likes',
         'actor_2_facebook_likes','actor_1_facebook_likes','cast_total_facebook_likes']])
df2.dropna(inplace=True)

def degistir(degisen):

    degisen = re.sub(r"\s+$", "", degisen, flags=re.UNICODE)
    return degisen
df2['movie_title']=df2["movie_title"].apply(degistir)
df2.sort_values(by=['imdb_score'],inplace=True,ascending=1)

df2.to_csv('out.csv',index="id")
print(df2)
#print(df.isnull().values.any()) //Hiç null verisi olup olmadıgını sorguluyor