from flask import Flask, request
import requests
import config.vault as vault

app = Flask(__name__)

token = vault.secret['token']

def fui_mencionado(body):
    if ("@eccodando_bot" in body['message']['text']):
        return True
    else:
        return False


url_sendMessage = f"https://api.telegram.org/bot{token}/sendMessage"

@app.route('/', methods=['GET'])
def index():
    return "O Servidor está no AR."

@app.route('/events-listener', methods=['POST'])
def event_listener():
    
    body = request.get_json()
    
    print(body)
    if "message" in body:
        dados = {'chat_id': body["message"]["chat"]["id"], 'text' : "Olá Transeunte Virtual, eu sou o EccoBot e estou aprendendo!!!"}
        primeiro_nome = body['message']['from']['first_name']
        print(f"Recebi um evento de: {primeiro_nome}")
        if body["message"]["chat"]["type"] == "private":
                    
                    print(f"Mandando msg para {primeiro_nome}")
                    requests.post(url_sendMessage, dados).json()
                    return 'Ok'

        if fui_mencionado(body):
            print("Respondendo a mensagem que fui mencionado")
            requests.post(url_sendMessage, dados).json()
            return 'OK'
        
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")