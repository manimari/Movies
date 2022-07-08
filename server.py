from functions.check_file_existence import check_file_existence 
from models.queries_for_sql import create_db 
import os 
from flask import Flask, session, redirect, url_for
from controls.users import route_users 
from controls.movies import route_movies 
from controls.actors import route_actors
from dotenv import load_dotenv #pip install python-dotenv

load_dotenv() 

current_working_directory=os.getcwd()+"\\" 
database_file_name=current_working_directory+f"data\\{os.getenv('DATABASE_NAME')}.db"   

if check_file_existence(database_file_name) == False : 
    create_db(database_file_name) 

app=Flask(__name__) 
app.secret_key=os.getenv("SECRET_KEY") #apokriptografei to session key automata
app.register_blueprint(route_users,url_prefix="/users") 
app.register_blueprint(route_movies,url_prefix="/movies") 
app.register_blueprint(route_actors,url_prefix="/actors") 

@app.route("/") 
def home() : 
    if "email" in session : 
        return redirect(url_for("route_movies.search_movies"))
    else : 
        return redirect(url_for("route_users.login"))

if __name__=="__main__":
    port=5000 
    app.run(port=port,debug=True)  