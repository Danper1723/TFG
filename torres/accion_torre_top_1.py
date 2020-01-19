import os

import pygame
import math

class Accion_torre_top_1:
    imgs = []

    #to = torres.img_torre_top_1.Img_torre_top_1()

    #print(to.vivas(), "dgbvfvhkwfbipwhfiwhffiop")
    def __init__(self):
        self.nombre = ""
        self.img = None
        self.dib = None
        #self.alive = to.vivas()

    def draw(self, win):
        self.nombre = self.id
        self.alive = self.viva

        #self.colocar()

    def colocar(self):
        if self.alive:
            self.img = self.imgv[0]
            return False
        else:
            self.img = self.imgm[0]
            return False

        self.dib = pygame.image.load(self.img)
        #self.dib = Game.background.blit(self.dib, (100,100))

        return False
