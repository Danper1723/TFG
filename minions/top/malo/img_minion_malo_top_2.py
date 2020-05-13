import pygame
import os

from minions.top.malo.accion_minion_malo_top_2 import Accion_minion_malo_top_2


class Img_minion_malo_top_2(Accion_minion_malo_top_2):

    imgs = []
    imgs2 = []
    imgs3 = []
    imgs4 = []
    for x in range(4):
        n = str(x)
        if x < 10:
            n = "0"+n
        imgs.append(pygame.image.load(os.path.join("..","imagenes/malo2_izquierda", "4_enemies_1_run_0" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs2.append(pygame.image.load(os.path.join("..", "imagenes/malo2_izquierda", "4_enemies_1_run_001.png")))
        imgs3.append(pygame.image.load(os.path.join("..", "imagenes/malo2_abajo", "4_enemies_1_run_0" + n + ".png")))
        imgs4.append(pygame.image.load(os.path.join("..", "imagenes/malo2_abajo", "4_enemies_1_run_001.png")))
    def __init__(self):
        super().__init__()
        self.id = "Malo_top_2"
