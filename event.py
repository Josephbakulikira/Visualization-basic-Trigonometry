import pygame

def HandleEvent(clicked, pause, showUI, showValues):
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
            if event.key == pygame.K_s:
                showValues = not showValues
    return running, clicked, pause, showUI, showValues
