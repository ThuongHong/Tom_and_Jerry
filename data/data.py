import json

def register(new_username: str, new_password: str):
    with open("data/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    register_flag = True
    for user in data: 
        if user["username"] == new_username:
            register_flag = False
            break

    if register_flag == True:
        new_user = {"username": new_username,
                    "password": new_password}
        data.append(new_user)
    
        with open("data/data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    return register_flag


def login(username: str, password: str):
    with open("data/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    login_flag = False
    for user in data: 
        if user["username"] == username and user["password"] == password:
            login_flag = True
            break

    return login_flag



