import pygame
import math
class Accion_minion_bueno_mid_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(621,829),(624,826),(627,823),(630,820),(633,817),(636,814),(639,811),(642,808),(645,805),(648,802),(651,799),(654,796),(657,793),(660,790),(663,787),(666,784),(669,781),(672,778),(675,775),(678,772),(681,769),(684,766),(687,763),(690,760),(693,757),(696,754),(699,751),(702,748),(705,745),(708,742),(711,739),(714,736),(717,733),(720,730),(723,727),(726,724),(729,721),(732,718),(735,715),(738,712),(741,709),(744,706),(747,703),(750,700),(753,697),(756,694),(759,691),(762,688),(765,685),(768,682),(771,679),(774,676),(777,673),(780,670),(783,667),(786,664),(789,661),(792,658),(795,655),(798,652),(801,649),(804,646),(807,643),(810,640),(813,637),(816,634),(819,631),(822,628),(825,625),(828,622),(831,619),(834,616),(837,613),(840,610),(843,607),(846,604),(849,601),(852,598),(855,595),(858,592),(861,589),(864,586),(867,583),(870,580),(873,577),(876,574),(879,571),(882,568),(885,568)]#,(888,568)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

        self.nombre = ""

    def draw(self, win):
        self.nombre = self.id
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        """

        if self.x == 885 and self.y == 568:
            self.img = self.imgs2[self.contador_animacion]
        else:
            if self.x >= 507 and self.y <= 315:
                self.img = self.imgs2[self.contador_animacion]
                print("giro")
            else:
                self.img = self.imgs[self.contador_animacion]
            """
            SIRVE QUE EL MINION GIRE CUANDO LLEGUE A LA CURVA
            """

        self.contador_animacion += 1
        #ESTE IF REINICIARA EL CONTADOR DE ANIMACIONES PAR A SIMULAR EL MOVIMIENTO DE LA IMGANES
        if self.contador_animacion >= len(self.imgs):
            self.contador_animacion = 0

        win.blit(self.img, (self.x, self.y))
        #if

        self.mover()

    def colision(self, X, Y):
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
        #TODA ESTA MIERDA ES PARA CALCULAR EL MOVIMIENTO ENTRE PUNTOS MEDIANTE EL TEOREMA DE PITAGORAS(VECTORES)
        x1,y1 = self.path[self.path_pos]
        print(self.path[self.path_pos], self.nombre)
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (672, 147)
        else:
            x2,y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.cont_mover += 1
        dirn = (x2-x1, y2-y1)


        mover_x, mover_y = (self.x + dirn[0] * self.cont_mover, self.y + dirn[1] * self.cont_mover)
        self.dis += math.sqrt((mover_x - x1) ** 2 + (mover_y - y1) ** 2)

        #VA AL SIGUIENTE PUNTO
        if self.dis >= move_dis:
            self.dis = 0
            self.cont_mover = 0
            """self.path_pos += 1
            if self.path_pos >= len(self.path):
                print(self.path_pos)
                return False"""
                #self.path_pos=0
                #self.path_pos += 1
            if self.path_pos < len(self.path)-1:
                self.path_pos += 1
            else:
                return False


        self.x = mover_x
        self.y = mover_y
        return True

    def hit(self):
        """
        DEVUELVE SI EL SUBDITO HA SIDO GOLPEADO Y LE RESTA VIDA
        :return: BOOLEAN
        """