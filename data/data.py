import json
import sqlite3 # Using this later. May be when merge to develop :>>.
from werkzeug.security import check_password_hash, generate_password_hash

def register(new_username: str, new_password: str):
    # with open("data/user_accounts.json", "r", encoding="utf-8") as f:
    #     data = json.load(f)

    # register_flag = True
    # for user in data: 
    #     if user["username"] == new_username:
    #         register_flag = False
    #         break

    # if register_flag == True:
    #     new_user = {"username": new_username,
    #                 "password": new_password}
    #     data.append(new_user)
    
    #     with open("data/user_accounts.json", "w", encoding="utf-8") as f:
    #         json.dump(data, f, ensure_ascii=False, indent=4)

    # return register_flag

    # FUHOA UPDATE USING DATABASE
    db_connect = sqlite3.connect(r'database/TomJerry.db')

    db_cursor = db_connect.cursor()

    # Check name in Database
    is_name_in_database = db_cursor.execute('SELECT * FROM "users" WHERE "username" = ?', [new_username])
    for r in is_name_in_database: print(r)

    if is_name_in_database: 
        return False
    
    # Check name not in Database
    hash_password = generate_password_hash(new_password)

    db_cursor.execute('INSERT INTO "users"("username", "password") VALUES (?, ?)', ((username,), (hash_password,)))

    db_connect.commit()

    return True

def login(username: str, password: str):
    # with open("data/user_accounts.json", "r", encoding="utf-8") as f:
    #     data = json.load(f)

    # login_flag = False
    # for user in data: 
    #     if user["username"] == username and user["password"] == password:
    #         login_flag = True
    #         break

    # return login_flag
    
    # FUHOA UPDATE USING DATABASE
    db_connect = sqlite3.connect(r'database/TomJerry.db')

    db_cursor = db_connect.cursor()

    # CHECK IF THE USERS EXIST
    is_user_exist = list(db_cursor.execute(f'SELECT "password" FROM "users" WHERE "username" = ?', [username]))
    if is_user_exist:
        if check_password_hash(pwhash= is_user_exist[0][0], password= password):
            return True
    else: return False
