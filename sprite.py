#!/usr/bin/env python
# coding=utf-8

background_image_filename = 'helloworld/sushiplate.jpg'
sprite_image_filename = 'helloworld/fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

#Clock对象
clock = pygame.time.Clock()

#sprite的起始x坐标
x = 0.
#速度（像素/秒）
speed = 250.

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved
    #如果移动出屏幕了，就搬到开始位置继续
    if x > 640.:
        x -= 640.

    pygame.display.update()
