import pygame
import math

#from torres.accion_torre_top_1 import Accion_torre_top_1
from torres.img_torre_top_1 import Img_torre_top_1

class Accion_malo_top_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(1130,125),(1127,125),(1124,125),(1121,125),(1118,125),(1115,125),(1112,125),(1109,125),(1106,125),(1103,125),(1100,125),(1097,125),(1094,125),(1091,125),(1088,125),(1085,125),(1082,125),(1079,125),(1076,125),(1073,125),(1070,125),(1067,125),(1064,125),(1061,125),(1058,125),(1055,125),(1052,125),(1049,125),(1046,125),(1043,125),(1040,125),(1037,125),(1034,125),(1031,125),(1028,125),(1025,125),(1022,125),(1019,125),(1016,125),(1013,125),(1010,125),(1007,125),(1004,125),(1001,125),(998,125),(995,125),(992,125),(989,125),(986,125),(983,125),(980,125),(977,125),(974,125),(971,125),(968,125),(965,125),(962,125),(959,125),(956,125),(953,125),(950,125),(947,125),(944,125),(941,125),(938,125),(935,125),(932,125),(929,125),(926,125),(923,125),(920,125),(917,125),(914,125),(911,125),(908,125),(905,125),(902,125),(899,125),(896,125),(893,125),(890,125),(887,125),(884,125),(881,125),(878,125),(875,125),(872,125),(869,125),(866,125),(863,125),(860,125),(857,125),(854,125),(851,125),(848,125),(845,125),(842,125),(839,125),(836,125),(833,125),(830,125),(827,125),(824,125),(821,125),(818,125),(815,125),(812,125),(809,125),(806,125),(803,125),(800,125),(797,125),(794,125),(791,125),(788,125),(785,125),(782,125),(779,125),(776,125),(773,125),(770,125),(767,125),(764,125),(761,125),(758,125),(755,125),(752,125),(749,125),(746,125),(743,125),(740,125),(737,125),(734,125),(731,125),(728,125),(725,125),(722,125),(719,125),(716,125),(713,125),(710,125),(707,125),(704,125),(701,125),(698,125),(695,125),(692,125),(689,125),(686,125),(683,125),(680,125),(677,125),(674,125),(671,125),(668,128),(665,131),(662,134),(659,137),(656,140),(653,143),(650,146),(647,149),(644,152),(641,155),(638,158),(635,161),(632,164),(629,167),(626,170),(623,173)]
        self.path1 = [(1130,125),(1127,125),(1124,125),(1121,125),(1118,125),(1115,125),(1112,125),(1109,125),(1106,125),(1103,125),(1100,125),(1097,125),(1094,125),(1091,125),(1088,125),(1085,125),(1082,125),(1079,125),(1076,125),(1073,125),(1070,125),(1067,125),(1064,125),(1061,125),(1058,125),(1055,125),(1052,125),(1049,125),(1046,125),(1043,125),(1040,125),(1037,125),(1034,125),(1031,125),(1028,125),(1025,125),(1022,125),(1019,125),(1016,125),(1013,125),(1010,125),(1007,125),(1004,125),(1001,125),(998,125),(995,125),(992,125),(989,125),(986,125),(983,125),(980,125),(977,125),(974,125),(971,125),(968,125),(965,125),(962,125),(959,125),(956,125),(953,125)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

        self.nombre = ""
        self.vT1 = False
        #self.T1 = Accion_torre_top_1()
        self.T1 = Img_torre_top_1()

    def draw(self, win):
        self.nombre = self.id
        self.vT1 = self.T1.viva
        #print(Img_torre_top_1.viv)
        #print(self.vT1, "Un mojon pa´ti")
        #self.vT1 = torreT1.hola(torreT1)
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        """

        #if self.x == 959 and self.y == 125:
            #self.T1.viva = False

        if self.vT1 is False and self.x == 953 and self.y == 125:
            self.img = self.imgs2[self.contador_animacion]
            #self.T1.viva = True
        elif self.x == 623 and self.y == 173:
            self.img = self.imgs2[self.contador_animacion]

        else:
            #print(self.vT1)
            #self.T1.viva = False
            self.img = self.imgs[self.contador_animacion]

            """
            SIRVE QUE EL MINION GIRE CUANDO LLEGUE A LA CURVA
            """
        #print(self.T1.viva, "dfgh")
        self.contador_animacion += 1
        #ESTE IF REINICIARA EL CONTADOR DE ANIMACIONES PAR A SIMULAR EL MOVIMIENTO DE LA IMGANES
        if self.contador_animacion >= len(self.imgs):
            self.contador_animacion = 0

        win.blit(self.img, (self.x, self.y))

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
        if self.vT1:
            #pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
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
            #pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
        else:
            # pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
            # TODA ESTA MIERDA ES PARA CALCULAR EL MOVIMIENTO ENTRE PUNTOS MEDIANTE EL TEOREMA DE PITAGORAS(VECTORES)
            x1, y1 = self.path1[self.path_pos]
            print(self.path1[self.path_pos], self.nombre)
            if self.path_pos + 1 >= len(self.path1):
                x2, y2 = (672, 147)
            else:
                x2, y2 = self.path1[self.path_pos + 1]

            move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            self.cont_mover += 1
            dirn = (x2 - x1, y2 - y1)

            mover_x, mover_y = (self.x + dirn[0] * self.cont_mover, self.y + dirn[1] * self.cont_mover)
            self.dis += math.sqrt((mover_x - x1) ** 2 + (mover_y - y1) ** 2)

            # VA AL SIGUIENTE PUNTO
            if self.dis >= move_dis:
                self.dis = 0
                self.cont_mover = 0
                # self.path_pos=0
                # self.path_pos += 1
                if self.path_pos < len(self.path1) - 1:
                    self.path_pos += 1
                else:
                    return False
            # pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp

        self.x = mover_x
        self.y = mover_y
        return True

    def hit(self):
        """
        DEVUELVE SI EL SUBDITO HA SIDO GOLPEADO Y LE RESTA VIDA
        :return: BOOLEAN
        """