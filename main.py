from flask import Flask, render_template, request, redirect, Response
import os

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html') 
    nome_jogador = request.form('name')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
