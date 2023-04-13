import random
import time
import pygame

pygame.init()

# creating variables
x, y, speed = 190, 500, 5
enemy_x = random.randint(0, 350)
enemy_y = 0
coin_x = random.randint(0, 350)
coin_y = 0
score = 0
coin_score = 0
dist_x, dist_y = 100, 100
c_dist_x, c_dist_y = 100, 100
pygame.mixer.music.load("crash.wav")

clock = pygame.time.Clock()
sc = pygame.display.set_mode((400, 600))

f1 = pygame.font.SysFont('serif', 65)
f2 = pygame.font.SysFont('serif', 30)
text1 = f1.render("GameOver", False, (0, 0, 0))
text4 = f2.render("Score: ", False, (0, 0, 0))
text5 = f2.render("Coins: ", False, (0, 0, 0))

# loading player image
player = pygame.image.load("Player.png")

# loading background and enemy image
back = pygame.image.load("AnimatedStreet.png")
enemy = pygame.image.load("Enemy.png")
coin = pygame.image.load("coin.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # game controls

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    elif keys[pygame.K_RIGHT] and x < 355:
        x += speed

    enemy_y += speed + (score * 0.5)  # increasing speed over time
    enemy_pos = (enemy_x, enemy_y)

    coin_y += speed * 0.3 + (score * 0.5)

    if coin_y > 550:
        coin_y = -100
        coin_x = random.randint(0, 350)

    if enemy_y > 550:
        enemy_y = 0  # respawns enemy
        enemy_x = random.randint(0, 350)
        score += 1

    c_dist_x = abs(x - coin_x)
    c_dist_y = abs(y - coin_y)  # coin collision
    if c_dist_y < 50 and c_dist_x < 50:
        coin_score += random.randint(1, 3)
        coin_y = -100
        coin_x = random.randint(0, 350)

    dist_x = abs(x - enemy_x)
    dist_y = abs(y - enemy_y)  # enemy collision
    if dist_y < 90 and dist_x < 40:
        pygame.mixer.music.play()
        time.sleep(1)
        sc.fill((255, 0, 0))
        sc.blit(text1, (60, 150))
        pygame.display.flip()
        time.sleep(3)
        exit()

        # display all objects on screen
    player_pos = (x, y)
    sc.blit(back, (0, 0))
    sc.blit(enemy, enemy_pos)
    coin = pygame.transform.scale(coin, (50, 50))
    sc.blit(coin, (coin_x, coin_y))
    sc.blit(player, player_pos)
    text2 = f2.render(str(score), False, (0, 0, 0))
    text3 = f2.render(str(coin_score), False, (0, 0, 0))
    sc.blit(text2, (90, 30))
    sc.blit(text3, (90, 70))
    sc.blit(text4, (10, 30))
    sc.blit(text5, (10, 70))
    pygame.display.update()

    clock.tick(60)