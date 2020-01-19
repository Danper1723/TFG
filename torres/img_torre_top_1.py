import pygame
import os

from torres.accion_torre_top_1 import Accion_torre_top_1


class Img_torre_top_1(Accion_torre_top_1):

    imgv = []
    imgm = []

    imgv.append(pygame.image.load(os.path.join("..", "torres", "torres", "torre_viva.png")))

    imgm.append(pygame.image.load(os.path.join("..", "torres", "torres", "torre_muerta.png")))

    def __init__(self):
        super().__init__()
        self.id = "Torre_top_1"
        self.viva = True #False
        self.vivas()

    def vivas(self):
        #global viv
        #viv = True
        #globals()['viv'] = True
        #self.viva = globals()
        return self.viva
