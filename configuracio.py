import pygame

class C (object):
  def __init__(self):
    pygame.init()
    self.WIDTH = 600
    self.HEIGHT = 400
    self.background = pygame.image.load("Imatges/fons.jpg")
    self.paddle = pygame.image.load("Imatges/pad.jpg")

  def fes(self):
    print("Això no està implementat")

c = C()
