from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only! Use specific origin in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auto-create DB table if not exists
@app.on_event("startup")
def startup():
    conn = sqlite3.connect("notes.db")
    conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)")
    conn.commit()
    conn.close()

@app.get("/notes")
def get_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.execute("SELECT id, text FROM notes")
    notes = [{"id": row[0], "text": row[1]} for row in cursor.fetchall()]
    conn.close()
    return notes

@app.post("/notes")
async def add_note(request: Request):
    data = await request.json()
    text = data.get("text", "")
    conn = sqlite3.connect("notes.db")
    conn.execute("INSERT INTO notes (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()
    return {"status": "ok", "text": text}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    conn = sqlite3.connect("notes.db")
    conn.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()
    return {"status": "deleted", "id": note_id}

