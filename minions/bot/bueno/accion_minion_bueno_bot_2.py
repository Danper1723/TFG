import random
import sqlite3

import pygame
import math
class Accion_minion_bueno_bot_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 100  # Barra de vida
        self.max_health = 100  # Barra de vida
        self.vel = 3
        self.path = [(694,885),(697,885),(700,885),(703,885),(706,885),(709,885),(712,885),(715,885),(718,885),(721,885),(724,885),(727,885),(730,885),(733,885),(736,885),(739,885),(742,885),(745,885),(748,885),(751,885),(754,885),(757,885),(760,885),(763,885),(766,885),(769,885),(772,885),(775,885),(778,885),(781,885),(784,885),(787,885),(790,885),(793,885),(796,885),(799,885),(802,885),(805,885),(808,885),(811,885),(814,885),(817,885),(820,885),(823,885),(826,885),(829,885),(832,885),(835,885),(838,885),(841,885),(844,885),(847,885),(850,885),(853,885),(856,885),(859,885),(862,885),(865,885),(868,885),(871,885),(874,885),(877,885),(880,885),(883,885),(886,885),(889,885),(892,885),(895,885),(898,885),(901,885),(904,885),(907,885),(910,885),(913,885),(916,885),(919,885),(922,885),(925,885),(928,885),(931,885),(934,885),(937,885),(940,885),(943,885),(946,885),(949,885),(952,885),(955,885),(958,885),(961,885),(964,885),(967,885),(970,885),(973,885),(976,885),(979,885),(982,885),(985,885),(988,885),(991,885),(994,885),(997,885),(1000,885),(1003,885),(1006,885),(1009,885),(1012,885),(1015,885),(1018,885),(1021,885),(1024,885),(1027,885),(1030,885),(1033,885),(1036,885),(1039,885),(1042,885),(1045,885),(1048,885),(1051,885),(1054,885),(1057,885),(1060,885),(1063,885),(1066,885),(1069,885),(1072,885),(1075,885),(1078,885),(1081,885),(1084,885),(1087,885),(1090,885),(1093,885),(1096,885),(1099,885),(1102,885),(1105,885),(1108,885),(1111,885),(1114,885),(1117,885),(1120,885),(1123,885),(1126,885),(1129,885),(1132,885),(1135,885),(1138,885),(1141,885),(1144,885),(1147,885),(1150,885),(1153,885),(1156,885),(1159,885),(1162,885),(1165,885),(1168,885),(1171,885),(1174,885),(1177,885),(1180,885),(1183,885),(1186,885),(1189,885),(1192,885),(1195,885),(1198,885),(1201,885),(1204,885),(1207,885),(1210,885),(1213,885),(1216,885),(1219,885),(1222,885),(1225,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1231,882),(1234,879),(1237,876),(1240,873),(1243,870),(1246,867),(1249,864),(1252,861),(1255,858),(1258,855),(1261,852),(1264,849),(1267,846),(1270,843),(1273,840),(1276,837),(1279,834),(1282,831),(1285,828),(1288,825),(1291,822)]
        
        self.path1 = [(694,885),(697,885),(700,885),(703,885),(706,885),(709,885),(712,885),(715,885),(718,885),(721,885),(724,885),(727,885),(730,885),(733,885),(736,885),(739,885),(742,885),(745,885),(748,885),(751,885),(754,885),(757,885),(760,885),(763,885),(766,885),(769,885),(772,885),(775,885),(778,885),(781,885),(784,885),(787,885),(790,885),(793,885),(796,885),(799,885),(802,885),(805,885),(808,885),(811,885),(814,885),(817,885),(820,885),(823,885),(826,885),(829,885),(832,885),(835,885),(838,885),(841,885),(844,885),(847,885),(850,885),(853,885),(856,885),(859,885),(862,885),(865,885),(868,885),(871,885),(874,885),(877,885),(880,885),(883,885),(886,885),(889,885),(892,885),(895,885),(898,885),(901,885),(904,885),(907,885),(910,885),(913,885),(916,885),(919,885),(922,885),(925,885),(928,885),(931,885),(934,885),(937,885),(940,885),(943,885),(946,885),(949,885),(952,885),(955,885),(958,885),(961,885),(964,885),(967,885),(970,885),(973,885),(976,885),(979,885),(982,885),(985,885),(988,885),(991,885),(994,885),(997,885),(1000,885),(1003,885),(1006,885),(1009,885),(1012,885),(1015,885),(1018,885),(1021,885),(1024,885),(1027,885),(1030,885),(1033,885),(1036,885),(1039,885),(1042,885),(1045,885),(1048,885),(1051,885),(1054,885),(1057,885),(1060,885),(1063,885),(1066,885),(1069,885),(1072,885),(1075,885),(1078,885),(1081,885),(1084,885),(1087,885),(1090,885),(1093,885),(1096,885),(1099,885),(1102,885),(1105,885),(1108,885),(1111,885),(1114,885),(1117,885),(1120,885),(1123,885),(1126,885),(1129,885),(1132,885),(1135,885),(1138,885),(1141,885),(1144,885),(1147,885),(1150,885),(1153,885),(1156,885),(1159,885),(1162,885),(1165,885),(1168,885),(1171,885),(1174,885),(1177,885),(1180,885),(1183,885),(1186,885),(1189,885),(1192,885),(1195,885),(1198,885),(1201,885),(1204,885),(1207,885),(1210,885),(1213,885),(1216,885),(1219,885),(1222,885),(1225,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1231,882),(1234,879),(1237,876),(1240,873),(1243,870),(1246,867),(1249,864),(1252,861),(1255,858),(1258,855),(1261,852),(1264,849),(1267,846),(1270,843),(1273,840),(1276,837),(1279,834),(1282,831),(1285,828),(1288,825),(1291,822)]
        self.path2v = [(694,885),(697,885),(700,885),(703,885),(706,885),(709,885),(712,885),(715,885),(718,885),(721,885),(724,885),(727,885),(730,885),(733,885),(736,885),(739,885),(742,885),(745,885),(748,885),(751,885),(754,885),(757,885),(760,885),(763,885),(766,885),(769,885),(772,885),(775,885),(778,885),(781,885),(784,885),(787,885),(790,885),(793,885),(796,885),(799,885),(802,885),(805,885),(808,885),(811,885),(814,885),(817,885),(820,885),(823,885),(826,885),(829,885),(832,885),(835,885),(838,885),(841,885),(844,885),(847,885),(850,885),(853,885),(856,885),(859,885),(862,885),(865,885),(868,885),(871,885),(874,885),(877,885),(880,885),(883,885),(886,885),(889,885),(892,885),(895,885),(898,885),(901,885),(904,885),(907,885),(910,885),(913,885),(916,885),(919,885),(922,885),(925,885),(928,885),(931,885),(934,885),(937,885),(940,885),(943,885),(946,885),(949,885),(952,885),(955,885),(958,885),(961,885),(964,885),(967,885),(970,885),(973,885),(976,885),(979,885),(982,885),(985,885),(988,885),(991,885),(994,885),(997,885),(1000,885),(1003,885),(1006,885),(1009,885),(1012,885),(1015,885),(1018,885),(1021,885),(1024,885),(1027,885),(1030,885),(1033,885),(1036,885),(1039,885),(1042,885),(1045,885),(1048,885),(1051,885),(1054,885),(1057,885),(1060,885),(1063,885),(1066,885),(1069,885),(1072,885),(1075,885),(1078,885),(1081,885),(1084,885),(1087,885),(1090,885),(1093,885),(1096,885),(1099,885),(1102,885),(1105,885),(1108,885),(1111,885),(1114,885),(1117,885),(1120,885),(1123,885),(1126,885),(1129,885),(1132,885),(1135,885),(1138,885),(1141,885),(1144,885),(1147,885),(1150,885),(1153,885),(1156,885),(1159,885),(1162,885),(1165,885),(1168,885),(1171,885),(1174,885),(1177,885),(1180,885),(1183,885),(1186,885),(1189,885),(1192,885),(1195,885),(1198,885),(1201,885),(1204,885),(1207,885),(1210,885),(1213,885),(1216,885),(1219,885),(1222,885),(1225,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1231,882),(1234,879),(1237,876),(1240,873),(1243,870),(1246,867),(1249,864),(1252,861),(1255,858),(1258,855),(1261,852),(1264,849),(1267,846),(1270,843),(1273,840),(1276,837),(1279,834),(1282,831),(1285,828),(1288,825),(1291,822),(1294,819),(1297,816),(1300,813),(1303,810),(1306,807),(1309,804),(1312,801),(1315,798),(1318,795),(1321,792),(1324,789),(1327,786),(1330,783),(1333,780),(1336,777),(1339,774),(1342,771),(1345,768),(1348,765),(1351,762),(1354,759),(1357,756),(1360,753),(1363,750),(1366,747),(1369,744),(1372,741),(1375,738),(1375,738),(1375,738),(1375,738),(1375,735),(1375,732),(1375,729),(1375,726),(1375,723),(1375,720),(1375,717),(1375,714),(1375,711),(1375,708),(1375,705),(1375,702),(1375,699),(1375,696),(1375,693),(1375,690),(1375,687),(1375,684),(1375,681),(1375,678),(1375,675),(1375,672),(1375,669),(1375,666),(1375,663),(1375,660),(1375,657),(1375,654),(1375,651),(1375,648),(1375,645),(1375,642),(1375,639),(1375,636),(1375,633),(1375,630),(1375,627),(1375,624),(1375,621),(1375,618),(1375,615),(1375,612),(1375,609),(1375,606),(1375,603),(1375,600),(1375,597),(1375,594),(1375,591),(1375,588),(1375,585),(1375,582),(1375,579),(1375,576),(1375,573),(1375,570),(1375,567),(1375,564),(1375,561)]
        self.path3v = [(694,885),(697,885),(700,885),(703,885),(706,885),(709,885),(712,885),(715,885),(718,885),(721,885),(724,885),(727,885),(730,885),(733,885),(736,885),(739,885),(742,885),(745,885),(748,885),(751,885),(754,885),(757,885),(760,885),(763,885),(766,885),(769,885),(772,885),(775,885),(778,885),(781,885),(784,885),(787,885),(790,885),(793,885),(796,885),(799,885),(802,885),(805,885),(808,885),(811,885),(814,885),(817,885),(820,885),(823,885),(826,885),(829,885),(832,885),(835,885),(838,885),(841,885),(844,885),(847,885),(850,885),(853,885),(856,885),(859,885),(862,885),(865,885),(868,885),(871,885),(874,885),(877,885),(880,885),(883,885),(886,885),(889,885),(892,885),(895,885),(898,885),(901,885),(904,885),(907,885),(910,885),(913,885),(916,885),(919,885),(922,885),(925,885),(928,885),(931,885),(934,885),(937,885),(940,885),(943,885),(946,885),(949,885),(952,885),(955,885),(958,885),(961,885),(964,885),(967,885),(970,885),(973,885),(976,885),(979,885),(982,885),(985,885),(988,885),(991,885),(994,885),(997,885),(1000,885),(1003,885),(1006,885),(1009,885),(1012,885),(1015,885),(1018,885),(1021,885),(1024,885),(1027,885),(1030,885),(1033,885),(1036,885),(1039,885),(1042,885),(1045,885),(1048,885),(1051,885),(1054,885),(1057,885),(1060,885),(1063,885),(1066,885),(1069,885),(1072,885),(1075,885),(1078,885),(1081,885),(1084,885),(1087,885),(1090,885),(1093,885),(1096,885),(1099,885),(1102,885),(1105,885),(1108,885),(1111,885),(1114,885),(1117,885),(1120,885),(1123,885),(1126,885),(1129,885),(1132,885),(1135,885),(1138,885),(1141,885),(1144,885),(1147,885),(1150,885),(1153,885),(1156,885),(1159,885),(1162,885),(1165,885),(1168,885),(1171,885),(1174,885),(1177,885),(1180,885),(1183,885),(1186,885),(1189,885),(1192,885),(1195,885),(1198,885),(1201,885),(1204,885),(1207,885),(1210,885),(1213,885),(1216,885),(1219,885),(1222,885),(1225,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1228,885),(1231,882),(1234,879),(1237,876),(1240,873),(1243,870),(1246,867),(1249,864),(1252,861),(1255,858),(1258,855),(1261,852),(1264,849),(1267,846),(1270,843),(1273,840),(1276,837),(1279,834),(1282,831),(1285,828),(1288,825),(1291,822),(1294,819),(1297,816),(1300,813),(1303,810),(1306,807),(1309,804),(1312,801),(1315,798),(1318,795),(1321,792),(1324,789),(1327,786),(1330,783),(1333,780),(1336,777),(1339,774),(1342,771),(1345,768),(1348,765),(1351,762),(1354,759),(1357,756),(1360,753),(1363,750),(1366,747),(1369,744),(1372,741),(1375,738),(1375,738),(1375,738),(1375,738),(1375,735),(1375,732),(1375,729),(1375,726),(1375,723),(1375,720),(1375,717),(1375,714),(1375,711),(1375,708),(1375,705),(1375,702),(1375,699),(1375,696),(1375,693),(1375,690),(1375,687),(1375,684),(1375,681),(1375,678),(1375,675),(1375,672),(1375,669),(1375,666),(1375,663),(1375,660),(1375,657),(1375,654),(1375,651),(1375,648),(1375,645),(1375,642),(1375,639),(1375,636),(1375,633),(1375,630),(1375,627),(1375,624),(1375,621),(1375,618),(1375,615),(1375,612),(1375,609),(1375,606),(1375,603),(1375,600),(1375,597),(1375,594),(1375,591),(1375,588),(1375,585),(1375,582),(1375,579),(1375,576),(1375,573),(1375,570),(1375,567),(1375,564),(1375,561),(1375,558),(1375,555),(1375,552),(1375,549),(1375,546),(1375,543),(1375,540),(1375,537),(1375,534),(1375,531),(1375,528),(1375,525),(1375,522),(1375,519),(1375,516),(1375,513),(1375,510),(1375,507),(1375,504),(1375,501),(1375,498),(1375,495),(1375,492),(1375,489),(1375,486),(1375,483),(1375,480),(1375,477),(1375,474),(1375,471),(1375,468),(1375,465),(1375,462),(1375,459),(1375,456),(1375,453),(1375,450),(1375,447),(1375,444),(1375,441),(1375,438),(1375,435),(1375,432),(1375,429),(1375,426),(1375,423),(1375,420),(1375,417),(1375,414),(1375,411),(1375,408),(1375,405),(1375,402),(1375,399),(1375,396),(1375,393),(1375,390)]
        self.path2d = [(694,885),(697,885),(700,885),(703,885),(706,885),(709,885),(712,885),(715,885),(718,885),(721,885),(724,885),(727,885),(730,885),(733,885),(736,885),(739,885),(742,885),(745,885),(748,885),(751,885),(754,885),(757,885),(760,885),(763,885),(766,885),(769,885),(772,885),(775,885),(778,885),(781,885),(784,885),(787,885),(790,885),(793,885),(796,885),(799,885),(802,885),(805,885),(808,885),(811,885),(814,885),(817,885),(820,885),(823,885),(826,885),(829,885),(832,885),(835,885),(838,885),(841,885),(844,885),(847,885),(850,885),(853,885),(856,885),(859,885),(862,885),(865,885),(868,885),(871,885),(874,885),(877,885),(880,885),(883,885),(886,885),(889,885),(892,885),(895,885),(898,885),(901,885),(904,885),(907,885),(910,885),(913,885),(916,885),(919,885),(922,885),(925,885),(928,885)]
        self.path3d = [(694,885),(697,885),(700,885),(703,885),(706,885),(709,885),(712,885),(715,885),(718,885)]
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
                if self.x == 1291 and self.y == 822 or self.x == 1228 and self.y == 885:
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
                if self.x == 1291 and self.y == 822 or self.x == 1228 and self.y == 885:
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
                if self.x == 1291 and self.y == 822 or self.x == 1228 and self.y == 885:
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
                if self.x == 928 and self.y == 885:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 718 and self.y == 885:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 718 and self.y == 885:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2V")
                # SELECCIONADOR DE IMAGENES EN FASE 2 VICTORIA
                if self.x == 1375 and self.y == 561 or self.x == 1375 and self.y == 738:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x == 1228 and self.y == 885:
                        self.img = self.imgs3[self.contador_animacion]
                    else:
                        if self.x >= 1369 and self.y <= 741:
                            self.img = self.imgs2[self.contador_animacion]
                            print("giro")
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 1375 and self.y == 390 or self.x == 1375 and self.y == 738:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x == 1228 and self.y == 885:
                        self.img = self.imgs3[self.contador_animacion]
                    else:
                        if self.x >= 1369 and self.y <= 741:
                            self.img = self.imgs2[self.contador_animacion]
                            print("giro")
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 1375 and self.y == 390 or self.x == 1375 and self.y == 738:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x == 1228 and self.y == 885:
                        self.img = self.imgs3[self.contador_animacion]
                    else:
                        if self.x >= 1369 and self.y <= 741:
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
            self.health = 100  # Barra de vida
            self.x = self.path[0][0]
            self.y = self.path[0][1]
            self.dis = 0
            self.path_pos = 0
            self.cont_mover = 0
            self.dist_mover = 0
