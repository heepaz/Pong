import pygame
from coordenades import *

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance
    
@singleton
class Pong (object):
  def __init__(self):
    pygame.init()
    self.WIDTH = 600
    self.HEIGHT = 400
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), 0, 32)
    self.background = pygame.image.load("Imatges/fons.jpg")
    # Els objectes s'afegeixen al final del fitxer, quan ja s'han definit
    # les altres classes
    self.objectes = {}
  

# Creem una instància de Pong per tal que la conegui la classe Pala
p = Pong()

class Pala(object):
  def __init__(self):
    self._img = pygame.image.load("Imatges/pad.jpg")
    pos_x = p.WIDTH - self._img.get_width()
    pos_y = self._img.get_height()/2 
    self._pos = Posicio(pos_x, pos_y)
    print(">>>> tipus de self._pos",type(self._pos),"<<<<")
    self._vel = Velocitat(0,0)

  def get_pos(self):
    print("!!!!!! tipus de self._pos", type(self._pos))
    print("!!!!!! tipus de self._vel", type(self._vel))
    return self._pos.posicio()
  def get_pos_x(self):
    return self._pos.posx()
  def get_pos_y(self):
    return self._pos.posy()

  def get_vel(self):
    return self._vel.velocitat()
  def get_vel_x(self):
    return self._vel.velx()
  def get_vel_y(self):
    return self._vel.vely()

  def mou_amunt(self):
    print("Ens movem amunt!")
    self._vel = Velocitat(0,-1)
  def mou_avall(self):
    self._vel = Velocitat(0,1)
  def atura(self):
    self._vel = Velocitat(0,0)

  def actualitza(self):
    self._pos = self._pos + self._vel

  def pinta(self, surface):
    surface.blit(self._img, self.get_pos())


p.objectes["pala"] = Pala()
