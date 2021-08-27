from flask import Flask, request
import requests
import config.vault as vault
from integration.telegram import TelegramIntegration, handle_webhook_event

app = Flask(__name__)
token = vault.secret['token']
telegram = TelegramIntegration(token)

@app.route('/', methods=['GET'])
def index():
    return "O Servidor está no AR."

@app.route('/events-listener', methods=['POST'])
def events_listener():
    body = request.get_json()
    chat_id, msg_from_name, msg, shouldRespond = handle_webhook_event(body)
    if shouldRespond:
         telegram.send_text_message(body["message"]["chat"]["id"], "Olá Transeunte Virtual, eu sou o EccoBot e estou aprendendo!!!")
    return 'Ok'            
    print(body) 

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")