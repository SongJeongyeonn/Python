import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((255, 255, 255))
        pygame.draw.rect(SURFACE, (255, 0, 0), (150, 10, 100, 30), 3)
        for xpos in range(0, 400, 25):
            pygame.draw.line(SURFACE, (0, 0, 0), (xpos, 0), (xpos, 300))
        for ypos in range(0, 300, 25):
            pygame.draw.line(SURFACE, (0, 0, 0), (0, ypos), (400, ypos))

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()