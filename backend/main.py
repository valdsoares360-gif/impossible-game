import random
import time
import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)






conn = sqlite3.connect("game.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS game_stats (
    id INTEGER PRIMARY KEY,
    tries INTEGER
)
""")


cursor.execute("SELECT * FROM game_stats WHERE id = 1")
if cursor.fetchone() is None:
    cursor.execute("INSERT INTO game_stats (id, tries) VALUES (1, 0)")
    conn.commit()


def add_try():
    cursor.execute("""
    UPDATE game_stats
    SET tries = tries + 1
    WHERE id = 1
    """)
    conn.commit()


@app.post("/game")
def play_game(player1: int, player2: int):

    machine = random.randint(1, 100)

    add_try()

    if player1 == player2 and player1 == machine:
        return {"result": f"yall win! Machine chose {machine}"}
    elif player1 != player2:
        return {"result": f"yall chose different numbers! Machine chose {machine}"}
    
    else:
        return {"result": f"yall lose! Machine chose {machine}"}


@app.get("/tries")
def get_tries():
    cursor.execute("SELECT tries FROM game_stats WHERE id = 1")
    tries = cursor.fetchone()[0]

    return {"tries": tries}