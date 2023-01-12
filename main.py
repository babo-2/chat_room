from flask import Flask, jsonify, request, render_template
import json
from datetime import datetime

app = Flask(__name__, static_url_path='/static', static_folder='static')

# this is a list to store the chat messages
messages = []


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/chat", methods=["GET"])
def chat():
    return render_template("chat.html")


@ app.route('/chat/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)


@ app.route('/chat/messages', methods=['POST'])
def add_message():
    j = json.loads(request.get_data())
    message = "[" + datetime.now().strftime("%H:%M:%S") + "] " + \
        j["username"] + ":   " + j["message"]
    messages.append(message)

    return message


if __name__ == '__main__':
    app.run(debug=True, port=80)
    
