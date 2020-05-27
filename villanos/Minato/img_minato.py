import pygame
import os

from villanos.Minato.accion_minato import Accion_minato



class Img_minato(Accion_minato):


    imgs = []
    imgs2 = []
    imgs3 = []
    imgs4 = []


    for x in range(4):
        n = str(x + 1)
        imgs.append(pygame.image.load(os.path.join("..", "villanos/imagenes/Minato/abajo", "m_abajo_" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs2.append(pygame.image.load(os.path.join("..", "villanos/imagenes/Minato/izquierda", "m_izquierda_" + n + ".png")))  # ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES
        imgs3.append(pygame.image.load(os.path.join("..", "villanos/imagenes/Minato/izquierda", "m_izquierda_2.png")))
        imgs4.append(pygame.image.load(os.path.join("..", "villanos/imagenes/Minato/abajo", "m_abajo_2.png")))

    def __init__(self):
        super().__init__()
        self.id = "Minato"
