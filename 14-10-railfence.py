import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 32)
user_text = ''
user_key = ''

active = False
active2 = False

textbox = pygame.Rect(50,50,200,32)
textbox2 = pygame.Rect(50,100,200,32)

def read_input(text):
    if event.key == pygame.K_BACKSPACE:
        text = text[:-1]
    else:
        text += event.unicode

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if textbox.collidepoint(event.pos):
                active = True
                active2 = False
            if textbox2.collidepoint(event.pos):
                active = False
                active2 = True
            
        if event.type == pygame.KEYDOWN:
            if active:
                read_input(user_text)
            if active2:
                read_input(user_key)

    screen.fill("black")

    pygame.draw.rect(screen, (255, 255, 253), textbox, 1)
    pygame.draw.rect(screen, (255, 255, 253), textbox2, 1)

    text_surface = font.render(user_text, True, (255, 255, 253))
    key_surface = font.render(user_key, True, (255, 255, 253))

    screen.blit(text_surface, (textbox.x+5, textbox.y+5))
    screen.blit(key_surface, (textbox2.x+5, textbox2.y+5))
    textbox.w = max(200, text_surface.get_width()+10)
    textbox2.w = max(200, text_surface.get_width()+10)

    pygame.display.update()
    clock.tick(60)



pygame.quit()