from configuracio import C
from pygame.image import load
#from configuracio import c as conf

class Sprite (object):
    def __init__ (self, nx, ny, nvisible = False, imatge = None):
        self.x = nx
        self.y = ny
        self.visible = nvisible
        if imatge == None:
            self.img = load("Imatges/pad.jpg")
        self.img = load(imatge)

    def draw(self):
        global c
        if self.visible:
            c.screen.blit(self.img, (self.x,self.y))

c = C()
