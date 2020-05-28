import random
import sqlite3

import pygame
import math
class Accion_minion_bueno_bot_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 200  # Barra de vida
        self.max_health = 200  # Barra de vida
        self.vel = 3
        self.path = [(661,860),(664,860),(667,860),(670,860),(673,860),(676,860),(679,860),(682,860),(685,860),(688,860),(691,860),(694,860),(697,860),(700,860),(703,860),(706,860),(709,860),(712,860),(715,860),(718,860),(721,860),(724,860),(727,860),(730,860),(733,860),(736,860),(739,860),(742,860),(745,860),(748,860),(751,860),(754,860),(757,860),(760,860),(763,860),(766,860),(769,860),(772,860),(775,860),(778,860),(781,860),(784,860),(787,860),(790,860),(793,860),(796,860),(799,860),(802,860),(805,860),(808,860),(811,860),(814,860),(817,860),(820,860),(823,860),(826,860),(829,860),(832,860),(835,860),(838,860),(841,860),(844,860),(847,860),(850,860),(853,860),(856,860),(859,860),(862,860),(865,860),(868,860),(871,860),(874,860),(877,860),(880,860),(883,860),(886,860),(889,860),(892,860),(895,860),(898,860),(901,860),(904,860),(907,860),(910,860),(913,860),(916,860),(919,860),(922,860),(925,860),(928,860),(931,860),(934,860),(937,860),(940,860),(943,860),(946,860),(949,860),(952,860),(955,860),(958,860),(961,860),(964,860),(967,860),(970,860),(973,860),(976,860),(979,860),(982,860),(985,860),(988,860),(991,860),(994,860),(997,860),(1000,860),(1003,860),(1006,860),(1009,860),(1012,860),(1015,860),(1018,860),(1021,860),(1024,860),(1027,860),(1030,860),(1033,860),(1036,860),(1039,860),(1042,860),(1045,860),(1048,860),(1051,860),(1054,860),(1057,860),(1060,860),(1063,860),(1066,860),(1069,860),(1072,860),(1075,860),(1078,860),(1081,860),(1084,860),(1087,860),(1090,860),(1093,860),(1096,860),(1099,860),(1102,860),(1105,860),(1108,860),(1111,860),(1114,860),(1117,860),(1120,860),(1123,860),(1126,860),(1129,860),(1132,860),(1135,860),(1138,860),(1141,860),(1144,860),(1147,860),(1150,860),(1153,860),(1156,860),(1159,860),(1162,860),(1165,860),(1168,860),(1171,860),(1174,860),(1177,860),(1180,860),(1183,860),(1186,860),(1189,860),(1192,860),(1195,860),(1198,860),(1201,860),(1204,860),(1207,860),(1210,860),(1213,860),(1216,860),(1219,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1225,857),(1228,854),(1231,851),(1234,848),(1237,845),(1240,842),(1243,839),(1246,836)]
        
        self.path1 = [(661,860),(664,860),(667,860),(670,860),(673,860),(676,860),(679,860),(682,860),(685,860),(688,860),(691,860),(694,860),(697,860),(700,860),(703,860),(706,860),(709,860),(712,860),(715,860),(718,860),(721,860),(724,860),(727,860),(730,860),(733,860),(736,860),(739,860),(742,860),(745,860),(748,860),(751,860),(754,860),(757,860),(760,860),(763,860),(766,860),(769,860),(772,860),(775,860),(778,860),(781,860),(784,860),(787,860),(790,860),(793,860),(796,860),(799,860),(802,860),(805,860),(808,860),(811,860),(814,860),(817,860),(820,860),(823,860),(826,860),(829,860),(832,860),(835,860),(838,860),(841,860),(844,860),(847,860),(850,860),(853,860),(856,860),(859,860),(862,860),(865,860),(868,860),(871,860),(874,860),(877,860),(880,860),(883,860),(886,860),(889,860),(892,860),(895,860),(898,860),(901,860),(904,860),(907,860),(910,860),(913,860),(916,860),(919,860),(922,860),(925,860),(928,860),(931,860),(934,860),(937,860),(940,860),(943,860),(946,860),(949,860),(952,860),(955,860),(958,860),(961,860),(964,860),(967,860),(970,860),(973,860),(976,860),(979,860),(982,860),(985,860),(988,860),(991,860),(994,860),(997,860),(1000,860),(1003,860),(1006,860),(1009,860),(1012,860),(1015,860),(1018,860),(1021,860),(1024,860),(1027,860),(1030,860),(1033,860),(1036,860),(1039,860),(1042,860),(1045,860),(1048,860),(1051,860),(1054,860),(1057,860),(1060,860),(1063,860),(1066,860),(1069,860),(1072,860),(1075,860),(1078,860),(1081,860),(1084,860),(1087,860),(1090,860),(1093,860),(1096,860),(1099,860),(1102,860),(1105,860),(1108,860),(1111,860),(1114,860),(1117,860),(1120,860),(1123,860),(1126,860),(1129,860),(1132,860),(1135,860),(1138,860),(1141,860),(1144,860),(1147,860),(1150,860),(1153,860),(1156,860),(1159,860),(1162,860),(1165,860),(1168,860),(1171,860),(1174,860),(1177,860),(1180,860),(1183,860),(1186,860),(1189,860),(1192,860),(1195,860),(1198,860),(1201,860),(1204,860),(1207,860),(1210,860),(1213,860),(1216,860),(1219,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1225,857),(1228,854),(1231,851),(1234,848),(1237,845),(1240,842),(1243,839),(1246,836)]
        self.path2v = [(661,860),(664,860),(667,860),(670,860),(673,860),(676,860),(679,860),(682,860),(685,860),(688,860),(691,860),(694,860),(697,860),(700,860),(703,860),(706,860),(709,860),(712,860),(715,860),(718,860),(721,860),(724,860),(727,860),(730,860),(733,860),(736,860),(739,860),(742,860),(745,860),(748,860),(751,860),(754,860),(757,860),(760,860),(763,860),(766,860),(769,860),(772,860),(775,860),(778,860),(781,860),(784,860),(787,860),(790,860),(793,860),(796,860),(799,860),(802,860),(805,860),(808,860),(811,860),(814,860),(817,860),(820,860),(823,860),(826,860),(829,860),(832,860),(835,860),(838,860),(841,860),(844,860),(847,860),(850,860),(853,860),(856,860),(859,860),(862,860),(865,860),(868,860),(871,860),(874,860),(877,860),(880,860),(883,860),(886,860),(889,860),(892,860),(895,860),(898,860),(901,860),(904,860),(907,860),(910,860),(913,860),(916,860),(919,860),(922,860),(925,860),(928,860),(931,860),(934,860),(937,860),(940,860),(943,860),(946,860),(949,860),(952,860),(955,860),(958,860),(961,860),(964,860),(967,860),(970,860),(973,860),(976,860),(979,860),(982,860),(985,860),(988,860),(991,860),(994,860),(997,860),(1000,860),(1003,860),(1006,860),(1009,860),(1012,860),(1015,860),(1018,860),(1021,860),(1024,860),(1027,860),(1030,860),(1033,860),(1036,860),(1039,860),(1042,860),(1045,860),(1048,860),(1051,860),(1054,860),(1057,860),(1060,860),(1063,860),(1066,860),(1069,860),(1072,860),(1075,860),(1078,860),(1081,860),(1084,860),(1087,860),(1090,860),(1093,860),(1096,860),(1099,860),(1102,860),(1105,860),(1108,860),(1111,860),(1114,860),(1117,860),(1120,860),(1123,860),(1126,860),(1129,860),(1132,860),(1135,860),(1138,860),(1141,860),(1144,860),(1147,860),(1150,860),(1153,860),(1156,860),(1159,860),(1162,860),(1165,860),(1168,860),(1171,860),(1174,860),(1177,860),(1180,860),(1183,860),(1186,860),(1189,860),(1192,860),(1195,860),(1198,860),(1201,860),(1204,860),(1207,860),(1210,860),(1213,860),(1216,860),(1219,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1225,857),(1228,854),(1231,851),(1234,848),(1237,845),(1240,842),(1243,839),(1246,836),(1249,833),(1252,830),(1255,827),(1258,824),(1261,821),(1264,818),(1267,815),(1270,812),(1273,809),(1276,806),(1279,803),(1282,800),(1285,797),(1288,794),(1291,791),(1294,788),(1297,785),(1300,782),(1303,779),(1306,776),(1309,773),(1312,770),(1315,767),(1318,764),(1321,761),(1324,758),(1327,755),(1330,752),(1333,749),(1336,746),(1339,743),(1342,740),(1345,737),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,731),(1348,728),(1348,725),(1348,722),(1348,719),(1348,716),(1348,713),(1348,710),(1348,707),(1348,704),(1348,701),(1348,698),(1348,695),(1348,692),(1348,689),(1348,686),(1348,683),(1348,680),(1348,677),(1348,674),(1348,671),(1348,668),(1348,665),(1348,662),(1348,659),(1348,656),(1348,653),(1348,650),(1348,647),(1348,644),(1348,641),(1348,638),(1348,635),(1348,632),(1348,629),(1348,626),(1348,623),(1348,620),(1348,617),(1348,614),(1348,611),(1348,608),(1348,605),(1348,602)]
        self.path3v = [(661,860),(664,860),(667,860),(670,860),(673,860),(676,860),(679,860),(682,860),(685,860),(688,860),(691,860),(694,860),(697,860),(700,860),(703,860),(706,860),(709,860),(712,860),(715,860),(718,860),(721,860),(724,860),(727,860),(730,860),(733,860),(736,860),(739,860),(742,860),(745,860),(748,860),(751,860),(754,860),(757,860),(760,860),(763,860),(766,860),(769,860),(772,860),(775,860),(778,860),(781,860),(784,860),(787,860),(790,860),(793,860),(796,860),(799,860),(802,860),(805,860),(808,860),(811,860),(814,860),(817,860),(820,860),(823,860),(826,860),(829,860),(832,860),(835,860),(838,860),(841,860),(844,860),(847,860),(850,860),(853,860),(856,860),(859,860),(862,860),(865,860),(868,860),(871,860),(874,860),(877,860),(880,860),(883,860),(886,860),(889,860),(892,860),(895,860),(898,860),(901,860),(904,860),(907,860),(910,860),(913,860),(916,860),(919,860),(922,860),(925,860),(928,860),(931,860),(934,860),(937,860),(940,860),(943,860),(946,860),(949,860),(952,860),(955,860),(958,860),(961,860),(964,860),(967,860),(970,860),(973,860),(976,860),(979,860),(982,860),(985,860),(988,860),(991,860),(994,860),(997,860),(1000,860),(1003,860),(1006,860),(1009,860),(1012,860),(1015,860),(1018,860),(1021,860),(1024,860),(1027,860),(1030,860),(1033,860),(1036,860),(1039,860),(1042,860),(1045,860),(1048,860),(1051,860),(1054,860),(1057,860),(1060,860),(1063,860),(1066,860),(1069,860),(1072,860),(1075,860),(1078,860),(1081,860),(1084,860),(1087,860),(1090,860),(1093,860),(1096,860),(1099,860),(1102,860),(1105,860),(1108,860),(1111,860),(1114,860),(1117,860),(1120,860),(1123,860),(1126,860),(1129,860),(1132,860),(1135,860),(1138,860),(1141,860),(1144,860),(1147,860),(1150,860),(1153,860),(1156,860),(1159,860),(1162,860),(1165,860),(1168,860),(1171,860),(1174,860),(1177,860),(1180,860),(1183,860),(1186,860),(1189,860),(1192,860),(1195,860),(1198,860),(1201,860),(1204,860),(1207,860),(1210,860),(1213,860),(1216,860),(1219,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1222,860),(1225,857),(1228,854),(1231,851),(1234,848),(1237,845),(1240,842),(1243,839),(1246,836),(1249,833),(1252,830),(1255,827),(1258,824),(1261,821),(1264,818),(1267,815),(1270,812),(1273,809),(1276,806),(1279,803),(1282,800),(1285,797),(1288,794),(1291,791),(1294,788),(1297,785),(1300,782),(1303,779),(1306,776),(1309,773),(1312,770),(1315,767),(1318,764),(1321,761),(1324,758),(1327,755),(1330,752),(1333,749),(1336,746),(1339,743),(1342,740),(1345,737),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,734),(1348,731),(1348,728),(1348,725),(1348,722),(1348,719),(1348,716),(1348,713),(1348,710),(1348,707),(1348,704),(1348,701),(1348,698),(1348,695),(1348,692),(1348,689),(1348,686),(1348,683),(1348,680),(1348,677),(1348,674),(1348,671),(1348,668),(1348,665),(1348,662),(1348,659),(1348,656),(1348,653),(1348,650),(1348,647),(1348,644),(1348,641),(1348,638),(1348,635),(1348,632),(1348,629),(1348,626),(1348,623),(1348,620),(1348,617),(1348,614),(1348,611),(1348,608),(1348,605),(1348,602),(1348,599),(1348,596),(1348,593),(1348,590),(1348,587),(1348,584),(1348,581),(1348,578),(1348,575),(1348,572),(1348,569),(1348,566),(1348,563),(1348,560),(1348,557),(1348,554),(1348,551),(1348,548),(1348,545),(1348,542),(1348,539),(1348,536),(1348,533),(1348,530),(1348,527),(1348,524),(1348,521),(1348,518),(1348,515),(1348,512),(1348,509),(1348,506),(1348,503),(1348,500),(1348,497),(1348,494),(1348,491),(1348,488),(1348,485),(1348,482),(1348,479),(1348,476),(1348,473),(1348,470),(1348,467),(1348,464),(1348,461),(1348,458),(1348,455),(1348,452),(1348,449),(1348,446),(1348,443),(1348,440),(1348,437),(1348,434),(1348,431)]
        self.path2d = [(661,860),(664,860),(667,860),(670,860),(673,860),(676,860),(679,860),(682,860),(685,860),(688,860),(691,860),(694,860),(697,860),(700,860),(703,860),(706,860),(709,860),(712,860),(715,860),(718,860),(721,860),(724,860),(727,860),(730,860),(733,860),(736,860),(739,860),(742,860),(745,860),(748,860),(751,860),(754,860),(757,860),(760,860),(763,860),(766,860),(769,860),(772,860),(775,860),(778,860),(781,860),(784,860),(787,860),(790,860),(793,860),(796,860),(799,860),(802,860),(805,860),(808,860),(811,860),(814,860),(817,860),(820,860),(823,860),(826,860),(829,860),(832,860),(835,860),(838,860),(841,860),(844,860),(847,860),(850,860),(853,860),(856,860),(859,860),(862,860),(865,860),(868,860),(871,860),(874,860),(877,860),(880,860),(883,860),(886,860),(889,860),(892,860),(895,860)]
        self.path3d = [(661,860),(664,860),(667,860),(670,860),(673,860),(676,860),(679,860),(682,860),(685,860)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

        self.nombre = ""
        self.estado = False
        self.torre_bot_1_derecha = 1
        self.torre_bot_2_derecha = 1
        self.torre_bot_1_izquierda = 1
        self.torre_bot_2_izquierda = 1

    def draw(self, win):
        self.nombre = self.id
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        """
        if self.estado:

            #---
            conexion = sqlite3.connect('../datos.db')
            cursor = conexion.cursor()

            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_1_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_1_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_1_derecha = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_2_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_2_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_2_derecha = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_1_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_1_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_1_izquierda = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_2_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_2_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_2_izquierda = r[0]
            conexion.close()
            #---

            """#CAMBIAR - Esto va fuera es para poder manipular el estado de las torres
            self.torre_bot_1_derecha = 0
            self.torre_bot_2_derecha = 1
            self.torre_bot_1_izquierda = 1
            self.torre_bot_2_izquierda = 1
            #-------"""

            #SELECCIONAR LAS IMAGENES SEGUN EL ESTADO DE LA PARTIDA
            if self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1222 and self.y == 860 or self.x == 1246 and self.y == 836:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                        print("giro")
                    else:
                        self.img = self.imgs[self.contador_animacion]

                    # SIRVE QUE EL MINION GIRE CUANDO LLEGUE A LA CURVA
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1222 and self.y == 860 or self.x == 1246 and self.y == 836:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                        print("giro")
                    else:
                        self.img = self.imgs[self.contador_animacion]

                    # SIRVE QUE EL MINION GIRE CUANDO LLEGUE A LA CURVA
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1222 and self.y == 860 or self.x == 1246 and self.y == 836:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                        print("giro")
                    else:
                        self.img = self.imgs[self.contador_animacion]

                    # SIRVE QUE EL MINION GIRE CUANDO LLEGUE A LA CURVA
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2D")
                # SELECCIONADOR DE IMAGENES EN FASE 2 DERROTA
                if self.x == 895 and self.y == 860:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 685 and self.y == 860:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 685 and self.y == 860:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2V")
                # SELECCIONADOR DE IMAGENES EN FASE 2 VICTORIA
                if self.x == 1348 and self.y == 602 or self.x == 1348 and self.y == 734:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1222 and self.y == 860:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x >= 1348 and self.y <= 734:
                            self.img = self.imgs2[self.contador_animacion]
                            print("giro")
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 1348 and self.y == 431 or self.x == 1348 and self.y == 734:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1222 and self.y == 860:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x >= 1348 and self.y <= 734:
                            self.img = self.imgs2[self.contador_animacion]
                            print("giro")
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 1348 and self.y == 431 or self.x == 1348 and self.y == 734:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1222 and self.y == 860:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x >= 1348 and self.y <= 734:
                            self.img = self.imgs2[self.contador_animacion]
                            print("giro")
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
                self.path_pos = 0

            #if

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
        if self.health > 0:
            if self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                self.path = self.path1
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                self.path = self.path1
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 1")
                self.path = self.path1
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2D")
                self.path = self.path2d
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3D")
                self.path = self.path3d
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3D")
                self.path = self.path3d
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2V")
                self.path = self.path2v
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3V")
                self.path = self.path3v
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3V")
                self.path = self.path3v

        #TODA ESTA MIERDA ES PARA CALCULAR EL MOVIMIENTO ENTRE PUNTOS MEDIANTE EL TEOREMA DE PITAGORAS(VECTORES)
        if self.health <= 0:
            self.path_pos = 0
        print("tPath", len(self.path), "pathPos", self.path_pos)
        x1,y1 = self.path[self.path_pos]
        #print(self.path[self.path_pos], self.nombre)
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

        if self.health > 0:  # SOLUCION a que el minion muera y dejen de atacar todos
            self.x = mover_x
            self.y = mover_y
        return True

    def hit(self):
        """
        DEVUELVE SI EL SUBDITO HA SIDO GOLPEADO Y LE RESTA VIDA
        :return: BOOLEAN
        """
        dmg = random.choice(range(0, 3))
        #dmg = 10
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

        pygame.draw.rect(win, (255, 0, 0), (self.x - 0, self.y - 7, length, 5), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 0, self.y - 7, health_bar, 5), 0)

    """
    Si el estado esta en True quiere decir que el minion se va a dibujar
    Si el estado esta en False quiere decir que el minion no se va a dibujar
    """
    def estado_partida(self):
        if self.estado:
            self.estado = False
        else:
            self.estado = True
            self.contador_animacion = 0
            self.health = 200  # Barra de vida
            self.x = self.path[0][0]
            self.y = self.path[0][1]
            self.dis = 0
            self.path_pos = 0
            self.cont_mover = 0
            self.dist_mover = 0
