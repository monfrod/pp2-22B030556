import pygame
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000, 500))
sound = [pygame.mixer.Sound("INTERWORLD_-_METAMORPHOSIS_Sped_Up_(musmore.com).mp3"),
         pygame.mixer.Sound("kordhell-murder-in-my-mind-muzonov.net_456239182.mp3"),
         pygame.mixer.Sound("2_pac_BIG_SYKE_-_All_eyez_on_me_(DJ_Belite_remix)_(ringon.site).mp3"),
         pygame.mixer.Sound("ZODIVK_-_Devil_eyes_Slowed_(ringon.site).mp3"),
         pygame.mixer.Sound("DNDM_-_Eastern_love_(Original_mix)_(ringon.site).mp3")]
shrift = pygame.font.SysFont("serif", 40)
name_music = "INTERWORLD_-_METAMORPHOSIS"
running = True
i = 0
sound[i].play()
while running:
    screen.fill("White")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sound[i].stop()
                i = i+1
                if i > len(sound)-1:
                    i = 0
                sound[i].play()
            elif event.key == pygame.K_LEFT:
                sound[i].stop()
                i = i-1
                if i < 0:
                    i = len(sound)-1
                sound[i].play()
            elif event.key == pygame.K_UP:
                sound[i].play()
            elif event.key == pygame.K_DOWN:
                sound[i].stop()
            if i == 0:
                name_music = "INTERWORLD_-_METAMORPHOSIS_Sped_Up"
            if i == 1:
                name_music = 'kordhell-murder-in-my-mind'
            if i == 2:
                name_music = "2_pac_BIG_SYKE_-_All_eyez_on_me"
            if i == 3:
                name_music = "ZODIVK_-_Devil_eyes_Slowed"
            if i == 4:
                name_music = "DNDM_-_Eastern_love_(Original_mix)"
    text_music = shrift.render(name_music, True, (0, 0, 0))
    screen.blit(text_music, (100, 150))
    pygame.display.flip()
    clock.tick(60)