from modules.assistant import VoiseAssistant, Owner
from modules.record_and_recognize import record_and_recognize_audio

if __name__ == "__main__":

    assistant = VoiseAssistant('Tyler', 'ru')
    owner = Owner("Ivan", "ru")
    
    while True:
        voice_input = record_and_recognize_audio()
        voice_input = voice_input.split(" ")
        command = str(voice_input[0])
        command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        VoiseAssistant.execute_command(assistant, command, command_options)