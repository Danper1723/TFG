import random
import sqlite3

import pygame
import math
class Accion_minion_malo_bot_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 300  # Barra de vida
        self.max_health = 300  # Barra de vida
        self.vel = 3
        self.path = [(1370, 323), (1370, 326), (1370, 329), (1370, 332), (1370, 335), (1370, 338), (1370, 341),
                     (1370, 344), (1370, 347), (1370, 350), (1370, 353), (1370, 356), (1370, 359), (1370, 362),
                     (1370, 365), (1370, 368), (1370, 371), (1370, 374), (1370, 377), (1370, 380), (1370, 383),
                     (1370, 386), (1370, 389), (1370, 392), (1370, 395), (1370, 398), (1370, 401), (1370, 404),
                     (1370, 407), (1370, 410), (1370, 413), (1370, 416), (1370, 419), (1370, 422), (1370, 425),
                     (1370, 428), (1370, 431), (1370, 434), (1370, 437), (1370, 440), (1370, 443), (1370, 446),
                     (1370, 449), (1370, 452), (1370, 455), (1370, 458), (1370, 461), (1370, 464), (1370, 467),
                     (1370, 470), (1370, 473), (1370, 476), (1370, 479), (1370, 482), (1370, 485), (1370, 488),
                     (1370, 491), (1370, 494), (1370, 497), (1370, 500), (1370, 503), (1370, 506), (1370, 509),
                     (1370, 512), (1370, 515), (1370, 518), (1370, 521), (1370, 524), (1370, 527), (1370, 530),
                     (1370, 533), (1370, 536), (1370, 539), (1370, 542), (1370, 545), (1370, 548), (1370, 551),
                     (1370, 554), (1370, 557), (1370, 560), (1370, 563), (1370, 566), (1370, 569), (1370, 572),
                     (1370, 575), (1370, 578), (1370, 581), (1370, 584), (1370, 587), (1370, 590), (1370, 593),
                     (1370, 596), (1370, 599), (1370, 602), (1370, 605), (1370, 608), (1370, 611), (1370, 614),
                     (1370, 617), (1370, 620), (1370, 623), (1370, 626), (1370, 629), (1370, 632), (1370, 635),
                     (1370, 638), (1370, 641), (1370, 644), (1370, 647), (1370, 650), (1370, 653), (1370, 656),
                     (1370, 659), (1370, 662), (1370, 665), (1370, 668), (1370, 671), (1370, 674), (1370, 677),
                     (1370, 680), (1370, 683), (1370, 686), (1370, 689), (1370, 692), (1370, 695), (1370, 698),
                     (1370, 701), (1370, 704), (1370, 707), (1370, 710), (1370, 713), (1370, 716), (1370, 719),
                     (1370, 722), (1370, 725), (1370, 728), (1370, 731), (1370, 734), (1370, 737), (1370, 737),
                     (1370, 737), (1370, 737), (1370, 737), (1370, 737), (1370, 737), (1370, 737), (1370, 737),
                     (1367, 740), (1364, 743), (1361, 746), (1358, 749), (1355, 752), (1352, 755), (1349, 758),
                     (1346, 761), (1343, 764), (1340, 767), (1337, 770), (1334, 773), (1331, 776), (1328, 779),
                     (1325, 782), (1322, 785), (1319, 788), (1316, 791)]

        self.path1 = [(1370,323),(1370,326),(1370,329),(1370,332),(1370,335),(1370,338),(1370,341),(1370,344),(1370,347),(1370,350),(1370,353),(1370,356),(1370,359),(1370,362),(1370,365),(1370,368),(1370,371),(1370,374),(1370,377),(1370,380),(1370,383),(1370,386),(1370,389),(1370,392),(1370,395),(1370,398),(1370,401),(1370,404),(1370,407),(1370,410),(1370,413),(1370,416),(1370,419),(1370,422),(1370,425),(1370,428),(1370,431),(1370,434),(1370,437),(1370,440),(1370,443),(1370,446),(1370,449),(1370,452),(1370,455),(1370,458),(1370,461),(1370,464),(1370,467),(1370,470),(1370,473),(1370,476),(1370,479),(1370,482),(1370,485),(1370,488),(1370,491),(1370,494),(1370,497),(1370,500),(1370,503),(1370,506),(1370,509),(1370,512),(1370,515),(1370,518),(1370,521),(1370,524),(1370,527),(1370,530),(1370,533),(1370,536),(1370,539),(1370,542),(1370,545),(1370,548),(1370,551),(1370,554),(1370,557),(1370,560),(1370,563),(1370,566),(1370,569),(1370,572),(1370,575),(1370,578),(1370,581),(1370,584),(1370,587),(1370,590),(1370,593),(1370,596),(1370,599),(1370,602),(1370,605),(1370,608),(1370,611),(1370,614),(1370,617),(1370,620),(1370,623),(1370,626),(1370,629),(1370,632),(1370,635),(1370,638),(1370,641),(1370,644),(1370,647),(1370,650),(1370,653),(1370,656),(1370,659),(1370,662),(1370,665),(1370,668),(1370,671),(1370,674),(1370,677),(1370,680),(1370,683),(1370,686),(1370,689),(1370,692),(1370,695),(1370,698),(1370,701),(1370,704),(1370,707),(1370,710),(1370,713),(1370,716),(1370,719),(1370,722),(1370,725),(1370,728),(1370,731),(1370,734),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1367,740),(1364,743),(1361,746),(1358,749),(1355,752),(1352,755),(1349,758),(1346,761),(1343,764),(1340,767),(1337,770),(1334,773),(1331,776),(1328,779),(1325,782),(1322,785),(1319,788),(1316,791)]
        self.path2v = [(1370,323),(1370,326),(1370,329),(1370,332),(1370,335),(1370,338),(1370,341),(1370,344),(1370,347),(1370,350),(1370,353),(1370,356),(1370,359),(1370,362),(1370,365),(1370,368),(1370,371),(1370,374),(1370,377),(1370,380),(1370,383),(1370,386),(1370,389),(1370,392),(1370,395),(1370,398),(1370,401),(1370,404),(1370,407),(1370,410),(1370,413),(1370,416),(1370,419),(1370,422),(1370,425),(1370,428),(1370,431),(1370,434),(1370,437),(1370,440),(1370,443),(1370,446),(1370,449),(1370,452),(1370,455),(1370,458),(1370,461),(1370,464),(1370,467),(1370,470),(1370,473),(1370,476),(1370,479),(1370,482),(1370,485),(1370,488),(1370,491),(1370,494),(1370,497),(1370,500),(1370,503),(1370,506),(1370,509),(1370,512),(1370,515),(1370,518),(1370,521),(1370,524),(1370,527),(1370,530),(1370,533),(1370,536),(1370,539),(1370,542),(1370,545),(1370,548),(1370,551),(1370,554),(1370,557),(1370,560),(1370,563),(1370,566),(1370,569),(1370,572),(1370,575),(1370,578),(1370,581),(1370,584),(1370,587),(1370,590),(1370,593),(1370,596),(1370,599),(1370,602),(1370,605),(1370,608),(1370,611),(1370,614),(1370,617),(1370,620),(1370,623),(1370,626),(1370,629),(1370,632),(1370,635),(1370,638),(1370,641),(1370,644),(1370,647),(1370,650),(1370,653),(1370,656),(1370,659),(1370,662),(1370,665),(1370,668),(1370,671),(1370,674),(1370,677),(1370,680),(1370,683),(1370,686),(1370,689),(1370,692),(1370,695),(1370,698),(1370,701),(1370,704),(1370,707),(1370,710),(1370,713),(1370,716),(1370,719),(1370,722),(1370,725),(1370,728),(1370,731),(1370,734),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1367,740),(1364,743),(1361,746),(1358,749),(1355,752),(1352,755),(1349,758),(1346,761),(1343,764),(1340,767),(1337,770),(1334,773),(1331,776),(1328,779),(1325,782),(1322,785),(1319,788),(1316,791),(1313,794),(1310,797),(1307,800),(1304,803),(1301,806),(1298,809),(1295,812),(1292,815),(1289,818),(1286,821),(1283,824),(1280,827),(1277,830),(1274,833),(1271,836),(1268,839),(1265,842),(1262,845),(1259,848),(1256,851),(1253,854),(1250,857),(1247,860),(1244,863),(1241,866),(1238,869),(1235,872),(1232,875),(1229,878),(1226,881),(1223,884),(1223,884),(1223,884),(1223,884),(1220,884),(1217,884),(1214,884),(1211,884),(1208,884),(1205,884),(1202,884),(1199,884),(1196,884),(1193,884),(1190,884),(1187,884),(1184,884),(1181,884),(1178,884),(1175,884),(1172,884),(1169,884),(1166,884),(1163,884),(1160,884),(1157,884),(1154,884),(1151,884),(1148,884),(1145,884),(1142,884),(1139,884),(1136,884),(1133,884),(1130,884),(1127,884),(1124,884),(1121,884),(1118,884),(1115,884),(1112,884),(1109,884),(1106,884),(1103,884),(1100,884),(1097,884),(1094,884),(1091,884),(1088,884),(1085,884),(1082,884),(1079,884),(1076,884),(1073,884),(1070,884),(1067,884),(1064,884),(1061,884),(1058,884),(1055,884),(1052,884),(1049,884),(1046,884),(1043,884),(1040,884),(1037,884),(1034,884),(1031,884),(1028,884),(1025,884),(1022,884),(1019,884),(1016,884),(1013,884),(1010,884),(1007,884),(1004,884),(1001,884),(998,884),(995,884),(992,884),(989,884),(986,884),(983,884),(980,884),(977,884),(974,884),(971,884),(968,884),(965,884),(962,884),(959,884),(956,884)]
        self.path3v = [(1370,323),(1370,326),(1370,329),(1370,332),(1370,335),(1370,338),(1370,341),(1370,344),(1370,347),(1370,350),(1370,353),(1370,356),(1370,359),(1370,362),(1370,365),(1370,368),(1370,371),(1370,374),(1370,377),(1370,380),(1370,383),(1370,386),(1370,389),(1370,392),(1370,395),(1370,398),(1370,401),(1370,404),(1370,407),(1370,410),(1370,413),(1370,416),(1370,419),(1370,422),(1370,425),(1370,428),(1370,431),(1370,434),(1370,437),(1370,440),(1370,443),(1370,446),(1370,449),(1370,452),(1370,455),(1370,458),(1370,461),(1370,464),(1370,467),(1370,470),(1370,473),(1370,476),(1370,479),(1370,482),(1370,485),(1370,488),(1370,491),(1370,494),(1370,497),(1370,500),(1370,503),(1370,506),(1370,509),(1370,512),(1370,515),(1370,518),(1370,521),(1370,524),(1370,527),(1370,530),(1370,533),(1370,536),(1370,539),(1370,542),(1370,545),(1370,548),(1370,551),(1370,554),(1370,557),(1370,560),(1370,563),(1370,566),(1370,569),(1370,572),(1370,575),(1370,578),(1370,581),(1370,584),(1370,587),(1370,590),(1370,593),(1370,596),(1370,599),(1370,602),(1370,605),(1370,608),(1370,611),(1370,614),(1370,617),(1370,620),(1370,623),(1370,626),(1370,629),(1370,632),(1370,635),(1370,638),(1370,641),(1370,644),(1370,647),(1370,650),(1370,653),(1370,656),(1370,659),(1370,662),(1370,665),(1370,668),(1370,671),(1370,674),(1370,677),(1370,680),(1370,683),(1370,686),(1370,689),(1370,692),(1370,695),(1370,698),(1370,701),(1370,704),(1370,707),(1370,710),(1370,713),(1370,716),(1370,719),(1370,722),(1370,725),(1370,728),(1370,731),(1370,734),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1370,737),(1367,740),(1364,743),(1361,746),(1358,749),(1355,752),(1352,755),(1349,758),(1346,761),(1343,764),(1340,767),(1337,770),(1334,773),(1331,776),(1328,779),(1325,782),(1322,785),(1319,788),(1316,791),(1313,794),(1310,797),(1307,800),(1304,803),(1301,806),(1298,809),(1295,812),(1292,815),(1289,818),(1286,821),(1283,824),(1280,827),(1277,830),(1274,833),(1271,836),(1268,839),(1265,842),(1262,845),(1259,848),(1256,851),(1253,854),(1250,857),(1247,860),(1244,863),(1241,866),(1238,869),(1235,872),(1232,875),(1229,878),(1226,881),(1223,884),(1223,884),(1223,884),(1223,884),(1220,884),(1217,884),(1214,884),(1211,884),(1208,884),(1205,884),(1202,884),(1199,884),(1196,884),(1193,884),(1190,884),(1187,884),(1184,884),(1181,884),(1178,884),(1175,884),(1172,884),(1169,884),(1166,884),(1163,884),(1160,884),(1157,884),(1154,884),(1151,884),(1148,884),(1145,884),(1142,884),(1139,884),(1136,884),(1133,884),(1130,884),(1127,884),(1124,884),(1121,884),(1118,884),(1115,884),(1112,884),(1109,884),(1106,884),(1103,884),(1100,884),(1097,884),(1094,884),(1091,884),(1088,884),(1085,884),(1082,884),(1079,884),(1076,884),(1073,884),(1070,884),(1067,884),(1064,884),(1061,884),(1058,884),(1055,884),(1052,884),(1049,884),(1046,884),(1043,884),(1040,884),(1037,884),(1034,884),(1031,884),(1028,884),(1025,884),(1022,884),(1019,884),(1016,884),(1013,884),(1010,884),(1007,884),(1004,884),(1001,884),(998,884),(995,884),(992,884),(989,884),(986,884),(983,884),(980,884),(977,884),(974,884),(971,884),(968,884),(965,884),(962,884),(959,884),(956,884),(953,884),(950,884),(947,884),(944,884),(941,884),(938,884),(935,884),(932,884),(929,884),(926,884),(923,884),(920,884),(917,884),(914,884),(911,884),(908,884),(905,884),(902,884),(899,884),(896,884),(893,884),(890,884),(887,884),(884,884),(881,884),(878,884),(875,884),(872,884),(869,884),(866,884),(863,884),(860,884),(857,884),(854,884),(851,884),(848,884),(845,884),(842,884),(839,884),(836,884),(833,884),(830,884),(827,884),(824,884),(821,884),(818,884),(815,884),(812,884),(809,884),(806,884),(803,884),(800,884),(797,884),(794,884),(791,884),(788,884),(785,884),(782,884),(779,884),(776,884),(773,884),(770,884),(767,884),(764,884),(761,884)]
        self.path2d = [(1370,323),(1370,326),(1370,329),(1370,332),(1370,335),(1370,338),(1370,341),(1370,344),(1370,347),(1370,350),(1370,353),(1370,356),(1370,359),(1370,362),(1370,365),(1370,368),(1370,371),(1370,374),(1370,377),(1370,380),(1370,383),(1370,386),(1370,389),(1370,392),(1370,395),(1370,398),(1370,401),(1370,404),(1370,407),(1370,410),(1370,413),(1370,416),(1370,419),(1370,422),(1370,425),(1370,428),(1370,431),(1370,434),(1370,437),(1370,440),(1370,443),(1370,446),(1370,449),(1370,452),(1370,455),(1370,458),(1370,461),(1370,464),(1370,467),(1370,470),(1370,473),(1370,476),(1370,479),(1370,482),(1370,485),(1370,488),(1370,491),(1370,494),(1370,497),(1370,500),(1370,503),(1370,506),(1370,509),(1370,512),(1370,515),(1370,518)]
        self.path3d = [(1370,323),(1370,326),(1370,329),(1370,332),(1370,335),(1370,338)]
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
                if self.x == 1316 and self.y == 791:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1370 and self.y == 737:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1375 and self.y >= 737:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1316 and self.y == 791:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1370 and self.y == 737:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1375 and self.y >= 737:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1316 and self.y == 791:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1370 and self.y == 737:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1375 and self.y >= 737:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2V")
                # SELECCIONADOR DE IMAGENES EN FASE 2 VICTORIA
                if self.x == 956 and self.y == 884 or self.x == 1223 and self.y == 884:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1370 and self.y == 737:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1375 and self.y >= 737:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 761 and self.y == 884 or self.x == 1223 and self.y == 884:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1370 and self.y == 737:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1375 and self.y >= 737:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 761 and self.y == 884 or self.x == 1223 and self.y == 884:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1370 and self.y == 737:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1375 and self.y >= 737:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2D")
                # SELECCIONADOR DE IMAGENES EN FASE 2 DERROTA
                if self.x == 1370 and self.y == 518:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 1370 and self.y == 338:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 1370 and self.y == 338:
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
        print("ahora tengo", self.health)
        if self.health <= 0:
            self.path_pos = 0
            self.health = 0
            print("he muerto", self.health)

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