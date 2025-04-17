import sys
import pygame
from math import floor
from random import randint
from pygame.locals import QUIT, MOUSEBUTTONDOWN

width = 20
height = 15
size = 50
num_of_bombs = 20
empty = 0
bomb = 1
opened = 2

open_count = 0
checked = [[0 for _ in range(width)] for _ in range(height)]

pygame.init()
surface = pygame.display.set_mode([width * size, height * size])
fpsclock = pygame.time.Clock()


def num_of_bomb(field, x_pos, y_pos):
    count = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < width and 0 <= ypos < height and field[ypos][xpos] == bomb:
                count += 1
    return count


def open_tile(field, x_pos, y_pos):
    global open_count
    if checked[y_pos][x_pos]:
        return
    checked[y_pos][x_pos] = True

    if field[y_pos][x_pos] != empty:
        return

    field[y_pos][x_pos] = opened
    open_count += 1

    count = num_of_bomb(field, x_pos, y_pos)
    if count == 0:
        for yoffset in range(-1, 2):
            for xoffset in range(-1, 2):
                xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
                if 0 <= xpos < width and 0 <= ypos < height:
                    if not (xpos == x_pos and ypos == y_pos):
                        open_tile(field, xpos, ypos)

def main():
    global open_count
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!", True, (0, 255, 225))
    message_over = largefont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_clear.get_rect()
    message_rect.center = (width * size / 2, height * size / 2)

    game_over = False
    field = [[empty for _ in range(width)] for _ in range(height)]
    open_count = 0
    for y in range(height):
        for x in range(width):
            checked[y][x] = False

    count = 0
    while count < num_of_bombs:
        xpos, ypos = randint(0, width - 1), randint(0, height - 1)
        if field[ypos][xpos] == empty:
            field[ypos][xpos] = bomb
            count += 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == MOUSEBUTTONDOWN and event.button == 1:
                xpos, ypos = floor(event.pos[0] / size), floor(event.pos[1] / size)
                if field[ypos][xpos] == bomb:
                    game_over = True
                else:
                    open_tile(field, xpos, ypos)

        # 그리기
        surface.fill((0, 0, 0))
        for ypos in range(height):
            for xpos in range(width):
                tile = field[ypos][xpos]
                rect = (xpos * size, ypos * size, size, size)

                if tile == opened:
                    pygame.draw.rect(surface, (96, 96, 96), rect)
                    count = num_of_bomb(field, xpos, ypos)
                    if count > 0:
                        num_image = smallfont.render(str(count), True, (255, 255, 0))
                        surface.blit(num_image, (xpos * size + 10, ypos * size + 10))
                else:
                    pygame.draw.rect(surface, (192, 192, 192), rect)
                    if game_over and tile == bomb:
                        pygame.draw.ellipse(surface, (225, 225, 0), rect)

        # 선 그리기
        for index in range(0, width * size, size):
            pygame.draw.line(surface, (255, 255, 255), (index, 0), (index, height * size))
        for index in range(0, height * size, size):
            pygame.draw.line(surface, (255, 255, 255), (0, index), (width * size, index))

        if open_count == width * height - num_of_bombs:
            surface.blit(message_clear, message_rect)
        elif game_over:
            surface.blit(message_over, message_rect)

        fpsclock.tick(15)
        pygame.display.update()


if __name__ == '__main__':
    main()