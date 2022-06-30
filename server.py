import imp
from functions.check_file_existence import check_file_existence 
from models.queries_for_sql import create_db 
import os 
from flask import Flask
from controls.users import route_users

current_working_directory=os.getcwd()+"\\" 
database_file_name=current_working_directory+"data\\movies.db"   

if check_file_existence(database_file_name) == False : 
    create_db(database_file_name) 

app=Flask(__name__) 
app.register_blueprint(route_users,url_prefix="/users") 

if __name__=="__main__":
    port=5000 
    app.run(port=port,debug=True)  