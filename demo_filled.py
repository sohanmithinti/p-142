import pandas as pd 
import numpy as np 

df = pd.read_csv("final.csv")
C = df["vote_average"].mean()
M = df["vote_count"].quantile(0.9)
q_movies = df.copy().loc[df["vote_count"]>= M] 

def weighted_rating(x, m = M, c = C):
    v = x["vote_count"]
    r = x["vote_average"]
    return(v/(v+m)*r)+(m/(m+v)*c) 

q_movies["score"] = q_movies.apply(weighted_rating, axis = 1) 
q_movies = q_movies.sort_values("score", ascending = False)
output = q_movies[["title", "poster_link", "release_date", "runtime", "vote_average", "overview"]].head(20).values.tolist()  
print(output) 