from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-tarefa")
def get_tarefa():
  resposta = requests.get("https://quote-generator-api-six.vercel.app/api/quotes/?limit=1")

  return jsonify(resposta.json())

if __name__ == "__main__":
  app.run()
