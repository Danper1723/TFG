import pygame
import os

from minions.top.bueno.accion_minion_bueno_top_3 import Accion_minion_bueno_top_3


class Img_minion_bueno_top_3(Accion_minion_bueno_top_3):

    imgs = []
    imgs2 = []
    imgs3 = []
    imgs4 = []
    for x in range(4):
        n = str(x)
        if x < 10:
            n = "0"+n
        imgs.append(pygame.image.load(os.path.join("..","imagenes/minion1_alante", "1_enemies_1_run_0" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs2.append(pygame.image.load(os.path.join("..", "imagenes/minion1_derecha", "1_enemies_1_run_0" + n + ".png")))  # ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs3.append(pygame.image.load(os.path.join("..", "imagenes/minion1_derecha", "1_enemies_1_run_001.png")))
        imgs4.append(pygame.image.load(os.path.join("..", "imagenes/minion1_alante", "1_enemies_1_run_001.png")))
    def __init__(self):
        super().__init__()
        self.id = "Minion_top_3"
