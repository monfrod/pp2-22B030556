import pygame
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((500, 500))
sound = [pygame.mixer.Sound("Рингтон - Пиу пиу пиу.mp3"),
         pygame.mixer.Sound("2_pac_BIG_SYKE_-_All_eyez_on_me_(DJ_Belite_remix)_(ringon.site).mp3"),
         pygame.mixer.Sound("ZODIVK_-_Devil_eyes_Slowed_(ringon.site).mp3"),
         pygame.mixer.Sound("DNDM_-_Eastern_love_(Original_mix)_(ringon.site).mp3")]
running = True
i = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                sound[i].stop
                i+=1
                sound[i].play
            if event.key == pygame.K_a:
                sound[i].stop
                i-=1
                sound[i].play
            if event.key == pygame.K_w:
                sound[i].play()
            if event.key == pygame.K_s:
                sound[i].stop()
    if i > len(sound) or i < len(sound):
        i = 0
    clock.tick(60)