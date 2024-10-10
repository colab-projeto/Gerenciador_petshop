import sqlite3
conn = sqlite3.connect('petshop.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especie TEXT NOT NULL,
    raca TEXT,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    hora TEXT NOT NULL,
    pet_id INTEGER,
    FOREIGN KEY (pet_id) REFERENCES Pets(id)
)
''')



print("Banco de dados e tabelas criados com sucesso!")

