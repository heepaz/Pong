#! /usr/bin/python3

class Coordenades(object):
  def __init__(self,nx=0,ny=0):
    self.x = nx
    self.y = ny
  def __add__(self,other):
    return Coordenades(self.x + other.x, self.y + other.y)
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
