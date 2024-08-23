# Standart modules
import sys
import threading

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

def main():
    """Main function"""

    while True:
        voice_input = record_and_recognize_audio()
        commands_list, command_options_list = split_phrase(voice_input)

        for i, command in enumerate(commands_list):
            assistant.recognize_and_execute_command(command, command_options_list[i])


if __name__ == "__main__":
    main()
