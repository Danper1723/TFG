import pygame
import math
import random
import sqlite3
class Accion_minion_malo_mid_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 100  # Barra de vida
        self.max_health = 100  # Barra de vida
        self.vel = 3

        self.path = [(1234,287),(1231,290),(1228,293),(1225,296),(1222,299),(1219,302),(1216,305),(1213,308),(1210,311),(1207,314),(1204,317),(1201,320),(1198,323),(1195,326),(1192,329),(1189,332),(1186,335),(1183,338),(1180,341),(1177,344),(1174,347),(1171,350),(1168,353),(1165,356),(1162,359),(1159,362),(1156,365),(1153,368),(1150,371),(1147,374),(1144,377),(1141,380),(1138,383),(1135,386),(1132,389),(1129,392),(1126,395),(1123,398),(1120,401),(1117,404),(1114,407),(1111,410),(1108,413),(1105,416),(1102,419),(1099,422),(1096,425),(1093,428),(1090,431),(1087,434),(1084,437),(1081,440),(1078,443),(1075,446),(1072,449),(1069,452),(1066,455),(1063,458),(1060,461),(1057,464),(1054,467),(1051,470),(1048,473),(1045,476),(1042,479),(1039,482),(1036,485),(1033,488),(1030,491),(1027,494),(1024,497),(1021,500),(1018,503),(1015,506),(1012,509),(1009,512),(1006,515),(1003,518),(1000,521),(1000,521),(1000,521),(1000,521),(1000,521),(997,521),(994,521),(991,521),(988,521),(985,521),(982,521),(979,521),(976,521),(973,521),(970,521),(967,521),(964,521),(961,521),(958,521),(955,521),(952,521)]
        
        self.path1 = [(1234,287),(1231,290),(1228,293),(1225,296),(1222,299),(1219,302),(1216,305),(1213,308),(1210,311),(1207,314),(1204,317),(1201,320),(1198,323),(1195,326),(1192,329),(1189,332),(1186,335),(1183,338),(1180,341),(1177,344),(1174,347),(1171,350),(1168,353),(1165,356),(1162,359),(1159,362),(1156,365),(1153,368),(1150,371),(1147,374),(1144,377),(1141,380),(1138,383),(1135,386),(1132,389),(1129,392),(1126,395),(1123,398),(1120,401),(1117,404),(1114,407),(1111,410),(1108,413),(1105,416),(1102,419),(1099,422),(1096,425),(1093,428),(1090,431),(1087,434),(1084,437),(1081,440),(1078,443),(1075,446),(1072,449),(1069,452),(1066,455),(1063,458),(1060,461),(1057,464),(1054,467),(1051,470),(1048,473),(1045,476),(1042,479),(1039,482),(1036,485),(1033,488),(1030,491),(1027,494),(1024,497),(1021,500),(1018,503),(1015,506),(1012,509),(1009,512),(1006,515),(1003,518),(1000,521),(1000,521),(1000,521),(1000,521),(1000,521),(997,521),(994,521),(991,521),(988,521),(985,521),(982,521),(979,521),(976,521),(973,521),(970,521),(967,521),(964,521),(961,521),(958,521),(955,521),(952,521)]
        self.path2v = [(1234,287),(1231,290),(1228,293),(1225,296),(1222,299),(1219,302),(1216,305),(1213,308),(1210,311),(1207,314),(1204,317),(1201,320),(1198,323),(1195,326),(1192,329),(1189,332),(1186,335),(1183,338),(1180,341),(1177,344),(1174,347),(1171,350),(1168,353),(1165,356),(1162,359),(1159,362),(1156,365),(1153,368),(1150,371),(1147,374),(1144,377),(1141,380),(1138,383),(1135,386),(1132,389),(1129,392),(1126,395),(1123,398),(1120,401),(1117,404),(1114,407),(1111,410),(1108,413),(1105,416),(1102,419),(1099,422),(1096,425),(1093,428),(1090,431),(1087,434),(1084,437),(1081,440),(1078,443),(1075,446),(1072,449),(1069,452),(1066,455),(1063,458),(1060,461),(1057,464),(1054,467),(1051,470),(1048,473),(1045,476),(1042,479),(1039,482),(1036,485),(1033,488),(1030,491),(1027,494),(1024,497),(1021,500),(1018,503),(1015,506),(1012,509),(1009,512),(1006,515),(1003,518),(1000,521),(1000,521),(1000,521),(1000,521),(1000,521),(997,521),(994,521),(991,521),(988,521),(985,521),(982,521),(979,521),(976,521),(973,521),(970,521),(967,521),(964,521),(961,521),(958,521),(955,521),(952,521),(949,521),(946,521),(943,521),(940,521),(937,521),(934,521),(931,521),(928,521),(925,521),(922,521),(919,521),(916,521),(913,521),(910,521),(907,521),(904,521),(901,521),(898,521),(895,521),(892,521),(889,521),(886,521),(883,521),(880,521),(877,521),(877,521),(877,521),(877,521),(877,521),(877,521),(874,524),(871,527),(868,530),(865,533),(862,536),(859,539),(856,542),(853,545),(850,548),(847,551),(844,554),(841,557),(838,560),(835,563),(832,566),(829,569),(826,572),(823,575),(820,578),(817,581),(814,584),(811,587),(808,590),(805,593),(802,596),(799,599),(796,602),(793,605),(790,608),(787,611),(784,614)]
        self.path3v = [(1234,287),(1231,290),(1228,293),(1225,296),(1222,299),(1219,302),(1216,305),(1213,308),(1210,311),(1207,314),(1204,317),(1201,320),(1198,323),(1195,326),(1192,329),(1189,332),(1186,335),(1183,338),(1180,341),(1177,344),(1174,347),(1171,350),(1168,353),(1165,356),(1162,359),(1159,362),(1156,365),(1153,368),(1150,371),(1147,374),(1144,377),(1141,380),(1138,383),(1135,386),(1132,389),(1129,392),(1126,395),(1123,398),(1120,401),(1117,404),(1114,407),(1111,410),(1108,413),(1105,416),(1102,419),(1099,422),(1096,425),(1093,428),(1090,431),(1087,434),(1084,437),(1081,440),(1078,443),(1075,446),(1072,449),(1069,452),(1066,455),(1063,458),(1060,461),(1057,464),(1054,467),(1051,470),(1048,473),(1045,476),(1042,479),(1039,482),(1036,485),(1033,488),(1030,491),(1027,494),(1024,497),(1021,500),(1018,503),(1015,506),(1012,509),(1009,512),(1006,515),(1003,518),(1000,521),(1000,521),(1000,521),(1000,521),(1000,521),(997,521),(994,521),(991,521),(988,521),(985,521),(982,521),(979,521),(976,521),(973,521),(970,521),(967,521),(964,521),(961,521),(958,521),(955,521),(952,521),(949,521),(946,521),(943,521),(940,521),(937,521),(934,521),(931,521),(928,521),(925,521),(922,521),(919,521),(916,521),(913,521),(910,521),(907,521),(904,521),(901,521),(898,521),(895,521),(892,521),(889,521),(886,521),(883,521),(880,521),(877,521),(877,521),(877,521),(877,521),(877,521),(877,521),(874,524),(871,527),(868,530),(865,533),(862,536),(859,539),(856,542),(853,545),(850,548),(847,551),(844,554),(841,557),(838,560),(835,563),(832,566),(829,569),(826,572),(823,575),(820,578),(817,581),(814,584),(811,587),(808,590),(805,593),(802,596),(799,599),(796,602),(793,605),(790,608),(787,611),(784,614),(781,617),(778,620),(775,623),(772,626),(769,629),(766,632),(763,635),(760,638),(757,641),(754,644),(751,647),(748,650),(745,653),(742,656),(739,659),(736,662),(733,665),(730,668),(727,671),(724,674),(721,677),(718,680),(715,683),(712,686),(709,689),(706,692),(703,695),(700,698),(697,701),(694,704)]
        self.path2d = [(1234,287),(1231,290),(1228,293),(1225,296),(1222,299),(1219,302),(1216,305),(1213,308),(1210,311),(1207,314),(1204,317),(1201,320),(1198,323),(1195,326),(1192,329),(1189,332),(1186,335),(1183,338),(1180,341),(1177,344),(1174,347),(1171,350),(1168,353),(1165,356),(1162,359),(1159,362),(1156,365),(1153,368),(1150,371),(1147,374),(1144,377),(1141,380),(1138,383),(1135,386),(1132,389),(1129,392),(1126,395)]
        self.path3d = [(1234,287),(1231,290),(1228,293),(1225,296),(1222,299),(1219,302),(1216,305),(1213,308),(1210,311)]

        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

        self.nombre = ""
        self.estado = False
        self.torre_mid_1_derecha = 1
        self.torre_mid_2_derecha = 1
        self.torre_mid_1_izquierda = 1
        self.torre_mid_2_izquierda = 1

    def draw(self, win):
        self.nombre = self.id
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        """
        if self.estado:

            # ---
            conexion = sqlite3.connect('../datos.db')
            cursor = conexion.cursor()

            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_mid_1_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_mid_1_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_mid_1_derecha = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_mid_2_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_mid_2_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_mid_2_derecha = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_mid_1_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_mid_1_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_mid_1_izquierda = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_mid_2_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_mid_2_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_mid_2_izquierda = r[0]
            conexion.close()
            # ---

            """#CAMBIAR - Esto va fuera es para poder manipular el estado de las torres
            self.torre_mid_1_derecha = 0
            self.torre_mid_2_derecha = 1
            self.torre_mid_1_izquierda = 1
            self.torre_mid_2_izquierda = 1
            #-------"""
            if self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 1")
                if self.x == 1000 and self.y == 521 or self.x == 952 and self.y == 521:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 1")
                if self.x == 1000 and self.y == 521 or self.x == 952 and self.y == 521:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 1")
                if self.x == 1000 and self.y == 521 or self.x == 952 and self.y == 521:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2V")
                if self.x == 1000 and self.y == 521 or self.x == 877 and self.y == 521 or self.x == 784 and self.y == 614:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 1000 and self.y == 521 or self.x == 877 and self.y == 521 or self.x == 694 and self.y == 704:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 1000 and self.y == 521 or self.x == 877 and self.y == 521 or self.x == 694 and self.y == 704:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2D")
                if self.x == 1126 and self.y == 395:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3D")
                if self.x == 1210 and self.y == 311:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3D")
                if self.x == 1210 and self.y == 311:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]


            self.contador_animacion += 1
            #ESTE IF REINICIARA EL CONTADOR DE ANIMACIONES PAR A SIMULAR EL MOVIMIENTO DE LA IMGANES
            if self.contador_animacion >= len(self.imgs):
                self.contador_animacion = 0

            if self.health > 0:
                win.blit(self.img, (self.x, self.y))
            else:
                win.blit(self.img, (10000, 10000))
                self.health = 0
                # if

            self.mover()
            if self.health > 0:
                self.draw_health_bar(win)

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
        # SELECCIONAR EL PATH SEGUN EL ESTADO DE LA PARTIDA
        if self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
            print("FASE 1")
            self.path = self.path1
        elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
            print("FASE 1")
            self.path = self.path1
        elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
            print("FASE 1")
            self.path = self.path1
        elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
            print("FASE 2V")
            self.path = self.path2v
        elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
            print("FASE 3V")
            self.path = self.path3v
        elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
            print("FASE 3V")
            self.path = self.path3v
        elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
            print("FASE 2D")
            self.path = self.path2d
        elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
            print("FASE 3D")
            self.path = self.path3d
        elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
            print("FASE 3D")
            self.path = self.path3d
        #TODA ESTA MIERDA ES PARA CALCULAR EL MOVIMIENTO ENTRE PUNTOS MEDIANTE EL TEOREMA DE PITAGORAS(VECTORES)
        if self.health <= 0:
            self.path_pos = 0
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
        dmg = random.choice(range(0, 3))
        # dmg = 10
        self.health -= dmg
        if self.health <= 0:
            self.path_pos = 0
            self.health = 0

    def draw_health_bar(self, win):  # Barra de vida
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """

        length = 25
        move_by = length / self.max_health
        health_bar = round(move_by * self.health)

        pygame.draw.rect(win, (255, 0, 0), (self.x + 5, self.y - 5, length, 5), 0)
        pygame.draw.rect(win, (158, 18, 228), (self.x + 5, self.y - 5, health_bar, 5), 0)

    def estado_partida(self):
        if self.estado:
            self.estado = False
        else:
            self.estado = True
            self.contador_animacion = 0
            self.health = 100  # Barra de vida
            self.x = self.path[0][0]
            self.y = self.path[0][1]
            self.dis = 0
            self.path_pos = 0
            self.cont_mover = 0
            self.dist_mover = 0