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
    pos_x = p.WIDTH - self._img.get_width()/2
    pos_y = 0 
    self.posicio = Coordenades(pos_x, self._img.get_height()/2)
    self.velocitat = Coordenades(0,0)

  def pos(self):
    return self.posicio.x, self.posicio.y
  def x(self):
    return self.posicio.x
  def y(self):
    return self.posicio.y

  def vel(self):
    return self.velocitat.x, self.velocitat.y
  def vx(self):
    return self.velocitat.x
  def vy(self):
    return self.velocitat.y

  def top(self):
    return self.y() - self._img.get_height()/2
  def bottom(self):
    return self.y() + self._img.get_height()/2

  def mou_amunt(self):
    self.velocitat = Coordenades(0,-1)
  def mou_avall(self):
    self.velocitat = Coordenades(0,1)
  def atura(self):
    self.velocitat = Coordenades(0,0)

  def actualitza(self):
    h_min = self._img.get_height()/2  
    h_max = p.HEIGHT - self._img.get_height()/2

    if self.top() < 0:
      self.posicio.y = h_min
    elif self.bottom() > p.HEIGHT:
      self.posicio.y = h_max
    else:
      self.posicio += self.velocitat

  def pinta(self, surface):
    offset_x = - self._img.get_width()/2
    offset_y = - self._img.get_height()/2

    pos_x = self.x() + offset_x
    pos_y = self.y() + offset_y

    surface.blit(self._img, (pos_x,pos_y))


p.objectes["pala"] = Pala()
