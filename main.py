"""BackEnd Principal

Retorna a frase aleatória gerada em um JSON

Rotas:
    /: Ponto inicial
    /get-tarefa: Retorna a tarefa ao acessar

Dev: Anna
Github: https://github.com/0xAA55-P
Data de atualização: 16/05/2026
"""

from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get-tarefa")
def get_tarefa():
    try:
        resposta = requests.get(
            "https://quote-generator-api-six.vercel.app/api/quotes/?limit=1", timeout=5
        )

        if resposta.status_code != 200:
            return {}

        return jsonify(resposta.json())

    except requests.Timeout:
        return {}


if __name__ == "__main__":
    app.run()
