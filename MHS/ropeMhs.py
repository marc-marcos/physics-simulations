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

    y = numpy.linspace(50, 550, 100)
    desphase = numpy.linspace(0, 2*math.pi, 100)

    for i in range(100):
        x = mhs.movimentHarmonic(300, 0.5, timeElapsed, desphase[i])
        pygame.draw.circle(window_surface, (227, 11, 92), (400 + x[0], y[i]), 5, 0)

    pygame.display.update()

 
