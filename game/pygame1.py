import sys
import pygame
from pygame.locals import QUIT
pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Just Window")
FPSCLOCK = pygame.time.Clock()

def main():
    """ Main Routine """
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0 
    while True:
        SURFACE.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        counter += 1
        SURFACE.fill((0, 0, 0))
        count_image = sysfont.render(f"Count is {counter}", True, (225, 225, 225))
        SURFACE.blit(count_image, (50, 50))
        pygame.display.update()
        FPSCLOCK.tick(10)
if __name__ == '__main__':
    main()