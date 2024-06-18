import pyttsx3
import sys
import random
import googlesearch
import webbrowser
from modules.owner import Owner
                
class VoiceAssistant:
    def __init__(self, name: str, language: str) -> None:
        self.name      = name
        self.language  = language

        self.commands  = Commands()
        self.commands_dict = self.commands.dictionary()
        
        VoiceAssistant.Engine = pyttsx3.init()
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
                break
            else:
                continue
    
    def quit(self, status):
        self.Engine.stop()
        sys.exit(status)

class Commands:
    def __init__(self) -> None:
        pass

    def dictionary(self):
        self.Commands = {
            ("привет ", "здравствуй ", "здарово ", "здарова ", "добрый день ", "доброе утро ", "добрый вечер "): play_greeting,
            ("пока ", "покедова ", "досвидания ", "до скорого ", "до встречи ", "увидимся "): play_farewell_and_quit,
            ("найди в гугл ", "найди в гугле ", "поищи в гугле "): google_search,
            ("найди видео ", "покажи видео "): youtube_search,
            ("прогноз погоды ", "какая погода "): get_weather_forecast,
            ("включи песню ", "поставь песню "): play_song,
        }
        
        return self.Commands

def play_greeting(*args: tuple):
    greetings = [
        "Привет {}, чем могу помочь?".format(Owner.name), 
        "Здравствуйте {}! Чем обязан?".format(Owner.name),
        "Приветствую {}, чем могу быть полезен?".format(Owner.name)
    ]
    VoiceAssistant.assistant_say(VoiceAssistant, greetings[random.randint(0, len(greetings) - 1)])


def play_farewell_and_quit(*args: tuple):
    farewells = [
        "До свидания {}".format(Owner.name),
        "Пока {}".format(Owner.name),
        "До скорого {}".format(Owner.name)
    ]
    VoiceAssistant.assistant_say(VoiceAssistant, farewells[random.randint(0, len(farewells) - 1)])
    VoiceAssistant.quit(VoiceAssistant, 0)

def google_search(*args: tuple):
    if not args[0]:
        return -1
    
    search_term = " ".join(args[0])
    url = "https://google.com/search?q=" + search_term
    try:
        webbrowser.get().open(url)
        # search_results = []
        # for result in googlesearch.search(search_term, num_results=1, lang=VoiceAssistant.language):
        #     search_results.append(result)
        #     webbrowser.get().open(result)
        VoiceAssistant.assistant_say(VoiceAssistant, "Вот что мне удалось найти по запросу" + search_term)
    except:
        return -1
    
    return 0

def youtube_search(*args: tuple):
    if not args[0]:
        return -1
    
    search_term = " ".join(args[0])
    url = "https://www.youtube.com/results?search_query=" + search_term
    try:
        webbrowser.get().open(url)
        VoiceAssistant.assistant_say(VoiceAssistant, "Вот что мне удалось найти на Youtube по запросу" + search_term)
    except:
        return -1
    
    return 0

def get_weather_forecast(*args: tuple):
    print("get_weather_forecast")


def play_song(*args : tuple):
    print('play_song')