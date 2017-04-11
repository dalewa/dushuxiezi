# -*- coding: utf-8 -*-
import pygame
import random
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('heart.png').convert_alpha()
        self.active = False

    def move(self):
        if self.active:
            self.y -= 3
        if self.y < 0:
            self.active = False

    def restart(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width() / 2
        self.y = mouseY - self.image.get_height() / 2
        self.active = True

class Enemy:
    def restart(self):
        self.x = random.randint(10, 430)
        self.y = random.randint(-200, -50)
        self.speed = random.random()

    def __init__(self):
        self.restart()
        self.image = pygame.image.load('pine1.png').convert_alpha()

    def move(self):
        if self.y < 640:
            self.y += self.speed
        else:
            self.restart()

class Plane:
    def restart(self):
        self.x = 220
        self.y = 640
        
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('face.jpg').convert()

    def move(self):
        x, y = pygame.mouse.get_pos()
        x -= self.image.get_width() / 2
        y -= self.image.get_height() / 2
        self.x = x
        self.y = y

def checkHit(enemy, bullet):
    if (bullet.x + bullet.image.get_width() / 2 > enemy.x) and (
        bullet.x + bullet.image.get_width() / 2 < enemy.x + enemy.image.get_width()) and (
            bullet.y + bullet.image.get_height() / 2 > enemy.y) and (
                bullet.y + bullet.image.get_height() / 2 < enemy.y + enemy.image.get_height()):
        enemy.restart()
        bullet.active = False
        return True
    return False

def checkCrash(enemy, plane):
    if (plane.x + 0.7 * plane.image.get_width() > enemy.x) and (
        plane.x + 0.3 * plane.image.get_width() < enemy.x + enemy.image.get_width()) and (
            plane.y + 0.7 * plane.image.get_height() > enemy.y) and (
                plane.y + 0.3*plane.image.get_height() < enemy.y + enemy.image.get_height()):
        return True
    return False

pygame.init()
screen = pygame.display.set_mode((440, 641), 0, 32)
pygame.display.set_caption('替周森挡菠萝')
bg1 = pygame.image.load('bg1.jpg').convert()
bg2 = pygame.image.load('bg2.jpg')
bg3 = pygame.image.load('bg3.jpg')
bg4 = pygame.image.load('bg4.jpg')
bg5 = pygame.image.load('bg5.jpg')
album = [bg1, bg2, bg3, bg4, bg5]
background = random.choice(album)
plane = Plane()

bullets = []
for i in range(5):
    bullets.append(Bullet())
count_b = len(bullets)
index_b = 0
interval_b = 0

enemies = []
for i in range(5):
    enemies.append(Enemy())

gameover = False
score = 0
font = pygame.font.Font('verdanab.ttf', 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            background = random.choice(album)
        if gameover and event.type == pygame.MOUSEBUTTONUP:
            plane.restart()
            for e in enemies:
                e.restart()
            for b in bullets:
                b.active = False
            score = 0
            gameover = False    
    screen.blit(background, (0, 0))

    if not gameover:
        interval_b -= 1
        if interval_b < 0:
            bullets[index_b].restart()
            interval_b = 100
            index_b = (index_b + 1) % count_b
        for b in bullets:
            if b.active:
                for e in enemies:
                    if checkHit(e, b):
                        score += 100
                b.move()
                screen.blit(b.image, (b.x, b.y))                
        for e in enemies:
            if checkCrash(e, plane):
                gameover = True
            e.move()
            screen.blit(e.image, (e.x, e.y))
        plane.move()
        screen.blit(plane.image, (plane.x, plane.y))
        text = font.render('Score: %d' % score, 1, (122, 248, 254))
        screen.blit(text, (0, 0))
    else:
        text = font.render('Score: %d QingJiXuHuoPo~' % score, 1, (122, 248, 254))
        screen.blit(text, (40, 320))
        

    pygame.display.update()



