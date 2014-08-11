#!/usr/bin/env python
#coding=utf-8

import math

class Vector2(object):
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    @classmethod
    def form_points(cls, P1, P2):
        return cls(P2[0] - P1[0], P2[1] - P1[1])
    
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
   
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude

    def __add__(self, rhs):   #__重载__
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)
    
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

#我们可以使用下面的方法来计算两个点之间的向量
A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.form_points(A, B)
C = AB.get_magnitude()
print AB, C
