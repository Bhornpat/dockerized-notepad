from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
def startup():
    conn = sqlite3.connect("notes.db")
    conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")
    conn.close()

@app.get("/notes")
def get_notes():
    conn = sqlite3.connect("notes.db")
    rows = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()
    return [{"id": row[0], "text": row[1]} for row in rows]

@app.post("/notes")
async def create_note(request: Request):
    body = await request.json()
    text = body.get("text", "")
    conn = sqlite3.connect("notes.db")
    conn.execute("INSERT INTO notes (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()
    return {"status": "ok"}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    conn = sqlite3.connect("notes.db")
    conn.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()
    return {"status": "deleted"}

