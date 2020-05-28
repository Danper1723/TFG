import random
import sqlite3

import pygame
import math
class Accion_minion_bueno_bot_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 200  # Barra de vida
        self.max_health = 200#Barra de vida
        self.vel = 3
        self.path = [(661,910),(664,910),(667,910),(670,910),(673,910),(676,910),(679,910),(682,910),(685,910),(688,910),(691,910),(694,910),(697,910),(700,910),(703,910),(706,910),(709,910),(712,910),(715,910),(718,910),(721,910),(724,910),(727,910),(730,910),(733,910),(736,910),(739,910),(742,910),(745,910),(748,910),(751,910),(754,910),(757,910),(760,910),(763,910),(766,910),(769,910),(772,910),(775,910),(778,910),(781,910),(784,910),(787,910),(790,910),(793,910),(796,910),(799,910),(802,910),(805,910),(808,910),(811,910),(814,910),(817,910),(820,910),(823,910),(826,910),(829,910),(832,910),(835,910),(838,910),(841,910),(844,910),(847,910),(850,910),(853,910),(856,910),(859,910),(862,910),(865,910),(868,910),(871,910),(874,910),(877,910),(880,910),(883,910),(886,910),(889,910),(892,910),(895,910),(898,910),(901,910),(904,910),(907,910),(910,910),(913,910),(916,910),(919,910),(922,910),(925,910),(928,910),(931,910),(934,910),(937,910),(940,910),(943,910),(946,910),(949,910),(952,910),(955,910),(958,910),(961,910),(964,910),(967,910),(970,910),(973,910),(976,910),(979,910),(982,910),(985,910),(988,910),(991,910),(994,910),(997,910),(1000,910),(1003,910),(1006,910),(1009,910),(1012,910),(1015,910),(1018,910),(1021,910),(1024,910),(1027,910),(1030,910),(1033,910),(1036,910),(1039,910),(1042,910),(1045,910),(1048,910),(1051,910),(1054,910),(1057,910),(1060,910),(1063,910),(1066,910),(1069,910),(1072,910),(1075,910),(1078,910),(1081,910),(1084,910),(1087,910),(1090,910),(1093,910),(1096,910),(1099,910),(1102,910),(1105,910),(1108,910),(1111,910),(1114,910),(1117,910),(1120,910),(1123,910),(1126,910),(1129,910),(1132,910),(1135,910),(1138,910),(1141,910),(1144,910),(1147,910),(1150,910),(1153,910),(1156,910),(1159,910),(1162,910),(1165,910),(1168,910),(1171,910),(1174,910),(1177,910),(1180,910),(1183,910),(1186,910),(1189,910),(1192,910),(1195,910),(1198,910),(1201,910),(1204,910),(1207,910),(1210,910),(1213,910),(1216,910),(1219,910),(1222,910),(1225,907),(1228,904),(1231,901),(1234,898),(1237,895),(1240,892),(1243,889),(1246,886),(1249,883),(1252,880),(1255,877),(1258,874),(1261,871),(1264,868),(1267,865),(1270,862)]
        
        self.path1 = [(661,910),(664,910),(667,910),(670,910),(673,910),(676,910),(679,910),(682,910),(685,910),(688,910),(691,910),(694,910),(697,910),(700,910),(703,910),(706,910),(709,910),(712,910),(715,910),(718,910),(721,910),(724,910),(727,910),(730,910),(733,910),(736,910),(739,910),(742,910),(745,910),(748,910),(751,910),(754,910),(757,910),(760,910),(763,910),(766,910),(769,910),(772,910),(775,910),(778,910),(781,910),(784,910),(787,910),(790,910),(793,910),(796,910),(799,910),(802,910),(805,910),(808,910),(811,910),(814,910),(817,910),(820,910),(823,910),(826,910),(829,910),(832,910),(835,910),(838,910),(841,910),(844,910),(847,910),(850,910),(853,910),(856,910),(859,910),(862,910),(865,910),(868,910),(871,910),(874,910),(877,910),(880,910),(883,910),(886,910),(889,910),(892,910),(895,910),(898,910),(901,910),(904,910),(907,910),(910,910),(913,910),(916,910),(919,910),(922,910),(925,910),(928,910),(931,910),(934,910),(937,910),(940,910),(943,910),(946,910),(949,910),(952,910),(955,910),(958,910),(961,910),(964,910),(967,910),(970,910),(973,910),(976,910),(979,910),(982,910),(985,910),(988,910),(991,910),(994,910),(997,910),(1000,910),(1003,910),(1006,910),(1009,910),(1012,910),(1015,910),(1018,910),(1021,910),(1024,910),(1027,910),(1030,910),(1033,910),(1036,910),(1039,910),(1042,910),(1045,910),(1048,910),(1051,910),(1054,910),(1057,910),(1060,910),(1063,910),(1066,910),(1069,910),(1072,910),(1075,910),(1078,910),(1081,910),(1084,910),(1087,910),(1090,910),(1093,910),(1096,910),(1099,910),(1102,910),(1105,910),(1108,910),(1111,910),(1114,910),(1117,910),(1120,910),(1123,910),(1126,910),(1129,910),(1132,910),(1135,910),(1138,910),(1141,910),(1144,910),(1147,910),(1150,910),(1153,910),(1156,910),(1159,910),(1162,910),(1165,910),(1168,910),(1171,910),(1174,910),(1177,910),(1180,910),(1183,910),(1186,910),(1189,910),(1192,910),(1195,910),(1198,910),(1201,910),(1204,910),(1207,910),(1210,910),(1213,910),(1216,910),(1219,910),(1222,910),(1225,907),(1228,904),(1231,901),(1234,898),(1237,895),(1240,892),(1243,889),(1246,886),(1249,883),(1252,880),(1255,877),(1258,874),(1261,871),(1264,868),(1267,865),(1270,862)]
        self.path2v = [(661,910),(664,910),(667,910),(670,910),(673,910),(676,910),(679,910),(682,910),(685,910),(688,910),(691,910),(694,910),(697,910),(700,910),(703,910),(706,910),(709,910),(712,910),(715,910),(718,910),(721,910),(724,910),(727,910),(730,910),(733,910),(736,910),(739,910),(742,910),(745,910),(748,910),(751,910),(754,910),(757,910),(760,910),(763,910),(766,910),(769,910),(772,910),(775,910),(778,910),(781,910),(784,910),(787,910),(790,910),(793,910),(796,910),(799,910),(802,910),(805,910),(808,910),(811,910),(814,910),(817,910),(820,910),(823,910),(826,910),(829,910),(832,910),(835,910),(838,910),(841,910),(844,910),(847,910),(850,910),(853,910),(856,910),(859,910),(862,910),(865,910),(868,910),(871,910),(874,910),(877,910),(880,910),(883,910),(886,910),(889,910),(892,910),(895,910),(898,910),(901,910),(904,910),(907,910),(910,910),(913,910),(916,910),(919,910),(922,910),(925,910),(928,910),(931,910),(934,910),(937,910),(940,910),(943,910),(946,910),(949,910),(952,910),(955,910),(958,910),(961,910),(964,910),(967,910),(970,910),(973,910),(976,910),(979,910),(982,910),(985,910),(988,910),(991,910),(994,910),(997,910),(1000,910),(1003,910),(1006,910),(1009,910),(1012,910),(1015,910),(1018,910),(1021,910),(1024,910),(1027,910),(1030,910),(1033,910),(1036,910),(1039,910),(1042,910),(1045,910),(1048,910),(1051,910),(1054,910),(1057,910),(1060,910),(1063,910),(1066,910),(1069,910),(1072,910),(1075,910),(1078,910),(1081,910),(1084,910),(1087,910),(1090,910),(1093,910),(1096,910),(1099,910),(1102,910),(1105,910),(1108,910),(1111,910),(1114,910),(1117,910),(1120,910),(1123,910),(1126,910),(1129,910),(1132,910),(1135,910),(1138,910),(1141,910),(1144,910),(1147,910),(1150,910),(1153,910),(1156,910),(1159,910),(1162,910),(1165,910),(1168,910),(1171,910),(1174,910),(1177,910),(1180,910),(1183,910),(1186,910),(1189,910),(1192,910),(1195,910),(1198,910),(1201,910),(1204,910),(1207,910),(1210,910),(1213,910),(1216,910),(1219,910),(1222,910),(1225,907),(1228,904),(1231,901),(1234,898),(1237,895),(1240,892),(1243,889),(1246,886),(1249,883),(1252,880),(1255,877),(1258,874),(1261,871),(1264,868),(1267,865),(1270,862),(1273,859),(1276,856),(1279,853),(1282,850),(1285,847),(1288,844),(1291,841),(1294,838),(1297,835),(1300,832),(1303,829),(1306,826),(1309,823),(1312,820),(1315,817),(1318,814),(1321,811),(1324,808),(1327,805),(1330,802),(1333,799),(1336,796),(1339,793),(1342,790),(1345,787),(1348,784),(1351,781),(1354,778),(1357,775),(1360,772),(1363,769),(1366,766),(1369,763),(1372,760),(1375,757),(1378,754),(1381,751),(1384,748),(1387,745),(1390,742),(1393,739),(1396,736),(1399,733),(1399,730),(1399,727),(1399,724),(1399,721),(1399,718),(1399,715),(1399,712),(1399,709),(1399,706),(1399,703),(1399,700),(1399,697),(1399,694),(1399,691),(1399,688),(1399,685),(1399,682),(1399,679),(1399,676),(1399,673),(1399,670),(1399,667),(1399,664),(1399,661),(1399,658),(1399,655),(1399,652),(1399,649),(1399,646),(1399,643),(1399,640),(1399,637),(1399,634),(1399,631),(1399,628),(1399,625),(1399,622),(1399,619),(1399,616),(1399,613),(1399,610),(1399,607),(1399,604),(1399,601)]
        self.path3v = [(661,910),(664,910),(667,910),(670,910),(673,910),(676,910),(679,910),(682,910),(685,910),(688,910),(691,910),(694,910),(697,910),(700,910),(703,910),(706,910),(709,910),(712,910),(715,910),(718,910),(721,910),(724,910),(727,910),(730,910),(733,910),(736,910),(739,910),(742,910),(745,910),(748,910),(751,910),(754,910),(757,910),(760,910),(763,910),(766,910),(769,910),(772,910),(775,910),(778,910),(781,910),(784,910),(787,910),(790,910),(793,910),(796,910),(799,910),(802,910),(805,910),(808,910),(811,910),(814,910),(817,910),(820,910),(823,910),(826,910),(829,910),(832,910),(835,910),(838,910),(841,910),(844,910),(847,910),(850,910),(853,910),(856,910),(859,910),(862,910),(865,910),(868,910),(871,910),(874,910),(877,910),(880,910),(883,910),(886,910),(889,910),(892,910),(895,910),(898,910),(901,910),(904,910),(907,910),(910,910),(913,910),(916,910),(919,910),(922,910),(925,910),(928,910),(931,910),(934,910),(937,910),(940,910),(943,910),(946,910),(949,910),(952,910),(955,910),(958,910),(961,910),(964,910),(967,910),(970,910),(973,910),(976,910),(979,910),(982,910),(985,910),(988,910),(991,910),(994,910),(997,910),(1000,910),(1003,910),(1006,910),(1009,910),(1012,910),(1015,910),(1018,910),(1021,910),(1024,910),(1027,910),(1030,910),(1033,910),(1036,910),(1039,910),(1042,910),(1045,910),(1048,910),(1051,910),(1054,910),(1057,910),(1060,910),(1063,910),(1066,910),(1069,910),(1072,910),(1075,910),(1078,910),(1081,910),(1084,910),(1087,910),(1090,910),(1093,910),(1096,910),(1099,910),(1102,910),(1105,910),(1108,910),(1111,910),(1114,910),(1117,910),(1120,910),(1123,910),(1126,910),(1129,910),(1132,910),(1135,910),(1138,910),(1141,910),(1144,910),(1147,910),(1150,910),(1153,910),(1156,910),(1159,910),(1162,910),(1165,910),(1168,910),(1171,910),(1174,910),(1177,910),(1180,910),(1183,910),(1186,910),(1189,910),(1192,910),(1195,910),(1198,910),(1201,910),(1204,910),(1207,910),(1210,910),(1213,910),(1216,910),(1219,910),(1222,910),(1225,907),(1228,904),(1231,901),(1234,898),(1237,895),(1240,892),(1243,889),(1246,886),(1249,883),(1252,880),(1255,877),(1258,874),(1261,871),(1264,868),(1267,865),(1270,862),(1273,859),(1276,856),(1279,853),(1282,850),(1285,847),(1288,844),(1291,841),(1294,838),(1297,835),(1300,832),(1303,829),(1306,826),(1309,823),(1312,820),(1315,817),(1318,814),(1321,811),(1324,808),(1327,805),(1330,802),(1333,799),(1336,796),(1339,793),(1342,790),(1345,787),(1348,784),(1351,781),(1354,778),(1357,775),(1360,772),(1363,769),(1366,766),(1369,763),(1372,760),(1375,757),(1378,754),(1381,751),(1384,748),(1387,745),(1390,742),(1393,739),(1396,736),(1399,733),(1399,730),(1399,727),(1399,724),(1399,721),(1399,718),(1399,715),(1399,712),(1399,709),(1399,706),(1399,703),(1399,700),(1399,697),(1399,694),(1399,691),(1399,688),(1399,685),(1399,682),(1399,679),(1399,676),(1399,673),(1399,670),(1399,667),(1399,664),(1399,661),(1399,658),(1399,655),(1399,652),(1399,649),(1399,646),(1399,643),(1399,640),(1399,637),(1399,634),(1399,631),(1399,628),(1399,625),(1399,622),(1399,619),(1399,616),(1399,613),(1399,610),(1399,607),(1399,604),(1399,601),(1399,598),(1399,595),(1399,592),(1399,589),(1399,586),(1399,583),(1399,580),(1399,577),(1399,574),(1399,571),(1399,568),(1399,565),(1399,562),(1399,559),(1399,556),(1399,553),(1399,550),(1399,547),(1399,544),(1399,541),(1399,538),(1399,535),(1399,532),(1399,529),(1399,526),(1399,523),(1399,520),(1399,517),(1399,514),(1399,511),(1399,508),(1399,505),(1399,502),(1399,499),(1399,496),(1399,493),(1399,490),(1399,487),(1399,484),(1399,481),(1399,478),(1399,475),(1399,472),(1399,469),(1399,466),(1399,463),(1399,460),(1399,457),(1399,454),(1399,451),(1399,448),(1399,445),(1399,442),(1399,439),(1399,436),(1399,433),(1399,430)]
        self.path2d = [(661,910),(664,910),(667,910),(670,910),(673,910),(676,910),(679,910),(682,910),(685,910),(688,910),(691,910),(694,910),(697,910),(700,910),(703,910),(706,910),(709,910),(712,910),(715,910),(718,910),(721,910),(724,910),(727,910),(730,910),(733,910),(736,910),(739,910),(742,910),(745,910),(748,910),(751,910),(754,910),(757,910),(760,910),(763,910),(766,910),(769,910),(772,910),(775,910),(778,910),(781,910),(784,910),(787,910),(790,910),(793,910),(796,910),(799,910),(802,910),(805,910),(808,910),(811,910),(814,910),(817,910),(820,910),(823,910),(826,910),(829,910),(832,910),(835,910),(838,910),(841,910),(844,910),(847,910),(850,910),(853,910),(856,910),(859,910),(862,910),(865,910),(868,910),(871,910),(874,910),(877,910),(880,910),(883,910),(886,910),(889,910),(892,910),(895,910)]
        self.path3d = [(661,910),(664,910),(667,910),(670,910),(673,910),(676,910),(679,910),(682,910),(685,910)]
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
                if self.x == 1270 and self.y == 862:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                        print("giro")
                    else:
                        self.img = self.imgs[self.contador_animacion]
                    # SIRVE QUE EL MINION GIRE CUANDO LLEGUE A LA CURVA
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1270 and self.y == 862:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                        print("giro")
                    else:
                        self.img = self.imgs[self.contador_animacion]
                    # SIRVE QUE EL MINION GIRE CUANDO LLEGUE A LA CURVA
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1270 and self.y == 862:
                    self.img = self.imgs3[self.contador_animacion]
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
                if self.x == 895 and self.y == 910:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 685 and self.y == 910:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 685 and self.y == 910:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2V")
                # SELECCIONADOR DE IMAGENES EN FASE 2 VICTORIA
                if self.x == 1399 and self.y == 601:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x >= 1399 and self.y <= 733:
                        self.img = self.imgs2[self.contador_animacion]
                        print("giro")
                    else:
                        self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 1399 and self.y == 430:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x >= 1399 and self.y <= 733:
                        self.img = self.imgs2[self.contador_animacion]
                        print("giro")
                    else:
                        self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 1399 and self.y == 430:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x >= 1399 and self.y <= 733:
                        self.img = self.imgs2[self.contador_animacion]
                        print("giro")
                    else:
                        self.img = self.imgs[self.contador_animacion]

            self.contador_animacion += 1
            #ESTE IF REINICIARA EL CONTADOR DE ANIMACIONES PAR A SIMULAR EL MOVIMIENTO DE LA IMGANES
            if self.contador_animacion >= len(self.imgs):
                self.contador_animacion = 0

            #"""

            if self.health > 0:
                win.blit(self.img, (self.x, self.y))
            else:
                win.blit(self.img, (10000, 10000))
                self.health = 0
                self.path_pos = 0

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

        pygame.draw.rect(win, (255, 0, 0), (self.x + 0, self.y - 5, length, 5), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x + 0, self.y - 5, health_bar, 5), 0)

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
