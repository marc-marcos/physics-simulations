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

    y = numpy.linspace(100, 500, 10)
    desphase = numpy.linspace(0, math.pi/2, 10)

    for i in range(10):
        x = mhs.movimentHarmonic(300, 1, timeElapsed, desphase[i])
        pygame.draw.circle(window_surface, (0, 255, 0), (400 + x[0], y[i]), 20, 0)

    pygame.display.update()

 
