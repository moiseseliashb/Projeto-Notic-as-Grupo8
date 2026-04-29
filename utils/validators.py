import re

def validar_email(email):
    # Verifica se o email tem o formato correto (ex: nome@dominio.com)
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    return False

def validar_senha(password):
    # A senha não pode ser muito curta para ser segura [cite: 120]
    if len(password) >= 6:
        return True
    return False

def validar_dados_registo(dados):
    # Verifica se todos os campos obrigatórios existem 
    campos = ['nome', 'email', 'password']
    for campo in campos:
        if campo not in dados or not dados[campo]:
            return False, f"O campo {campo} é obrigatório!"
    
    if not validar_email(dados['email']):
        return False, "O email inserido não é válido."
        
    return True, "Dados válidos!"