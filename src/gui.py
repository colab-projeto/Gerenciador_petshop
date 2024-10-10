import tkinter as tk
from tkinter import messagebox
from database import add_cliente, remove_cliente, list_clientes


def start_gui():
    root = tk.Tk()
    root.title("Gerenciador Petshop")

    # Frames para organização
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Campos de entrada
    tk.Label(frame, text="Nome:").grid(row=0, column=0)
    entry_nome = tk.Entry(frame)
    entry_nome.grid(row=0, column=1)

    tk.Label(frame, text="Telefone:").grid(row=1, column=0)
    entry_telefone = tk.Entry(frame)
    entry_telefone.grid(row=1, column=1)

    tk.Label(frame, text="Email:").grid(row=2, column=0)
    entry_email = tk.Entry(frame)
    entry_email.grid(row=2, column=1)

    tk.Label(frame, text="Endereço:").grid(row=3, column=0)
    entry_endereco = tk.Entry(frame)
    entry_endereco.grid(row=3, column=1)

    # Função para adicionar cliente
    def add_cliente_gui():
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        endereco = entry_endereco.get()
        add_cliente(nome, telefone, email, endereco)
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")

    # Botão para adicionar cliente
    btn_add = tk.Button(frame, text="Adicionar Cliente", command=add_cliente_gui)
    btn_add.grid(row=4, columnspan=2)

    # Função para listar clientes
    def show_clientes():
        clientes = list_clientes()
        clientes_str = "\n".join([f"{cliente[0]}: {cliente[1]}" for cliente in clientes])
        messagebox.showinfo("Lista de Clientes", clientes_str)

    # Botão para listar clientes
    btn_list = tk.Button(frame, text="Listar Clientes", command=show_clientes)
    btn_list.grid(row=5, columnspan=2)

    # Função para remover cliente
    def remove_cliente_gui():
        cliente_id = entry_nome.get()  # Usando o nome como exemplo, idealmente seria um campo separado para ID
        remove_cliente(cliente_id)
        messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")

    # Botão para remover cliente
    btn_remove = tk.Button(frame, text="Remover Cliente", command=remove_cliente_gui)
    btn_remove.grid(row=6, columnspan=2)

    root.mainloop()

