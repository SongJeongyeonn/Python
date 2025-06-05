import sys
import pygame
import random
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

pygame.init()
win = pygame.display.set_mode((600, 600))
fps = pygame.time.Clock()

# 전역 변수
FOODS = []      # 먹이 좌표 리스트
SNAKE = []      # 뱀의 좌표 리스트
(W, H) = (20, 20)  # 격자 크기 (20x20)

def add_food():
    """ 임의의 장소에 먹이 배치 """
    while True:
        pos = (random.randint(0, W - 1), random.randint(0, H - 1))
        if pos in FOODS or pos in SNAKE:
            continue
        FOODS.append(pos)
        break

def move_food(pos):
    """ 먹이를 다른 장소로 이동 """
    i = FOODS.index(pos)
    del FOODS[i]
    add_food()

def paint(message):
    """ 화면 전체 그리기 """
    win.fill((0, 0, 0))
    for food in FOODS:
        pygame.draw.ellipse(win, (0, 255, 0), Rect(food[0]*30, food[1]*30, 30, 30))
    for body in SNAKE:
        pygame.draw.rect(win, (0, 255, 255), Rect(body[0]*30, body[1]*30, 30, 30))
    for index in range(20):
        pygame.draw.line(win, (64, 64, 64), (index*30, 0), (index*30, 600))
        pygame.draw.line(win, (64, 64, 64), (0, index*30), (600, index*30))
    if message is not None:
        win.blit(message, (150, 300))
    pygame.display.update()

def main():
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False

    # 초기 위치 중앙
    SNAKE.clear()
    SNAKE.append((W // 2, H // 2))
    FOODS.clear()
    for _ in range(20):
        add_food()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN)):
                    key = event.key

        if not game_over:
            head = SNAKE[0]
            if key == K_LEFT:
                head = (head[0] - 1, head[1])
            elif key == K_RIGHT:
                head = (head[0] + 1, head[1])
            elif key == K_UP:
                head = (head[0], head[1] - 1)
            elif key == K_DOWN:
                head = (head[0], head[1] + 1)

            # 충돌 검사
            if head in SNAKE or head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= H:
                message = myfont.render("Game Over!", True, (255, 255, 0))
                game_over = True
            else:
                SNAKE.insert(0, head)
                if head in FOODS:
                    move_food(head)
                else:
                    SNAKE.pop()

        paint(message)
        fps.tick(10)

if __name__ == '__main__':
    main()