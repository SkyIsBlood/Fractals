import pygame
from settings import *



pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BACKGROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






    pygame.display.flip()
    clock.tick(FPS)




pygame.quit()
