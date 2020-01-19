import pygame
import os
from personajes.accion_minion_top_1 import Accion_minion_top_1


class Img_minion_top_1(Accion_minion_top_1):

    imgs = []
    imgs2 = []
    imgs3 = []
    for x in range(4):
        n = str(x)
        if x < 10:
            n = "0"+n
        imgs.append(pygame.image.load(os.path.join("..","personajes/minion1_alante", "1_enemies_1_run_0" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs2.append(pygame.image.load(os.path.join("..", "personajes/minion1_derecha", "1_enemies_1_run_0" + n + ".png")))  # ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs3.append(pygame.image.load(os.path.join("..", "personajes/minion1_derecha", "1_enemies_1_run_001.png")))
    def __init__(self):
        super().__init__()
        self.id = "Minion_top_1"
