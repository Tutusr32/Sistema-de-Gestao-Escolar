import sqlite3 

def conectar():
    conn = sqlite3.connect("alunos.db")
    return conn

def set_database():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
    )   
    """)