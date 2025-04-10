import pygame #파이 게임 모듈 임포트
import random
import copy

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#화면 크기 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock() 
#변수
game_over = False
BLACK = (0, 0, 0) 
GREEN = (0, 255, 0)
airplane_image = pygame.image.load('ship.png')
airplane = airplane_image.get_rect(left=0, centery=SCREEN_HEIGHT // 2)
large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 36)
score = 0
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

explosion_image = pygame.image.load('bang.png')
airplane_dy = 5
slope=2 
rects = []

for column_index in range(80):
    rect = pygame.Rect(column_index * 10, 100, 10, 400)
    rects.append(rect)

pygame.mixer.init()
pygame.mixer.music.load('music.mid') #배경 음악
pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번
explosion_sound = pygame.mixer.Sound('explosion.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')

while True: #게임 루프
    screen.fill(GREEN)
    event = pygame.event.poll() #이벤트 처리
    
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN and not game_over:
        if event.key == pygame.K_SPACE: airplane_dy = -5
    elif event.type == pygame.KEYUP and not game_over:
        if event.key == pygame.K_SPACE: airplane_dy = 5
    if not game_over:
        score += 1 

    new_rect = copy.deepcopy(rects[-1])

    if new_rect.top <= 0 or new_rect.bottom >= SCREEN_HEIGHT: 
          slope = random.randint(2, 6) * (-1 if slope > 0 else 1) #반대 방향으로 기울어 지게 하기
          #동굴 좁아지게 하기
          new_rect.height = new_rect.height -20

    new_rect.left = new_rect.left + 10
    new_rect.top = new_rect.top + slope

    rects.append(new_rect)

    for rect in rects:
         rect.left = rect.left - 10
    del rects[0]

    airplane.top += airplane_dy

    if airplane.top < rects[0].top or airplane.bottom > rects[0].bottom:
            game_over = True
            explosion_sound.play()
            pygame.mixer.music.stop()
            game_over_sound.play()

    #화면 그리기
    for rect in rects:
        pygame.draw.rect(screen, BLACK, rect)

    screen.blit(airplane_image, airplane)

    if game_over == True:
         screen.blit(explosion_image, (0, airplane.top - 40))
         game_over_image = large_font.render('게임 종료', True, RED)
         screen.blit(game_over_image, game_over_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    score_image = small_font.render('점수 {}'.format(score), True, YELLOW)  
    screen.blit(score_image, (10, 10))

    pygame.display.flip()
    clock.tick(15) 
pygame.quit()