import pygame
import math
class Accion_minion_malo_top_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(1130,175),(1127,175),(1124,175),(1121,175),(1118,175),(1115,175),(1112,175),(1109,175),(1106,175),(1103,175),(1100,175),(1097,175),(1094,175),(1091,175),(1088,175),(1085,175),(1082,175),(1079,175),(1076,175),(1073,175),(1070,175),(1067,175),(1064,175),(1061,175),(1058,175),(1055,175),(1052,175),(1049,175),(1046,175),(1043,175),(1040,175),(1037,175),(1034,175),(1031,175),(1028,175),(1025,175),(1022,175),(1019,175),(1016,175),(1013,175),(1010,175),(1007,175),(1004,175),(1001,175),(998,175),(995,175),(992,175),(989,175),(986,175),(983,175),(980,175),(977,175),(974,175),(971,175),(968,175),(965,175),(962,175),(959,175),(956,175),(953,175),(950,175),(947,175),(944,175),(941,175),(938,175),(935,175),(932,175),(929,175),(926,175),(923,175),(920,175),(917,175),(914,175),(911,175),(908,175),(905,175),(902,175),(899,175),(896,175),(893,175),(890,175),(887,175),(884,175),(881,175),(878,175),(875,175),(872,175),(869,175),(866,175),(863,175),(860,175),(857,175),(854,175),(851,175),(848,175),(845,175),(842,175),(839,175),(836,175),(833,175),(830,175),(827,175),(824,175),(821,175),(818,175),(815,175),(812,175),(809,175),(806,175),(803,175),(800,175),(797,175),(794,175),(791,175),(788,175),(785,175),(782,175),(779,175),(776,175),(773,175),(770,175),(767,175),(764,175),(761,175),(758,175),(755,175),(752,175),(749,175),(746,175),(743,175),(740,175),(737,175),(734,175),(731,175),(728,175),(725,175),(722,175),(719,175),(716,175),(713,175),(710,175),(707,175),(704,175),(701,175),(698,175),(695,175),(692,175),(689,175),(686,175),(683,175),(680,175),(677,175),(674,175),(671,175),(668,178),(665,181),(662,184),(659,187),(656,190),(653,193),(650,196),(647,199)]
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
        if self.x == 647 and self.y == 199:
            self.img = self.imgs2[self.contador_animacion]
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