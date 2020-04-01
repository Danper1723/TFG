import pygame
import math
class Accion_minion_malo_mid_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(1244,242),(1241,245),(1238,248),(1235,251),(1232,254),(1229,257),(1226,260),(1223,263),(1220,266),(1217,269),(1214,272),(1211,275),(1208,278),(1205,281),(1202,284),(1199,287),(1196,290),(1193,293),(1190,296),(1187,299),(1184,302),(1181,305),(1178,308),(1175,311),(1172,314),(1169,317),(1166,320),(1163,323),(1160,326),(1157,329),(1154,332),(1151,335),(1148,338),(1145,341),(1142,344),(1139,347),(1136,350),(1133,353),(1130,356),(1127,359),(1124,362),(1121,365),(1118,368),(1115,371),(1112,374),(1109,377),(1106,380),(1103,383),(1100,386),(1097,389),(1094,392),(1091,395),(1088,398),(1085,401),(1082,404),(1079,407),(1076,410),(1073,413),(1070,416),(1067,419),(1064,422),(1061,425),(1058,428),(1055,431),(1052,434),(1049,437),(1046,440),(1043,443),(1040,446),(1037,449),(1034,452),(1031,455),(1028,458),(1025,461),(1022,464),(1019,467),(1016,470),(1013,473),(1010,476),(1007,479),(1004,482),(1001,485),(998,488),(995,491),(992,494),(989,497)]
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

        if self.x == 989 and self.y == 497:
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