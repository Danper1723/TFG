import pygame
import os

from heroes.Asesina.accion_asesina import Accion_asesina



class Img_asesina(Accion_asesina):


    imgs = []
    imgs2 = []
    imgs3 = []
    imgs4 = []


    for x in range(4):
        n = str(x + 1)
        imgs.append(pygame.image.load(os.path.join("..", "heroes/imagenes/asesina/derecha", "a_derecha_" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs2.append(pygame.image.load(os.path.join("..", "heroes/imagenes/asesina/alante", "a_alante_" + n + ".png")))  # ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs3.append(pygame.image.load(os.path.join("..", "heroes/imagenes/asesina/alante", "a_alante_2.png")))
        imgs4.append(pygame.image.load(os.path.join("..", "heroes/imagenes/asesina/derecha", "a_derecha_2.png")))

    def __init__(self):
        super().__init__()
        self.id = "Asesina"
