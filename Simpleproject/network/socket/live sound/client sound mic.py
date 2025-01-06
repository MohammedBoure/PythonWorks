import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILENAME = "test_output.wav"
INPUT_DEVICE_INDEX = 7

p = pyaudio.PyAudio()

info = p.get_device_info_by_index(INPUT_DEVICE_INDEX)
if info['max_input_channels'] == 0:
    print(f"Device {INPUT_DEVICE_INDEX} does not support input.")
    p.terminate()
    exit()

try:
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=INPUT_DEVICE_INDEX,
                    frames_per_buffer=CHUNK)
except IOError as e:
    print(f"Error: {e}")
    p.terminate()
    exit()

print("Recording...")

frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    try:
        data = stream.read(CHUNK)
        frames.append(data)
    except IOError as e:
        print(f"Error: {e}")
        break

print("Recording finished.")

stream.stop_stream()
stream.close()
p.terminate()

with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"File saved as {OUTPUT_FILENAME}")
