#!/usr/bin/env python
# coding=utf-8

#指定图像文件名称
background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

#导入pygame库
import pygame
#导入一些常用的函数和常量
from pygame.locals import *          #'from pygame.locals import *'used;unable to detect undefined names
#向sys模块借一个exit函数来退出程序
from sys import exit

#初始化pygame,为使用硬件做准备
pygame.init()

#创建一个窗口
screen = pygame.display.set_mode((640, 480), 0, 32)
#设置窗口标题
pygame.display.set_caption("Hello, World!")

#加载并转换图像
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

#游戏主循环
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()

    #背景图画上去
    screen.blit(background, (0, 0))

    #获取鼠标位置
    x, y = pygame.mouse.get_pos()
    #计算光标的左上角位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    #把光标画上去
    screen.blit(mouse_cursor, (x, y))

    #刷新一下画面
    pygame.display.update()
