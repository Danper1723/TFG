import pygame
import os

from heroes.Elfa.accion_elfa import Accion_elfa



class Img_elfa(Accion_elfa):


    imgs = []
    imgs2 = []
    imgs3 = []
    imgs4 = []


    for x in range(4):
        n = str(x + 1)
        imgs.append(pygame.image.load(os.path.join("..", "heroes/imagenes/Elfa/derecha", "e_derecha_" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs2.append(pygame.image.load(os.path.join("..", "heroes/imagenes/Elfa/alante", "e_alante_" + n + ".png")))  # ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs3.append(pygame.image.load(os.path.join("..", "heroes/imagenes/Elfa/alante", "e_alante_2.png")))
        imgs4.append(pygame.image.load(os.path.join("..", "heroes/imagenes/Elfa/derecha", "e_derecha_2.png")))

    def __init__(self):
        super().__init__()
        self.id = "Elfa"
