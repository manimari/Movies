from flask import Blueprint, render_template, request

from ..models.queries_for_sql import insert_one_user 
import os 

current_working_directory=os.getcwd()+"\\" 
database_file_name=current_working_directory+"data\\movies.db"    

route_users=Blueprint("route_users",__name__)  


@route_users.route("/register",methods=["GET","POST"]) 
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
        insert_one_user(database_file_name, email, password, name, lastname)
        return render_template("register.html")
    else : 
        return render_template("register.html")



