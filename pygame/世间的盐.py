# -*- coding: utf-8 -*-
import pygame
from random import choice
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('star1.png').convert_alpha()

    def move(self):
        if self.y < 0:
            mouseX, mouseY = pygame.mouse.get_pos()
            self.x = mouseX - self.image.get_width() / 2
            self.y = mouseY - self.image.get_height() / 2
        else:
            self.y -= 5

pygame.init()
screen = pygame.display.set_mode((440, 641), 0, 32)
pygame.display.set_caption('Hello, Tiedan!')
bg1 = pygame.image.load('世间的盐.jpg').convert()
bg2 = pygame.image.load('bg2.jpg')
bg3 = pygame.image.load('bg3.jpg')
bg4 = pygame.image.load('bg4.jpg')
bg5 = pygame.image.load('bg5.jpg')
album = [bg1, bg2, bg3, bg4, bg5]
background = choice(album)
plane = pygame.image.load('face.jpg').convert()
bullet = Bullet()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            background = choice(album)

    screen.blit(background, (0, 0))

    bullet.move()
    screen.blit(bullet.image, (bullet.x, bullet.y))

    x, y = pygame.mouse.get_pos()
    x -= plane.get_width() / 2
    y -= plane.get_height() / 2
    screen.blit(plane, (x, y))

    pygame.display.update()

