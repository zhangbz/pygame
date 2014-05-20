#!/usr/bin/env python
# coding=utf-8
#记住上面这行是必须的，而且保持文件的编码要一致

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

font  = pygame.font.SysFont("宋体", 40)
#font  = pygame.font.Font("simsun.ttc", 40)
text_surface = font.render(u"你好", True, (0, 0, 255))

x = 0
y = (480 - text_surface.get_height()) / 2

background = pygame.image.load("helloworld/sushiplate.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x -= 2 #文字滚动太快的话，改改这个数字
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))

    pygame.display.update()
