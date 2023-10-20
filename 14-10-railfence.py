import pygame, sys, pygame_gui, railfence

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((1280, 720))
font = pygame.font.Font(None, 32)
user_text = ''
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            user_text += event.unicode

    screen.fill("black")
    text_surface = font.render(user_text, True, (255, 255, 253))
    screen.blit(text_surface, (10,10))

    pygame.display.update()
    clock.tick(60)



pygame.quit()