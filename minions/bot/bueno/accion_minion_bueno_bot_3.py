import pygame
import math
class Accion_minion_bueno_bot_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(625,910),(628,910),(631,910),(634,910),(637,910),(640,910),(643,910),(646,910),(649,910),(652,910),(655,910),(658,910),(661,910),(664,910),(667,910),(670,910),(673,910),(676,910),(679,910),(682,910),(685,910),(688,910),(691,910),(694,910),(697,910),(700,910),(703,910),(706,910),(709,910),(712,910),(715,910),(718,910),(721,910),(724,910),(727,910),(730,910),(733,910),(736,910),(739,910),(742,910),(745,910),(748,910),(751,910),(754,910),(757,910),(760,910),(763,910),(766,910),(769,910),(772,910),(775,910),(778,910),(781,910),(784,910),(787,910),(790,910),(793,910),(796,910),(799,910),(802,910),(805,910),(808,910),(811,910),(814,910),(817,910),(820,910),(823,910),(826,910),(829,910),(832,910),(835,910),(838,910),(841,910),(844,910),(847,910),(850,910),(853,910),(856,910),(859,910),(862,910),(865,910),(868,910),(871,910),(874,910),(877,910),(880,910),(883,910),(886,910),(889,910),(892,910),(895,910),(898,910),(901,910),(904,910),(907,910),(910,910),(913,910),(916,910),(919,910),(922,910),(925,910),(928,910),(931,910),(934,910),(937,910),(940,910),(943,910),(946,910),(949,910),(952,910),(955,910),(958,910),(961,910),(964,910),(967,910),(970,910),(973,910),(976,910),(979,910),(982,910),(985,910),(988,910),(991,910),(994,910),(997,910),(1000,910),(1003,910),(1006,910),(1009,910),(1012,910),(1015,910),(1018,910),(1021,910),(1024,910),(1027,910),(1030,910),(1033,910),(1036,910),(1039,910),(1042,910),(1045,910),(1048,910),(1051,910),(1054,910),(1057,910),(1060,910),(1063,910),(1066,910),(1069,910),(1072,910),(1075,910),(1078,910),(1081,910),(1084,910),(1087,910),(1090,910),(1093,910),(1096,910),(1099,910),(1102,910),(1105,910),(1108,910),(1111,910),(1114,910),(1117,910),(1120,910),(1123,910),(1126,910),(1129,910),(1132,910),(1135,910),(1138,910),(1141,910),(1144,910),(1147,910),(1150,910),(1153,910),(1156,910),(1159,910),(1162,910),(1165,910),(1168,910),(1171,910),(1174,910),(1177,910),(1180,910),(1183,910),(1186,910),(1189,910),(1192,910),(1195,910),(1198,910),(1201,910),(1204,910),(1207,910),(1210,910),(1213,910),(1216,910),(1219,910),(1222,910),(1225,907),(1228,904),(1231,901),(1234,898),(1237,895),(1240,892),(1243,889),(1246,886),(1249,883),(1252,880),(1255,877),(1258,874),(1261,871),(1264,868),(1267,865),(1270,862)]
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
        if self.x == 1270 and self.y == 862:
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