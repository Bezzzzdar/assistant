# Standart modules
import sys
import os
import random
import time
import concurrent.futures
import webbrowser

# Spotify module
from spotipy import SpotifyException

# Voice synthesis
import pyttsx3

# Unix utils
import psutil

# Local modules
from modules.owner import Owner

# GLOBALS
DEVICE_ID = 0
DEFAULT_VOLUME = 50
CURRENT_VOLUME = DEFAULT_VOLUME


class VoiceAssistant:
    """Class representing the Assistant"""

    def __init__(self, name: str, language: str) -> None:
        self.name = name
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
        """Function for changing Assistant name"""
        VoiceAssistant.name = new_owner_name

    def change_assistant_language(self, new_owner_language: str):
        """Function for changing Assistant language"""
        VoiceAssistant.language = new_owner_language

    def assistant_say(self, text: str) -> None:
        """Function for the Assistant to speak"""
        self.Engine.say(text)
        self.Engine.runAndWait()

    def recognize_and_execute_command(self, command: str, *args: list) -> None:
        """Function for recognizing and executing the commands by Assistant"""
        for key, command_class in self.commands_dict.items():
            if command in key:
                command_class.execute(*args)
                break
            continue

    def quit(self, status):
        """Stop all and quit"""
        self.Engine.stop()
        sys.exit(status)

class CommandsDict:
    """Class for storing text commands"""

    def __init__(self) -> None:
        self.commands = {}

    def dictionary(self):
        """Store the commands in dictionary"""
        self.commands = {
            ("привет", "здравствуй", "здарово", "здарова", "добрый день", "доброе утро", "добрый вечер"): PlayGreetings(),
            ("пока", "покедова", "досвидания", "до скорого", "до встречи", "увидимся"): PlayFarewellAndQuit(),
            ("найди в гугл", "найди в гугле", "поищи в гугле"): GoogleSearch(),
            ("найди видео", "покажи видео"): YouTubeSearch(),
            ("прогноз погоды", "какая погода"): GetWeatherForecast(),
            ("включи песню", "поставь песню"): PlaySong(),
            ("выключи", "стоп", "поставь на паузу"): PauseSong(),
            ("установи громкость на", "поставь громкость на"): SetVolume(),
            ("сделай тише", "сделай потише", "сделай ещё тише", "сделай ещё потише", "ещё тише"): QuieterVolume(),
            ("сделай громче", "сделай погромче", "сделай ещё громче", "сделай ещё погромче", "ещё громче"): LouderVolume()
        }

        return self.commands

class Command:
    """Class for assistants's command"""

    def execute(self, *args: tuple, **kwargs):
        """Function for executing a command"""
        raise NotImplementedError("This method should be overridden by subclasses")

class PlayGreetings(Command):
    """Greet a Owner"""

    def execute(self, *args: tuple, **kwargs):
        greetings = [
        f"Привет {Owner.name}, чем могу помочь?",
        f"Здравствуйте {Owner.name}! Чем обязан?",
        f"Приветствую {Owner.name}, чем могу быть полезен?"
        ]
        VoiceAssistant.assistant_say(VoiceAssistant,
                                     greetings[random.randint(0, len(greetings) - 1)])

class PlayFarewellAndQuit(Command):
    """Farewell a Owner and quit"""

    def execute(self, *args: tuple, **kwargs):
        farewells = [
        f"До свидания {Owner.name}",
        f"Пока {Owner.name}",
        f"До скорого {Owner.name}"
        ]
        VoiceAssistant.assistant_say(VoiceAssistant,
                                     farewells[random.randint(0, len(farewells) - 1)])
        VoiceAssistant.quit(VoiceAssistant, 0)

class GoogleSearch(Command):
    """Search something on Google"""

    def execute(self, *args: tuple, **kwargs):
        if not args[0]:
            return

        search_term = " ".join(args[0])
        url = "https://google.com/search?q=" + search_term
        try:
            webbrowser.get().open(url)
            response = "Вот что мне удалось найти по запросу" + search_term
            VoiceAssistant.assistant_say(VoiceAssistant, response)
        except OSError:
            return

class YouTubeSearch(Command):
    """Search something on YouTube"""

    def execute(self, *args: tuple, **kwargs):
        if not args[0]:
            return

        search_term = " ".join(args[0])
        url = "https://www.youtube.com/results?search_query=" + search_term
        try:
            webbrowser.get().open(url)
            response = "Вот что мне удалось найти на Youtube по запросу" + search_term
            VoiceAssistant.assistant_say(VoiceAssistant, response)
        except OSError:
            return

class GetWeatherForecast(Command):
    """Check the weather"""

    def execute(self, *args: tuple, **kwargs):
        print("get_weather_forecast")


def _get_info_about_devices():
    global DEVICE_ID

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
            response = "У вас нет доступных устройств для воспроизведения. Пожалуйста установите приложение Spotify"
            VoiceAssistant.assistant_say(VoiceAssistant, response)
            return -1

    # use first available device
    DEVICE_ID = devices['devices'][0]['id']
    return 0

class PlaySong(Command):
    """Start streaming the song from Spotify"""

    def execute(self, *args: tuple, **kwargs):
        if not (Owner.SpotifyClientID and Owner.SpotifyClientSecret and Owner.SpotifyRedirectUri):
            VoiceAssistant.assistant_say(VoiceAssistant, "Вы не можете воспользоваться данной функцией, так как у вас не установлены переменные среды SpotifyClientID, SpotifyClientSecret и SpotifyRedirectUri. Как это сделать вы можете посмотреть в README") 
            return
        else:
            if not args[0]:
                return

            try:
                if _get_info_about_devices() == 0:
                    # find track by name
                    track_name = " ".join(args[0])
                    results = Owner.spotify.search(q=track_name, type='track', limit=1)
                    track = results['tracks']['items'][0]
                    track_uri = track['uri']

                    Owner.spotify.volume(volume_percent=CURRENT_VOLUME, device_id=DEVICE_ID)
                    Owner.spotify.start_playback(device_id=DEVICE_ID, uris=[track_uri])
            except SpotifyException as e:
                print(f"Error {e}")
                return

class PauseSong(Command):
    """Pause the song from Spotify"""

    def execute(self, *args: tuple, **kwargs):
        try:
            Owner.spotify.pause_playback(device_id=DEVICE_ID)
        except SpotifyException as e:
            print(f"Error {e}")
            return

class SetVolume(Command):
    """Set song volume of the current playing song at any percent"""

    def execute(self, *args: tuple, **kwargs):
        if not args[0]:
            return
        volume = args[0][0][:-1]
        try:
            Owner.spotify.volume(volume_percent=int(volume), device_id=DEVICE_ID)
        except SpotifyException as e:
            print(f"Error {e}")
            return

class QuieterVolume(Command):
    """Decrease the volume of the current playing song by 10 percent"""

    def execute(self, *args: tuple, **kwargs):
        try:
            global CURRENT_VOLUME
            CURRENT_VOLUME = max(CURRENT_VOLUME - 10, 0)
            Owner.spotify.volume(volume_percent=CURRENT_VOLUME, device_id=DEVICE_ID)
        except SpotifyException as e:
            print(f"Error {e}")
            return

class LouderVolume(Command):
    """Increase the volume of the current playing song by 10 percent"""

    def execute(self, *args: tuple, **kwargs):
        try:
            global CURRENT_VOLUME
            CURRENT_VOLUME = min(CURRENT_VOLUME + 10, 100)
            Owner.spotify.volume(volume_percent=CURRENT_VOLUME, device_id=DEVICE_ID)
        except SpotifyException as e:
            print(f"Error {e}")
            return
