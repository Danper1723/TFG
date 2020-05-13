import pygame
import math
import random
import sqlite3
class Accion_minion_malo_mid_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 100  # Barra de vida
        self.max_health = 100  # Barra de vida
        self.vel = 3
        self.path = [(1302,256),(1299,259),(1296,262),(1293,265),(1290,268),(1287,271),(1284,274),(1281,277),(1278,280),(1275,283),(1272,286),(1269,289),(1266,292),(1263,295),(1260,298),(1257,301),(1254,304),(1251,307),(1248,310),(1245,313),(1242,316),(1239,319),(1236,322),(1233,325),(1230,328),(1227,331),(1224,334),(1221,337),(1218,340),(1215,343),(1212,346),(1209,349),(1206,352),(1203,355),(1200,358),(1197,361),(1194,364),(1191,367),(1188,370),(1185,373),(1182,376),(1179,379),(1176,382),(1173,385),(1170,388),(1167,391),(1164,394),(1161,397),(1158,400),(1155,403),(1152,406),(1149,409),(1146,412),(1143,415),(1140,418),(1137,421),(1134,424),(1131,427),(1128,430),(1125,433),(1122,436),(1119,439),(1116,442),(1113,445),(1110,448),(1107,451),(1104,454),(1101,457),(1098,460),(1095,463),(1092,466),(1089,469),(1086,472),(1083,475),(1080,478),(1077,481),(1074,484),(1071,487),(1068,490),(1065,493),(1062,496),(1059,499),(1056,502),(1053,505),(1050,508),(1047,511),(1044,514),(1041,517),(1038,520),(1035,523),(1032,526),(1029,529),(1026,532),(1023,535),(1020,538),(1017,541),(1014,544),(1011,547),(1008,550),(1005,553),(1002,556),(999,559),(996,562),(993,562),(990,562),(987,562)]

        self.path1 = [(1302,256),(1299,259),(1296,262),(1293,265),(1290,268),(1287,271),(1284,274),(1281,277),(1278,280),(1275,283),(1272,286),(1269,289),(1266,292),(1263,295),(1260,298),(1257,301),(1254,304),(1251,307),(1248,310),(1245,313),(1242,316),(1239,319),(1236,322),(1233,325),(1230,328),(1227,331),(1224,334),(1221,337),(1218,340),(1215,343),(1212,346),(1209,349),(1206,352),(1203,355),(1200,358),(1197,361),(1194,364),(1191,367),(1188,370),(1185,373),(1182,376),(1179,379),(1176,382),(1173,385),(1170,388),(1167,391),(1164,394),(1161,397),(1158,400),(1155,403),(1152,406),(1149,409),(1146,412),(1143,415),(1140,418),(1137,421),(1134,424),(1131,427),(1128,430),(1125,433),(1122,436),(1119,439),(1116,442),(1113,445),(1110,448),(1107,451),(1104,454),(1101,457),(1098,460),(1095,463),(1092,466),(1089,469),(1086,472),(1083,475),(1080,478),(1077,481),(1074,484),(1071,487),(1068,490),(1065,493),(1062,496),(1059,499),(1056,502),(1053,505),(1050,508),(1047,511),(1044,514),(1041,517),(1038,520),(1035,523),(1032,526),(1029,529),(1026,532),(1023,535),(1020,538),(1017,541),(1014,544),(1011,547),(1008,550),(1005,553),(1002,556),(999,559),(996,562),(993,562),(990,562),(987,562)]
        self.path2v = [(1302,256),(1299,259),(1296,262),(1293,265),(1290,268),(1287,271),(1284,274),(1281,277),(1278,280),(1275,283),(1272,286),(1269,289),(1266,292),(1263,295),(1260,298),(1257,301),(1254,304),(1251,307),(1248,310),(1245,313),(1242,316),(1239,319),(1236,322),(1233,325),(1230,328),(1227,331),(1224,334),(1221,337),(1218,340),(1215,343),(1212,346),(1209,349),(1206,352),(1203,355),(1200,358),(1197,361),(1194,364),(1191,367),(1188,370),(1185,373),(1182,376),(1179,379),(1176,382),(1173,385),(1170,388),(1167,391),(1164,394),(1161,397),(1158,400),(1155,403),(1152,406),(1149,409),(1146,412),(1143,415),(1140,418),(1137,421),(1134,424),(1131,427),(1128,430),(1125,433),(1122,436),(1119,439),(1116,442),(1113,445),(1110,448),(1107,451),(1104,454),(1101,457),(1098,460),(1095,463),(1092,466),(1089,469),(1086,472),(1083,475),(1080,478),(1077,481),(1074,484),(1071,487),(1068,490),(1065,493),(1062,496),(1059,499),(1056,502),(1053,505),(1050,508),(1047,511),(1044,514),(1041,517),(1038,520),(1035,523),(1032,526),(1029,529),(1026,532),(1023,535),(1020,538),(1017,541),(1014,544),(1011,547),(1008,550),(1005,553),(1002,556),(999,559),(996,562),(993,562),(990,562),(987,562),(984,562),(981,562),(978,562),(975,562),(972,562),(969,562),(966,562),(963,562),(960,562),(957,562),(954,562),(951,562),(948,562),(945,562),(942,562),(939,562),(936,562),(933,562),(930,562),(927,562),(924,562),(921,562),(918,562),(915,562),(912,562),(909,562),(906,562),(903,562),(900,562),(897,562),(894,562),(891,562),(888,562),(885,562),(882,562),(879,562),(876,562),(873,562),(870,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(864,565),(861,568),(858,571),(855,574),(852,577),(849,580),(846,583),(843,586),(840,589)]
        self.path3v = [(1302,256),(1299,259),(1296,262),(1293,265),(1290,268),(1287,271),(1284,274),(1281,277),(1278,280),(1275,283),(1272,286),(1269,289),(1266,292),(1263,295),(1260,298),(1257,301),(1254,304),(1251,307),(1248,310),(1245,313),(1242,316),(1239,319),(1236,322),(1233,325),(1230,328),(1227,331),(1224,334),(1221,337),(1218,340),(1215,343),(1212,346),(1209,349),(1206,352),(1203,355),(1200,358),(1197,361),(1194,364),(1191,367),(1188,370),(1185,373),(1182,376),(1179,379),(1176,382),(1173,385),(1170,388),(1167,391),(1164,394),(1161,397),(1158,400),(1155,403),(1152,406),(1149,409),(1146,412),(1143,415),(1140,418),(1137,421),(1134,424),(1131,427),(1128,430),(1125,433),(1122,436),(1119,439),(1116,442),(1113,445),(1110,448),(1107,451),(1104,454),(1101,457),(1098,460),(1095,463),(1092,466),(1089,469),(1086,472),(1083,475),(1080,478),(1077,481),(1074,484),(1071,487),(1068,490),(1065,493),(1062,496),(1059,499),(1056,502),(1053,505),(1050,508),(1047,511),(1044,514),(1041,517),(1038,520),(1035,523),(1032,526),(1029,529),(1026,532),(1023,535),(1020,538),(1017,541),(1014,544),(1011,547),(1008,550),(1005,553),(1002,556),(999,559),(996,562),(993,562),(990,562),(987,562),(984,562),(981,562),(978,562),(975,562),(972,562),(969,562),(966,562),(963,562),(960,562),(957,562),(954,562),(951,562),(948,562),(945,562),(942,562),(939,562),(936,562),(933,562),(930,562),(927,562),(924,562),(921,562),(918,562),(915,562),(912,562),(909,562),(906,562),(903,562),(900,562),(897,562),(894,562),(891,562),(888,562),(885,562),(882,562),(879,562),(876,562),(873,562),(870,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(867,562),(864,565),(861,568),(858,571),(855,574),(852,577),(849,580),(846,583),(843,586),(840,589),(837,592),(834,595),(831,598),(828,601),(825,604),(822,607),(819,610),(816,613),(813,616),(810,619),(807,622),(804,625),(801,628),(798,631),(795,634),(792,637),(789,640),(786,643),(783,646),(780,649),(777,652),(774,655),(771,658),(768,661),(765,664),(762,667),(759,670),(756,673),(753,676),(750,679),(747,682),(744,685)]
        self.path2d = [(1302,256),(1299,259),(1296,262),(1293,265),(1290,268),(1287,271),(1284,274),(1281,277),(1278,280),(1275,283),(1272,286),(1269,289),(1266,292),(1263,295),(1260,298),(1257,301),(1254,304),(1251,307),(1248,310),(1245,313),(1242,316),(1239,319),(1236,322),(1233,325),(1230,328),(1227,331),(1224,334),(1221,337),(1218,340),(1215,343),(1212,346),(1209,349),(1206,352),(1203,355),(1200,358),(1197,361),(1194,364),(1191,367),(1188,370),(1185,373),(1182,376),(1179,379),(1176,382),(1173,385)]
        self.path3d = [(1302,256),(1299,259),(1296,262),(1293,265),(1290,268),(1287,271),(1284,274),(1281,277),(1278,280),(1275,283),(1272,286),(1269,289),(1266,292),(1263,295),(1260,298),(1257,301)]
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
                if self.x == 987 and self.y == 562:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 1")
                if self.x == 987 and self.y == 562:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 1")
                if self.x == 987 and self.y == 562:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2V")
                if self.x == 867 and self.y == 562 or self.x == 840 and self.y == 589:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 867 and self.y == 562 or self.x == 744 and self.y == 685:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 867 and self.y == 562 or self.x == 744 and self.y == 685:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2D")
                if self.x == 1173 and self.y == 385:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3D")
                if self.x == 1257 and self.y == 301:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3D")
                if self.x == 1257 and self.y == 301:
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