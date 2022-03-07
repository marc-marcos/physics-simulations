import pygame, pygame_gui
import pendulum
import math
import time

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((700, 700))

background = pygame.Surface((700, 700))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((700, 700))

clock = pygame.time.Clock()
is_running = True

startTime = time.time()

while is_running:
    time_delta = clock.tick(30)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        timeElapsed = time.time() - startTime

         
        pend = pendulum.calcPend(50, timeElapsed, math.pi)
        pygame.draw.circle(window_surface, (255, 0, 0), (300 + pend[0], 300 + pend[1]), 40, 0)

        print(time_delta)
        pygame.display.update()

