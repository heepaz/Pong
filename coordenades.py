#! /usr/bin/python3

class Coordenades(object):
  def __init__(self,nx=0,ny=0):
    self._x = nx
    self._y = ny
  def __add__(self,other):
    return Coordenades(self._x + other._x, self._y + other._y)
  def __eq__(self, other):
    return self._x == other._x and self._y == other._y

class Posicio (Coordenades):
    def __init__(self,nx=0,ny=0):
      Coordenades.__init__(self,nx,ny)
    def posicio(self):
        return (self._x,self._y)
    def posx(self):
        return self._x
    def posy(self):
        return self._y

class Velocitat (Coordenades):
    def __init__(self,nx=0,ny=0):
      Coordenades.__init__(self,nx,ny)
    def velocitat(self):
        return (self._x,self._y)
    def velx(self):
        return self._x
    def vely(self):
        return self._y

