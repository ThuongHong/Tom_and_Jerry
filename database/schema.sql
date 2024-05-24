-- THIS IS FILE TO CREATE DATABASE !!! --

CREATE TABLE "users" (
    "id" INTEGER NOT NULL,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "games" (
    "id" INTEGER NOT NULL,
    "date_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "maze_size" INTEGER NOT NULL CHECK("maze_size" > 0),
    "game_mode" TEXT CHECK("game_mode" IN ('Easy', 'Medium', 'Hard')),
    "energy_mode" INT DEFAULT 0,
    "insane_mode" INT DEFAULT 0,
    "grid_size" INTEGER NOT NULL CHECK("grid_size" > 0),
    "player_skin" TEXT DEFAULT NULL,
    "generate_algorithm" TEXT DEFAULT NULL,
    "is_visualize" INT DEFAULT 0,
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "played" (
    "user_id" INTEGER,
    "game_id" INTEGER,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("game_id") REFERENCES "games"("id")
);

CREATE TABLE "game_saves" (
    "game_id" INTEGER,
    "maze" BLOB NOT NULL, -- Json
    "current_position" TEXT NOT NULL,
    "start_position" TEXT NOT NULL,
    "end_position" TEXT NOT NULL,
    "scale" INT NOT NULL DEFAULT 1,
    "save_state" INT DEFAULT 1, -- mean save if we delete we just change it to 0 i.e Soft delete
    "times" NUMERIC NOT NULL,
    "moves" INT NOT NULL CHECK ("moves" >= 0),
    "energy_info" BLOB DEFAULT NULL,
    "tom_hp" INT DEFAULT 0,
    "theme" INT NOT NULL,
    "background" NOT NULL,
    "spawning_mode" TEXT DEFAULT 'RANDOM',
    FOREIGN KEY("game_id") REFERENCES "games"("id")
);

CREATE TABLE "leaderboard" (
    "game_id" INTEGER,
    "times" REAL NOT NULL CHECK("times" > 0),
    "moves" INTEGER NOT NULL CHECK("moves" > 0),
    FOREIGN KEY("game_id") REFERENCES "games"("id")
);
--------------------------INDEX-----------------------------------
-- -- CREATE INDEX STRUCTURE FOR LESS TIME SEARCH
-- -- We will use username to find in the database so it's will be the first index structure
CREATE INDEX "search_by_name" ON "users"("id");

-- -- Next one we will look to find the relative between users and game
-- -- So the covering index would fine!
CREATE INDEX "search_by_user_id" ON "played"("user_id");
CREATE INDEX "search_by_game_id" ON "played"("game_id");

-- -- One of the things we likely to search most is game_mode
CREATE INDEX "search_by_mode" ON "games"("game_mode");

-- -- Update later

---------------------------VIEW-----------------------------------
-- -- NOT NECESSARY IN THIS PROJECT BUT MAYBE IN REAL LIFE
CREATE VIEW "user_info" AS 
SELECT "id",
        "username",
        'Ambigious' AS "password"
FROM "users";

-- -- CREATE A FULLY SHOW LEADERBOARD TO ACESS EASIER
CREATE VIEW "pure_easy_leaderboard" AS
SELECT "users"."username" AS "user_name", 
        "games"."game_mode" AS "game_mode",
        "games"."energy_mode" AS "energy_mode",
        "leaderboard"."times" AS "times", 
        "leaderboard"."moves" AS "moves"
FROM "users" JOIN "played" ON "users"."id" = "played"."user_id"
JOIN "games" ON "played"."game_id" = "games"."id"
JOIN "leaderboard" ON "leaderboard"."game_id" = "games"."id"
WHERE "game_mode" = 'Easy'
AND "energy_mode" = 0
AND "insane_mode" = 0;

CREATE VIEW "pure_medium_leaderboard" AS
SELECT "users"."username" AS "user_name", 
        "games"."game_mode" AS "game_mode",
        "games"."energy_mode" AS "energy_mode",
        "leaderboard"."times" AS "times", 
        "leaderboard"."moves" AS "moves"
FROM "users" JOIN "played" ON "users"."id" = "played"."user_id"
JOIN "games" ON "played"."game_id" = "games"."id"
JOIN "leaderboard" ON "leaderboard"."game_id" = "games"."id"
WHERE "game_mode" = 'Medium'
AND "energy_mode" = 0
AND "insane_mode" = 0;

CREATE VIEW "pure_hard_leaderboard" AS
SELECT "users"."username" AS "user_name", 
        "games"."game_mode" AS "game_mode",
        "games"."energy_mode" AS "energy_mode",
        "leaderboard"."times" AS "times", 
        "leaderboard"."moves" AS "moves"
FROM "users" JOIN "played" ON "users"."id" = "played"."user_id"
JOIN "games" ON "played"."game_id" = "games"."id"
JOIN "leaderboard" ON "leaderboard"."game_id" = "games"."id"
WHERE "game_mode" = 'Hard'
AND "energy_mode" = 0
AND "insane_mode" = 0;

CREATE VIEW "energy_easy_leaderboard" AS
SELECT "users"."username" AS "user_name", 
        "games"."game_mode" AS "game_mode",
        "games"."energy_mode" AS "energy_mode",
        "leaderboard"."times" AS "times", 
        "leaderboard"."moves" AS "moves"
FROM "users" JOIN "played" ON "users"."id" = "played"."user_id"
JOIN "games" ON "played"."game_id" = "games"."id"
JOIN "leaderboard" ON "leaderboard"."game_id" = "games"."id"
WHERE "game_mode" = 'Easy'
AND "energy_mode" = 1
AND "insane_mode" = 0;

CREATE VIEW "energy_medium_leaderboard" AS
SELECT "users"."username" AS "user_name", 
        "games"."game_mode" AS "game_mode",
        "games"."energy_mode" AS "energy_mode",
        "leaderboard"."times" AS "times", 
        "leaderboard"."moves" AS "moves"
FROM "users" JOIN "played" ON "users"."id" = "played"."user_id"
JOIN "games" ON "played"."game_id" = "games"."id"
JOIN "leaderboard" ON "leaderboard"."game_id" = "games"."id"
WHERE "game_mode" = 'Medium'
AND "energy_mode" = 1
AND "insane_mode" = 0;

CREATE VIEW "energy_hard_leaderboard" AS
SELECT "users"."username" AS "user_name", 
        "games"."game_mode" AS "game_mode",
        "games"."energy_mode" AS "energy_mode",
        "leaderboard"."times" AS "times", 
        "leaderboard"."moves" AS "moves"
FROM "users" JOIN "played" ON "users"."id" = "played"."user_id"
JOIN "games" ON "played"."game_id" = "games"."id"
JOIN "leaderboard" ON "leaderboard"."game_id" = "games"."id"
WHERE "game_mode" = 'Hard'
AND "energy_mode" = 1
AND "insane_mode" = 0;

CREATE VIEW "insane_easy_leaderboard" AS
SELECT "users"."username" AS "user_name", 
        "games"."game_mode" AS "game_mode",
        "games"."energy_mode" AS "energy_mode",
        "leaderboard"."times" AS "times", 
        "leaderboard"."moves" AS "moves"
FROM "users" JOIN "played" ON "users"."id" = "played"."user_id"
JOIN "games" ON "played"."game_id" = "games"."id"
JOIN "leaderboard" ON "leaderboard"."game_id" = "games"."id"
WHERE "game_mode" = 'Easy'
AND "energy_mode" = 0
AND "insane_mode" = 1;

CREATE VIEW "insane_medium_leaderboard" AS
SELECT "users"."username" AS "user_name", 
        "games"."game_mode" AS "game_mode",
        "games"."energy_mode" AS "energy_mode",
        "leaderboard"."times" AS "times", 
        "leaderboard"."moves" AS "moves"
FROM "users" JOIN "played" ON "users"."id" = "played"."user_id"
JOIN "games" ON "played"."game_id" = "games"."id"
JOIN "leaderboard" ON "leaderboard"."game_id" = "games"."id"
WHERE "game_mode" = 'Medium'
AND "energy_mode" = 0
AND "insane_mode" = 1;

CREATE VIEW "insane_hard_leaderboard" AS
SELECT "users"."username" AS "user_name", 
        "games"."game_mode" AS "game_mode",
        "games"."energy_mode" AS "energy_mode",
        "leaderboard"."times" AS "times", 
        "leaderboard"."moves" AS "moves"
FROM "users" JOIN "played" ON "users"."id" = "played"."user_id"
JOIN "games" ON "played"."game_id" = "games"."id"
JOIN "leaderboard" ON "leaderboard"."game_id" = "games"."id"
WHERE "game_mode" = 'Hard'
AND "energy_mode" = 0
AND "insane_mode" = 1;

-- CREATE TRIGGER "delete_game_save"
-- INSTEAD OF DELETE ON "game_saves"
-- FOR EACH ROW
-- BEGIN  
--     UPDATE "game_saves" SET "save_state" = 0
--     WHERE "game_id" = OLD."game_id";
-- END;

--------------SAMPLE DATABASE------------------
-- INSERT INTO "users"("username", "password")
-- VALUES
-- ('fuhoa', 'xinhdep'),
-- ('angela', 'xinkdep');

-- INSERT INTO "games"("maze_size", "game_mode", "energy_mode", "grid_size", "player_skin", "generate_algorithm")
-- VALUES 
-- (20, 'Easy', 1, 30, 'Normal', 'HAK'),
-- (40, 'Medium', 1, 30, 'Normal', 'HAK'),
-- (100, 'Hard', 1, 30, 'Limited S++', 'DFS');

-- INSERT INTO "played"("user_id", "game_id")
-- VALUES
-- (1, 1),
-- (1, 2),
-- (2, 3);

-- -- INSERT INTO 