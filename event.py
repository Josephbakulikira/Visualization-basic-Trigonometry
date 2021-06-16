import pygame

def HandleEvent(clicked, pause, showUI):
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_p:
                pause = not pause
            if event.key == pygame.K_SPACE:
                showUI = not showUI
    return running, clicked, pause, showUI
