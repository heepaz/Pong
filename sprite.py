#! /usr/bin/python3
from pygame.image import load
from coordenades import *

class Sprite (object):
  def __init__(self, file_name, offset_x=None, offset_y=None, visible = True):
    self._img = load(file_name)

    # Si no s'indica un offset, es considera que ha de ser
    # de la meitat de l'sprite ja que les coordenades proporcionades
    # seran les del centre de la imatge
    if offset_x == None:
      self._off_x = - self._img.get_width() / 2
    else:
      self._off_x = offset_x
    if offset_y == None:
      self._off_y = - self._img.get_height() / 2
    else:
      self._off_y = offset_y
    self._vis = visible

  def draw(self, surface):
    if self._vis:
      x = self._pos.posx() + self._off_x
      y = self._pos.posy() + self._off_y
      surface.blit(self._img, (x,y))

