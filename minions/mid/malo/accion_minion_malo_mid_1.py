import pygame
import math
import random
import sqlite3
class Accion_minion_malo_mid_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 100  # Barra de vida
        self.max_health = 100  # Barra de vida
        self.vel = 3
        self.path = [(1264,223),(1261,226),(1258,229),(1255,232),(1252,235),(1249,238),(1246,241),(1243,244),(1240,247),(1237,250),(1234,253),(1231,256),(1228,259),(1225,262),(1222,265),(1219,268),(1216,271),(1213,274),(1210,277),(1207,280),(1204,283),(1201,286),(1198,289),(1195,292),(1192,295),(1189,298),(1186,301),(1183,304),(1180,307),(1177,310),(1174,313),(1171,316),(1168,319),(1165,322),(1162,325),(1159,328),(1156,331),(1153,334),(1150,337),(1147,340),(1144,343),(1141,346),(1138,349),(1135,352),(1132,355),(1129,358),(1126,361),(1123,364),(1120,367),(1117,370),(1114,373),(1111,376),(1108,379),(1105,382),(1102,385),(1099,388),(1096,391),(1093,394),(1090,397),(1087,400),(1084,403),(1081,406),(1078,409),(1075,412),(1072,415),(1069,418),(1066,421),(1063,424),(1060,427),(1057,430),(1054,433),(1051,436),(1048,439),(1045,442),(1042,445),(1039,448),(1036,451),(1033,454),(1030,457),(1027,460),(1024,463),(1021,466),(1018,469),(1015,472),(1012,475),(1009,478),(1006,481),(1003,484),(1000,487),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(994,490),(991,490),(988,490)]

        self.path1 = [(1264,223),(1261,226),(1258,229),(1255,232),(1252,235),(1249,238),(1246,241),(1243,244),(1240,247),(1237,250),(1234,253),(1231,256),(1228,259),(1225,262),(1222,265),(1219,268),(1216,271),(1213,274),(1210,277),(1207,280),(1204,283),(1201,286),(1198,289),(1195,292),(1192,295),(1189,298),(1186,301),(1183,304),(1180,307),(1177,310),(1174,313),(1171,316),(1168,319),(1165,322),(1162,325),(1159,328),(1156,331),(1153,334),(1150,337),(1147,340),(1144,343),(1141,346),(1138,349),(1135,352),(1132,355),(1129,358),(1126,361),(1123,364),(1120,367),(1117,370),(1114,373),(1111,376),(1108,379),(1105,382),(1102,385),(1099,388),(1096,391),(1093,394),(1090,397),(1087,400),(1084,403),(1081,406),(1078,409),(1075,412),(1072,415),(1069,418),(1066,421),(1063,424),(1060,427),(1057,430),(1054,433),(1051,436),(1048,439),(1045,442),(1042,445),(1039,448),(1036,451),(1033,454),(1030,457),(1027,460),(1024,463),(1021,466),(1018,469),(1015,472),(1012,475),(1009,478),(1006,481),(1003,484),(1000,487),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(994,490),(991,490),(988,490)]
        self.path2v = [(1264,223),(1261,226),(1258,229),(1255,232),(1252,235),(1249,238),(1246,241),(1243,244),(1240,247),(1237,250),(1234,253),(1231,256),(1228,259),(1225,262),(1222,265),(1219,268),(1216,271),(1213,274),(1210,277),(1207,280),(1204,283),(1201,286),(1198,289),(1195,292),(1192,295),(1189,298),(1186,301),(1183,304),(1180,307),(1177,310),(1174,313),(1171,316),(1168,319),(1165,322),(1162,325),(1159,328),(1156,331),(1153,334),(1150,337),(1147,340),(1144,343),(1141,346),(1138,349),(1135,352),(1132,355),(1129,358),(1126,361),(1123,364),(1120,367),(1117,370),(1114,373),(1111,376),(1108,379),(1105,382),(1102,385),(1099,388),(1096,391),(1093,394),(1090,397),(1087,400),(1084,403),(1081,406),(1078,409),(1075,412),(1072,415),(1069,418),(1066,421),(1063,424),(1060,427),(1057,430),(1054,433),(1051,436),(1048,439),(1045,442),(1042,445),(1039,448),(1036,451),(1033,454),(1030,457),(1027,460),(1024,463),(1021,466),(1018,469),(1015,472),(1012,475),(1009,478),(1006,481),(1003,484),(1000,487),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(994,490),(991,490),(988,490),(985,490),(982,490),(979,490),(976,490),(973,490),(970,490),(967,490),(964,490),(961,490),(958,490),(955,490),(952,490),(949,490),(946,490),(943,490),(940,490),(937,490),(934,490),(931,490),(928,490),(925,490),(922,490),(919,490),(916,490),(913,490),(910,490),(907,490),(904,490),(901,490),(898,490),(895,490),(892,490),(889,490),(886,490),(883,490),(880,490),(877,490),(874,490),(871,493),(868,496),(865,499),(862,502),(859,505),(856,508),(853,511),(850,514),(847,517),(844,520),(841,523),(838,526),(835,529),(832,532),(829,535),(826,538),(823,541),(820,544),(817,547),(814,550),(811,553),(808,556),(805,559)]
        self.path3v = [(1264,223),(1261,226),(1258,229),(1255,232),(1252,235),(1249,238),(1246,241),(1243,244),(1240,247),(1237,250),(1234,253),(1231,256),(1228,259),(1225,262),(1222,265),(1219,268),(1216,271),(1213,274),(1210,277),(1207,280),(1204,283),(1201,286),(1198,289),(1195,292),(1192,295),(1189,298),(1186,301),(1183,304),(1180,307),(1177,310),(1174,313),(1171,316),(1168,319),(1165,322),(1162,325),(1159,328),(1156,331),(1153,334),(1150,337),(1147,340),(1144,343),(1141,346),(1138,349),(1135,352),(1132,355),(1129,358),(1126,361),(1123,364),(1120,367),(1117,370),(1114,373),(1111,376),(1108,379),(1105,382),(1102,385),(1099,388),(1096,391),(1093,394),(1090,397),(1087,400),(1084,403),(1081,406),(1078,409),(1075,412),(1072,415),(1069,418),(1066,421),(1063,424),(1060,427),(1057,430),(1054,433),(1051,436),(1048,439),(1045,442),(1042,445),(1039,448),(1036,451),(1033,454),(1030,457),(1027,460),(1024,463),(1021,466),(1018,469),(1015,472),(1012,475),(1009,478),(1006,481),(1003,484),(1000,487),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(997,490),(994,490),(991,490),(988,490),(985,490),(982,490),(979,490),(976,490),(973,490),(970,490),(967,490),(964,490),(961,490),(958,490),(955,490),(952,490),(949,490),(946,490),(943,490),(940,490),(937,490),(934,490),(931,490),(928,490),(925,490),(922,490),(919,490),(916,490),(913,490),(910,490),(907,490),(904,490),(901,490),(898,490),(895,490),(892,490),(889,490),(886,490),(883,490),(880,490),(877,490),(874,490),(871,493),(868,496),(865,499),(862,502),(859,505),(856,508),(853,511),(850,514),(847,517),(844,520),(841,523),(838,526),(835,529),(832,532),(829,535),(826,538),(823,541),(820,544),(817,547),(814,550),(811,553),(808,556),(805,559),(802,562),(799,565),(796,568),(793,571),(790,574),(787,577),(784,580),(781,583),(778,586),(775,589),(772,592),(769,595),(766,598),(763,601),(760,604),(757,607),(754,610),(751,613),(748,616),(745,619),(742,622),(739,625),(736,628),(733,631),(730,634),(727,637),(724,640),(721,643),(718,646),(715,649)]
        self.path2d = [(1264,223),(1261,226),(1258,229),(1255,232),(1252,235),(1249,238),(1246,241),(1243,244),(1240,247),(1237,250),(1234,253),(1231,256),(1228,259),(1225,262),(1222,265),(1219,268),(1216,271),(1213,274),(1210,277),(1207,280),(1204,283),(1201,286),(1198,289),(1195,292),(1192,295),(1189,298),(1186,301),(1183,304),(1180,307),(1177,310),(1174,313),(1171,316),(1168,319),(1165,322),(1162,325),(1159,328),(1156,331),(1153,334),(1150,337),(1147,340),(1144,343),(1141,346),(1138,349),(1135,352)]
        self.path3d = [(1264,223),(1261,226),(1258,229),(1255,232),(1252,235),(1249,238),(1246,241),(1243,244),(1240,247),(1237,250),(1234,253),(1231,256),(1228,259),(1225,262),(1222,265),(1219,268)]
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
                if self.x == 997 and self.y == 490 or self.x == 988 and self.y == 490:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 1")
                if self.x == 997 and self.y == 490 or self.x == 988 and self.y == 490:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 1")
                if self.x == 997 and self.y == 490 or self.x == 988 and self.y == 490:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2V")
                if self.x == 997 and self.y == 490 or self.x == 805 and self.y == 559:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 997 and self.y == 490 or self.x == 715 and self.y == 649:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 997 and self.y == 490 or self.x == 715 and self.y == 649:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2D")
                if self.x == 1135 and self.y == 352:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3D")
                if self.x == 1219 and self.y == 268:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3D")
                if self.x == 1219 and self.y == 268:
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