import mhs
import math
import pygame, pygame_gui
import time

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
    time_delta = clock.tick(75)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    timeNow = time.time()
    timeElapsed = time.time() - startTime    

    x1 = mhs.movimentHarmonic(200, 1, timeElapsed)
    pygame.draw.circle(window_surface, (255, 0, 0), (400 + x1[0], 100), 40, 0)

    x2 = mhs.movimentHarmonic(200, 1, timeElapsed, faseInicial=math.pi/2)
    pygame.draw.circle(window_surface, (0, 0, 255), (400 + x2[0], 300), 40, 0)

    x3 = mhs.movimentHarmonic(200, 1, timeElapsed, faseInicial=-math.pi/2)
    pygame.draw.circle(window_surface, (0, 255, 0), (400 + x3[0], 500), 40, 0)

    print(timeElapsed)
    pygame.display.update()

 
