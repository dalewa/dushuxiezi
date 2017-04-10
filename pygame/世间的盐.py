# -*- coding: utf-8 -*-
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((440, 641), 0, 32)
pygame.display.set_caption('hello, tiedan!')
background = pygame.image.load('世间的盐.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))

    pygame.display.update()

