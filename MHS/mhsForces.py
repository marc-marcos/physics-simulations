import mhs
import math
import pygame, pygame_gui
import time
import numpy

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

clock = pygame.time.Clock()
is_running = True

startTime = time.time()

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    timeNow = time.time()
    timeElapsed = time.time() - startTime    

    x = mhs.movimentHarmonic(300, 0.5, timeElapsed)
    pygame.draw.circle(window_surface, (182, 33, 45), (400 + x[0], 300), 40, 0)

    maxes = mhs.maxMovimentHarmonic(300, 0.5, timeElapsed)

    relVel = x[1]/maxes[0]

    if relVel >= 0:
        pygame.draw.rect(window_surface, (182, 119, 33), (400 + x[0], 375, relVel * 200, 25))

    else:
        pygame.draw.rect(window_surface, (182, 119, 33), (400 + x[0] + relVel * 200, 375, relVel * -200, 25))


    relAcc = x[2]/maxes[1] 

    if relAcc >= 0:
        pygame.draw.rect(window_surface, (23, 127, 117), (400 + x[0], 200, relAcc * 200, 25))

    else:
        pygame.draw.rect(window_surface, (23, 127, 117), (400 + x[0] + relAcc * 200, 200, relAcc * -200, 25))


    pygame.display.update()

 
