import json
import pathlib
import pyttsx3

class VoiceAssistant:
    name = ""
    sex = ""
    language = ""

assistant = VoiceAssistant()
ttsEngine = pyttsx3.init()

class Commands:
    def __init__(self, greatings_examples: str, greatings_responses: str, farewell_examples: str, farewell_responses: str):
        self.greatings_examples     = greatings_examples
        self.greatings_responses    = greatings_responses
        self.farewell_examples      = farewell_examples
        self.farewell_responses     = farewell_responses
        
class CommandsDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    
    def object_hook(self, json_dict: dict):
        new_commands = Commands(
            json_dict.get('greetings', 'examples'),
            json_dict.get('greetings', 'responses'),
            json_dict.get('farewell', 'examples'),
            json_dict.get('farewell', 'responses')
        )
        return new_commands

def setup_voice_assistant(name: str, sex: str, language: str):

    assistant.name = name
    assistant.sex = sex
    assistant.language = language

    voices = ttsEngine.getProperty('voices')

    if language == 'ru':
        if sex == 'male':
            ttsEngine.setProperty('voice', voices[0].id)
            ttsEngine.setProperty('rate', 170)

def assistant_say(text):
    ttsEngine.say(str(text))
    ttsEngine.runAndWait()

def execute_command(speech: str):
    with open(pathlib.Path( './app', 'commands', 'commands.json'), "r") as file:
        commands = json.load(file, cls=CommandsDecoder)
    speech = speech.split(" ")

        


