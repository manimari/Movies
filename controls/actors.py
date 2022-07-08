from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import sys 
from pathlib import Path 
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from models.queries_movie_db import get_actor_url, get_actor_data
import os 
from werkzeug.security import check_password_hash 
from dotenv import load_dotenv #pip install python-dotenv

load_dotenv() 

current_working_directory=os.getcwd()+"\\" 
database_file_name=current_working_directory+f"data\\{os.getenv('DATABASE_NAME')}.db"   
  
route_actors=Blueprint("route_actors",__name__)  

@route_actors.route("/<id>",methods=["GET","POST"]) 
def actor_id(id) :
    actor_url = get_actor_url(id) 
    actor_id_array = get_actor_data(actor_url) 
    if "email" in session: 
        actor_url = get_actor_url(id) 
        actor_id_array = get_actor_data(actor_url) 
        return render_template("actor.html", actor = actor_id_array) 
    else : 
        return redirect(url_for("route_users.login"))
     