from flask import Flask, jsonify, request
import csv

all_movies = [] 
headers = [] 
movie_links = []
with open("movies.csv", encoding= "utf8") as f:
    reader = csv.reader(f)
    data = list(reader) 
    all_movies = data[1:]
    headers = data[0] 

headers.append("poster_link")
with open("final.csv", "a+", encoding= "utf8") as f:
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 

with open("movie_links.csv", encoding= "utf8") as f:
    reader = csv.reader(f)
    data = list(reader) 
    movie_links = data[1:] 

for item in all_movies:
    poster_found = any(item[8] in links for links in movie_links)
    if poster_found:
        for link in movie_links:
            if item[8] == link[0]:
                item.append(link[1]) 
                if len(item) == 28:
                    with open("final.csv", "a+", encoding= "utf8") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(item)    