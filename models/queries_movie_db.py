import requests
import json 
from dotenv import load_dotenv #pip install python-dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")

def get_data_movie_by_id(id) : 
    link=f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}"
    req=requests.get(link)
    result=req.text 
    result = json.loads(result) 
    result["poster_path"] = get_image_url(result["poster_path"])
    return result 

def get_image_url(link, size="w500") : 
   link = f"https://image.tmdb.org/t/p/{size}{link}"
   return link

def search_movie(movie_name, page=1, adult=False) : 
    link = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={movie_name}&page={page}&include_adult={adult}" 
    req=requests.get(link)
    result=req.text 
    result = json.loads(result) 
    result = result["results"] 
    for movie in result : 
        movie["poster_path"] = get_image_url(movie["poster_path"])
    return result 

def get_actor_url(id) : 
    link = f"https://api.themoviedb.org/3/person/{id}?api_key={api_key}&language=en-US" 
    return link 

def get_cast(movie_id) : 
    link = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=en-US" 
    req=requests.get(link)
    result=req.text 
    result = json.loads(result) 
    result = result["cast"] 
    for actor in result : 
        actor["profile_path"] = get_image_url(actor["profile_path"]) 
        actor["actor_url"] = get_actor_url(actor["id"])
    return result 



