import requests

# Esta é a tua chave mágica para entrar na NewsAPI [cite: 45]
API_KEY = 'TUA_CHAVE_AQUI'
URL_BASE = "https://newsapi.org/v2/top-headlines"

def obter_noticias(categoria="general"):
    # O mensageiro prepara o pedido 
    parametros = {
        'apiKey': API_KEY,
        'category': categoria,
        'language': 'pt'
    }
    
    try:
        resposta = requests.get(URL_BASE, params=parametros)
        dados = resposta.json()
        # Ele devolve a lista de notícias 
        return dados.get('articles', [])
    except:
        # Se o mensageiro tropeçar, ele avisa [cite: 52]
        return []

# FUNCIONALIDADE INTELIGENTE: Um resumo muito simples [cite: 71, 112]
def criar_resumo_inteligente(texto):
    if not texto: return "Sem descrição disponível."
    return texto[:100] + " (Resumo da IA...)"