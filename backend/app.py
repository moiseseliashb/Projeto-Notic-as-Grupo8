from flask import Flask, render_template
#from auth import auth_bp
#from preferences import pref_bp
#from news_api import obter_noticias

app = Flask(__name__)
#app.secret_key = "segredo_do_ipil_2026" # Chave para as sessões [cite: 85]

# O Chefe chama os seus ajudantes 
#app.register_blueprint(auth_bp)
#app.register_blueprint(pref_bp)

@app.route('/')
def pagina_principal():
    # O Chefe pede notícias ao Mensageiro para mostrar na entrada [cite: 92]
   # noticias = obter_noticias("technology")
    return render_template('index.html')
    #return render_template('index.html', news=noticias)


if __name__ == '__main__':
    # Liga o motor da aplicação!
    app.run(debug=True)