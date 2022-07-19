from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import sys 
from pathlib import Path 
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from models.queries_for_sql import insert_one_user, get_all_user, get_user_by_email, change_password_by_email, delete_account_by_email
import os 
from werkzeug.security import check_password_hash 
from dotenv import load_dotenv #pip install python-dotenv
from controls.movies import route_movies 

load_dotenv() 

current_working_directory=os.getcwd()+"\\" 
database_file_name=current_working_directory+f"data\\{os.getenv('DATABASE_NAME')}.db"   
  

route_users=Blueprint("route_users",__name__)  

route_users.register_blueprint(route_movies,url_prefix="/movies")  


@route_users.route("/register/",methods=["GET","POST"]) 
def register(): 
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
        if username_data != None: 
            if not check_password_hash(username_data[1], password) : 
                return render_template("login.html",error="password")
            session["email"] = email 
            return redirect(url_for("home"))
        else:
            return render_template("login.html",error="email")    

    else:#get request
        if "email" in session: 
            return redirect(url_for(".get_all"))
        else : 
            return render_template("login.html") 

@route_users.route("/get_all/",methods=["GET"])
def get_all(): 
    if "email" in session: 
        dict_to_send = {} 
        dict_to_send["data"] = get_all_user(database_file_name)
        dict_to_send["message"]='These are the users .'
        return jsonify(dict_to_send) 
    else : 
        return redirect(url_for(".login")) 



@route_users.route("/logout/") 
def logout(): 
    session.pop("email",None)#dioxnoume apo to session to username
    return redirect(url_for(".login")) #to onoma tis sunartisis


@route_users.route("/user/") 
def user(): 
    if "email" in session: 
        username_data=get_user_by_email(database_file_name, session["email"]) 
        return render_template("user.html", my_data = username_data)
    else : 
        return redirect(url_for(".login")) 

@route_users.route("/change_password/", methods=["POST", "GET"]) 
def change(): 
    if "email" in session: 
        if request.method=="POST": 
            old_password=request.form["old_password"] 
            new_password=request.form["new_password"] 
            verify_password=request.form["verify_password"] 
            username_data=get_user_by_email(database_file_name, session["email"]) 
            if not check_password_hash(username_data[1], old_password) : 
                return render_template("change_password.html", error = "old_password") 
            if new_password != verify_password : 
                return render_template("change_password.html", error = "verify")
            change_password=change_password_by_email(database_file_name, session["email"], new_password) 
            if change_password == False : 
                return render_template("change_password.html", error = "change") 
            else : 
                return render_template("change_password.html", error = "ok")  
        else : 
            return render_template("change_password.html")
    else : 
        return redirect(url_for(".login")) 

@route_users.route("/delete_account/", methods=["POST", "GET"]) 
def delete(): 
    if "email" in session: 
        if request.method=="POST": 
            if request.form["button"] == "Delete" : 
                deleted = delete_account_by_email(database_file_name, session["email"]) 
                if deleted == False : 
                    return render_template("delete_account.html") 
                else : 
                    session.pop("email",None)
                    return redirect(url_for(".register")) 
            elif request.form["button"] == "Cancel" :   
                return redirect(url_for(".user"))
        else : 
            return render_template("delete_account.html")
    else : 
        return redirect(url_for(".login")) 

