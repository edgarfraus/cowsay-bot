import requests
from flask import Flask, request

app = Flask(__name__)

# Token del tuo bot
TOKEN = '6166416132:AAHzTqLQJ-x7l5b9hbYdBLsp7NANiUjiIZw'

# URL dell'API di Telegram per l'invio dei messaggi
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# Funzione per gestire i messaggi ricevuti
def handle_message(message_text):
    # Esegui qui la generazione del "Cowsay" con il testo ricevuto
    cowsay_text = f" {message_text}\n  \\   ^__^\n   \\  (oo)\\_______\n      (__)\\       )\\/\\\n          ||----w |\n          ||     ||"

    return cowsay_text

@app.route(f'/{TOKEN}', methods=['POST'])
def respond():
    data = request.json
    chat_id = data['message']['chat']['id']
    message_text = data['message']['text']

    response_text = handle_message(message_text)

    # Invia la risposta al chat ID
    response = requests.post(URL, json={'chat_id': chat_id, 'text': response_text})

    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
