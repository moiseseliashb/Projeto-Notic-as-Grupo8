def gerar_resumo_noticia(texto_original):
    """
    Funcionalidade Inteligente: Resumo automático 
    Podes ligar isto a uma API como a do Gemini ou OpenAI mais tarde.
    """
    if not texto_original or len(texto_original) < 50:
        return "Notícia muito curta para resumir."
    
    # Simulação de IA: Pega nas primeiras frases importantes
    resumo = texto_original.split('.')[0] + "."
    return f"✨ Resumo IA: {resumo}"

def recomendar_artigos(preferencias_user, lista_noticias):
    """
    Funcionalidade Inteligente: Recomendação personalizada [cite: 73, 113]
    """
    recomendados = []
    for artigo in lista_noticias:
        # Se a categoria do artigo estiver nos gostos do utilizador [cite: 106]
        if artigo.get('category') in preferencias_user:
            recomendados.append(artigo)
            
    return recomendados[:3] # Devolve as 3 melhores sugestões