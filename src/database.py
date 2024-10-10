import sqlite3


def connect_db():
    conn = sqlite3.connect('petshop.db')
    return conn


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS CLIENTES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT NOT NULL,
        TELEFONE TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        ENDERECO TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS PETS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT NOT NULL,
        TIPO TEXT NOT NULL,
        RACA TEXT NOT NULL,
        ID_CLIENTE INTEGER,
        FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS AGENDAMENTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_AGENDAMENTO INTEGER,
        DATA TEXT NOT NULL,
        HORARIO TEXT NOT NULL,
        SERVIÇO TEXT NOT NULL,
        ID_CLIENTE INTEGER,
        FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID)
    )''')

    conn.commit()
    conn.close()


def add_cliente(nome, telefone, email, endereco):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO CLIENTES (NOME, TELEFONE, EMAIL, ENDERECO) VALUES (?, ?, ?, ?)',
                   (nome, telefone, email, endereco))
    conn.commit()
    conn.close()


def remove_cliente(cliente_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM CLIENTES WHERE ID = ?', (cliente_id,))
    conn.commit()
    conn.close()


def list_clientes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM CLIENTES')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

