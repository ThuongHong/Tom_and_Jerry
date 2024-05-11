import sqlite3
def str_to_tuple(encode_str: str) -> tuple[int]:
    x, y = encode_str.lstrip('(').rstrip(')').split(',')
    return (int(x), int(y))

if __name__ == '__main__':
    db = sqlite3.connect(r'database/TomJerry.db').cursor()
    name = 'hoa'
    user_in_data = list(db.execute(f'''SELECT "password" FROM "users" WHERE "username" = {name}'''))

    if user_in_data:
        print('hehe')
    # db.execute('''INSERT INTO "games"("maze_size", "game_mode", "energy_mode", "grid_size", "player_skin", "generate_algorithm")
    #     VALUES (?, ?, ?, ?, ?, ?)
    #     ''',
    #     20 +
    #     'Normal' +
    #     0 +
    #     30 +
    #     'S++' +
    #     'HAK'
    #     )
    # db.close()


