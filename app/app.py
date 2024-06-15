from modules.assistant import VoiceAssistant, Owner
from modules.record_and_recognize import record_and_recognize_audio, split_phrase

if __name__ == "__main__":

    assistant = VoiceAssistant('Tyler', 'ru')
    owner = Owner("Ivan", "ru")
    
    while True:
        voice_input = record_and_recognize_audio()
        commands_list, command_options_list = split_phrase(voice_input)
        
        for i in range(len(commands_list)):
            VoiceAssistant.execute_command(assistant, commands_list[i], command_options_list[i])    