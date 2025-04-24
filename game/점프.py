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
class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.isjump = False
        self.jumpcount = 10
    def draw(self):
        return pygame.draw.rect(screen,(0,0,255),(self.x,self.y,40,40))
    def jump(self):
        if self.isjump:
            if self.jumpcount >= -10:
                neg = 1
                if self.jumpcount < 0:
                    neg = -1
                self.y -= self.jumpcount**2*0.5*neg
                self.jumpcount -= 1
            else:
                self.isjump = False
                self.jumpcount = 10
class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        return pygame.draw.rect(screen,(255,0,0),(self.x,self.y,20,40))
    def move(self, speed):
        self.x = self.x-speed
        if self.x < 0:
            self.x = WIDTH

player = Player(50,HEIGHT-40)
enemy = Enemy(WIDTH,HEIGHT-40)
def main():
    global speed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.isjump = True
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
