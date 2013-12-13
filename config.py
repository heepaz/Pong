#! /usr/bin/python3
import pygame
import objectes as obj

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
    self.objectes = {}
    pala = obj.Pala()
    self.objectes["pala"] = pala
  
