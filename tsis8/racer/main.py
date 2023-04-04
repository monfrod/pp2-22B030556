import pygame
import random
import time
clock = pygame.time.Clock() #FPS
pygame.init()
x, y = 190, 500
screen_width = 400 #size our screen
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill("White") #white screen
player = pygame.image.load("Player.png") #load player
enemy = pygame.image.load("Enemy.png") #load enemy
speed_p = 8 #speed for our player
speed_e = 5 #speed for enemy
bc = pygame.image.load("AnimatedStreet.png") #load our background
pygame.mixer_music.load("crash.wav") #load our sound
ey = 0
ex = random.randint(0, screen_width-93)
shrift = pygame.font.SysFont("serif", 40)
shrift_2 = pygame.font.SysFont("serif", 70)
score = 0
dist_x, dist_y = 100, 100
text_go = shrift_2.render("Game Over", True, (0, 0, 0))
running = True
while running:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bc,(0, 0))
    if pressed[pygame.K_LEFT]:#move on left
        if x < 0:
            x = 0
        else:
            x -= speed_p

    if pressed[pygame.K_RIGHT]:#move on right
        if x > screen_width-44:
            x = screen_width-44
        else:
            x += speed_p
    ey += speed_e+(score*0.5) #increase speed for enemy
    dist_x = abs(x - ex)
    dist_y = abs(y - ey)
    if dist_y < 90 and dist_x < 40:
        pygame.mixer.music.play()
        time.sleep(1)
        screen.fill((255, 0, 0))
        screen.blit(text_go, (40, 150))
        pygame.display.flip()
        time.sleep(3)
        exit()
    text_score = shrift.render(str(score), True, (0, 0, 0))
    if ey > screen_height-48: #respawn our enemy
        ey = 0
        ex = random.randint(0, screen_width - 93)
        score +=1
    player_pos = (x, y)
    screen.blit(player, player_pos)
    screen.blit(enemy, (ex, ey))
    screen.blit(text_score, (20, 20))
    clock.tick(60)#FPS
    pygame.display.flip()

