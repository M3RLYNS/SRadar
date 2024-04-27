import pyaudio
import numpy as np

# Constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def main():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* Recording audio...")

    while True:
        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)
        print("Max amplitude:", np.max(np.abs(audio_data)))

    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    main()