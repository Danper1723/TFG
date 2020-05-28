import pygame
import math
import random
import sqlite3
class Accion_minion_bueno_mid_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 200  # Barra de vida
        self.max_health = 200  # Barra de vida
        self.vel = 3
        self.path = [(638,797),(641,794),(644,791),(647,788),(650,785),(653,782),(656,779),(659,776),(662,773),(665,770),(668,767),(671,764),(674,761),(677,758),(680,755),(683,752),(686,749),(689,746),(692,743),(695,740),(698,737),(701,734),(704,731),(707,728),(710,725),(713,722),(716,719),(719,716),(722,713),(725,710),(728,707),(731,704),(734,701),(737,698),(740,695),(743,692),(746,689),(749,686),(752,683),(755,680),(758,677),(761,674),(764,671),(767,668),(770,665),(773,662),(776,659),(779,656),(782,653),(785,650),(788,647),(791,644),(794,641),(797,638),(800,635),(803,632),(806,629),(809,626),(812,623),(815,620),(818,617),(821,614),(824,611),(827,608),(830,605),(833,602),(836,599),(839,596),(842,593),(845,590),(848,587),(851,584),(854,581),(857,578),(860,575),(863,572),(866,569),(869,566),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(875,563),(878,563),(881,563),(884,563),(887,563),(890,563),(893,563),(896,563),(899,563),(902,563),(905,563),(908,563),(911,563),(914,563),(917,563),(920,563),(923,563)]
        
        self.path1 = [(638,797),(641,794),(644,791),(647,788),(650,785),(653,782),(656,779),(659,776),(662,773),(665,770),(668,767),(671,764),(674,761),(677,758),(680,755),(683,752),(686,749),(689,746),(692,743),(695,740),(698,737),(701,734),(704,731),(707,728),(710,725),(713,722),(716,719),(719,716),(722,713),(725,710),(728,707),(731,704),(734,701),(737,698),(740,695),(743,692),(746,689),(749,686),(752,683),(755,680),(758,677),(761,674),(764,671),(767,668),(770,665),(773,662),(776,659),(779,656),(782,653),(785,650),(788,647),(791,644),(794,641),(797,638),(800,635),(803,632),(806,629),(809,626),(812,623),(815,620),(818,617),(821,614),(824,611),(827,608),(830,605),(833,602),(836,599),(839,596),(842,593),(845,590),(848,587),(851,584),(854,581),(857,578),(860,575),(863,572),(866,569),(869,566),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(875,563),(878,563),(881,563),(884,563),(887,563),(890,563),(893,563),(896,563),(899,563),(902,563),(905,563),(908,563),(911,563),(914,563),(917,563),(920,563),(923,563)]
        self.path2v = [(638,797),(641,794),(644,791),(647,788),(650,785),(653,782),(656,779),(659,776),(662,773),(665,770),(668,767),(671,764),(674,761),(677,758),(680,755),(683,752),(686,749),(689,746),(692,743),(695,740),(698,737),(701,734),(704,731),(707,728),(710,725),(713,722),(716,719),(719,716),(722,713),(725,710),(728,707),(731,704),(734,701),(737,698),(740,695),(743,692),(746,689),(749,686),(752,683),(755,680),(758,677),(761,674),(764,671),(767,668),(770,665),(773,662),(776,659),(779,656),(782,653),(785,650),(788,647),(791,644),(794,641),(797,638),(800,635),(803,632),(806,629),(809,626),(812,623),(815,620),(818,617),(821,614),(824,611),(827,608),(830,605),(833,602),(836,599),(839,596),(842,593),(845,590),(848,587),(851,584),(854,581),(857,578),(860,575),(863,572),(866,569),(869,566),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(875,563),(878,563),(881,563),(884,563),(887,563),(890,563),(893,563),(896,563),(899,563),(902,563),(905,563),(908,563),(911,563),(914,563),(917,563),(920,563),(923,563),(926,563),(929,563),(932,563),(935,563),(938,563),(941,563),(944,563),(947,563),(950,563),(953,563),(956,563),(959,563),(962,563),(965,563),(968,563),(971,563),(974,563),(977,563),(980,563),(983,563),(986,563),(989,563),(992,563),(995,563),(998,563),(1001,563),(1004,563),(1007,563),(1010,563),(1013,560),(1016,557),(1019,554),(1022,551),(1025,548),(1028,545),(1031,542),(1034,539),(1037,536),(1040,533),(1043,530),(1046,527),(1049,524),(1052,521),(1055,518),(1058,515),(1061,512),(1064,509),(1067,506),(1070,503),(1073,500),(1076,497),(1079,494),(1082,491),(1085,488),(1088,485),(1091,482),(1094,479)]
        self.path3v = [(638,797),(641,794),(644,791),(647,788),(650,785),(653,782),(656,779),(659,776),(662,773),(665,770),(668,767),(671,764),(674,761),(677,758),(680,755),(683,752),(686,749),(689,746),(692,743),(695,740),(698,737),(701,734),(704,731),(707,728),(710,725),(713,722),(716,719),(719,716),(722,713),(725,710),(728,707),(731,704),(734,701),(737,698),(740,695),(743,692),(746,689),(749,686),(752,683),(755,680),(758,677),(761,674),(764,671),(767,668),(770,665),(773,662),(776,659),(779,656),(782,653),(785,650),(788,647),(791,644),(794,641),(797,638),(800,635),(803,632),(806,629),(809,626),(812,623),(815,620),(818,617),(821,614),(824,611),(827,608),(830,605),(833,602),(836,599),(839,596),(842,593),(845,590),(848,587),(851,584),(854,581),(857,578),(860,575),(863,572),(866,569),(869,566),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(872,563),(875,563),(878,563),(881,563),(884,563),(887,563),(890,563),(893,563),(896,563),(899,563),(902,563),(905,563),(908,563),(911,563),(914,563),(917,563),(920,563),(923,563),(926,563),(929,563),(932,563),(935,563),(938,563),(941,563),(944,563),(947,563),(950,563),(953,563),(956,563),(959,563),(962,563),(965,563),(968,563),(971,563),(974,563),(977,563),(980,563),(983,563),(986,563),(989,563),(992,563),(995,563),(998,563),(1001,563),(1004,563),(1007,563),(1010,563),(1013,560),(1016,557),(1019,554),(1022,551),(1025,548),(1028,545),(1031,542),(1034,539),(1037,536),(1040,533),(1043,530),(1046,527),(1049,524),(1052,521),(1055,518),(1058,515),(1061,512),(1064,509),(1067,506),(1070,503),(1073,500),(1076,497),(1079,494),(1082,491),(1085,488),(1088,485),(1091,482),(1094,479),(1097,476),(1100,473),(1103,470),(1106,467),(1109,464),(1112,461),(1115,458),(1118,455),(1121,452),(1124,449),(1127,446),(1130,443),(1133,440),(1136,437),(1139,434),(1142,431),(1145,428),(1148,425),(1151,422),(1154,419),(1157,416),(1160,413),(1163,410),(1166,407),(1169,404),(1172,401),(1175,398)]
        self.path2d = [(638,797),(641,794),(644,791),(647,788),(650,785),(653,782),(656,779),(659,776),(662,773),(665,770),(668,767),(671,764),(674,761),(677,758),(680,755),(683,752),(686,749),(689,746),(692,743),(695,740),(698,737),(701,734),(704,731),(707,728),(710,725),(713,722),(716,719),(719,716),(722,713),(725,710),(728,707),(731,704),(734,701),(737,698),(740,695),(743,692)]
        self.path3d = [(638,797),(641,794),(644,791),(647,788),(650,785),(653,782)]        
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

            #---
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
            #---

            """#CAMBIAR - Esto va fuera es para poder manipular el estado de las torres
            self.torre_mid_1_derecha = 0
            self.torre_mid_2_derecha = 1
            self.torre_mid_1_izquierda = 1
            self.torre_mid_2_izquierda = 1
            #-------"""
            if self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 872 and self.y == 563 or self.x == 923 and self.y == 563:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 872 and self.y == 563 or self.x == 923 and self.y == 563:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 872 and self.y == 563 or self.x == 923 and self.y == 563:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2D")
                if self.x == 743 and self.y == 692:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 653 and self.y == 782:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 653 and self.y == 782:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2V")

                if self.x == 872 and self.y == 563 or self.x == 1094 and self.y == 479:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 872 and self.y == 563 or self.x == 1175 and self.y == 398:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 872 and self.y == 563 or self.x == 1175 and self.y == 398:
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
                self.path = self.path2d
            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3V")
                self.path = self.path3d
            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3V")
                self.path = self.path3d
            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2D")
                self.path = self.path2v
            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3D")
                self.path = self.path3v
            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3D")
                self.path = self.path3v
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