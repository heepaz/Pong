#! /usr/bin/python3
import pygame, sys
from configuracio import c
from pygame.locals import *

def inicia():
  pygame.init()
  c.screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT), 0, 32)

def handleEvents():
  for event in pygame.event.get():
    if event.type == QUIT:
      quit()

def render():
  c.screen.blit(c.background, (0, 0))


  pygame.display.update()

def mainLoop():
  while True:
    handleEvents()
    render()

def main():
  inicia()
  mainLoop()

if __name__ == "__main__":
  main()
