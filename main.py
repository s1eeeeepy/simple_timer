import time
import pygame.mixer


def timer():
    while True:
        try:
            value = int(input("Time in minutes: ")) * 60
        except ValueError:
            break
        pygame.mixer.init()
        file = "sound.mp3"
        sound = pygame.mixer.Sound(file)
        while value > 0:
            print(f"Time left: {value}")
            time.sleep(1)
            value -= 1
        print("Time to chill!")
        sound.play()
        time.sleep(sound.get_length())
        pygame.mixer.quit()


timer()
