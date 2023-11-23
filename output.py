import pandas as pd

df1 = pd.read_csv("final.csv")
# print(df1["weighted_rating"])
df1 = df1.sort_values("weighted_rating",ascending = False)
# print(df1["weighted_rating"])

df2 = df1[["original_title","release_date","runtime","weighted_rating","poster_link"]].head(10)
print(df2)