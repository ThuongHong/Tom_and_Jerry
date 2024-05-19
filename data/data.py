import json
import sqlite3 # Using this later. May be when merge to develop :>>.
from werkzeug.security import check_password_hash, generate_password_hash
import pygame
from os.path import join

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
    # new_username = str(new_username)
    # new_password = str(new_password)
    db_connect = sqlite3.connect(r'database/TomJerry.db')

    db_cursor = db_connect.cursor()

    # Check name in Database
    is_name_in_database = list(db_cursor.execute('SELECT * FROM "users" WHERE "username" = ?', [new_username]))
        
    # Check name not in Database
    if is_name_in_database:
        return [False, None]
    
    hash_password = str(generate_password_hash(new_password))

    db_cursor.execute('INSERT INTO "users"("username", "password") VALUES(?, ?)', (new_username, hash_password))
    
    user_id = list(db_cursor.execute(f'SELECT "id" FROM "users" WHERE "username" = ?', [new_username]))[0][0]

    db_connect.commit()
    
    return [True, user_id]

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
            user_id = list(db_cursor.execute(f'SELECT "id" FROM "users" WHERE "username" = ?', [username]))[0][0]
            print(True, user_id)
            return [True, user_id]
    
    return [False, None]

def get_img_and_game_id_load_game(user_id: int):
    """Return a list of game_id and image

    Args:
        user_id (int): _description_

    Returns:
        _type_: _description_
    """
    db_connect = sqlite3.connect(r'database/TomJerry.db')

    db_cursor = db_connect.cursor()

    saved_game_ids = list(
        db_cursor.execute(
            '''
            SELECT "game_id" FROM "game_saves"
            WHERE "game_id" IN (
                SELECT "game_id" FROM "played"
                WHERE "user_id" = ? AND save_state = 1
            )
            ''',
            ([user_id])
        )
    )

    format_game_ids = [saved_game_ids[i][0] for i in range(len(saved_game_ids))]
    print(format_game_ids)

    saved_game_ids = []
    game_images = []
    
    for game_id in format_game_ids:
        try:
            img = pygame.image.load(join('database', 'save_game_images', 'Game_' + str(game_id) + '.png')).convert_alpha()
            # return img
            saved_game_ids.append(game_id)
            game_images.append(img)
        except FileNotFoundError:
            pass
    return list(zip(saved_game_ids, game_images))

def remove_game_save(game_id: int):
    db_connect = sqlite3.connect(r'database/TomJerry.db')

    db_cursor = db_connect.cursor()

    db_cursor.execute(
        '''
        UPDATE "game_saves"
        SET "save_state" = 0
        WHERE "game_id" = ?
        ''',
        ([game_id])
    )

    db_connect.commit()

def leaderboard(mode: str) -> list:
    db_connect = sqlite3.connect(r'database/TomJerry.db')

    db_cursor = db_connect.cursor()

    if mode.upper() == 'EASY':
        board = 'easy_leaderboard'
    elif mode.upper() == 'MEDIUM':
        board = 'medium_leaderboard'
    elif mode.upper() == 'HARD':
        board = 'hard_leaderboard'


    leaderboard_data = list(db_cursor.execute(F'''
        SELECT  "user_name", "times", "moves" FROM {board}
        ORDER BY moves ASC, times ASC;
    '''))

    return leaderboard_data