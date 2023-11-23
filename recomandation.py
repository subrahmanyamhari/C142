import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df3 = pd.read_csv("final.csv")
df3 = df3[df3["soup"].notna()]

count = CountVectorizer(stop_words = "english")
count=count.fit_transform(df3["soup"])


similarity = cosine_similarity(count,count)
df3 = df3.reset_index()
data = pd.Series(df3.index,index = df3["original_title"])

def get_recomendation(title):
    data1 = data[title]
    data_similarity = list(enumerate(similarity[data1]))
    data_similarity = sorted(data_similarity)
    data_similarity = data_similarity[1:11]
    similar_movie = [i[0] for i in data_similarity]
    print((df3[["original_title","release_date","runtime","weighted_rating","poster_link"]].iloc[similar_movie]))
    return(df3[["original_title","release_date","runtime","weighted_rating","poster_link"]].iloc[similar_movie])

get_recomendation("The Lion King")