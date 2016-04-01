import pygame
from game import Game
from pygame.locals import *

pygame.init()
env = pygame.display.set_mode((640,480))
fond = pygame.image.load("background.jpg").convert()
env.blit(fond, (0,0))
pygame.display.flip()
on = 1
while on:
    for event in pygame.event.get():
        if event.type == QUIT:
            on = 0
g = Game(4,50)
g.display_grid()
