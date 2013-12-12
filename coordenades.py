#! /usr/bin/python3

class Coordenades(object):
  def __init__(self,nx=0,ny=0):
    self.x = nx
    self.y = ny
  def __add__(self,other):
    return Coordenades(self.x + other.x, self.y + other.y)
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  def coordenades(self):
    return (self.x,self.y)
  def coordX(self):
    return self.x
  def coordY(self):
    return self.y

class Posicio (object):
    def __init__(self,nx=0,ny=0):
      self.coord = Coordenades(nx,ny)
    def __add__(self,other):
      return self.coord + other.coord
    def posicio(self):
        return self.coord.coordenades()
    def posx(self):
        return self.coord.coordX()
    def posy(self):
        return self.coord.coordY()

class Velocitat (object):
    def __init__(self,nx=0,ny=0):
      self.coord = Coordenades(nx,ny)
    def __add__(self,other):
      return self.coord + other.coord
    def velocitat(self):
        return self.coord.coordenades()
    def velx(self):
        return self.coord.coordX()
    def vely(self):
        return self.coord.coordY()

class Element (object):
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.pos = Posicio(x,y)
        self.vel = Velocitat(vx,vy)
    def posicio(self):
      return self.pos.posicio()
    def velocitat(self):
      return self.vel.velocitat()
    def mou(self):
        self.pos += self.vel
