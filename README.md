# Dependencies (Python):
* PyAudio
* pyttsx3
* SpeechRecognition
* googlesearch-python
* geocoder 
* geopy
* Flask
* flask-cors
* spotipy

# How to install:
* `pip install -r requirements.txt`

# Dependencies (JS):
* Electron

# How to install:
* `npm install electron --save-dev`
  
# Virtual environment (execute from the project root): 
* `python -m venv venv`
* `.\venv\Scripts\Activate.ps1`
* `pip install -r modules/requirements.txt`

# Setup the environment variables for using Spotify (Windows 10):
```PowerShell
$variableNameToAdd = "SpotifyClientID"
$variableValueToAdd = "value to add"
[System.Environment]::SetEnvironmentVariable($variableNameToAdd, $variableValueToAdd, [System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable($variableNameToAdd, $variableValueToAdd, [System.EnvironmentVariableTarget]::Process)
[System.Environment]::SetEnvironmentVariable($variableNameToAdd, $variableValueToAdd, [System.EnvironmentVariableTarget]::User)

$variableNameToAdd = "SpotifyClientSecret"
$variableValueToAdd = "value to add"
[System.Environment]::SetEnvironmentVariable($variableNameToAdd, $variableValueToAdd, [System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable($variableNameToAdd, $variableValueToAdd, [System.EnvironmentVariableTarget]::Process)
[System.Environment]::SetEnvironmentVariable($variableNameToAdd, $variableValueToAdd, [System.EnvironmentVariableTarget]::User)

$variableNameToAdd = "SpotifyRedirectUri"
$variableValueToAdd = "value to add"
[System.Environment]::SetEnvironmentVariable($variableNameToAdd, $variableValueToAdd, [System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable($variableNameToAdd, $variableValueToAdd, [System.EnvironmentVariableTarget]::Process)
[System.Environment]::SetEnvironmentVariable($variableNameToAdd, $variableValueToAdd, [System.EnvironmentVariableTarget]::User)
```
ClientID, ClientSecret and RedirectUri you can get on [Spotify for Developers Dashboard](https://developer.spotify.com/dashboard)

# Neuro:
GitHub - [Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning)