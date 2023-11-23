from flask import Flask, render_template, jsonify,request
import pandas as pd
from output import df2
movie_data = pd.read_csv("final.csv")

app = Flask(__name__)
movies = movie_data[["original_title","release_date","runtime","weighted_rating","poster_link"]] #

print(df2)

liked_movies = []
disliked_movies = []
did_not_watch_movies = []
popular_movies = []

def get_movies():
    m_data = {"original_title":movies.iloc[0,0],"release_date":movies.iloc[0,1],"runtime":movies.iloc[0,2],"rating":movies.iloc[0,3],"poster_link":movies.iloc[0,4]}
    return m_data


@app.route("/movies")
def display_movies():
    mov_data = get_movies()
    return jsonify({"data":mov_data,"success":"success"})

@app.route("/like")
def like():
    global movies
    move_data = get_movies()
    liked_movies.append(move_data)
    movies.drop([0],inplace=True)
    movies = movies.reset_index(drop = True)
    return jsonify({"success":"success"})

@app.route("/dislike")
def dislike():
    global movies
    move_data = get_movies()
    disliked_movies.append(move_data)
    movies.drop([0],inplace=True)
    movies = movies.reset_index(drop = True)
    return jsonify({"success":"success"})

@app.route("/didntw")
def didnt_watch():
    global movies
    move_data = get_movies()
    did_not_watch_movies.append(move_data)
    movies.drop([0],inplace=True)
    movies = movies.reset_index(drop = True)
    return jsonify({"success":"success"})

@app.route("/liked")
def diplay_like():
    global liked_movies
    return jsonify({"data":liked_movies})

@app.route("/disliked")
def diplay_dislike():
    global disliked_movies
    return jsonify({"data":disliked_movies})

@app.route("/didntwm")
def diplay_didntwm():
    global did_not_watch_movies
    return jsonify({"data":did_not_watch_movies,"success":"success"})

@app.route("/populars")
def populars_movies():
    global popular_movies
    for key,value in df2.iterrows():
        popular_data = {
            "original_title":value["original_title"],
            "release_date":value["release_date"],
            "runtime":value["runtime"],
            "weighted_rating":value["weighted_rating"],
            "poster_link":value["poster_link"]
        }
        popular_movies.append(popular_data)
    return jsonify({"data":popular_movies,"success":"success"})

app.run()