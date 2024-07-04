import torch
from pathlib import Path
from synthesizer.inference import Synthesizer
from encoder import inference as encoder
from vocoder import inference as vocoder
import librosa
import numpy as np
import soundfile as sf

# class NeuroVoice():
#     def __init__(self, 
#                  encoder_pretrained_model: str,
#                  synthesizer_pretrained_model: str, 
#                  vocoder_pretrained_model: str) -> None:
#         # load pretrained models
#         pass
    
#     def clone_voice():
#         pass


# Загрузка моделей
encoder.load_model(Path("encoder/pretrained/encoder.pt"))
synthesizer = Synthesizer(Path("synthesizer/pretrained/synthesizer.pt"))
vocoder.load_model(Path("vocoder/pretrained/vocoder.pt"))

def clone_voice(reference_wav_path, text, output_wav_path):
    # Загрузка референсного аудио
    original_wav, sampling_rate = librosa.load(reference_wav_path, sr=None)
    preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)

    # Генерация эмбеддингов голоса
    embed = encoder.embed_utterance(preprocessed_wav)

    # Синтез мел-спектрограммы
    spec = synthesizer.synthesize_spectrograms([text], [embed])[0]

    # Преобразование мел-спектрограммы в аудио
    generated_wav = vocoder.infer_waveform(spec)

    # Сохранение аудио
    sf.write(output_wav_path, generated_wav, synthesizer.sample_rate)

if __name__ == "__main__":
    reference_wav_path = "voice.wav"
    text = "Это синтезированный голос"
    output_wav_path = "output.wav"
    clone_voice(reference_wav_path, text, output_wav_path)
