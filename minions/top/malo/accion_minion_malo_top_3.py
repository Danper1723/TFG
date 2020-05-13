import pygame
import math
import random
import sqlite3
class Accion_minion_malo_top_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 100  # Barra de vida
        self.max_health = 100  # Barra de vida
        self.vel = 3
        self.path = [(1230,175),(1227,175),(1224,175),(1221,175),(1218,175),(1215,175),(1212,175),(1209,175),(1206,175),(1203,175),(1200,175),(1197,175),(1194,175),(1191,175),(1188,175),(1185,175),(1182,175),(1179,175),(1176,175),(1173,175),(1170,175),(1167,175),(1164,175),(1161,175),(1158,175),(1155,175),(1152,175),(1149,175),(1146,175),(1143,175),(1140,175),(1137,175),(1134,175),(1131,175),(1128,175),(1125,175),(1122,175),(1119,175),(1116,175),(1113,175),(1110,175),(1107,175),(1104,175),(1101,175),(1098,175),(1095,175),(1092,175),(1089,175),(1086,175),(1083,175),(1080,175),(1077,175),(1074,175),(1071,175),(1068,175),(1065,175),(1062,175),(1059,175),(1056,175),(1053,175),(1050,175),(1047,175),(1044,175),(1041,175),(1038,175),(1035,175),(1032,175),(1029,175),(1026,175),(1023,175),(1020,175),(1017,175),(1014,175),(1011,175),(1008,175),(1005,175),(1002,175),(999,175),(996,175),(993,175),(990,175),(987,175),(984,175),(981,175),(978,175),(975,175),(972,175),(969,175),(966,175),(963,175),(960,175),(957,175),(954,175),(951,175),(948,175),(945,175),(942,175),(939,175),(936,175),(933,175),(930,175),(927,175),(924,175),(921,175),(918,175),(915,175),(912,175),(909,175),(906,175),(903,175),(900,175),(897,175),(894,175),(891,175),(888,175),(885,175),(882,175),(879,175),(876,175),(873,175),(870,175),(867,175),(864,175),(861,175),(858,175),(855,175),(852,175),(849,175),(846,175),(843,175),(840,175),(837,175),(834,175),(831,175),(828,175),(825,175),(822,175),(819,175),(816,175),(813,175),(810,175),(807,175),(804,175),(801,175),(798,175),(795,175),(792,175),(789,175),(786,175),(783,175),(780,175),(777,175),(774,175),(771,175),(768,175),(765,175),(762,175),(759,175),(756,175),(753,175),(750,175),(747,175),(744,175),(741,175),(738,175),(735,175),(732,175),(729,175),(726,175),(723,175),(720,175),(717,175),(714,175),(711,175),(708,175),(705,175),(702,175),(699,175),(696,175),(693,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(687,178),(684,181),(681,184),(678,187),(675,190),(672,193),(669,196),(666,199),(663,202),(660,205),(657,208),(654,211),(651,214),(648,217),(645,220),(642,223)]

        self.path1 = [(1230,175),(1227,175),(1224,175),(1221,175),(1218,175),(1215,175),(1212,175),(1209,175),(1206,175),(1203,175),(1200,175),(1197,175),(1194,175),(1191,175),(1188,175),(1185,175),(1182,175),(1179,175),(1176,175),(1173,175),(1170,175),(1167,175),(1164,175),(1161,175),(1158,175),(1155,175),(1152,175),(1149,175),(1146,175),(1143,175),(1140,175),(1137,175),(1134,175),(1131,175),(1128,175),(1125,175),(1122,175),(1119,175),(1116,175),(1113,175),(1110,175),(1107,175),(1104,175),(1101,175),(1098,175),(1095,175),(1092,175),(1089,175),(1086,175),(1083,175),(1080,175),(1077,175),(1074,175),(1071,175),(1068,175),(1065,175),(1062,175),(1059,175),(1056,175),(1053,175),(1050,175),(1047,175),(1044,175),(1041,175),(1038,175),(1035,175),(1032,175),(1029,175),(1026,175),(1023,175),(1020,175),(1017,175),(1014,175),(1011,175),(1008,175),(1005,175),(1002,175),(999,175),(996,175),(993,175),(990,175),(987,175),(984,175),(981,175),(978,175),(975,175),(972,175),(969,175),(966,175),(963,175),(960,175),(957,175),(954,175),(951,175),(948,175),(945,175),(942,175),(939,175),(936,175),(933,175),(930,175),(927,175),(924,175),(921,175),(918,175),(915,175),(912,175),(909,175),(906,175),(903,175),(900,175),(897,175),(894,175),(891,175),(888,175),(885,175),(882,175),(879,175),(876,175),(873,175),(870,175),(867,175),(864,175),(861,175),(858,175),(855,175),(852,175),(849,175),(846,175),(843,175),(840,175),(837,175),(834,175),(831,175),(828,175),(825,175),(822,175),(819,175),(816,175),(813,175),(810,175),(807,175),(804,175),(801,175),(798,175),(795,175),(792,175),(789,175),(786,175),(783,175),(780,175),(777,175),(774,175),(771,175),(768,175),(765,175),(762,175),(759,175),(756,175),(753,175),(750,175),(747,175),(744,175),(741,175),(738,175),(735,175),(732,175),(729,175),(726,175),(723,175),(720,175),(717,175),(714,175),(711,175),(708,175),(705,175),(702,175),(699,175),(696,175),(693,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(687,178),(684,181),(681,184),(678,187),(675,190),(672,193),(669,196),(666,199),(663,202),(660,205),(657,208),(654,211),(651,214),(648,217),(645,220),(642,223)]
        self.path2v = [(1230,175),(1227,175),(1224,175),(1221,175),(1218,175),(1215,175),(1212,175),(1209,175),(1206,175),(1203,175),(1200,175),(1197,175),(1194,175),(1191,175),(1188,175),(1185,175),(1182,175),(1179,175),(1176,175),(1173,175),(1170,175),(1167,175),(1164,175),(1161,175),(1158,175),(1155,175),(1152,175),(1149,175),(1146,175),(1143,175),(1140,175),(1137,175),(1134,175),(1131,175),(1128,175),(1125,175),(1122,175),(1119,175),(1116,175),(1113,175),(1110,175),(1107,175),(1104,175),(1101,175),(1098,175),(1095,175),(1092,175),(1089,175),(1086,175),(1083,175),(1080,175),(1077,175),(1074,175),(1071,175),(1068,175),(1065,175),(1062,175),(1059,175),(1056,175),(1053,175),(1050,175),(1047,175),(1044,175),(1041,175),(1038,175),(1035,175),(1032,175),(1029,175),(1026,175),(1023,175),(1020,175),(1017,175),(1014,175),(1011,175),(1008,175),(1005,175),(1002,175),(999,175),(996,175),(993,175),(990,175),(987,175),(984,175),(981,175),(978,175),(975,175),(972,175),(969,175),(966,175),(963,175),(960,175),(957,175),(954,175),(951,175),(948,175),(945,175),(942,175),(939,175),(936,175),(933,175),(930,175),(927,175),(924,175),(921,175),(918,175),(915,175),(912,175),(909,175),(906,175),(903,175),(900,175),(897,175),(894,175),(891,175),(888,175),(885,175),(882,175),(879,175),(876,175),(873,175),(870,175),(867,175),(864,175),(861,175),(858,175),(855,175),(852,175),(849,175),(846,175),(843,175),(840,175),(837,175),(834,175),(831,175),(828,175),(825,175),(822,175),(819,175),(816,175),(813,175),(810,175),(807,175),(804,175),(801,175),(798,175),(795,175),(792,175),(789,175),(786,175),(783,175),(780,175),(777,175),(774,175),(771,175),(768,175),(765,175),(762,175),(759,175),(756,175),(753,175),(750,175),(747,175),(744,175),(741,175),(738,175),(735,175),(732,175),(729,175),(726,175),(723,175),(720,175),(717,175),(714,175),(711,175),(708,175),(705,175),(702,175),(699,175),(696,175),(693,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(687,178),(684,181),(681,184),(678,187),(675,190),(672,193),(669,196),(666,199),(663,202),(660,205),(657,208),(654,211),(651,214),(648,217),(645,220),(642,223),(639,226),(636,229),(633,232),(630,235),(627,238),(624,241),(621,244),(618,247),(615,250),(612,253),(609,256),(606,259),(603,262),(600,265),(597,268),(594,271),(591,274),(588,277),(585,280),(582,283),(579,286),(576,289),(573,292),(570,295),(567,298),(564,301),(561,304),(558,307),(555,310),(552,313),(549,316),(546,319),(543,322),(540,325),(537,328),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,334),(534,337),(534,340),(534,343),(534,346),(534,349),(534,352),(534,355),(534,358),(534,361),(534,364),(534,367),(534,370),(534,373),(534,376),(534,379),(534,382),(534,385),(534,388),(534,391),(534,394),(534,397),(534,400),(534,403),(534,406),(534,409),(534,412),(534,415),(534,418),(534,421),(534,424),(534,427),(534,430),(534,433),(534,436),(534,439),(534,442),(534,445),(534,448),(534,451),(534,454),(534,457),(534,460),(534,463),(534,466),(534,469),(534,472)]
        self.path3v = [(1230,175),(1227,175),(1224,175),(1221,175),(1218,175),(1215,175),(1212,175),(1209,175),(1206,175),(1203,175),(1200,175),(1197,175),(1194,175),(1191,175),(1188,175),(1185,175),(1182,175),(1179,175),(1176,175),(1173,175),(1170,175),(1167,175),(1164,175),(1161,175),(1158,175),(1155,175),(1152,175),(1149,175),(1146,175),(1143,175),(1140,175),(1137,175),(1134,175),(1131,175),(1128,175),(1125,175),(1122,175),(1119,175),(1116,175),(1113,175),(1110,175),(1107,175),(1104,175),(1101,175),(1098,175),(1095,175),(1092,175),(1089,175),(1086,175),(1083,175),(1080,175),(1077,175),(1074,175),(1071,175),(1068,175),(1065,175),(1062,175),(1059,175),(1056,175),(1053,175),(1050,175),(1047,175),(1044,175),(1041,175),(1038,175),(1035,175),(1032,175),(1029,175),(1026,175),(1023,175),(1020,175),(1017,175),(1014,175),(1011,175),(1008,175),(1005,175),(1002,175),(999,175),(996,175),(993,175),(990,175),(987,175),(984,175),(981,175),(978,175),(975,175),(972,175),(969,175),(966,175),(963,175),(960,175),(957,175),(954,175),(951,175),(948,175),(945,175),(942,175),(939,175),(936,175),(933,175),(930,175),(927,175),(924,175),(921,175),(918,175),(915,175),(912,175),(909,175),(906,175),(903,175),(900,175),(897,175),(894,175),(891,175),(888,175),(885,175),(882,175),(879,175),(876,175),(873,175),(870,175),(867,175),(864,175),(861,175),(858,175),(855,175),(852,175),(849,175),(846,175),(843,175),(840,175),(837,175),(834,175),(831,175),(828,175),(825,175),(822,175),(819,175),(816,175),(813,175),(810,175),(807,175),(804,175),(801,175),(798,175),(795,175),(792,175),(789,175),(786,175),(783,175),(780,175),(777,175),(774,175),(771,175),(768,175),(765,175),(762,175),(759,175),(756,175),(753,175),(750,175),(747,175),(744,175),(741,175),(738,175),(735,175),(732,175),(729,175),(726,175),(723,175),(720,175),(717,175),(714,175),(711,175),(708,175),(705,175),(702,175),(699,175),(696,175),(693,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(690,175),(687,178),(684,181),(681,184),(678,187),(675,190),(672,193),(669,196),(666,199),(663,202),(660,205),(657,208),(654,211),(651,214),(648,217),(645,220),(642,223),(639,226),(636,229),(633,232),(630,235),(627,238),(624,241),(621,244),(618,247),(615,250),(612,253),(609,256),(606,259),(603,262),(600,265),(597,268),(594,271),(591,274),(588,277),(585,280),(582,283),(579,286),(576,289),(573,292),(570,295),(567,298),(564,301),(561,304),(558,307),(555,310),(552,313),(549,316),(546,319),(543,322),(540,325),(537,328),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,331),(534,334),(534,337),(534,340),(534,343),(534,346),(534,349),(534,352),(534,355),(534,358),(534,361),(534,364),(534,367),(534,370),(534,373),(534,376),(534,379),(534,382),(534,385),(534,388),(534,391),(534,394),(534,397),(534,400),(534,403),(534,406),(534,409),(534,412),(534,415),(534,418),(534,421),(534,424),(534,427),(534,430),(534,433),(534,436),(534,439),(534,442),(534,445),(534,448),(534,451),(534,454),(534,457),(534,460),(534,463),(534,466),(534,469),(534,472),(534,475),(534,478),(534,481),(534,484),(534,487),(534,490),(534,493),(534,496),(534,499),(534,502),(534,505),(534,508),(534,511),(534,514),(534,517),(534,520),(534,523),(534,526),(534,529),(534,532),(534,535),(534,538),(534,541),(534,544),(534,547),(534,550),(534,553),(534,556),(534,559),(534,562),(534,565),(534,568),(534,571),(534,574),(534,577),(534,580),(534,583),(534,586),(534,589),(534,592),(534,595),(534,598),(534,601),(534,604),(534,607),(534,610),(534,613)]
        self.path2d =[(1230,175),(1227,175),(1224,175),(1221,175),(1218,175),(1215,175),(1212,175),(1209,175),(1206,175),(1203,175),(1200,175),(1197,175),(1194,175),(1191,175),(1188,175),(1185,175),(1182,175),(1179,175),(1176,175),(1173,175),(1170,175),(1167,175),(1164,175),(1161,175),(1158,175),(1155,175),(1152,175),(1149,175),(1146,175),(1143,175),(1140,175),(1137,175),(1134,175),(1131,175),(1128,175),(1125,175),(1122,175),(1119,175),(1116,175),(1113,175),(1110,175),(1107,175),(1104,175),(1101,175),(1098,175),(1095,175),(1092,175),(1089,175),(1086,175),(1083,175),(1080,175),(1077,175),(1074,175),(1071,175),(1068,175),(1065,175),(1062,175),(1059,175),(1056,175),(1053,175),(1050,175),(1047,175),(1044,175),(1041,175),(1038,175),(1035,175),(1032,175),(1029,175),(1026,175),(1023,175),(1020,175),(1017,175),(1014,175),(1011,175),(1008,175),(1005,175)]
        self.path3d = [(1230,175),(1227,175),(1224,175),(1221,175),(1218,175),(1215,175),(1212,175),(1209,175),(1206,175),(1203,175),(1200,175),(1197,175),(1194,175),(1191,175),(1188,175),(1185,175)]
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

            # ---
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
            # ---

            """#CAMBIAR - Esto va fuera es para poder manipular el estado de las torres
            self.torre_top_1_derecha = 0
            self.torre_top_2_derecha = 1
            self.torre_top_1_izquierda = 1
            self.torre_top_2_izquierda = 1
            #-------"""
            if self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 642 and self.y == 223 or self.x == 690 and self.y == 175:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 642 and self.y == 223 or self.x == 690 and self.y == 175:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 642 and self.y == 223 or self.x == 690 and self.y == 175:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2V")
                if self.x == 690 and self.y == 175:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    if self.x == 534 and self.y == 331 or self.x == 534 and self.y == 472:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x == 534 and self.y > 331:
                            self.img = self.imgs3[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 690 and self.y == 175:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    if self.x == 534 and self.y == 331 or self.x == 534 and self.y == 613:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x == 534 and self.y > 331:
                            self.img = self.imgs3[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 690 and self.y == 175:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    if self.x == 534 and self.y == 331 or self.x == 534 and self.y == 613:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x == 534 and self.y > 331:
                            self.img = self.imgs3[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2D")
                if self.x == 1005 and self.y == 175:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3D")
                if self.x == 1185 and self.y == 175:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3D")
                if self.x == 1185 and self.y == 175:
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
            print("FASE 2V")
            self.path = self.path2v
        elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
            print("FASE 3V")
            self.path = self.path3v
        elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
            print("FASE 3V")
            self.path = self.path3v
        elif not self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
            print("FASE 2D")
            self.path = self.path2d
        elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
            print("FASE 3D")
            self.path = self.path3d
        elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
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