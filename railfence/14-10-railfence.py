import pygame, sys, railfence

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 32)
user_text = ''
user_key = ''
output = ''
btn_txt = 'Encode'
btn2_txt = 'Decode'

active = False
active2 = False

textbox = pygame.Rect(50,50,200,32)
textbox2 = pygame.Rect(50,100,200,32)
btn = pygame.Rect(50,160,90,32)
btn2 = pygame.Rect(160,160,90,32)

'''def read_input(text):
    if event.key == pygame.K_BACKSPACE:
        text = text[:-1]
    else:
        text += event.unicode'''

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
            if btn.collidepoint(event.pos):
                output = ''
                output += railfence.encode(user_text*int(user_key), int(user_key))
            if btn2.collidepoint(event.pos):
                output = ''
                output += railfence.decode(user_text*int(user_key), int(user_key))
            
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            elif active2:
                if event.key == pygame.K_BACKSPACE:
                    user_key = user_key[:-1]
                else:
                    user_key += event.unicode

    screen.fill("black")

    pygame.draw.rect(screen, (255, 255, 253), textbox, 1)
    pygame.draw.rect(screen, (255, 255, 253), textbox2, 1)
    pygame.draw.rect(screen, (110, 110, 110), btn)
    pygame.draw.rect(screen, (110, 110, 110), btn2)

    text_surface = font.render(user_text, True, (255, 255, 253))
    key_surface = font.render(user_key, True, (255, 255, 253))
    btn_surface = font.render(btn_txt, True, (255, 255, 253))
    btn2_surface = font.render(btn2_txt, True, (255, 255, 253))
    output_surface = font.render(output, True, (255, 255, 253))

    screen.blit(text_surface, (textbox.x+5, textbox.y+5))
    screen.blit(key_surface, (textbox2.x+5, textbox2.y+5))
    screen.blit(btn_surface, (btn.x+5, btn.y+5))
    screen.blit(btn2_surface, (btn2.x+5, btn2.y+5))
    screen.blit(output_surface, (50, 210))
    textbox.w = max(200, text_surface.get_width()+10)
    textbox2.w = max(200, text_surface.get_width()+10)

    pygame.display.update()
    clock.tick(60)


pygame.quit()