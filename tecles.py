import pygame
from objectes import *
from pygame.locals import *

p = Pong()

def printu():
  print("Has pitjat la u!")

key_down_opts = {
    K_q : pygame.quit,
    K_ESCAPE : pygame.quit,
    K_u : printu,
    K_UP : p.objectes["pala"].mou_amunt,
    K_DOWN : p.objectes["pala"].mou_avall,
    K_w : p.objectes["palaC"].mou_amunt,
    K_s : p.objectes["palaC"].mou_avall
    }

key_up_opts = {
    K_UP : p.objectes["pala"].atura_amunt,
    K_DOWN : p.objectes["pala"].atura_avall,
    K_w : p.objectes["palaC"].atura_amunt,
    K_s : p.objectes["palaC"].atura_avall
    }

def key_down(event):
  if event.type == KEYDOWN:
    if event.key in key_down_opts.keys():
      key_down_opts[event.key]()

def key_up(event):
  if event.type == KEYUP:
    if event.key in key_up_opts.keys():
      key_up_opts[event.key]()

