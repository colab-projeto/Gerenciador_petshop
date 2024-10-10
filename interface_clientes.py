import tkinter as tk
from tkinter import messagebox
import sqlite3

# Funções do banco de dados
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

# Funções da Interface Gráfica
def adicionar_cliente_interface():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if not nome or not telefone or not email:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios.")
        return

    if not telefone.isdigit():
        messagebox.showwarning("Erro", "O telefone deve conter apenas números.")
        return

    adicionar_cliente(nome, telefone, email)
    messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
    limpar_campos()
    listar_clientes_interface()

def listar_clientes_interface():
    clientes_cadastrados = listar_clientes()
    output_text.delete(1.0, tk.END)  # Limpa o campo de exibição
    for cliente in clientes_cadastrados:
        output_text.insert(tk.END, f"ID: {cliente[0]}, Nome: {cliente[1]}, Telefone: {cliente[2]}, Email: {cliente[3]}\n")

def atualizar_cliente_interface():
    try:
        cliente_id = int(entry_id.get())
    except ValueError:
        messagebox.showerror("Erro", "O ID deve ser um número válido.")
        return

    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if not nome or not telefone or not email:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios.")
        return

    atualizar_cliente(cliente_id, nome, telefone, email)
    messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
    listar_clientes_interface()

def deletar_cliente_interface():
    try:
        cliente_id = int(entry_id.get())
    except ValueError:
        messagebox.showerror("Erro", "O ID deve ser um número válido.")
        return

    deletar_cliente(cliente_id)
    messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
    listar_clientes_interface()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_id.delete(0, tk.END)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerenciamento de Clientes")
root.geometry("500x600")
root.configure(bg="lightgray")

# Título
label_titulo = tk.Label(root, text="Gerenciamento de Clientes", font=('Helvetica', 16, 'bold'), bg="lightgray")
label_titulo.grid(row=0, column=0, pady=10, padx=10)

# Frame para Adicionar/Atualizar Cliente
frame_adicionar = tk.LabelFrame(root, text="Adicionar/Atualizar Cliente", padx=10, pady=10, bg="lightgray")
frame_adicionar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Labels e Entradas
label_id = tk.Label(frame_adicionar, text="ID (para atualizar/deletar):", bg="lightgray")
label_id.grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame_adicionar)
entry_id.grid(row=0, column=1, padx=5, pady=5)

label_nome = tk.Label(frame_adicionar, text="Nome:", bg="lightgray")
label_nome.grid(row=1, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_adicionar)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

label_telefone = tk.Label(frame_adicionar, text="Telefone:", bg="lightgray")
label_telefone.grid(row=2, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_adicionar)
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

label_email = tk.Label(frame_adicionar, text="Email:", bg="lightgray")
label_email.grid(row=3, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_adicionar)
entry_email.grid(row=3, column=1, padx=5, pady=5)

# Botões para as funcionalidades
botao_adicionar = tk.Button(frame_adicionar, text="Adicionar Cliente", command=adicionar_cliente_interface, bg="lightblue", font=('Arial', 12))
botao_adicionar.grid(row=4, column=0, columnspan=2, pady=10)

botao_atualizar = tk.Button(frame_adicionar, text="Atualizar Cliente", command=atualizar_cliente_interface, bg="lightgreen", font=('Arial', 12))
botao_atualizar.grid(row=5, column=0, columnspan=2, pady=10)

botao_deletar = tk.Button(frame_adicionar, text="Deletar Cliente", command=deletar_cliente_interface, bg="lightcoral", font=('Arial', 12))
botao_deletar.grid(row=6, column=0, columnspan=2, pady=10)

# Frame para Lista de Clientes
frame_lista = tk.LabelFrame(root, text="Clientes Cadastrados", padx=10, pady=10, bg="lightgray")
frame_lista.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Scrollbar e Text Widget para listagem
scrollbar = tk.Scrollbar(frame_lista)
scrollbar.grid(row=0, column=1, sticky='ns')

output_text = tk.Text(frame_lista, height=10, width=50, yscrollcommand=scrollbar.set)
output_text.grid(row=0, column=0)
scrollbar.config(command=output_text.yview)

# Rodar a interface
listar_clientes_interface()  # Exibir os clientes já cadastrados
root.mainloop()
