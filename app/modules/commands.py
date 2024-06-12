import random
from modules.assistant import VoiseAssistant, Owner
import googlesearch
import webbrowser

class Commands:
    def __init__(self) -> None:
        pass

    def dictionary(self):
        self.Commands = {
            ("привет", "здравствуй", "здарово", "здарова", "добрый день", "доброе утро", "добрый вечер"): play_greeting,
            ("пока", "покедова", "досвидания", "до скорого", "до встречи", "увидимся"): play_farewell_and_quit,
            ("найди в гугл", "найди в гугле", "поищи в гугле", "найди"): google_search,
            ("найди видео", "покажи видео"): youtube_search,
            ("найди определение", "найди на википедии"): wikipedia_search,
            ("прогноз погоды", "какая погода"): get_weather_forecast,
        }
        
        return self.Commands

def play_greeting(*args: tuple):
    greetings = [
        "Привет {}, чем могу помочь?".format(Owner.name), 
        "Здравствуйте {}! Чем обязан?".format(Owner.name),
        "Приветствую {}, чем могу быть полезен?".format(Owner.name)
    ]
    VoiseAssistant.assistant_say(VoiseAssistant, greetings[random.randint(0, len(greetings) - 1)])


def play_farewell_and_quit(*args: tuple):
    farewells = [
        "До свидания {}".format(Owner.name),
        "Пока {}".format(Owner.name),
        "До скорого {}".format(Owner.name)
    ]
    VoiseAssistant.assistant_say(VoiseAssistant, farewells[random.randint(0, len(farewells) - 1)])
    VoiseAssistant.quit(VoiseAssistant, 0)

def google_search(*args: tuple):
    if not args[0]:
        return -1
    search_term = " ".join(args[0])
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)
    # search_results = []
    # for result in googlesearch.search(search_term, num_results=1, lang=VoiseAssistant.language):
    #     search_results.append(result)
    #     webbrowser.get().open(result)
    VoiseAssistant.assistant_say(VoiseAssistant, "Вот что мне удалось найти по запросу" + search_term)

    return 0
def youtube_search(*args: tuple):
    print('youtube_search')

def wikipedia_search(*args: tuple):
    print('wikipedia_search')

def get_weather_forecast(*args: tuple):
    print('get_weather_forecast')