import pygame
import os

from personajes.accion_malo_mid_1 import Accion_malo_mid_1


class Img_malo_mid_1(Accion_malo_mid_1):

    imgs = []
    imgs2 = []
    for x in range(4):
        n = str(x)
        if x < 10:
            n = "0"+n
        imgs.append(pygame.image.load(os.path.join("..","personajes/malo1_izquierda", "3_enemies_1_run_0" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs2.append(pygame.image.load(os.path.join("..", "personajes/malo1_izquierda", "3_enemies_1_run_001.png")))
    def __init__(self):
        super().__init__()
        self.id = "Malo_mid_1"
