import pygame
from pygame.locals import Rect
r = Rect(10,20,30,40)
r.move(50,60)
print(r)
r.move_ip(50,60)
print(r)