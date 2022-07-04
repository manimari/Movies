from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import sys 
from pathlib import Path 
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from models.queries_for_sql import insert_one_user, get_all_user, get_user_by_email
import os 
from werkzeug.security import check_password_hash 
from dotenv import load_dotenv #pip install python-dotenv

load_dotenv() 

current_working_directory=os.getcwd()+"\\" 
database_file_name=current_working_directory+f"data\\{os.getenv('DATABASE_NAME')}.db"   
  

route_users=Blueprint("route_users",__name__)  


@route_users.route("/register/",methods=["GET","POST"]) 
def register(): 
    # new_user = request.get_json() 
    # dict_to_send = {} 
    # insert_one_user(new_user["username"], new_user["password"]) 
    # dict_to_send["message"]=f'The user with username {new_user["username"]} is registered.'
    # #return jsonify(dict_to_send) 

    if request.method=="POST": 
        email=request.form["email"] 
        password=request.form["password"] 
        name=request.form["name"] 
        lastname=request.form["lastname"] 
        new_user = insert_one_user(database_file_name, email, password, name, lastname) 
        if new_user == False : 
            return render_template("register.html") 
        else : 
            return redirect(url_for(".login")) 
    else : 
        return render_template("register.html")


@route_users.route("/login/", methods=["GET", "POST"]) 
def login(): 
    if request.method=="POST":
        email=request.form["email"]#"email"-> einai to name tou input sto html
        password=request.form["password"]#"password"-> einai to name tou input sto html
        username_data=get_user_by_email(database_file_name, email) 
        print(username_data)
        if username_data != None: 
            if not check_password_hash(username_data[1], password) : 
                return render_template("login.html",error="password")
            session["email"] = email 
            return redirect(url_for(".get_all"))
        else:
            return render_template("login.html",error="email")    

    else:#get request
        if "email" in session: 
            return redirect(url_for(".get_all"))
        else : 
            return render_template("login.html") 

@route_users.route("/get_all/",methods=["GET"])
def get_all(): 
    dict_to_send = {} 
    dict_to_send["data"] = get_all_user(database_file_name)
    dict_to_send["message"]='These are the users .'
    return jsonify(dict_to_send) 

@route_users.route("/logout/") 
def logout(): 
    session.pop("email",None)#dioxnoume apo to session to username
    return redirect(url_for(".login")) #to onoma tis sunartisis