import threading
from flask import Flask, request, jsonify
from modules.assistant import VoiceAssistant
from modules.owner import Owner
from modules.record_and_recognize import record_and_recognize_audio, split_phrase

app = Flask(__name__)

assistant = VoiceAssistant('Tyler', 'ru')
owner = Owner("Ivan", 'ru')

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")
    if 'owner' in data:
        owner.name = data['owner']
        print(f"Owner updated to: {owner.name}")
    return jsonify({"status": "success", "data_received": data}), 200

def run_flask():
    app.run(host='0.0.0.0', port=5000)

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