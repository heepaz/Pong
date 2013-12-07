#! /usr/bin/python3
import pygame, sys
from configuracio import c
from pygame.locals import *

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
      pygame.init()
      c.screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT), 0, 32)

    def handleEvents(self):
      for event in pygame.event.get():
        if event.type == QUIT:
          quit()

    def render(self):
      c.screen.blit(c.background, (0, 0))


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
