import pygame
import os

from villanos.Leia.accion_leia import Accion_leia



class Img_leia(Accion_leia):


    imgs = []
    imgs2 = []
    imgs3 = []
    imgs4 = []


    for x in range(4):
        n = str(x + 1)
        imgs.append(pygame.image.load(os.path.join("..", "villanos/imagenes/Leia/abajo", "l_abajo_" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs2.append(pygame.image.load(os.path.join("..", "villanos/imagenes/Leia/izquierda", "l_izquierda_" + n + ".png")))  # ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs3.append(pygame.image.load(os.path.join("..", "villanos/imagenes/Leia/izquierda", "l_izquierda_2.png")))
        imgs4.append(pygame.image.load(os.path.join("..", "villanos/imagenes/Leia/abajo", "l_abajo_2.png")))

    def __init__(self):
        super().__init__()
        self.id = "Minato"
