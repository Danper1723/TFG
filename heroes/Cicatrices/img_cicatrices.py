import pygame
import os

from heroes.Cicatrices.accion_cicatrices import Accion_cicatrices



class Img_cicatrices(Accion_cicatrices):


    imgs = []
    imgs2 = []
    imgs3 = []
    imgs4 = []


    for x in range(4):
        n = str(x + 1)
        imgs.append(pygame.image.load(os.path.join("..", "heroes/imagenes/Cicatrices/derecha", "c_derecha_" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs2.append(pygame.image.load(os.path.join("..", "heroes/imagenes/Cicatrices/alante", "c_alante_" + n + ".png")))  # ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs3.append(pygame.image.load(os.path.join("..", "heroes/imagenes/Cicatrices/alante", "c_alante_2.png")))
        imgs4.append(pygame.image.load(os.path.join("..", "heroes/imagenes/Cicatrices/derecha", "c_derecha_2.png")))

    def __init__(self):
        super().__init__()
        self.id = "Cicatrices"
