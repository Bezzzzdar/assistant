from modules.assistant_module import setup_voice_assistant, assistant_say, execute_command
from modules.rec_module import record_and_recognize_audio

if __name__ == "__main__":

    setup_voice_assistant("Tayler", "male", "ru")

    voice_input = record_and_recognize_audio()
    execute_command(str(voice_input))
    
    

    