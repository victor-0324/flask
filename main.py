from flask import Flask, render_template, request, redirect, Response
import os

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def index():
    # nome_jogador = request.form('name')
    return render_template('index.html') 
    
# Tela Das Cartelas
@app.route("/cartela", methods=["GET","POST"])
def cartela():
    usuario = request.form.get('name')
    return render_template("/cartela.html",nome=usuario.upper())



# Tela do jogo da velha 
@app.route("/jogodavelha", methods=["GET","POST"])
def velha():
    usuarios1 = request.form.get('name')
    return render_template("/")




# Tela do narrador 
@app.route("/narrador/")
def narrador():
    return render_template('/narrador.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
