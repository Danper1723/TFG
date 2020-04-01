import pygame
import math
class Accion_minion_bueno_bot_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(625,860),(628,860),(631,860),(634,860),(637,860),(640,860),(643,860),(646,860),(649,860),(652,860),(655,860),(658,860),(661,860),(664,860),(667,860),(670,860),(673,860),(676,860),(679,860),(682,860),(685,860),(688,860),(691,860),(694,860),(697,860),(700,860),(703,860),(706,860),(709,860),(712,860),(715,860),(718,860),(721,860),(724,860),(727,860),(730,860),(733,860),(736,860),(739,860),(742,860),(745,860),(748,860),(751,860),(754,860),(757,860),(760,860),(763,860),(766,860),(769,860),(772,860),(775,860),(778,860),(781,860),(784,860),(787,860),(790,860),(793,860),(796,860),(799,860),(802,860),(805,860),(808,860),(811,860),(814,860),(817,860),(820,860),(823,860),(826,860),(829,860),(832,860),(835,860),(838,860),(841,860),(844,860),(847,860),(850,860),(853,860),(856,860),(859,860),(862,860),(865,860),(868,860),(871,860),(874,860),(877,860),(880,860),(883,860),(886,860),(889,860),(892,860),(895,860),(898,860),(901,860),(904,860),(907,860),(910,860),(913,860),(916,860),(919,860),(922,860),(925,860),(928,860),(931,860),(934,860),(937,860),(940,860),(943,860),(946,860),(949,860),(952,860),(955,860),(958,860),(961,860),(964,860),(967,860),(970,860),(973,860),(976,860),(979,860),(982,860),(985,860),(988,860),(991,860),(994,860),(997,860),(1000,860),(1003,860),(1006,860),(1009,860),(1012,860),(1015,860),(1018,860),(1021,860),(1024,860),(1027,860),(1030,860),(1033,860),(1036,860),(1039,860),(1042,860),(1045,860),(1048,860),(1051,860),(1054,860),(1057,860),(1060,860),(1063,860),(1066,860),(1069,860),(1072,860),(1075,860),(1078,860),(1081,860),(1084,860),(1087,860),(1090,860),(1093,860),(1096,860),(1099,860),(1102,860),(1105,860),(1108,860),(1111,860),(1114,860),(1117,860),(1120,860),(1123,860),(1126,860),(1129,860),(1132,860),(1135,860),(1138,860),(1141,860),(1144,860),(1147,860),(1150,860),(1153,860),(1156,860),(1159,860),(1162,860),(1165,860),(1168,860),(1171,860),(1174,860),(1177,860),(1180,860),(1183,860),(1186,860),(1189,860),(1192,860),(1195,860),(1198,860),(1201,860),(1204,860),(1207,860),(1210,860),(1213,857),(1216,854),(1219,851),(1222,848),(1225,845),(1228,842),(1231,839),(1234,836),(1237,833),(1240,830),(1243,827)]
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
        if self.x == 1243 and self.y == 827:
            self.img = self.imgs3[self.contador_animacion]
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