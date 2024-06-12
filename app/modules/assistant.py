import pyttsx3
import sys

class Owner:
    def __init__(self, name: str, language: str) -> None:
        Owner.name = name
        Owner.language = language
                
class VoiseAssistant:
    def __init__(self, name: str, language: str) -> None:
        VoiseAssistant.name      = name
        VoiseAssistant.language  = language
        from modules.commands import Commands
        self.commands  = Commands()
        self.commands_dict = Commands.dictionary(self.commands)

        VoiseAssistant.Engine = pyttsx3.init()
        voices = self.Engine.getProperty('voices')
    
        if self.name == 'Tyler':
            if self.language == 'ru':
                self.Engine.setProperty('voice', voices[0].id)
                self.Engine.setProperty('rate', 170)
            elif self.language == 'en':
                # TODO: set english language
                self.Engine.setProperty('voice', voices[0].id) 
                self.Engine.setProperty('rate', 170)
             
        elif self.name == 'Marla':
            # TODO: set women voise
            if self.language == 'ru':
                self.Engine.setProperty('voice', voices[0].id)
                self.Engine.setProperty('rate', 170)
            elif self.language == 'en':
                # TODO: set english language
                self.Engine.setProperty('voice', voices[0].id) 
                self.Engine.setProperty('rate', 170)
    
    def assistant_say(self, text: str) -> None:
        self.Engine.say(text)
        self.Engine.runAndWait()
    
    def execute_command(self, command: str, *args: list) -> None:
        for key in self.commands_dict.keys():
            if command in key:
                self.commands_dict[key](*args)
            else:
                pass
    
    def quit(self, status):
        self.Engine.stop()
        sys.exit(status)