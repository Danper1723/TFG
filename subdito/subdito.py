import pygame

class subditos:
    imgs = []

    def __init__(self, x , y , width , height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.contador_animacion = 0
        self.vida = 1
        self.path = []
        self.img = None

    def draw(self, win):
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        :return: NADA
        """
        self.contador_animacion +=1
        self.img = self.imgs[self.contador_animacion]
        #ESTE IF REINICIARA EL CONTADOR DE ANIMACIONES PAR A SIMULAR EL MOVIMIENTO DE LA IMGANES
        if self.contador_animacion >= len(self.imgs):
            self.contador_animacion = 0
        win.blit(self.img, (self.x , self.y))
        self.mover()

    def colision(self, X ,Y):
        """
        DETECTA QUE EL SUBDITO RECIBA UNA COLISION
        :param x: INT
        :param y: INT
        :return: BOOLEAN
        """
        #ESTE IF COMPROBARA MEDIANTE LAS POSICIONES EN EL EJE SI HAN GOLPEADO AL SUBDITO
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >=self.y:
                return True
        return False


    def mover(self):
        """
        MUEVE AL SUBDITO
        :return: NADA
        """

    def hit(self):
        """
        DEVUELVE SI EL SUBDITO HA SIDO GOLPEADO Y LE RESTA VIDA
        :return: BOOLEAN
        """