from configuracio import c
from pygame.image import load
import pygame
#from configuracio import c as conf

class Sprite (object):
    def __init__ (self, imatge = "", nx=0, ny=0, nvisible = False):
        print("Sprite! ", imatge, nx, ny, nvisible)
        self.x = nx
        self.y = ny
        self.visible = nvisible
        if imatge == "":
            self.img = load("Imatges/pad.jpg")
        print("Carregant imatge %s" % imatge)
        self.img = load(imatge)

    def draw(self):
        global c
        if self.visible:
            c.screen.blit(self.img, (self.x,self.y))

