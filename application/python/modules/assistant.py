import pyttsx3
import sys
import random
import googlesearch
import webbrowser
import os
import spotipy
import time
import psutil
import concurrent.futures
from spotipy.oauth2 import SpotifyOAuth
from modules.owner import Owner
                
class VoiceAssistant:
    def __init__(self, name: str, language: str) -> None:
        self.name      = name
        self.language  = language

        self.commands  = CommandsDict()
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
    
    def change_assistant_name(self, new_owner_name: str):
        VoiceAssistant.name = new_owner_name

    def change_assistant_language(self, new_owner_language: str):
        VoiceAssistant.language = new_owner_language

    def assistant_say(self, text: str) -> None:
        self.Engine.say(text)
        self.Engine.runAndWait()
    
    def execute_command(self, command: str, *args: list) -> None:
        for key in self.commands_dict.keys():
            if command in key:
                self.commands_dict[key].execute(*args)
                break
            else:
                continue
    
    def quit(self, status):
        self.Engine.stop()
        sys.exit(status)

class CommandsDict:
    def __init__(self) -> None:
        pass

    def dictionary(self):
        self.Commands = {
            ("привет ", "здравствуй ", "здарово ", "здарова ", "добрый день ", "доброе утро ", "добрый вечер "): PlayGreetings(),
            ("пока ", "покедова ", "досвидания ", "до скорого ", "до встречи ", "увидимся "): PlayFarewellAndQuit(),
            ("найди в гугл ", "найди в гугле ", "поищи в гугле "): GoogleSearch(),
            ("найди видео ", "покажи видео "): YouTubeSearch(),
            ("прогноз погоды ", "какая погода "): GetWeatherForecast(),
            ("включи песню ", "поставь песню "): PlaySong(),
            ("выключи ", "стоп ", "поставь на паузу "): PauseSong(),
            ("установи громкость на ", "поставь громкость на "): SetVolume(),
            ("сделай тише ", "сделай потише ", "сделай ещё тише ", "сделай ещё потише ", "ещё тише "): QuieterVolume(),
            ("сделай громче ", "сделай погромче ", "сделай ещё громче ", "сделай ещё погромче ", "ещё громче "): LouderVolume()
        }
        
        return self.Commands

class Command:
    def execute(self, *args: tuple, **kwargs):
        raise NotImplementedError("This method should be overridden by subclasses")

class PlayGreetings(Command):
    def execute(self, *args: tuple, **kwargs):
        greetings = [
        "Привет {}, чем могу помочь?".format(Owner.name), 
        "Здравствуйте {}! Чем обязан?".format(Owner.name),
        "Приветствую {}, чем могу быть полезен?".format(Owner.name)
        ]
        VoiceAssistant.assistant_say(VoiceAssistant, greetings[random.randint(0, len(greetings) - 1)])

class PlayFarewellAndQuit(Command):
    def execute(self, *args: tuple, **kwargs):
        farewells = [
        "До свидания {}".format(Owner.name),
        "Пока {}".format(Owner.name),
        "До скорого {}".format(Owner.name)
        ]
        VoiceAssistant.assistant_say(VoiceAssistant, farewells[random.randint(0, len(farewells) - 1)])
        VoiceAssistant.quit(VoiceAssistant, 0)

class GoogleSearch(Command):
    def execute(self, *args: tuple, **kwargs):
        if not args[0]:
            return 
    
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
            return 
        
class YouTubeSearch(Command):
    def execute(self, *args: tuple, **kwargs):
        if not args[0]:
            return 
    
        search_term = " ".join(args[0])
        url = "https://www.youtube.com/results?search_query=" + search_term
        try:
            webbrowser.get().open(url)
            VoiceAssistant.assistant_say(VoiceAssistant, "Вот что мне удалось найти на Youtube по запросу" + search_term)
        except:
            return 

class GetWeatherForecast(Command):
    def execute(self, *args: tuple, **kwargs):
        print("get_weather_forecast")


def _get_info_about_devices():
    global DEVICE_ID
    global DEFAULT_VOLUME
    global current_volume

    # get info about devices
    find_flag = 0 
    spotify_proc = "Spotify.exe"
    for proc in psutil.process_iter():
        if proc.name == spotify_proc:
            devices = Owner.spotify.devices()
            find_flag = 1
            break

    if find_flag == 0:
        possible_directories = [
            os.path.join(os.environ.get("ProgramFiles", ""), "Spotify"),
            os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Spotify"),
            os.path.expanduser("~\\AppData\\Roaming\\Spotify"),
            os.path.expanduser("~\\AppData\\Local\\Microsoft\\WindowsApps")
        ]

        spotify_executable_path = None

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {}
            for directory in possible_directories:
                spotify_executable = os.path.join(directory, "Spotify.exe")
                futures[executor.submit(os.path.exists, spotify_executable)] = spotify_executable
            
            for future in concurrent.futures.as_completed(futures):
                spotify_executable = futures[future]
                if future.result():
                    spotify_executable_path = spotify_executable
                    break

        if spotify_executable_path and os.path.exists(spotify_executable_path):
            os.startfile(spotify_executable_path)
            time.sleep(5)
            devices = Owner.spotify.devices()
        else:
            VoiceAssistant.assistant_say(VoiceAssistant, "У вас нет доступных устройств для воспроизведения. Пожалуйста установите приложение Spotify")
            return -1
    
    # use first available device 
    DEVICE_ID = devices['devices'][0]['id']
    DEFAULT_VOLUME = 50
    current_volume = DEFAULT_VOLUME
    return 0

class PlaySong(Command):
    def execute(self, *args: tuple, **kwargs):
        if not (Owner.SpotifyClientID and Owner.SpotifyClientSecret and Owner.SpotifyRedirectUri):
            VoiceAssistant.assistant_say(VoiceAssistant, "Вы не можете воспользоваться данной функцией, так как у вас не установлены переменные среды SpotifyClientID, SpotifyClientSecret и SpotifyRedirectUri. Как это сделать вы можете посмотреть в README") 
            return -1
        else:
            if not args[0]:
                return -1
        
            if _get_info_about_devices() == 0:
                # find track by name
                track_name = " ".join(args[0])
                results = Owner.spotify.search(q=track_name, type='track', limit=1)
                track = results['tracks']['items'][0]
                track_uri = track['uri']

                Owner.spotify.volume(volume_percent=current_volume, device_id=DEVICE_ID)
                Owner.spotify.start_playback(device_id=DEVICE_ID, uris=[track_uri])

class PauseSong(Command):
    def execute(self, *args: tuple, **kwargs):
        try:
            Owner.spotify.pause_playback(device_id=DEVICE_ID)
        except:
            pass

class SetVolume(Command):
    def execute(self, *args: tuple, **kwargs):
        if not args[0]:
            return -1
        volume = args[0][0][:-1]
        try:
            Owner.spotify.volume(volume_percent=int(volume), device_id=DEVICE_ID)
        except:
            pass           

class QuieterVolume(Command):
    def execute(self, *args: tuple, **kwargs):
        try:
            global current_volume
            current_volume = max(current_volume - 10, 0)
            Owner.spotify.volume(volume_percent=current_volume, device_id=DEVICE_ID)
        except:
            pass

class LouderVolume(Command):
    def execute(self, *args: tuple, **kwargs):
        try:
            global current_volume
            current_volume = min(current_volume + 10, 100)
            Owner.spotify.volume(volume_percent=current_volume, device_id=DEVICE_ID)
        except:
            pass 