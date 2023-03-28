import pygame
clock = pygame.time.Clock()
pygame.init()
W = 1050
H = 650
screen = pygame.display.set_mode((W, H))
running = True
x = 25
y = 25
step = 20
while running:
    screen.fill("White")
    if x < 25:
        x =25
    if y < 25:
        y = 25
    pygame.draw.circle(screen, "Red", (x, y), 25)
    if x > W-25:
        x = W-25
    if y > H-25:
        y = H-25
    pygame.draw.circle(screen, "Red", (x, y), 25)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x += step
            if event.key == pygame.K_a:
                x -= step
            if event.key == pygame.K_s:
                y += step
            if event.key == pygame.K_w:
                y -= step
    clock.tick(60)
