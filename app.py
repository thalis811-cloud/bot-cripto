from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def enviar_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

@app.route("/")
def home():
    return "ok"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    msg = f"""
ALERTA RECEBIDO

Moeda: {data.get("moeda")}
Preço: {data.get("preco")}
RSI: {data.get("rsi")}
Volume: {data.get("volume")}
Tempo: {data.get("tempo")}
Contexto: {data.get("contexto")}
"""

    enviar_telegram(msg)

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
