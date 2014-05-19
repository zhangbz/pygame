#!/usr/bin/env python
# coding=utf-8
import pygame
from pygame.locals import *

my_event = pygame.event.Event(KEYDOWN, key = K_SPACE, mod = 0, unicode = u' ')
#other way
my_event = pygame.event.Event(KEYDOWN, {"key": K_SPACE, "mod": 0, "unicode": u' '})
pygame.event.post(my_event)
