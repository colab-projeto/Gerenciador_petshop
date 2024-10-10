import sqlite3

def conectar():
    """Conecta ao banco de dados."""
    return sqlite3.connect('petshop.db')

def adicionar_cliente(nome, telefone, email):
    """Adiciona um novo cliente."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    conn.close()

def listar_clientes():
    """Lista todos os clientes."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes_list = cursor.fetchall()
    conn.close()
    return clientes_list

def atualizar_cliente(cliente_id, nome, telefone, email):
    """Atualiza as informações de um cliente existente."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Clientes SET nome = ?, telefone = ?, email = ? WHERE id = ?", (nome, telefone, email, cliente_id))
    conn.commit()
    conn.close()

def deletar_cliente(cliente_id):
    """Deleta um cliente pelo ID."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (cliente_id,))
    conn.commit()
    conn.close()

# Testando as funções
if __name__ == "__main__":
    try:
        # Aqui você pode adicionar clientes para teste, se necessário
        # Exemplo: adicionar_cliente('João Silva', '123456789', 'joao@email.com')
        pass
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
