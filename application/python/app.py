# Standart modules
import sys
import threading

# Flask
from flask import Flask, request, jsonify
from flask_cors import CORS

# Local modules
from modules.assistant import VoiceAssistant
from modules.owner import Owner
from modules.record_and_recognize import record_and_recognize_audio, split_phrase

# command-line arguments:
# -o [owner_name]
# -a [assistant_name]
# -l [language ru/en]
# e.g. app -o Ivan -a Tayler -l ru

# set defaults
owner_name = "Ivan"
assistant_name = "Tayler"
language = "ru"

# processing command-line arguments
argv = sys.argv
for i, arg in enumerate(argv):
    if arg == '-o' and i + 1 < len(argv):
        owner_name = argv[i + 1]
    if arg == '-a' and i + 1 < len(argv):
        assistant_name = argv[i + 1]
    if arg == '-l' and i + 1 < len(argv):
        language = argv[i + 1]

assistant = VoiceAssistant(assistant_name, language)
owner = Owner(owner_name, language)

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['POST'])
def receive_data():
    """Function for receiving data from gui app"""

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
    except Exception as e:
        print(f"Error {e}")

    print(f"Received data: {data}")
    return jsonify({"status": "success", "data_received": data}), 200

def run_flask():
    """Function for start flask session"""

    app.run(host='localhost', port=5000)

def main():
    """Main function"""

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    while True:
        voice_input = record_and_recognize_audio()
        commands_list, command_options_list = split_phrase(voice_input)

        for i, command in enumerate(commands_list):
            assistant.recognize_and_execute_command(command, command_options_list[i])


if __name__ == "__main__":
    main()
