import sqlite3
import typing

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


con: sqlite3.Connection = sqlite3.connect("visitors.db")
app: FastAPI = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_count() -> int:
    cur: sqlite3.Cursor = con.cursor()
    res: sqlite3.Cursor = cur.execute("SELECT COUNT(v.id) FROM visitors v")
    return res.fetchone()[0]

@app.get("/")
async def read_root():
    return { "We're": "Alive" }

@app.get("/create_tables")
async def create_tables() -> dict[str, str]:
    cur: sqlite3.Cursor = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visitors(id INTEGER PRIMARY KEY AUTOINCREMENT)")
    return {"Success": "0"}

@app.get("/visCount")
async def visitor_count() -> dict[str, typing.Any]:
    return { "visitors": get_count() }

@app.get("/visit")
async def visit() -> dict[str, str]:
    cur: sqlite3.Cursor = con.cursor()
    cur.execute("INSERT INTO visitors(id) DEFAULT VALUES")
    return {"Success": "0"}