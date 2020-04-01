import pygame
import math
class Accion_minion_bueno_bot_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(658,885),(661,885),(664,885),(667,885),(670,885),(673,885),(676,885),(679,885),(682,885),(685,885),(688,885),(691,885),(694,885),(697,885),(700,885),(703,885),(706,885),(709,885),(712,885),(715,885),(718,885),(721,885),(724,885),(727,885),(730,885),(733,885),(736,885),(739,885),(742,885),(745,885),(748,885),(751,885),(754,885),(757,885),(760,885),(763,885),(766,885),(769,885),(772,885),(775,885),(778,885),(781,885),(784,885),(787,885),(790,885),(793,885),(796,885),(799,885),(802,885),(805,885),(808,885),(811,885),(814,885),(817,885),(820,885),(823,885),(826,885),(829,885),(832,885),(835,885),(838,885),(841,885),(844,885),(847,885),(850,885),(853,885),(856,885),(859,885),(862,885),(865,885),(868,885),(871,885),(874,885),(877,885),(880,885),(883,885),(886,885),(889,885),(892,885),(895,885),(898,885),(901,885),(904,885),(907,885),(910,885),(913,885),(916,885),(919,885),(922,885),(925,885),(928,885),(931,885),(934,885),(937,885),(940,885),(943,885),(946,885),(949,885),(952,885),(955,885),(958,885),(961,885),(964,885),(967,885),(970,885),(973,885),(976,885),(979,885),(982,885),(985,885),(988,885),(991,885),(994,885),(997,885),(1000,885),(1003,885),(1006,885),(1009,885),(1012,885),(1015,885),(1018,885),(1021,885),(1024,885),(1027,885),(1030,885),(1033,885),(1036,885),(1039,885),(1042,885),(1045,885),(1048,885),(1051,885),(1054,885),(1057,885),(1060,885),(1063,885),(1066,885),(1069,885),(1072,885),(1075,885),(1078,885),(1081,885),(1084,885),(1087,885),(1090,885),(1093,885),(1096,885),(1099,885),(1102,885),(1105,885),(1108,885),(1111,885),(1114,885),(1117,885),(1120,885),(1123,885),(1126,885),(1129,885),(1132,885),(1135,885),(1138,885),(1141,885),(1144,885),(1147,885),(1150,885),(1153,885),(1156,885),(1159,885),(1162,885),(1165,885),(1168,885),(1171,885),(1174,885),(1177,885),(1180,885),(1183,885),(1186,885),(1189,885),(1192,885),(1195,885),(1198,885),(1201,885),(1204,885),(1207,885),(1210,885),(1213,885),(1216,885),(1219,885),(1222,885),(1225,885),(1228,885),(1231,882),(1234,879),(1237,876),(1240,873),(1243,870),(1246,867),(1249,864),(1252,861),(1255,858),(1258,855),(1261,852),(1264,849),(1267,846),(1270,843),(1273,840),(1276,837),(1279,834),(1282,831),(1285,828),(1288,825)]
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
        if self.x == 1288 and self.y == 825:
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