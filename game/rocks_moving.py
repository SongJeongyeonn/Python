import sys
from random import randint

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    rock_image = pygame.image.load("rock.png")
    speed = 25
    rocks = []

    while len(rocks) < 200:
        rocks.append({
            "pos": [randint(-1600, 1600),
                    randint(-1600, 1600),
                    randint(0, 4095)],
            "theta": randint(0, 360)
        })                                      

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        for rock in rocks:
            rock["pos"][2] -= speed
            #print(rocks)
            if rock["pos"][2] < 64:
                rock["pos"] = [randint(-1600, 1600),
                               randint(-1600, 1600), 4095]
                
        SURFACE.fill((0, 0, 0))

        rocks = sorted(rocks, key=lambda x: x["pos"][2], reverse=True)
        
        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - 0) *500  ) / zpos + 400
            ypos = ((rock["pos"][1] - 0) << 9) / zpos + 400
            size = (50 * 500) / zpos
            
            rotated = pygame.transform.rotozoom(rock_image, rock["theta"], size / 145)  # size/145는 배율 
            SURFACE.blit(rotated, (xpos, ypos))

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()
