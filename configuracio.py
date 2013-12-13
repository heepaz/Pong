#from sprite import Sprite
import pygame

class C (object):
  def __init__(self):
    pygame.init()
    self.WIDTH = 600
    self.HEIGHT = 400
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), 0, 32)
    self.images = {}
    self.background = None

#  def draw_all(self):
#    if self.background != None:
#      self.background.draw()
#      for name, image in self.images:
#          image.draw()
#
#  def new_image(self, file_name, name, x=0, y=0, visible=True):
#    print("new_image! ", file_name, name, x, y, visible)
#    self.images[name] = Sprite(file_name,x,y,visible)
#
#  def new_background(self,file_name):
#    self.background = Sprite(file_name,0,0,True)

  def fes(self):
    print("Això no està implementat")

c = C()
