import pygame
import math
from torres.img_torre_top_1 import Img_torre_top_1


class Accion_minion_malo_top_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(1100,147),(1097,147),(1094,147),(1091,147),(1088,147),(1085,147),(1082,147),(1079,147),(1076,147),(1073,147),(1070,147),(1067,147),(1064,147),(1061,147),(1058,147),(1055,147),(1052,147),(1049,147),(1046,147),(1043,147),(1040,147),(1037,147),(1034,147),(1031,147),(1028,147),(1025,147),(1022,147),(1019,147),(1016,147),(1013,147),(1010,147),(1007,147),(1004,147),(1001,147),(998,147),(995,147),(992,147),(989,147),(986,147),(983,147),(980,147),(977,147),(974,147),(971,147),(968,147),(965,147),(962,147),(959,147),(956,147),(953,147),(950,147),(947,147),(944,147),(941,147),(938,147),(935,147),(932,147),(929,147),(926,147),(923,147),(920,147),(917,147),(914,147),(911,147),(908,147),(905,147),(902,147),(899,147),(896,147),(893,147),(890,147),(887,147),(884,147),(881,147),(878,147),(875,147),(872,147),(869,147),(866,147),(863,147),(860,147),(857,147),(854,147),(851,147),(848,147),(845,147),(842,147),(839,147),(836,147),(833,147),(830,147),(827,147),(824,147),(821,147),(818,147),(815,147),(812,147),(809,147),(806,147),(803,147),(800,147),(797,147),(794,147),(791,147),(788,147),(785,147),(782,147),(779,147),(776,147),(773,147),(770,147),(767,147),(764,147),(761,147),(758,147),(755,147),(752,147),(749,147),(746,147),(743,147),(740,147),(737,147),(734,147),(731,147),(728,147),(725,147),(722,147),(719,147),(716,147),(713,147),(710,147),(707,147),(704,147),(701,147),(698,147),(695,147),(692,147),(689,147),(686,147),(683,147),(680,147),(677,147),(674,147),(671,147),(668,150),(665,153),(662,156),(659,159),(656,162),(653,165),(650,168),(647,171),(644,174),(641,177),(638,180),(635,183),(632,186),(629,189),(626,192),(623,195),(620,198),(617,201),(614,204),(611,207),(608,210)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

        self.nombre = ""
        self.vT1 = False
        self.T1 = Img_torre_top_1()
    def draw(self, win):
        self.nombre = self.id
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        """
        if self.x == 608 and self.y == 210:
            self.img = self.imgs2[self.contador_animacion]
            print(self.T1.viva, "Accion malo top 2")
        else:
            self.img = self.imgs[self.contador_animacion]
            print(self.T1.viva, "Accion malo top 2")

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