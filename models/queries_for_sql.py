import sqlite3
from werkzeug.security import generate_password_hash
import os 
  

def create_db(database_file_name) : 
    con = sqlite3.connect(database_file_name)
    try : 
        query = """Create Table User
            (email varchar(100) not NULL primary key, 
            password varchar(100), 
            name varchar(100), 
            last_name varchar(100)
            );"""  
        cursor = con.cursor() 
        cursor.execute(query) 
        query = """Create Table Favorite
            (email varchar(100) not NULL primary key, 
            movie_id int 
            );"""  
        cursor = con.cursor() 
        cursor.execute(query)  
        query = """Create Table Rates
            (email varchar(100) not NULL primary key, 
            movie_id int, 
            rate real
            );"""  
        cursor = con.cursor() 
        cursor.execute(query)   
    except : 
        print("An exception occurred") 
    con.close() 

def insert_one_user(database_file_name,email, password, name, last_name) : 
    con = sqlite3.connect(database_file_name) 
    added = False 
    try : 
        hashed_password = generate_password_hash(password,method='sha256') 
        query = f"""Insert Into User (email, password, name, last_name) values('{email}', '{hashed_password}', '{name}', '{last_name}')"""
        cursor = con.cursor() 
        cursor.execute(query)   
        con.commit() 
        added = True 
    except : 
        print("An exception occurred") 
    con.close()  
    return added 

def get_all_user(database_file_name): 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = "Select * from User" 
        cursor = con.cursor() 
        cursor.execute(query) 
        all_user = cursor.fetchall() 
    except : 
        print("An exception occurred") 
    con.close() 
    return all_user  

def get_user_by_email(database_file_name, email): 
    con = sqlite3.connect(database_file_name) 
    #print("email",email)
    try : 
        query = f"Select * from User where email='{email}'" 
        cursor = con.cursor() 
        cursor.execute(query) 
        all_user = cursor.fetchone() 
    except : 
        print("An exception occurred") 
    con.close() 
    #print(all_user) 
    return all_user   

def change_password_by_email(database_file_name, email, password): 
    con = sqlite3.connect(database_file_name) 
    changed = False 
    try : 
        hashed_password = generate_password_hash(password,method='sha256')
        query = f"Update User set password = '{hashed_password}' where email='{email}'" 
        cursor = con.cursor() 
        cursor.execute(query)   
        con.commit() 
        changed = True 
    except : 
        print("An exception occurred") 
    con.close() 
    return changed 

def delete_account_by_email(database_file_name, email): 
    con = sqlite3.connect(database_file_name) 
    deleted = False 
    try : 
        query = f"Delete from User where email='{email}'" 
        cursor = con.cursor() 
        cursor.execute(query)   
        con.commit() 
        deleted = True 
    except : 
        print("An exception occurred") 
    con.close() 
    return deleted 



# current_working_directory=os.getcwd()+"\\" 
# database_file_name=current_working_directory+"data\\movies.db" 
# #insert_one_user(database_file_name,"m@gmail", "1", "mar", "man") 
# print(get_all_user(database_file_name))

# print(get_user_by_email(database_file_name, "123@gmail.com"))