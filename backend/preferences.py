from flask import Blueprint, request, jsonify, session

pref_bp = Blueprint('preferences', __name__)

# Gavetas para guardar as preferências de cada um [cite: 132]
preferencias = {} 
favoritos = {}

@pref_bp.route('/guardar_categoria', methods=['POST'])
def salvar_gosto():
    email = session.get('usuario_logado')
    if not email: return jsonify({"erro": "Quem és tu? Faz login!"}), 401
    
    dados = request.json
    # Guarda o que o utilizador escolheu [cite: 87, 98]
    preferencias[email] = dados.get('categorias', [])
    return jsonify({"status": "Já sei do que gostas!"})

@pref_bp.route('/favorito', methods=['POST'])
def add_favorito():
    email = session.get('usuario_logado')
    if not email: return jsonify({"erro": "Login necessário"}), 401
    
    artigo = request.json.get('artigo')
    if email not in favoritos: favoritos[email] = []
    
    # Guarda a notícia na tua lista especial [cite: 88, 100]
    favoritos[email].append(artigo)
    return jsonify({"status": "Guardado nos teus favoritos!"})