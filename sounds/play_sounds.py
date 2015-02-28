__author__ = 'marion'

import wave
import pyaudio
import os

CWD = os.path.abspath(os.getcwd())

def play_attention_sound():
    path_to_wav = "data/high_pitch_signal_short.wav"
    play_sound(path_to_wav)

def play_meditation_sound():
    path_to_wav = "data/signal.wav"
    play_sound(path_to_wav)


def play_sound(path_to_file):

    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(path_to_file)
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

