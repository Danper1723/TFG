import random
import sqlite3

import pygame
import math
class Accion_minion_malo_bot_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 200  # Barra de vida
        self.max_health = 200  # Barra de vida
        self.vel = 3
        self.path = [(1400, 289), (1400, 292), (1400, 295), (1400, 298), (1400, 301), (1400, 304), (1400, 307),
                     (1400, 310), (1400, 313), (1400, 316), (1400, 319), (1400, 322), (1400, 325), (1400, 328),
                     (1400, 331), (1400, 334), (1400, 337), (1400, 340), (1400, 343), (1400, 346), (1400, 349),
                     (1400, 352), (1400, 355), (1400, 358), (1400, 361), (1400, 364), (1400, 367), (1400, 370),
                     (1400, 373), (1400, 376), (1400, 379), (1400, 382), (1400, 385), (1400, 388), (1400, 391),
                     (1400, 394), (1400, 397), (1400, 400), (1400, 403), (1400, 406), (1400, 409), (1400, 412),
                     (1400, 415), (1400, 418), (1400, 421), (1400, 424), (1400, 427), (1400, 430), (1400, 433),
                     (1400, 436), (1400, 439), (1400, 442), (1400, 445), (1400, 448), (1400, 451), (1400, 454),
                     (1400, 457), (1400, 460), (1400, 463), (1400, 466), (1400, 469), (1400, 472), (1400, 475),
                     (1400, 478), (1400, 481), (1400, 484), (1400, 487), (1400, 490), (1400, 493), (1400, 496),
                     (1400, 499), (1400, 502), (1400, 505), (1400, 508), (1400, 511), (1400, 514), (1400, 517),
                     (1400, 520), (1400, 523), (1400, 526), (1400, 529), (1400, 532), (1400, 535), (1400, 538),
                     (1400, 541), (1400, 544), (1400, 547), (1400, 550), (1400, 553), (1400, 556), (1400, 559),
                     (1400, 562), (1400, 565), (1400, 568), (1400, 571), (1400, 574), (1400, 577), (1400, 580),
                     (1400, 583), (1400, 586), (1400, 589), (1400, 592), (1400, 595), (1400, 598), (1400, 601),
                     (1400, 604), (1400, 607), (1400, 610), (1400, 613), (1400, 616), (1400, 619), (1400, 622),
                     (1400, 625), (1400, 628), (1400, 631), (1400, 634), (1400, 637), (1400, 640), (1400, 643),
                     (1400, 646), (1400, 649), (1400, 652), (1400, 655), (1400, 658), (1400, 661), (1400, 664),
                     (1400, 667), (1400, 670), (1400, 673), (1400, 676), (1400, 679), (1400, 682), (1400, 685),
                     (1400, 688), (1400, 691), (1400, 694), (1400, 697), (1400, 700), (1400, 703), (1400, 706),
                     (1400, 709), (1400, 712), (1400, 715), (1400, 718), (1400, 721), (1400, 724), (1400, 727),
                     (1400, 730), (1400, 733), (1400, 736), (1400, 739), (1397, 742), (1394, 745), (1391, 748),
                     (1388, 751), (1385, 754), (1382, 757), (1379, 760), (1376, 763), (1373, 766), (1370, 769),
                     (1367, 772), (1364, 775)]

        self.path1 = [(1400,289),(1400,292),(1400,295),(1400,298),(1400,301),(1400,304),(1400,307),(1400,310),(1400,313),(1400,316),(1400,319),(1400,322),(1400,325),(1400,328),(1400,331),(1400,334),(1400,337),(1400,340),(1400,343),(1400,346),(1400,349),(1400,352),(1400,355),(1400,358),(1400,361),(1400,364),(1400,367),(1400,370),(1400,373),(1400,376),(1400,379),(1400,382),(1400,385),(1400,388),(1400,391),(1400,394),(1400,397),(1400,400),(1400,403),(1400,406),(1400,409),(1400,412),(1400,415),(1400,418),(1400,421),(1400,424),(1400,427),(1400,430),(1400,433),(1400,436),(1400,439),(1400,442),(1400,445),(1400,448),(1400,451),(1400,454),(1400,457),(1400,460),(1400,463),(1400,466),(1400,469),(1400,472),(1400,475),(1400,478),(1400,481),(1400,484),(1400,487),(1400,490),(1400,493),(1400,496),(1400,499),(1400,502),(1400,505),(1400,508),(1400,511),(1400,514),(1400,517),(1400,520),(1400,523),(1400,526),(1400,529),(1400,532),(1400,535),(1400,538),(1400,541),(1400,544),(1400,547),(1400,550),(1400,553),(1400,556),(1400,559),(1400,562),(1400,565),(1400,568),(1400,571),(1400,574),(1400,577),(1400,580),(1400,583),(1400,586),(1400,589),(1400,592),(1400,595),(1400,598),(1400,601),(1400,604),(1400,607),(1400,610),(1400,613),(1400,616),(1400,619),(1400,622),(1400,625),(1400,628),(1400,631),(1400,634),(1400,637),(1400,640),(1400,643),(1400,646),(1400,649),(1400,652),(1400,655),(1400,658),(1400,661),(1400,664),(1400,667),(1400,670),(1400,673),(1400,676),(1400,679),(1400,682),(1400,685),(1400,688),(1400,691),(1400,694),(1400,697),(1400,700),(1400,703),(1400,706),(1400,709),(1400,712),(1400,715),(1400,718),(1400,721),(1400,724),(1400,727),(1400,730),(1400,733),(1400,736),(1400,739),(1397,742),(1394,745),(1391,748),(1388,751),(1385,754),(1382,757),(1379,760),(1376,763),(1373,766),(1370,769),(1367,772),(1364,775)]
        self.path2v = [(1400,289),(1400,292),(1400,295),(1400,298),(1400,301),(1400,304),(1400,307),(1400,310),(1400,313),(1400,316),(1400,319),(1400,322),(1400,325),(1400,328),(1400,331),(1400,334),(1400,337),(1400,340),(1400,343),(1400,346),(1400,349),(1400,352),(1400,355),(1400,358),(1400,361),(1400,364),(1400,367),(1400,370),(1400,373),(1400,376),(1400,379),(1400,382),(1400,385),(1400,388),(1400,391),(1400,394),(1400,397),(1400,400),(1400,403),(1400,406),(1400,409),(1400,412),(1400,415),(1400,418),(1400,421),(1400,424),(1400,427),(1400,430),(1400,433),(1400,436),(1400,439),(1400,442),(1400,445),(1400,448),(1400,451),(1400,454),(1400,457),(1400,460),(1400,463),(1400,466),(1400,469),(1400,472),(1400,475),(1400,478),(1400,481),(1400,484),(1400,487),(1400,490),(1400,493),(1400,496),(1400,499),(1400,502),(1400,505),(1400,508),(1400,511),(1400,514),(1400,517),(1400,520),(1400,523),(1400,526),(1400,529),(1400,532),(1400,535),(1400,538),(1400,541),(1400,544),(1400,547),(1400,550),(1400,553),(1400,556),(1400,559),(1400,562),(1400,565),(1400,568),(1400,571),(1400,574),(1400,577),(1400,580),(1400,583),(1400,586),(1400,589),(1400,592),(1400,595),(1400,598),(1400,601),(1400,604),(1400,607),(1400,610),(1400,613),(1400,616),(1400,619),(1400,622),(1400,625),(1400,628),(1400,631),(1400,634),(1400,637),(1400,640),(1400,643),(1400,646),(1400,649),(1400,652),(1400,655),(1400,658),(1400,661),(1400,664),(1400,667),(1400,670),(1400,673),(1400,676),(1400,679),(1400,682),(1400,685),(1400,688),(1400,691),(1400,694),(1400,697),(1400,700),(1400,703),(1400,706),(1400,709),(1400,712),(1400,715),(1400,718),(1400,721),(1400,724),(1400,727),(1400,730),(1400,733),(1400,736),(1400,739),(1397,742),(1394,745),(1391,748),(1388,751),(1385,754),(1382,757),(1379,760),(1376,763),(1373,766),(1370,769),(1367,772),(1364,775),(1361,778),(1358,781),(1355,784),(1352,787),(1349,790),(1346,793),(1343,796),(1340,799),(1337,802),(1334,805),(1331,808),(1328,811),(1325,814),(1322,817),(1319,820),(1316,823),(1313,826),(1310,829),(1307,832),(1304,835),(1301,838),(1298,841),(1295,844),(1292,847),(1289,850),(1286,853),(1283,856),(1280,859),(1277,862),(1274,865),(1271,868),(1268,871),(1265,874),(1262,877),(1259,880),(1256,883),(1253,886),(1250,889),(1247,892),(1244,895),(1241,898),(1238,901),(1235,904),(1232,907),(1229,910),(1226,910),(1223,910),(1220,910),(1217,910),(1214,910),(1211,910),(1208,910),(1205,910),(1202,910),(1199,910),(1196,910),(1193,910),(1190,910),(1187,910),(1184,910),(1181,910),(1178,910),(1175,910),(1172,910),(1169,910),(1166,910),(1163,910),(1160,910),(1157,910),(1154,910),(1151,910),(1148,910),(1145,910),(1142,910),(1139,910),(1136,910),(1133,910),(1130,910),(1127,910),(1124,910),(1121,910),(1118,910),(1115,910),(1112,910),(1109,910),(1106,910),(1103,910),(1100,910),(1097,910),(1094,910),(1091,910),(1088,910),(1085,910),(1082,910),(1079,910),(1076,910),(1073,910),(1070,910),(1067,910),(1064,910),(1061,910),(1058,910),(1055,910),(1052,910),(1049,910),(1046,910),(1043,910),(1040,910),(1037,910),(1034,910),(1031,910),(1028,910),(1025,910),(1022,910),(1019,910),(1016,910),(1013,910),(1010,910),(1007,910),(1004,910),(1001,910),(998,910),(995,910),(992,910)]
        self.path3v = [(1400,289),(1400,292),(1400,295),(1400,298),(1400,301),(1400,304),(1400,307),(1400,310),(1400,313),(1400,316),(1400,319),(1400,322),(1400,325),(1400,328),(1400,331),(1400,334),(1400,337),(1400,340),(1400,343),(1400,346),(1400,349),(1400,352),(1400,355),(1400,358),(1400,361),(1400,364),(1400,367),(1400,370),(1400,373),(1400,376),(1400,379),(1400,382),(1400,385),(1400,388),(1400,391),(1400,394),(1400,397),(1400,400),(1400,403),(1400,406),(1400,409),(1400,412),(1400,415),(1400,418),(1400,421),(1400,424),(1400,427),(1400,430),(1400,433),(1400,436),(1400,439),(1400,442),(1400,445),(1400,448),(1400,451),(1400,454),(1400,457),(1400,460),(1400,463),(1400,466),(1400,469),(1400,472),(1400,475),(1400,478),(1400,481),(1400,484),(1400,487),(1400,490),(1400,493),(1400,496),(1400,499),(1400,502),(1400,505),(1400,508),(1400,511),(1400,514),(1400,517),(1400,520),(1400,523),(1400,526),(1400,529),(1400,532),(1400,535),(1400,538),(1400,541),(1400,544),(1400,547),(1400,550),(1400,553),(1400,556),(1400,559),(1400,562),(1400,565),(1400,568),(1400,571),(1400,574),(1400,577),(1400,580),(1400,583),(1400,586),(1400,589),(1400,592),(1400,595),(1400,598),(1400,601),(1400,604),(1400,607),(1400,610),(1400,613),(1400,616),(1400,619),(1400,622),(1400,625),(1400,628),(1400,631),(1400,634),(1400,637),(1400,640),(1400,643),(1400,646),(1400,649),(1400,652),(1400,655),(1400,658),(1400,661),(1400,664),(1400,667),(1400,670),(1400,673),(1400,676),(1400,679),(1400,682),(1400,685),(1400,688),(1400,691),(1400,694),(1400,697),(1400,700),(1400,703),(1400,706),(1400,709),(1400,712),(1400,715),(1400,718),(1400,721),(1400,724),(1400,727),(1400,730),(1400,733),(1400,736),(1400,739),(1397,742),(1394,745),(1391,748),(1388,751),(1385,754),(1382,757),(1379,760),(1376,763),(1373,766),(1370,769),(1367,772),(1364,775),(1361,778),(1358,781),(1355,784),(1352,787),(1349,790),(1346,793),(1343,796),(1340,799),(1337,802),(1334,805),(1331,808),(1328,811),(1325,814),(1322,817),(1319,820),(1316,823),(1313,826),(1310,829),(1307,832),(1304,835),(1301,838),(1298,841),(1295,844),(1292,847),(1289,850),(1286,853),(1283,856),(1280,859),(1277,862),(1274,865),(1271,868),(1268,871),(1265,874),(1262,877),(1259,880),(1256,883),(1253,886),(1250,889),(1247,892),(1244,895),(1241,898),(1238,901),(1235,904),(1232,907),(1229,910),(1226,910),(1223,910),(1220,910),(1217,910),(1214,910),(1211,910),(1208,910),(1205,910),(1202,910),(1199,910),(1196,910),(1193,910),(1190,910),(1187,910),(1184,910),(1181,910),(1178,910),(1175,910),(1172,910),(1169,910),(1166,910),(1163,910),(1160,910),(1157,910),(1154,910),(1151,910),(1148,910),(1145,910),(1142,910),(1139,910),(1136,910),(1133,910),(1130,910),(1127,910),(1124,910),(1121,910),(1118,910),(1115,910),(1112,910),(1109,910),(1106,910),(1103,910),(1100,910),(1097,910),(1094,910),(1091,910),(1088,910),(1085,910),(1082,910),(1079,910),(1076,910),(1073,910),(1070,910),(1067,910),(1064,910),(1061,910),(1058,910),(1055,910),(1052,910),(1049,910),(1046,910),(1043,910),(1040,910),(1037,910),(1034,910),(1031,910),(1028,910),(1025,910),(1022,910),(1019,910),(1016,910),(1013,910),(1010,910),(1007,910),(1004,910),(1001,910),(998,910),(995,910),(992,910),(989,910),(986,910),(983,910),(980,910),(977,910),(974,910),(971,910),(968,910),(965,910),(962,910),(959,910),(956,910),(953,910),(950,910),(947,910),(944,910),(941,910),(938,910),(935,910),(932,910),(929,910),(926,910),(923,910),(920,910),(917,910),(914,910),(911,910),(908,910),(905,910),(902,910),(899,910),(896,910),(893,910),(890,910),(887,910),(884,910),(881,910),(878,910),(875,910),(872,910),(869,910),(866,910),(863,910),(860,910),(857,910),(854,910),(851,910),(848,910),(845,910),(842,910),(839,910),(836,910),(833,910),(830,910),(827,910),(824,910),(821,910),(818,910),(815,910),(812,910),(809,910),(806,910),(803,910),(800,910),(797,910)]
        self.path2d = [(1400,289),(1400,292),(1400,295),(1400,298),(1400,301),(1400,304),(1400,307),(1400,310),(1400,313),(1400,316),(1400,319),(1400,322),(1400,325),(1400,328),(1400,331),(1400,334),(1400,337),(1400,340),(1400,343),(1400,346),(1400,349),(1400,352),(1400,355),(1400,358),(1400,361),(1400,364),(1400,367),(1400,370),(1400,373),(1400,376),(1400,379),(1400,382),(1400,385),(1400,388),(1400,391),(1400,394),(1400,397),(1400,400),(1400,403),(1400,406),(1400,409),(1400,412),(1400,415),(1400,418),(1400,421),(1400,424),(1400,427),(1400,430),(1400,433),(1400,436),(1400,439),(1400,442),(1400,445),(1400,448),(1400,451),(1400,454),(1400,457),(1400,460),(1400,463),(1400,466),(1400,469),(1400,472),(1400,475),(1400,478),(1400,481),(1400,484)]
        self.path3d = [(1400,289),(1400,292),(1400,295),(1400,298),(1400,301),(1400,304)]
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
            self.torre_bot_1_derecha = 1
            self.torre_bot_2_derecha = 1
            self.torre_bot_1_izquierda = 1
            self.torre_bot_2_izquierda = 1
            if self.x <= 1327:
                self.torre_bot_1_izquierda = 1
                self.torre_bot_2_izquierda = 1
            #-------"""

            #SELECCIONAR LAS IMAGENES SEGUN EL ESTADO DE LA PARTIDA
            if self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1364 and self.y == 775:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x <= 1400 and self.y >= 739:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1364 and self.y == 775:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x <= 1400 and self.y >= 739:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1364 and self.y == 775:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x <= 1400 and self.y >= 739:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2V")
                # SELECCIONADOR DE IMAGENES EN FASE 2 VICTORIA
                if self.x == 992 and self.y == 910:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x <= 1400 and self.y >= 739:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 797 and self.y == 910:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x <= 1400 and self.y >= 739:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 797 and self.y == 910:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x <= 1400 and self.y >= 739:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2D")
                # SELECCIONADOR DE IMAGENES EN FASE 2 DERROTA
                if self.x == 1400 and self.y == 484:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 1400 and self.y == 304:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 1400 and self.y == 304:
                    self.img = self.imgs4[self.contador_animacion]
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
                print("FASE 2V")
                self.path = self.path2v
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                self.path = self.path3v
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                self.path = self.path3v
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2D")
                self.path = self.path2d
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                self.path = self.path3d
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                self.path = self.path3d

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