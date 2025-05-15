import sys
import pygame
from pygame.locals import QUIT
pygame.init()
SURFACE = pygame.display.set_mode((800,800))
FPSCLOCK = pygame.time.Clock()
from random import randint
def main():
    rock_image = pygame.image.load("rock.png")
    rocks = []
    while len(rocks) < 20:
        rocks.append(
            {
                "pos":[randint(-1600, 1600),
                       randint(-1600, 1600),
                       randint(0, 4095)],
                "theta":randint(0,360)
            }
        )
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            SURFACE.fill((0,0,0))
            pygame.display.update()
            FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()
