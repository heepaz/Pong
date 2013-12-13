#! /usr/bin/python3
import pygame, sys
from configuracio import *
from pygame.locals import *
from sprite import *

class Imatges (object):
  def __init__(self):
    self.background = None
    self.images = {}

  def new_image(self, file_name, name, x=0, y=0, visible=True):
    self.images[name] = Sprite(file_name,x,y,visible)

  def new_background(self, file_name):
    self.background = Sprite(file_name,0,0,True)

  def draw_all(self):
    if self.background != None:
      self.background.draw()
      for image in self.images.values():
        image.draw() 

i = Imatges()
  

class Posicio (object):
    def __init__(self,nx=0,ny=0):
        self.x = nx
        self.y = ny
    def posicio(self):
        return (self.x,self.y)
    def posx(self):
        return self.x
    def posy(self):
        return self.y

class Velocitat (object):
    def __init__(self,nvx=0,nvy=0):
        self.vx = nvx
        self.vy = nvy
    def velocitat(self):
        return (self.vx,self.vy)
    def velx(self):
        return self.vx
    def vely(self):
        return self.vy

class Element (Posicio,Velocitat):
    def __init__(self, x=0, y=0, vx=0, vy=0):
        Posicio.__init__(self,x,y)
        Velocitat.__init__(self,vx,vy)
    def mou(self):
        self.x += self.vx
        self.y += self.vy
        

class Pong (object):
    def inicia(self):
       i.new_image("Imatges/ball.png","sprite",20,30,True) 
       i.new_background("Imatges/fons.jpg")
       i.new_image("Imatges/pad.jpg","paddle",0,0,False)

    def handleEvents(self):
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()

    def render(self):
      i.draw_all()
      pygame.display.update()

    def mainLoop(self):
      while True:
        self.handleEvents()
        self.render()

    def say():
        print("Això no està implementat!")

def main():
  p = Pong()
  p.inicia()
  p.mainLoop()

if __name__ == "__main__":
  main()
