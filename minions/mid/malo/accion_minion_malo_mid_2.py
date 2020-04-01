import pygame
import math
class Accion_minion_malo_mid_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(1255,266),(1252,269),(1249,272),(1246,275),(1243,278),(1240,281),(1237,284),(1234,287),(1231,290),(1228,293),(1225,296),(1222,299),(1219,302),(1216,305),(1213,308),(1210,311),(1207,314),(1204,317),(1201,320),(1198,323),(1195,326),(1192,329),(1189,332),(1186,335),(1183,338),(1180,341),(1177,344),(1174,347),(1171,350),(1168,353),(1165,356),(1162,359),(1159,362),(1156,365),(1153,368),(1150,371),(1147,374),(1144,377),(1141,380),(1138,383),(1135,386),(1132,389),(1129,392),(1126,395),(1123,398),(1120,401),(1117,404),(1114,407),(1111,410),(1108,413),(1105,416),(1102,419),(1099,422),(1096,425),(1093,428),(1090,431),(1087,434),(1084,437),(1081,440),(1078,443),(1075,446),(1072,449),(1069,452),(1066,455),(1063,458),(1060,461),(1057,464),(1054,467),(1051,470),(1048,473),(1045,476),(1042,479),(1039,482),(1036,485),(1033,488),(1030,491),(1027,494),(1024,497),(1021,500),(1018,503),(1015,506),(1012,509),(1009,512),(1006,515),(1003,518),(1000,521),(997,524),(994,527),(991,527),(988,527),(985,527),(982,527),(979,527),(976,527),(973,527),(970,527),(967,527),(964,527),(961,527),(958,527),(955,527)]
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

        if self.x == 955 and self.y == 527:
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