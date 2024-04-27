import pygame
import math
import numpy as np
import pyaudio

# Constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Function to draw radar
def draw_radar(screen, angle):
    radar_center = (250, 250)
    radius = 200
    end_point = (radar_center[0] + radius * math.cos(math.radians(angle)),
                 radar_center[1] - radius * math.sin(math.radians(angle)))
    pygame.draw.circle(screen, (255, 255, 255), radar_center, radius, 2)
    pygame.draw.line(screen, (255, 255, 255), radar_center, end_point, 2)
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Sound Radar")

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    running = True
    angle = 0

    print("* Recording audio...")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)

        max_amplitude_index = np.argmax(np.abs(audio_data))
        angle = (max_amplitude_index / len(audio_data)) * 360

        screen.fill((0, 0, 0))
        draw_radar(screen, angle)

    pygame.quit()

if __name__ == "__main__":
    main()