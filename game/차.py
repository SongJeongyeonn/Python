import sys
import pygame
FPS = 60
WIDTH = 600
HEIGHT = 400
white = (255,255,255)
velocity = 7
mass = 2
pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
speed = 10

class Car():
    def __init__(self, x, y):
        self.dx = x
        self.dy = y
        self.rect = ""
        
    def load_car(self):
        self.image = pygame.image.load("car.png")
        self.image = pygame.transform.scale(self.image, (150, 57))
        self.rect = self.image.get_rect()
        self.rect.centerx = round(WIDTH/2)
        self.rect.bottom = HEIGHT
    
    def draw_car(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    def move_x(self):
        self.rect.x += self.dx
    def check_screen(self):
        if self.rect.right > WIDTH or self.rect.x < 0:
            self.rect.x -= self.dx
        if self.rect.bottom > HEIGHT or self.rect.y < 0:
            self.rect.y -= self.dy

def main():
    global screeen, WIDTH, HEIGHT
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.dx=5
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        screen.fill((255,255,255))
        player.jump()
        enemy_rect = enemy.draw()
        enemy.move(speed)
        speed+=0.01
        if player.x > WIDTH:
            player.x = 0
        elif player.x < 0:
            player.x = WIDTH
        player.x = (player.x+(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]*speed)%WIDTH)
        player_rect = player.draw()
        if player_rect.colliderect(enemy_rect): 
            print("충돌!!!")
            pygame.quit()
            sys.exit()
        pygame.display.update()
if __name__=='__main__':
    main()
