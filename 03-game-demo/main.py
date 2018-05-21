import pygame
import time


def main():
    screen = pygame.display.set_mode((480, 852), 0, 32)

    background = pygame.image.load("./feiji/background.png")

    hero = pygame.image.load("./feiji/hero1.png")

    while True:
        screen.blit(background, (0, 0))

        screen.blit(hero, (150, 700))

        pygame.display.update()

        time.sleep(0.1)


if __name__ == "__main__":
    main()
