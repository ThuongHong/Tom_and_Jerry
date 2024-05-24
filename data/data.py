import json
import sqlite3  # Using this later. May be when merge to develop :>>.
from werkzeug.security import check_password_hash, generate_password_hash
import pygame
from os import remove

def register(new_username: str, new_password: str):
    db_connect = sqlite3.connect(r"database/TomJerry.db")

    db_cursor = db_connect.cursor()

    # Check name in Database
    is_name_in_database = list(
        db_cursor.execute('SELECT * FROM "users" WHERE "username" = ?', [new_username])
    )

    # Check name not in Database
    if is_name_in_database:
        return [False, None]

    hash_password = str(generate_password_hash(new_password))

    db_cursor.execute(
        'INSERT INTO "users"("username", "password") VALUES(?, ?)',
        (new_username, hash_password),
    )

    user_id = list(
        db_cursor.execute(
            f'SELECT "id" FROM "users" WHERE "username" = ?', [new_username]
        )
    )[0][0]

    db_connect.commit()

    return [True, user_id]


def login(username: str, password: str):
    # FUHOA UPDATE USING DATABASE
    db_connect = sqlite3.connect(r"database/TomJerry.db")

    db_cursor = db_connect.cursor()

    # CHECK IF THE USERS EXIST
    is_user_exist = list(
        db_cursor.execute(
            f'SELECT "password" FROM "users" WHERE "username" = ?', [username]
        )
    )
    if is_user_exist:
        if check_password_hash(pwhash=is_user_exist[0][0], password=password):
            user_id = list(
                db_cursor.execute(
                    f'SELECT "id" FROM "users" WHERE "username" = ?', [username]
                )
            )[0][0]
            # print(True, user_id)
            return [True, user_id]

    return [False, None]


def get_saved_game(user_id: int):
    """Return a list of game_id and image

    Args:
        user_id (int): description

    Returns:
        type: list of all thing we need
    """
    db_connect = sqlite3.connect(r"database/TomJerry.db")

    db_cursor = db_connect.cursor()

    saved_game_ids = list(
        db_cursor.execute(
            """
            SELECT "game_id", "times", "moves", "background", "theme", "spawning" FROM "game_saves"
            WHERE "game_id" IN (
                SELECT "game_id" FROM "played"
                WHERE "user_id" = ?
            )
            AND save_state = 1
            """,
            ([user_id])
        )
    )

    # format_game_ids = [saved_game_ids[i][0] for i in range(len(saved_game_ids))]
    game_saves_data = []

    for i in range(len(saved_game_ids)):
        game_id = saved_game_ids[i][0]

        time = saved_game_ids[i][1]
        time = f"{str(int(time / 1000))} s"

        steps = saved_game_ids[i][2]

        background = saved_game_ids[i][-3]

        theme = saved_game_ids[i][-2]

        spawn_mode = saved_game_ids[i][-1]

        try:
            single_data_row = []

            # Game Id
            # single_data_row.append(game_id)
            single_data_row.extend([game_id, time, steps])
            # Mode
            single_data_row.extend(
                list(
                    db_cursor.execute(
                        """
                        SELECT "game_mode", "energy_mode", "insane_mode", "generate_algorithm", "is_visualize" FROM "games"
                        WHERE "id" = ?
                        """,
                        ([game_id]),
                    )
                )[0]
            )
            # Background and Theme and Spawning_mode
            single_data_row.extend([background, theme, spawn_mode])

            game_saves_data.append(single_data_row)
        except FileNotFoundError:
            continue

    return game_saves_data


def remove_game_save(game_id: int):
    db_connect = sqlite3.connect(r"database/TomJerry.db")

    db_cursor = db_connect.cursor()

    db_cursor.execute(
        """
        UPDATE "game_saves"
        SET "save_state" = 0
        WHERE "game_id" = ?
        """,
        ([game_id]),
    )
    saved_image_path = f"database/save_game_images/Game_{game_id}.png"
    remove(saved_image_path)

    db_connect.commit()


def leaderboard(mode: str) -> list:
    db_connect = sqlite3.connect(r"database/TomJerry.db")

    db_cursor = db_connect.cursor()

    if mode.upper() == "PUREEASY": board = "pure_easy_leaderboard"
    elif mode.upper() == "PUREMEDIUM": board = "pure_medium_leaderboard"
    elif mode.upper() == "PUREHARD": board = "pure_hard_leaderboard"
    elif mode.upper() == 'ENERGYEASY': board = "energy_easy_leaderboard"
    elif mode.upper() == 'ENERGYMEDIUM': board = "energy_medium_leaderboard"
    elif mode.upper() == 'ENERGYHARD': board = "energy_hard_leaderboard"
    elif mode.upper() == 'INSANEEASY': board = "insane_easy_leaderboard"
    elif mode.upper() == 'INSANEMEDIUM': board = "insane_medium_leaderboard"
    elif mode.upper() == 'INSANEHARD': board = "insane_hard_leaderboard"

    # ----- OLD -------------------------------------------------#
    # leaderboard_data = list(
    #     db_cursor.execute(
    #         f"""
    #     SELECT  "user_name", "times", "moves" FROM {board}
    #     ORDER BY "moves" ASC, "times" ASC;
    # """
    #     )
    # )

    # ----- NEW -------------------------------------------------#
    leaderboard_data = list(
        db_cursor.execute(
            f"""
            SELECT  "user_name", "times", "moves", "score" FROM {board}
            ORDER BY "score" DESC;
            """
        )
    )

    return leaderboard_data


# if __name__ == '__main__':
#     pygame.init()
#     sc = pygame.display.set_mode((100, 100))
#     print(get_img_and_game_id_load_game(3))
