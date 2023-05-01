import pygame

pygame.init()
def user_input():
    screen = pygame.display.set_mode((600, 600))
    # Определяем шрифт, который будет использоваться для отображения ввода пользователя
    font = pygame.font.Font('serif', 32)

    # Создаем переменную для хранения ввода пользователя
    user_input = ""
    running = True
    # Основной цикл игры
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Ввод завершен, выходим из цикла
                    running = False
                elif pygame.K_a <= event.key <= pygame.K_z or pygame.K_0 <= event.key <= pygame.K_9:
                    # Добавляем символ в переменную ввода пользователя
                    user_input += chr(event.key)

        # Отображаем текущий ввод пользователя
        input_text = font.render(user_input, True, (255, 255, 255))
        input_rect = input_text.get_rect()
        input_rect.center = (400, 300)
        screen.blit(input_text, input_rect)

        pygame.display.update()
    pygame.quit()
user_input()
