CREATE TABLE 'game_save' (
    'id' INTEGER,
    'times' REAL CHECK('times' > 0),
    'moves' INTEGER CHECK('moves' > 0),
    PRIMARY KEY('id' AUTOINCREMENT)
)