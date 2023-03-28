import pygame

pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Load the audio files
audio_files = ["2_pac_BIG_SYKE_-_All_eyez_on_me_(DJ_Belite_remix)_(ringon.site).mp3", "ZODIVK_-_Devil_eyes_Slowed_(ringon.site).mp3", "DNDM_-_Eastern_love_(Original_mix)_(ringon.site).mp3"]
sounds = []
for file in audio_files:
    sound = pygame.mixer.Sound(file)
    sounds.append(sound)    1

# Set up the current sound index
current_sound_index = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Play the previous sound
                current_sound_index -= 1
                if current_sound_index < 0:
                    current_sound_index = len(sounds) - 1
                sounds[current_sound_index].play()
            elif event.key == pygame.K_RIGHT:
                # Play the next sound
                current_sound_index += 1
                if current_sound_index >= len(sounds):
                    current_sound_index = 0
                sounds[current_sound_index].play()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.update()
