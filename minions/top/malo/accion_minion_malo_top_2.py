import pygame
import math
import random
import sqlite3


class Accion_minion_malo_top_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 300  # Barra de vida
        self.max_health = 300  # Barra de vida
        self.vel = 3
        self.path = [(1185,147),(1182,147),(1179,147),(1176,147),(1173,147),(1170,147),(1167,147),(1164,147),(1161,147),(1158,147),(1155,147),(1152,147),(1149,147),(1146,147),(1143,147),(1140,147),(1137,147),(1134,147),(1131,147),(1128,147),(1125,147),(1122,147),(1119,147),(1116,147),(1113,147),(1110,147),(1107,147),(1104,147),(1101,147),(1098,147),(1095,147),(1092,147),(1089,147),(1086,147),(1083,147),(1080,147),(1077,147),(1074,147),(1071,147),(1068,147),(1065,147),(1062,147),(1059,147),(1056,147),(1053,147),(1050,147),(1047,147),(1044,147),(1041,147),(1038,147),(1035,147),(1032,147),(1029,147),(1026,147),(1023,147),(1020,147),(1017,147),(1014,147),(1011,147),(1008,147),(1005,147),(1002,147),(999,147),(996,147),(993,147),(990,147),(987,147),(984,147),(981,147),(978,147),(975,147),(972,147),(969,147),(966,147),(963,147),(960,147),(957,147),(954,147),(951,147),(948,147),(945,147),(942,147),(939,147),(936,147),(933,147),(930,147),(927,147),(924,147),(921,147),(918,147),(915,147),(912,147),(909,147),(906,147),(903,147),(900,147),(897,147),(894,147),(891,147),(888,147),(885,147),(882,147),(879,147),(876,147),(873,147),(870,147),(867,147),(864,147),(861,147),(858,147),(855,147),(852,147),(849,147),(846,147),(843,147),(840,147),(837,147),(834,147),(831,147),(828,147),(825,147),(822,147),(819,147),(816,147),(813,147),(810,147),(807,147),(804,147),(801,147),(798,147),(795,147),(792,147),(789,147),(786,147),(783,147),(780,147),(777,147),(774,147),(771,147),(768,147),(765,147),(762,147),(759,147),(756,147),(753,147),(750,147),(747,147),(744,147),(741,147),(738,147),(735,147),(732,147),(729,147),(726,147),(723,147),(720,147),(717,147),(714,147),(711,147),(708,147),(705,147),(702,147),(699,147),(696,147),(693,147),(690,147),(687,147),(684,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(678,150),(675,153),(672,156),(669,159),(666,162),(663,165),(660,168),(657,171),(654,174),(651,177),(648,180),(645,183),(642,186),(639,189),(636,192),(633,195),(630,198),(627,201),(624,204),(621,207),(618,210),(615,213),(612,216),(609,219),(606,222),(603,225),(600,228),(597,231)]

        self.path1 = [(1185,147),(1182,147),(1179,147),(1176,147),(1173,147),(1170,147),(1167,147),(1164,147),(1161,147),(1158,147),(1155,147),(1152,147),(1149,147),(1146,147),(1143,147),(1140,147),(1137,147),(1134,147),(1131,147),(1128,147),(1125,147),(1122,147),(1119,147),(1116,147),(1113,147),(1110,147),(1107,147),(1104,147),(1101,147),(1098,147),(1095,147),(1092,147),(1089,147),(1086,147),(1083,147),(1080,147),(1077,147),(1074,147),(1071,147),(1068,147),(1065,147),(1062,147),(1059,147),(1056,147),(1053,147),(1050,147),(1047,147),(1044,147),(1041,147),(1038,147),(1035,147),(1032,147),(1029,147),(1026,147),(1023,147),(1020,147),(1017,147),(1014,147),(1011,147),(1008,147),(1005,147),(1002,147),(999,147),(996,147),(993,147),(990,147),(987,147),(984,147),(981,147),(978,147),(975,147),(972,147),(969,147),(966,147),(963,147),(960,147),(957,147),(954,147),(951,147),(948,147),(945,147),(942,147),(939,147),(936,147),(933,147),(930,147),(927,147),(924,147),(921,147),(918,147),(915,147),(912,147),(909,147),(906,147),(903,147),(900,147),(897,147),(894,147),(891,147),(888,147),(885,147),(882,147),(879,147),(876,147),(873,147),(870,147),(867,147),(864,147),(861,147),(858,147),(855,147),(852,147),(849,147),(846,147),(843,147),(840,147),(837,147),(834,147),(831,147),(828,147),(825,147),(822,147),(819,147),(816,147),(813,147),(810,147),(807,147),(804,147),(801,147),(798,147),(795,147),(792,147),(789,147),(786,147),(783,147),(780,147),(777,147),(774,147),(771,147),(768,147),(765,147),(762,147),(759,147),(756,147),(753,147),(750,147),(747,147),(744,147),(741,147),(738,147),(735,147),(732,147),(729,147),(726,147),(723,147),(720,147),(717,147),(714,147),(711,147),(708,147),(705,147),(702,147),(699,147),(696,147),(693,147),(690,147),(687,147),(684,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(678,150),(675,153),(672,156),(669,159),(666,162),(663,165),(660,168),(657,171),(654,174),(651,177),(648,180),(645,183),(642,186),(639,189),(636,192),(633,195),(630,198),(627,201),(624,204),(621,207),(618,210),(615,213),(612,216),(609,219),(606,222),(603,225),(600,228),(597,231)]
        self.path2v = [(1185,147),(1182,147),(1179,147),(1176,147),(1173,147),(1170,147),(1167,147),(1164,147),(1161,147),(1158,147),(1155,147),(1152,147),(1149,147),(1146,147),(1143,147),(1140,147),(1137,147),(1134,147),(1131,147),(1128,147),(1125,147),(1122,147),(1119,147),(1116,147),(1113,147),(1110,147),(1107,147),(1104,147),(1101,147),(1098,147),(1095,147),(1092,147),(1089,147),(1086,147),(1083,147),(1080,147),(1077,147),(1074,147),(1071,147),(1068,147),(1065,147),(1062,147),(1059,147),(1056,147),(1053,147),(1050,147),(1047,147),(1044,147),(1041,147),(1038,147),(1035,147),(1032,147),(1029,147),(1026,147),(1023,147),(1020,147),(1017,147),(1014,147),(1011,147),(1008,147),(1005,147),(1002,147),(999,147),(996,147),(993,147),(990,147),(987,147),(984,147),(981,147),(978,147),(975,147),(972,147),(969,147),(966,147),(963,147),(960,147),(957,147),(954,147),(951,147),(948,147),(945,147),(942,147),(939,147),(936,147),(933,147),(930,147),(927,147),(924,147),(921,147),(918,147),(915,147),(912,147),(909,147),(906,147),(903,147),(900,147),(897,147),(894,147),(891,147),(888,147),(885,147),(882,147),(879,147),(876,147),(873,147),(870,147),(867,147),(864,147),(861,147),(858,147),(855,147),(852,147),(849,147),(846,147),(843,147),(840,147),(837,147),(834,147),(831,147),(828,147),(825,147),(822,147),(819,147),(816,147),(813,147),(810,147),(807,147),(804,147),(801,147),(798,147),(795,147),(792,147),(789,147),(786,147),(783,147),(780,147),(777,147),(774,147),(771,147),(768,147),(765,147),(762,147),(759,147),(756,147),(753,147),(750,147),(747,147),(744,147),(741,147),(738,147),(735,147),(732,147),(729,147),(726,147),(723,147),(720,147),(717,147),(714,147),(711,147),(708,147),(705,147),(702,147),(699,147),(696,147),(693,147),(690,147),(687,147),(684,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(678,150),(675,153),(672,156),(669,159),(666,162),(663,165),(660,168),(657,171),(654,174),(651,177),(648,180),(645,183),(642,186),(639,189),(636,192),(633,195),(630,198),(627,201),(624,204),(621,207),(618,210),(615,213),(612,216),(609,219),(606,222),(603,225),(600,228),(597,231),(594,234),(591,237),(588,240),(585,243),(582,246),(579,249),(576,252),(573,255),(570,258),(567,261),(564,264),(561,267),(558,270),(555,273),(552,276),(549,279),(546,282),(543,285),(540,288),(537,291),(534,294),(531,297),(528,300),(525,303),(522,306),(519,309),(516,312),(513,315),(513,315),(513,315),(513,315),(513,318),(513,321),(513,324),(513,327),(513,330),(513,333),(513,336),(513,339),(513,342),(513,345),(513,348),(513,351),(513,354),(513,357),(513,360),(513,363),(513,366),(513,369),(513,372),(513,375),(513,378),(513,381),(513,384),(513,387),(513,390),(513,393),(513,396),(513,399),(513,402),(513,405),(513,408),(513,411),(513,414),(513,417),(513,420),(513,423),(513,426),(513,429),(513,432),(513,435),(513,438),(513,441),(513,444),(513,447),(513,450),(513,453),(513,456),(513,459),(513,462),(513,465),(513,468),(513,471),(513,474),(513,477),(513,480),(513,483),(513,486),(513,489),(513,492),(513,495),(513,498),(513,501),(513,504),(513,507),(513,510),(513,513),(513,516),(513,519)]
        self.path3v = [(1185,147),(1182,147),(1179,147),(1176,147),(1173,147),(1170,147),(1167,147),(1164,147),(1161,147),(1158,147),(1155,147),(1152,147),(1149,147),(1146,147),(1143,147),(1140,147),(1137,147),(1134,147),(1131,147),(1128,147),(1125,147),(1122,147),(1119,147),(1116,147),(1113,147),(1110,147),(1107,147),(1104,147),(1101,147),(1098,147),(1095,147),(1092,147),(1089,147),(1086,147),(1083,147),(1080,147),(1077,147),(1074,147),(1071,147),(1068,147),(1065,147),(1062,147),(1059,147),(1056,147),(1053,147),(1050,147),(1047,147),(1044,147),(1041,147),(1038,147),(1035,147),(1032,147),(1029,147),(1026,147),(1023,147),(1020,147),(1017,147),(1014,147),(1011,147),(1008,147),(1005,147),(1002,147),(999,147),(996,147),(993,147),(990,147),(987,147),(984,147),(981,147),(978,147),(975,147),(972,147),(969,147),(966,147),(963,147),(960,147),(957,147),(954,147),(951,147),(948,147),(945,147),(942,147),(939,147),(936,147),(933,147),(930,147),(927,147),(924,147),(921,147),(918,147),(915,147),(912,147),(909,147),(906,147),(903,147),(900,147),(897,147),(894,147),(891,147),(888,147),(885,147),(882,147),(879,147),(876,147),(873,147),(870,147),(867,147),(864,147),(861,147),(858,147),(855,147),(852,147),(849,147),(846,147),(843,147),(840,147),(837,147),(834,147),(831,147),(828,147),(825,147),(822,147),(819,147),(816,147),(813,147),(810,147),(807,147),(804,147),(801,147),(798,147),(795,147),(792,147),(789,147),(786,147),(783,147),(780,147),(777,147),(774,147),(771,147),(768,147),(765,147),(762,147),(759,147),(756,147),(753,147),(750,147),(747,147),(744,147),(741,147),(738,147),(735,147),(732,147),(729,147),(726,147),(723,147),(720,147),(717,147),(714,147),(711,147),(708,147),(705,147),(702,147),(699,147),(696,147),(693,147),(690,147),(687,147),(684,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(681,147),(678,150),(675,153),(672,156),(669,159),(666,162),(663,165),(660,168),(657,171),(654,174),(651,177),(648,180),(645,183),(642,186),(639,189),(636,192),(633,195),(630,198),(627,201),(624,204),(621,207),(618,210),(615,213),(612,216),(609,219),(606,222),(603,225),(600,228),(597,231),(594,234),(591,237),(588,240),(585,243),(582,246),(579,249),(576,252),(573,255),(570,258),(567,261),(564,264),(561,267),(558,270),(555,273),(552,276),(549,279),(546,282),(543,285),(540,288),(537,291),(534,294),(531,297),(528,300),(525,303),(522,306),(519,309),(516,312),(513,315),(513,315),(513,315),(513,315),(513,318),(513,321),(513,324),(513,327),(513,330),(513,333),(513,336),(513,339),(513,342),(513,345),(513,348),(513,351),(513,354),(513,357),(513,360),(513,363),(513,366),(513,369),(513,372),(513,375),(513,378),(513,381),(513,384),(513,387),(513,390),(513,393),(513,396),(513,399),(513,402),(513,405),(513,408),(513,411),(513,414),(513,417),(513,420),(513,423),(513,426),(513,429),(513,432),(513,435),(513,438),(513,441),(513,444),(513,447),(513,450),(513,453),(513,456),(513,459),(513,462),(513,465),(513,468),(513,471),(513,474),(513,477),(513,480),(513,483),(513,486),(513,489),(513,492),(513,495),(513,498),(513,501),(513,504),(513,507),(513,510),(513,513),(513,516),(513,519),(513,522),(513,525),(513,528),(513,531),(513,534),(513,537),(513,540),(513,543),(513,546),(513,549),(513,552),(513,555),(513,558),(513,561),(513,564),(513,567),(513,570),(513,573),(513,576),(513,579),(513,582),(513,585),(513,588),(513,591),(513,594),(513,597),(513,600),(513,603),(513,606),(513,609),(513,612),(513,615),(513,618),(513,621),(513,624),(513,627),(513,630)]
        self.path2d = [(1185,147),(1182,147),(1179,147),(1176,147),(1173,147),(1170,147),(1167,147),(1164,147),(1161,147),(1158,147),(1155,147),(1152,147),(1149,147),(1146,147),(1143,147),(1140,147),(1137,147),(1134,147),(1131,147),(1128,147),(1125,147),(1122,147),(1119,147),(1116,147),(1113,147),(1110,147),(1107,147),(1104,147),(1101,147),(1098,147),(1095,147),(1092,147),(1089,147),(1086,147),(1083,147),(1080,147),(1077,147),(1074,147),(1071,147),(1068,147),(1065,147),(1062,147),(1059,147),(1056,147),(1053,147),(1050,147),(1047,147),(1044,147),(1041,147),(1038,147),(1035,147),(1032,147),(1029,147),(1026,147),(1023,147),(1020,147),(1017,147),(1014,147),(1011,147),(1008,147),(1005,147),(1002,147),(999,147),(996,147),(993,147),(990,147),(987,147),(984,147),(981,147),(978,147),(975,147),(972,147),(969,147),(966,147),(963,147),(960,147)]
        self.path3d = [(1185,147),(1182,147),(1179,147),(1176,147),(1173,147),(1170,147),(1167,147),(1164,147),(1161,147),(1158,147),(1155,147),(1152,147),(1149,147),(1146,147),(1143,147),(1140,147)]
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
                if self.x == 597 and self.y == 231 or self.x == 681 and self.y == 147:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 597 and self.y == 231 or self.x == 681 and self.y == 147:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 597 and self.y == 231 or self.x == 681 and self.y == 147:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2V")
                if self.x == 681 and self.y == 147:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    if self.x == 513 and self.y == 315 or self.x == 513 and self.y == 519:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x == 513 and self.y > 315:
                            self.img = self.imgs3[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 681 and self.y == 147:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    if self.x == 513 and self.y == 315 or self.x == 513 and self.y == 630:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x == 513 and self.y > 315:
                            self.img = self.imgs3[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 681 and self.y == 147:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    if self.x == 513 and self.y == 315 or self.x == 513 and self.y == 630:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x == 513 and self.y > 315:
                            self.img = self.imgs3[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2D")
                if self.x == 960 and self.y == 147:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3D")
                if self.x == 1140 and self.y == 147:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3D")
                if self.x == 1140 and self.y == 147:
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
            self.health = 300  # Barra de vida
            self.x = self.path[0][0]
            self.y = self.path[0][1]
            self.dis = 0
            self.path_pos = 0
            self.cont_mover = 0
            self.dist_mover = 0