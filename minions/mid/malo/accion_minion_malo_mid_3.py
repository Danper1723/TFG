import pygame
import math
class Accion_minion_malo_mid_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(1266,292),(1263,295),(1260,298),(1257,301),(1254,304),(1251,307),(1248,310),(1245,313),(1242,316),(1239,319),(1236,322),(1233,325),(1230,328),(1227,331),(1224,334),(1221,337),(1218,340),(1215,343),(1212,346),(1209,349),(1206,352),(1203,355),(1200,358),(1197,361),(1194,364),(1191,367),(1188,370),(1185,373),(1182,376),(1179,379),(1176,382),(1173,385),(1170,388),(1167,391),(1164,394),(1161,397),(1158,400),(1155,403),(1152,406),(1149,409),(1146,412),(1143,415),(1140,418),(1137,421),(1134,424),(1131,427),(1128,430),(1125,433),(1122,436),(1119,439),(1116,442),(1113,445),(1110,448),(1107,451),(1104,454),(1101,457),(1098,460),(1095,463),(1092,466),(1089,469),(1086,472),(1083,475),(1080,478),(1077,481),(1074,484),(1071,487),(1068,490),(1065,493),(1062,496),(1059,499),(1056,502),(1053,505),(1050,508),(1047,511),(1044,514),(1041,517),(1038,520),(1035,523),(1032,526),(1029,529),(1026,532),(1023,535),(1020,538),(1017,541),(1014,544),(1011,547),(1008,550),(1005,553),(1002,556),(999,559),(996,562),(993,565),(990,568),(987,568)]
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

        if self.x == 987 and self.y == 568:
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