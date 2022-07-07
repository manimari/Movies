from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import sys 
from pathlib import Path 
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from models.queries_movie_db import search_movie
import os 
from werkzeug.security import check_password_hash 
from dotenv import load_dotenv #pip install python-dotenv

load_dotenv() 

current_working_directory=os.getcwd()+"\\" 
database_file_name=current_working_directory+f"data\\{os.getenv('DATABASE_NAME')}.db"   
  
route_movies=Blueprint("route_movies",__name__)  

@route_movies.route("/search/",methods=["GET","POST"]) 
def search_movies() :
    search = request.args.get("search") 
    if search != None : 
        movie_array = search_movie(search, page=1, adult=False) 
        print(movie_array)
    else : 
        movie_array = []
    return render_template("search_movies.html", movie_data = movie_array) 