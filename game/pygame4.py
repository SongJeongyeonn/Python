import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 300
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Points")

pointlist = []
for _ in range(10):
    xpos = random.randint(0, 400)
    ypos = random.randint(0, 300)
    pointlist.append((xpos, ypos))
SURFACE.fill((0, 0, 0))
pygame.draw.lines(SURFACE, (255, 255, 255), True, pointlist, 5)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
