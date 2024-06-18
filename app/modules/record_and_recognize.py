import speech_recognition
import os

def record_and_recognize_audio():

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    with microphone:
        recognized_data = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=1)

        try:
            
            print("listening...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("something went wrong...")
            return
        
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass
            # recognized_data = recognizer.recognize_google(audio, language="en").lover()
    
    os.remove("microphone-results.wav")
    return(recognized_data)

def split_phrase(voice: str):
    voice = voice.split(" ")
    commands_list = []
    command_options_list = []
    command = ''

    for i in range(len(voice)):
        command = command + voice[i] + ' '
        command_options = [str(input_part) for input_part in voice[i+1:len(voice)]]
        commands_list.append(command)
        command_options_list.append(command_options)
        
    return commands_list, command_options_list