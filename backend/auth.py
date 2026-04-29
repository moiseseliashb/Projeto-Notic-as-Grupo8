from flask import Blueprint, request, session, jsonify
from flask_bcrypt import Bcrypt # Precisas de: pip install flask-bcrypt [cite: 55]

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

# O nosso livro de registos (no futuro será uma base de dados) [cite: 132]
utilizadores = {} 

@auth_bp.route('/registo', methods=['POST'])
def registar():
    dados = request.json
    # Esconde a palavra-passe para ninguém roubar [cite: 55, 120]
    senha_segura = bcrypt.generate_password_hash(dados['password']).decode('utf-8')
    
    utilizadores[dados['email']] = {
        'nome': dados['nome'],
        'password': senha_segura
    }
    return jsonify({"status": "Conta criada! Podes entrar."})

@auth_bp.route('/login', methods=['POST'])
def entrar():
    dados = request.json
    user = utilizadores.get(dados['email'])
    
    # O guarda verifica se a chave bate com o segredo [cite: 55, 83]
    if user and bcrypt.check_password_hash(user['password'], dados['password']):
        session['usuario_logado'] = dados['email'] # Lembra-se de ti [cite: 85]
        return jsonify({"status": "Bem-vindo!"})
    
    return jsonify({"erro": "Chave errada!"}), 401