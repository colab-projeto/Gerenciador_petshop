def validate_cliente_data(nome, telefone, email, endereco):
    if not nome or not telefone or not email or not endereco:
        return false
    return true