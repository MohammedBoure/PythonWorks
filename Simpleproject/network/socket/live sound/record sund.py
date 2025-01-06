import sounddevice as sd
import numpy as np
import wave


fs = 44100
seconds = 10


recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()

with wave.open('recording.wav', 'wb') as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(fs)
    wf.writeframes(recording.tobytes())

print("save file recording.wav")
