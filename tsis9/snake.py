import pygame
import random
clock = pygame.time.Clock()
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
sc_weight = 800
sc_height = 600
screen = pygame.display.set_mode((sc_weight, sc_height))
screen.fill(WHITE)

x1 = sc_weight/2
y1 = sc_height/2
dx1 = 0
dy1 = 0
score = 0
shrift = pygame.font.SysFont("serif", 35)

foodx = random.randint(0, (sc_weight-20) / 20)*20
foody = random.randint(0, (sc_height-20) / 20)*20


def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], 20, 20])
snake_List = []
Length_snake = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                dx1 = -20
                dy1 = 0
            if event.key == pygame.K_d:
                dx1 = 20
                dy1 = 0
            if event.key == pygame.K_s:
                dx1 = 0
                dy1 = 20
            if event.key == pygame.K_w:
                dx1 = 0
                dy1 = -20
    x1 += dx1
    y1 += dy1

    screen.fill(WHITE)
    show_score = shrift.render("Счет: " + str(score), True, (0, 0, 200) )
    screen.blit(show_score, (0, 0))
    if x1 > sc_weight-20 or y1 > sc_height-20 or x1 < 0 or y1 < 0:
        running = False

    pygame.draw.rect(screen, RED, (foodx, foody, 20, 20))

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)

    if len(snake_List) > Length_snake:
        del snake_List[0]
    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True
    our_snake(snake_List)
    pygame.display.flip()
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, sc_weight - 20) / 20.0) * 20.0
        foody = round(random.randrange(0, sc_height - 20) / 20.0) * 20.0
        Length_snake += 1
        score += 1
    clock.tick(10)