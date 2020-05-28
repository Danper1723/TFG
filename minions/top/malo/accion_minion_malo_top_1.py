import pygame
import math
import random
import sqlite3


class Accion_minion_malo_top_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 200  # Barra de vida
        self.max_health = 200  # Barra de vida
        self.vel = 3
        self.path = [(1230,125),(1227,125),(1224,125),(1221,125),(1218,125),(1215,125),(1212,125),(1209,125),(1206,125),(1203,125),(1200,125),(1197,125),(1194,125),(1191,125),(1188,125),(1185,125),(1182,125),(1179,125),(1176,125),(1173,125),(1170,125),(1167,125),(1164,125),(1161,125),(1158,125),(1155,125),(1152,125),(1149,125),(1146,125),(1143,125),(1140,125),(1137,125),(1134,125),(1131,125),(1128,125),(1125,125),(1122,125),(1119,125),(1116,125),(1113,125),(1110,125),(1107,125),(1104,125),(1101,125),(1098,125),(1095,125),(1092,125),(1089,125),(1086,125),(1083,125),(1080,125),(1077,125),(1074,125),(1071,125),(1068,125),(1065,125),(1062,125),(1059,125),(1056,125),(1053,125),(1050,125),(1047,125),(1044,125),(1041,125),(1038,125),(1035,125),(1032,125),(1029,125),(1026,125),(1023,125),(1020,125),(1017,125),(1014,125),(1011,125),(1008,125),(1005,125),(1002,125),(999,125),(996,125),(993,125),(990,125),(987,125),(984,125),(981,125),(978,125),(975,125),(972,125),(969,125),(966,125),(963,125),(960,125),(957,125),(954,125),(951,125),(948,125),(945,125),(942,125),(939,125),(936,125),(933,125),(930,125),(927,125),(924,125),(921,125),(918,125),(915,125),(912,125),(909,125),(906,125),(903,125),(900,125),(897,125),(894,125),(891,125),(888,125),(885,125),(882,125),(879,125),(876,125),(873,125),(870,125),(867,125),(864,125),(861,125),(858,125),(855,125),(852,125),(849,125),(846,125),(843,125),(840,125),(837,125),(834,125),(831,125),(828,125),(825,125),(822,125),(819,125),(816,125),(813,125),(810,125),(807,125),(804,125),(801,125),(798,125),(795,125),(792,125),(789,125),(786,125),(783,125),(780,125),(777,125),(774,125),(771,125),(768,125),(765,125),(762,125),(759,125),(756,125),(753,125),(750,125),(747,125),(744,125),(741,125),(738,125),(735,125),(732,125),(729,125),(726,125),(723,125),(720,125),(717,125),(714,125),(711,125),(708,125),(705,125),(702,125),(699,125),(696,125),(693,125),(690,125),(687,125),(684,125),(681,125),(678,125),(675,125),(672,125),(669,125),(666,125),(663,125),(660,125),(657,128),(654,131),(651,134),(648,137),(645,140),(642,143),(639,146),(636,149),(633,152),(630,155),(627,158),(624,161),(621,164),(618,167),(615,170),(612,173),(609,176),(606,179),(603,182),(600,185),(597,188)]

        self.path1 = [(1230,125),(1227,125),(1224,125),(1221,125),(1218,125),(1215,125),(1212,125),(1209,125),(1206,125),(1203,125),(1200,125),(1197,125),(1194,125),(1191,125),(1188,125),(1185,125),(1182,125),(1179,125),(1176,125),(1173,125),(1170,125),(1167,125),(1164,125),(1161,125),(1158,125),(1155,125),(1152,125),(1149,125),(1146,125),(1143,125),(1140,125),(1137,125),(1134,125),(1131,125),(1128,125),(1125,125),(1122,125),(1119,125),(1116,125),(1113,125),(1110,125),(1107,125),(1104,125),(1101,125),(1098,125),(1095,125),(1092,125),(1089,125),(1086,125),(1083,125),(1080,125),(1077,125),(1074,125),(1071,125),(1068,125),(1065,125),(1062,125),(1059,125),(1056,125),(1053,125),(1050,125),(1047,125),(1044,125),(1041,125),(1038,125),(1035,125),(1032,125),(1029,125),(1026,125),(1023,125),(1020,125),(1017,125),(1014,125),(1011,125),(1008,125),(1005,125),(1002,125),(999,125),(996,125),(993,125),(990,125),(987,125),(984,125),(981,125),(978,125),(975,125),(972,125),(969,125),(966,125),(963,125),(960,125),(957,125),(954,125),(951,125),(948,125),(945,125),(942,125),(939,125),(936,125),(933,125),(930,125),(927,125),(924,125),(921,125),(918,125),(915,125),(912,125),(909,125),(906,125),(903,125),(900,125),(897,125),(894,125),(891,125),(888,125),(885,125),(882,125),(879,125),(876,125),(873,125),(870,125),(867,125),(864,125),(861,125),(858,125),(855,125),(852,125),(849,125),(846,125),(843,125),(840,125),(837,125),(834,125),(831,125),(828,125),(825,125),(822,125),(819,125),(816,125),(813,125),(810,125),(807,125),(804,125),(801,125),(798,125),(795,125),(792,125),(789,125),(786,125),(783,125),(780,125),(777,125),(774,125),(771,125),(768,125),(765,125),(762,125),(759,125),(756,125),(753,125),(750,125),(747,125),(744,125),(741,125),(738,125),(735,125),(732,125),(729,125),(726,125),(723,125),(720,125),(717,125),(714,125),(711,125),(708,125),(705,125),(702,125),(699,125),(696,125),(693,125),(690,125),(687,125),(684,125),(681,125),(678,125),(675,125),(672,125),(669,125),(666,125),(663,125),(660,125),(657,128),(654,131),(651,134),(648,137),(645,140),(642,143),(639,146),(636,149),(633,152),(630,155),(627,158),(624,161),(621,164),(618,167),(615,170),(612,173),(609,176),(606,179),(603,182),(600,185),(597,188)]
        self.path2v = [(1230,125),(1227,125),(1224,125),(1221,125),(1218,125),(1215,125),(1212,125),(1209,125),(1206,125),(1203,125),(1200,125),(1197,125),(1194,125),(1191,125),(1188,125),(1185,125),(1182,125),(1179,125),(1176,125),(1173,125),(1170,125),(1167,125),(1164,125),(1161,125),(1158,125),(1155,125),(1152,125),(1149,125),(1146,125),(1143,125),(1140,125),(1137,125),(1134,125),(1131,125),(1128,125),(1125,125),(1122,125),(1119,125),(1116,125),(1113,125),(1110,125),(1107,125),(1104,125),(1101,125),(1098,125),(1095,125),(1092,125),(1089,125),(1086,125),(1083,125),(1080,125),(1077,125),(1074,125),(1071,125),(1068,125),(1065,125),(1062,125),(1059,125),(1056,125),(1053,125),(1050,125),(1047,125),(1044,125),(1041,125),(1038,125),(1035,125),(1032,125),(1029,125),(1026,125),(1023,125),(1020,125),(1017,125),(1014,125),(1011,125),(1008,125),(1005,125),(1002,125),(999,125),(996,125),(993,125),(990,125),(987,125),(984,125),(981,125),(978,125),(975,125),(972,125),(969,125),(966,125),(963,125),(960,125),(957,125),(954,125),(951,125),(948,125),(945,125),(942,125),(939,125),(936,125),(933,125),(930,125),(927,125),(924,125),(921,125),(918,125),(915,125),(912,125),(909,125),(906,125),(903,125),(900,125),(897,125),(894,125),(891,125),(888,125),(885,125),(882,125),(879,125),(876,125),(873,125),(870,125),(867,125),(864,125),(861,125),(858,125),(855,125),(852,125),(849,125),(846,125),(843,125),(840,125),(837,125),(834,125),(831,125),(828,125),(825,125),(822,125),(819,125),(816,125),(813,125),(810,125),(807,125),(804,125),(801,125),(798,125),(795,125),(792,125),(789,125),(786,125),(783,125),(780,125),(777,125),(774,125),(771,125),(768,125),(765,125),(762,125),(759,125),(756,125),(753,125),(750,125),(747,125),(744,125),(741,125),(738,125),(735,125),(732,125),(729,125),(726,125),(723,125),(720,125),(717,125),(714,125),(711,125),(708,125),(705,125),(702,125),(699,125),(696,125),(693,125),(690,125),(687,125),(684,125),(681,125),(678,125),(675,125),(672,125),(669,125),(666,125),(663,125),(660,125),(657,128),(654,131),(651,134),(648,137),(645,140),(642,143),(639,146),(636,149),(633,152),(630,155),(627,158),(624,161),(621,164),(618,167),(615,170),(612,173),(609,176),(606,179),(603,182),(600,185),(597,188),(594,191),(591,194),(588,197),(585,200),(582,203),(579,206),(576,209),(573,212),(570,215),(567,218),(564,221),(561,224),(558,227),(555,230),(552,233),(549,236),(546,239),(543,242),(540,245),(537,248),(534,251),(531,254),(528,257),(525,260),(522,263),(519,266),(516,269),(513,272),(510,275),(507,278),(504,281),(501,284),(498,287),(495,290),(492,293),(492,296),(492,299),(492,302),(492,305),(492,308),(492,311),(492,314),(492,317),(492,320),(492,323),(492,326),(492,329),(492,332),(492,335),(492,338),(492,341),(492,344),(492,347),(492,350),(492,353),(492,356),(492,359),(492,362),(492,365),(492,368),(492,371),(492,374),(492,377),(492,380),(492,383),(492,386),(492,389),(492,392),(492,395),(492,398),(492,401),(492,404),(492,407),(492,410),(492,413),(492,416),(492,419),(492,422),(492,425),(492,428),(492,431),(492,434),(492,437),(492,440),(492,443),(492,446),(492,449),(492,452),(492,455),(492,458),(492,461),(492,464),(492,467),(492,470)]
        self.path3v = [(1230,125),(1227,125),(1224,125),(1221,125),(1218,125),(1215,125),(1212,125),(1209,125),(1206,125),(1203,125),(1200,125),(1197,125),(1194,125),(1191,125),(1188,125),(1185,125),(1182,125),(1179,125),(1176,125),(1173,125),(1170,125),(1167,125),(1164,125),(1161,125),(1158,125),(1155,125),(1152,125),(1149,125),(1146,125),(1143,125),(1140,125),(1137,125),(1134,125),(1131,125),(1128,125),(1125,125),(1122,125),(1119,125),(1116,125),(1113,125),(1110,125),(1107,125),(1104,125),(1101,125),(1098,125),(1095,125),(1092,125),(1089,125),(1086,125),(1083,125),(1080,125),(1077,125),(1074,125),(1071,125),(1068,125),(1065,125),(1062,125),(1059,125),(1056,125),(1053,125),(1050,125),(1047,125),(1044,125),(1041,125),(1038,125),(1035,125),(1032,125),(1029,125),(1026,125),(1023,125),(1020,125),(1017,125),(1014,125),(1011,125),(1008,125),(1005,125),(1002,125),(999,125),(996,125),(993,125),(990,125),(987,125),(984,125),(981,125),(978,125),(975,125),(972,125),(969,125),(966,125),(963,125),(960,125),(957,125),(954,125),(951,125),(948,125),(945,125),(942,125),(939,125),(936,125),(933,125),(930,125),(927,125),(924,125),(921,125),(918,125),(915,125),(912,125),(909,125),(906,125),(903,125),(900,125),(897,125),(894,125),(891,125),(888,125),(885,125),(882,125),(879,125),(876,125),(873,125),(870,125),(867,125),(864,125),(861,125),(858,125),(855,125),(852,125),(849,125),(846,125),(843,125),(840,125),(837,125),(834,125),(831,125),(828,125),(825,125),(822,125),(819,125),(816,125),(813,125),(810,125),(807,125),(804,125),(801,125),(798,125),(795,125),(792,125),(789,125),(786,125),(783,125),(780,125),(777,125),(774,125),(771,125),(768,125),(765,125),(762,125),(759,125),(756,125),(753,125),(750,125),(747,125),(744,125),(741,125),(738,125),(735,125),(732,125),(729,125),(726,125),(723,125),(720,125),(717,125),(714,125),(711,125),(708,125),(705,125),(702,125),(699,125),(696,125),(693,125),(690,125),(687,125),(684,125),(681,125),(678,125),(675,125),(672,125),(669,125),(666,125),(663,125),(660,125),(657,128),(654,131),(651,134),(648,137),(645,140),(642,143),(639,146),(636,149),(633,152),(630,155),(627,158),(624,161),(621,164),(618,167),(615,170),(612,173),(609,176),(606,179),(603,182),(600,185),(597,188),(594,191),(591,194),(588,197),(585,200),(582,203),(579,206),(576,209),(573,212),(570,215),(567,218),(564,221),(561,224),(558,227),(555,230),(552,233),(549,236),(546,239),(543,242),(540,245),(537,248),(534,251),(531,254),(528,257),(525,260),(522,263),(519,266),(516,269),(513,272),(510,275),(507,278),(504,281),(501,284),(498,287),(495,290),(492,293),(492,296),(492,299),(492,302),(492,305),(492,308),(492,311),(492,314),(492,317),(492,320),(492,323),(492,326),(492,329),(492,332),(492,335),(492,338),(492,341),(492,344),(492,347),(492,350),(492,353),(492,356),(492,359),(492,362),(492,365),(492,368),(492,371),(492,374),(492,377),(492,380),(492,383),(492,386),(492,389),(492,392),(492,395),(492,398),(492,401),(492,404),(492,407),(492,410),(492,413),(492,416),(492,419),(492,422),(492,425),(492,428),(492,431),(492,434),(492,437),(492,440),(492,443),(492,446),(492,449),(492,452),(492,455),(492,458),(492,461),(492,464),(492,467),(492,470),(492,473),(492,476),(492,479),(492,482),(492,485),(492,488),(492,491),(492,494),(492,497),(492,500),(492,503),(492,506),(492,509),(492,512),(492,515),(492,518),(492,521),(492,524),(492,527),(492,530),(492,533),(492,536),(492,539),(492,542),(492,545),(492,548),(492,551),(492,554),(492,557),(492,560),(492,563),(492,566),(492,569),(492,572),(492,575),(492,578),(492,581),(492,584),(492,587),(492,590),(492,593),(492,596),(492,599),(492,602),(492,605),(492,608),(492,611)]
        self.path2d = [(1230,125),(1227,125),(1224,125),(1221,125),(1218,125),(1215,125),(1212,125),(1209,125),(1206,125),(1203,125),(1200,125),(1197,125),(1194,125),(1191,125),(1188,125),(1185,125),(1182,125),(1179,125),(1176,125),(1173,125),(1170,125),(1167,125),(1164,125),(1161,125),(1158,125),(1155,125),(1152,125),(1149,125),(1146,125),(1143,125),(1140,125),(1137,125),(1134,125),(1131,125),(1128,125),(1125,125),(1122,125),(1119,125),(1116,125),(1113,125),(1110,125),(1107,125),(1104,125),(1101,125),(1098,125),(1095,125),(1092,125),(1089,125),(1086,125),(1083,125),(1080,125),(1077,125),(1074,125),(1071,125),(1068,125),(1065,125),(1062,125),(1059,125),(1056,125),(1053,125),(1050,125),(1047,125),(1044,125),(1041,125),(1038,125),(1035,125),(1032,125),(1029,125),(1026,125),(1023,125),(1020,125),(1017,125),(1014,125),(1011,125),(1008,125),(1005,125)]
        self.path3d = [(1230,125),(1227,125),(1224,125),(1221,125),(1218,125),(1215,125),(1212,125),(1209,125),(1206,125),(1203,125),(1200,125),(1197,125),(1194,125),(1191,125),(1188,125),(1185,125)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

        self.nombre = ""
        self.estado = False
        self.torre_top_1_derecha = 1
        self.torre_top_2_derecha = 1
        self.torre_top_1_izquierda = 1
        self.torre_top_2_izquierda = 1

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

            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_1_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_1_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_top_1_derecha = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_2_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_2_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_top_2_derecha = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_1_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_1_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_top_1_izquierda = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_2_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_2_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_top_2_izquierda = r[0]
            conexion.close()
            #---

            """#CAMBIAR - Esto va fuera es para poder manipular el estado de las torres
            self.torre_top_1_derecha = 0
            self.torre_top_2_derecha = 1
            self.torre_top_1_izquierda = 1
            self.torre_top_2_izquierda = 1
            #-------"""
            if self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 597 and self.y == 188:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 597 and self.y == 188:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 597 and self.y == 188:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2V")
                if self.x == 492 and self.y == 470:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x == 492 and self.y > 296:
                        self.img = self.imgs3[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 492 and self.y == 611:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x == 492 and self.y > 296:
                        self.img = self.imgs3[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 492 and self.y == 611:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    if self.x == 492 and self.y > 296:
                        self.img = self.imgs3[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2D")
                if self.x == 1005 and self.y == 125:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3D")
                if self.x == 1185 and self.y == 125:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3D")
                if self.x == 1185 and self.y == 125:
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
            if self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                self.path = self.path1
            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                self.path = self.path1
            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 1")
                self.path = self.path1
            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2D")
                self.path = self.path2v
            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3D")
                self.path = self.path3v
            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3D")
                self.path = self.path3v
            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2V")
                self.path = self.path2d
            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3V")
                self.path = self.path3d
            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3V")
                self.path = self.path3d

        # TODA ESTA MIERDA ES PARA CALCULAR EL MOVIMIENTO ENTRE PUNTOS MEDIANTE EL TEOREMA DE PITAGORAS(VECTORES)
        if self.health <= 0:
            self.path_pos = 0
        x1, y1 = self.path[self.path_pos]
        # print(self.path[self.path_pos], self.nombre)
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (672, 147)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.cont_mover += 1
        dirn = (x2 - x1, y2 - y1)

        mover_x, mover_y = (self.x + dirn[0] * self.cont_mover, self.y + dirn[1] * self.cont_mover)
        self.dis += math.sqrt((mover_x - x1) ** 2 + (mover_y - y1) ** 2)

        # VA AL SIGUIENTE PUNTO
        if self.dis >= move_dis:
            self.dis = 0
            self.cont_mover = 0
            """self.path_pos += 1
            if self.path_pos >= len(self.path):
                print(self.path_pos)
                return False"""
            # self.path_pos=0
            # self.path_pos += 1
            if self.path_pos < len(self.path) - 1:
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
            self.health = 200  # Barra de vida
            self.x = self.path[0][0]
            self.y = self.path[0][1]
            self.dis = 0
            self.path_pos = 0
            self.cont_mover = 0
            self.dist_mover = 0