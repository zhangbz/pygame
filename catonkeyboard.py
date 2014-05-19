#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.locals import *

CATONKEYBOARD = USEREVENT + 1
my_event = pygame.event.Event(CATONKEYBOARD, message = "Bad cat!")

for event in pygame.event.get():
    if event.type == CATONKEYBOARD:
        print event.message
