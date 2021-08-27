import requests

class TelegramIntegration():

    def __init__(self, token):
        self.__token = token
        self.__url_sendMessage = f"https://api.telegram.org/bot{token}/sendMessage"

    @property
    def url_sendMessage(self):
        return self.__url_sendMessage

    def send_text_message(self, chat_id, text):
        dados = {'chat_id': chat_id, 'text' : text}
        requests.post(self.__url_sendMessage, dados).json()

def been_mentioned(event):
    if "text" in event['message']:
        if ("@eccodando_bot" in event['message']['text']):
            return True
        else:
            return False
    else:
        return False


def handle_webhook_event(event):
    # Função para tratar todas as regras do webhook de notificação do telegram. 
    # Extrair os dados relevantes para nosso contexto.
    
    # example = {
    #     'update_id': 456543247, 
    #     'message': {
    #         'message_id': 48, 
    #         'from': {
    #             'id': 204711477, 
    #             'is_bot': False, 
    #             'first_name': 'Claudio', 
    #             'last_name': 'Moura', 
    #             'username': 'ccpmoura', 
    #             'language_code': 'pt-br'
    #         }, 
    #         'chat': {
    #             'id': 204711477, 
    #             'first_name': 'Claudio', 
    #             'last_name': 'Moura', 
    #             'username': 'ccpmoura', 
    #             'type': 'private'
    #         }, 
    #         'date': 1630018599, 
    #         'text': 'Ola'
    #     }
    # }

    if 'message' in event:
        chat_id = event['message']['chat']['id']
        msg_from_name = event['message']['from']['first_name']
        msg = event['message']['text'] if 'text' in event['message'] else 'no_text'
    # Checando se é msg de grupo e só retornando se tiver sido mencionado
    if event["message"]["chat"]["type"] == "private":
        return chat_id, msg_from_name, msg, True
    else:
        if been_mentioned(event):
            return chat_id, msg_from_name, msg, True
        else:
            return chat_id, msg_from_name, msg, False



    