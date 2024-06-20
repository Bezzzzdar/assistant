import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.assistant import VoiceAssistant
from modules.owner import Owner
from modules.record_and_recognize import record_and_recognize_audio, split_phrase

app = Flask(__name__)
CORS(app)

assistant = VoiceAssistant('Tyler', 'ru')
owner = Owner("Ivan", 'ru')

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    try:
        if 'owner_name' in data:
            owner.change_owner_name(data['owner_name'])
        elif 'owner_language' in data:
            owner.change_owner_language(data['owner_language'])
        elif 'assistant_name' in data:
            assistant.change_assistant_name(data['assistant_name'])
        elif 'assistant_language' in data:
            assistant.change_assistant_language(data['assistant_language'])
    except:
        pass

    print(f"Received data: {data}")
    return jsonify({"status": "success", "data_received": data}), 200

def run_flask():
    app.run(host='localhost', port=5000)

def main():
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    while True:
        voice_input = record_and_recognize_audio()
        commands_list, command_options_list = split_phrase(voice_input)
        
        for i in range(len(commands_list)):
            assistant.execute_command(commands_list[i], command_options_list[i])

if __name__ == "__main__":
    main()