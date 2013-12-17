import pygame
import random
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

    self.newtime = pygame.time.get_ticks()
    self.oldtime = self.newtime + 5
    self.DT = 5

    self.puntsR = 0
    self.puntsL = 0

    self.font = pygame.font.SysFont("Arial", 20)

  def dt(self):
    self.oldtime = self.newtime
    self.newtime = pygame.time.get_ticks()
    self.DT = self.newtime - self.oldtime
  

# Creem una instància de Pong per tal que la conegui la classe Pala
p = Pong()

class Element (object):
  def __init__(self):
    self._img = pygame.image.load("Imatges/Default.png")
    self.posicio = Coordenades(0,0)
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
  def right(self):
    return self.x() + self._img.get_width()/2
  def left(self):
    return self.x() - self._img.get_width()/2

  def actualitza(self):
    self.posicio += self.velocitat

  def pinta(self, surface):
    offset_x = - self._img.get_width()/2
    offset_y = - self._img.get_height()/2

    pos_x = self.x() + offset_x
    pos_y = self.y() + offset_y

    surface.blit(self._img, (pos_x,pos_y))


class Pala(Element):
  def __init__(self, x=None, y=None):
    Element.__init__
    self._img = pygame.image.load("Imatges/pad.jpg")
    self.amunt = False
    self.avall = False
    if x == None:
      pos_x = p.WIDTH - self._img.get_width()/2
    else:
      pos_x = x
    if y == None:
      pos_y = 0 
    else:
      pos_y = y
    self.posicio = Coordenades(pos_x, self._img.get_height()/2)
    self.velocitat = Coordenades(0,0)

  def mou_amunt(self):
    self.amunt = True
    #self.velocitat = Coordenades(0,-1)
  def mou_avall(self):
    self.avall = True
    #self.velocitat = Coordenades(0,1)
  def atura_amunt(self):
    self.amunt = False
  def atura_avall(self):
    self.avall = False

  def actualitza(self):
    h_min = self._img.get_height()/2  
    h_max = p.HEIGHT - self._img.get_height()/2

    if self.top() < 0:
      self.posicio.y = h_min
      self.velocitat = Coordenades(0,0)
    elif self.bottom() > p.HEIGHT:
      self.posicio.y = h_max
      self.velocitat = Coordenades(0,0)
    elif self.amunt == False and self.avall == False:
      self.velocitat = Coordenades(0,0)
    elif self.amunt == True and self.avall == True:
      self.velocitat = Coordenades(0,0)
    elif self.amunt == True:
      self.velocitat = Coordenades(0,-1)
    elif self.avall == True:
      self.velocitat = Coordenades(0,1)
    self.posicio += self.velocitat/5 * p.DT

class Pilota (Element):
  def __init__(self, x=None, y=None, vx=None, vy=None):
    self._img = pygame.image.load("Imatges/ball.png")
    if x == None or y == None:
      pos_x = p.WIDTH/2
      pos_y = p.HEIGHT/2
    else:
      pos_x = x
      pos_y = y
    if vx == None or vy == None:
      pos_vx = random.randrange(12, 24) * 0.050
      pos_vy = random.randrange(5, 18) * 0.050
    else:
      pos_vx = vx
      pos_vy = vy

    self.posicio = Coordenades(pos_x, pos_y)
    self.velocitat = Coordenades(pos_vx, pos_vy)

  def collision(self, other, nom):
    if nom == "palaR":
      if self.right() >= other.left() and other.top() <= self.posicio.y <= other.bottom():
        return True
      else:
        return False
    elif nom == "palaL":
      if self.left() <= other.right() and other.top() <= self.posicio.y <= other.bottom():
        return True
      else:
        return False
    else:
      return False

  def actualitza(self):
    for nom, elem in p.objectes.items():
      if nom != "pilota":
        if self.collision(elem, nom):
          self.velocitat.x *= -1.1
    if self.top() <= 0:
      self.velocitat.y *= -1
    elif self.bottom() >= p.HEIGHT:
      self.velocitat.y *= -1
    self.posicio += self.velocitat/5 * p.DT

  def reinicia(self):
    self.posicio.x = p.WIDTH/2
    self.posicio.y = p.HEIGHT/2
    self.velocitat.x = random.randrange(12, 24) * 0.050
    self.velocitat.y = random.randrange(5, 18) * 0.050




p.objectes["palaR"] = Pala()
p.objectes["palaL"] = Pala(4,0)
p.objectes["pilota"] = Pilota()
