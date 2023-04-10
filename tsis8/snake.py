import pygame
clock = pygame.time.Clock()
pygame.init()
SIZE_BLOCK = 20
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Snake")
running = True
SNAKE_COLOR = (209, 36, 93)
back_color = (0, 255, 204)
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [40 + column * SIZE_BLOCK + column + 1,
                                     150 + row * SIZE_BLOCK + row + 1,
                                     SIZE_BLOCK, SIZE_BLOCK])
snake_block = [SnakeBlock(7, 8)]
while running:
    clock.tick(60)
    screen.fill(back_color)
    for row in range(15):
        for column in range(15):
            if (row+column)%2 == 0:
                color = (204, 255, 255)
            else:
                color = (255, 255, 255)
            draw_block(color, row, column)
    for block in snake_block:
        draw_block(SNAKE_COLOR, block.x, block.y )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()