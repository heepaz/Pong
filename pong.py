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

  p.dt()
  text = p.font.render("%d" % p.puntsL,1,(0,0,0))
  p.screen.blit(text,(p.WIDTH/2 -30, p.HEIGHT/4))
  text = p.font.render("%d" % p.puntsR,1,(0,0,0))
  p.screen.blit(text,(p.WIDTH/2 +10, p.HEIGHT/4))
  pygame.display.update()

def fites():
  pilota = p.objectes["pilota"]
  if pilota.x() > p.WIDTH:
    p.puntsL += 1
    pilota.reinicia()
    print(p.puntsL, p.puntsR)
  elif pilota.x() < 0:
    p.puntsR += 1
    pilota.reinicia()
    print(p.puntsL, p.puntsR)

def main():
  inicia()
  while p.quit == False:
    esdeveniments()
    actualitza()
    fites()
    pinta()
  pygame.quit()


if __name__ == "__main__":
  main()
