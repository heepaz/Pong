#! /usr/bin/python3
import pygame
from coordenades import *
from pygame.locals import *
from tecles import *
from objectes import *
    

def inicia():
  global p
  p = Pong()
  pygame.init()

def esdeveniments():
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
    elif event.type == KEYDOWN:
      key_down(event)
    elif event.type == KEYUP:
      key_up(event)


def actualitza():
  for elem in p.objectes.values():
    elem.actualitza()

def pinta():
  p.screen.blit(p.background,(0,0))
  for elem in p.objectes.values():
    elem.pinta(p.screen)

  pygame.display.update()


def main():
  p = inicia()
  while True:
    esdeveniments()
    actualitza()
    pinta()


if __name__ == "__main__":
  main()
