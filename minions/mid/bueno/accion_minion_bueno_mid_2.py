import pygame
import math
import random
import sqlite3
class Accion_minion_bueno_mid_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 100  # Barra de vida
        self.max_health = 100  # Barra de vida
        self.vel = 3
        self.path = [(655,755),(658,752),(661,749),(664,746),(667,743),(670,740),(673,737),(676,734),(679,731),(682,728),(685,725),(688,722),(691,719),(694,716),(697,713),(700,710),(703,707),(706,704),(709,701),(712,698),(715,695),(718,692),(721,689),(724,686),(727,683),(730,680),(733,677),(736,674),(739,671),(742,668),(745,665),(748,662),(751,659),(754,656),(757,653),(760,650),(763,647),(766,644),(769,641),(772,638),(775,635),(778,632),(781,629),(784,626),(787,623),(790,620),(793,617),(796,614),(799,611),(802,608),(805,605),(808,602),(811,599),(814,596),(817,593),(820,590),(823,587),(826,584),(829,581),(832,578),(835,575),(838,572),(841,569),(844,566),(847,563),(850,560),(853,557),(856,554),(859,551),(862,548),(865,545),(868,542),(871,539),(874,536),(877,533),(880,530),(883,527),(886,524),(889,521),(889,521),(889,521),(889,521),(889,521),(889,521),(892,521),(895,521),(898,521),(901,521),(904,521),(907,521),(910,521),(913,521),(916,521),(919,521),(922,521)]
        
        self.path1 = [(655,755),(658,752),(661,749),(664,746),(667,743),(670,740),(673,737),(676,734),(679,731),(682,728),(685,725),(688,722),(691,719),(694,716),(697,713),(700,710),(703,707),(706,704),(709,701),(712,698),(715,695),(718,692),(721,689),(724,686),(727,683),(730,680),(733,677),(736,674),(739,671),(742,668),(745,665),(748,662),(751,659),(754,656),(757,653),(760,650),(763,647),(766,644),(769,641),(772,638),(775,635),(778,632),(781,629),(784,626),(787,623),(790,620),(793,617),(796,614),(799,611),(802,608),(805,605),(808,602),(811,599),(814,596),(817,593),(820,590),(823,587),(826,584),(829,581),(832,578),(835,575),(838,572),(841,569),(844,566),(847,563),(850,560),(853,557),(856,554),(859,551),(862,548),(865,545),(868,542),(871,539),(874,536),(877,533),(880,530),(883,527),(886,524),(889,521),(889,521),(889,521),(889,521),(889,521),(889,521),(892,521),(895,521),(898,521),(901,521),(904,521),(907,521),(910,521),(913,521),(916,521),(919,521),(922,521)]
        self.path2v = [(655,755),(658,752),(661,749),(664,746),(667,743),(670,740),(673,737),(676,734),(679,731),(682,728),(685,725),(688,722),(691,719),(694,716),(697,713),(700,710),(703,707),(706,704),(709,701),(712,698),(715,695),(718,692),(721,689),(724,686),(727,683),(730,680),(733,677),(736,674),(739,671),(742,668),(745,665),(748,662),(751,659),(754,656),(757,653),(760,650),(763,647),(766,644),(769,641),(772,638),(775,635),(778,632),(781,629),(784,626),(787,623),(790,620),(793,617),(796,614),(799,611),(802,608),(805,605),(808,602),(811,599),(814,596),(817,593),(820,590),(823,587),(826,584),(829,581),(832,578),(835,575),(838,572),(841,569),(844,566),(847,563),(850,560),(853,557),(856,554),(859,551),(862,548),(865,545),(868,542),(871,539),(874,536),(877,533),(880,530),(883,527),(886,524),(889,521),(889,521),(889,521),(889,521),(889,521),(889,521),(892,521),(895,521),(898,521),(901,521),(904,521),(907,521),(910,521),(913,521),(916,521),(919,521),(922,521),(925,521),(928,521),(931,521),(934,521),(937,521),(940,521),(943,521),(946,521),(949,521),(952,521),(955,521),(958,521),(961,521),(964,521),(967,521),(970,521),(973,521),(976,521),(979,521),(982,521),(985,521),(988,521),(991,521),(994,521),(997,521),(1000,521),(1003,521),(1006,521),(1009,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1015,518),(1018,515),(1021,512),(1024,509),(1027,506),(1030,503),(1033,500),(1036,497),(1039,494),(1042,491),(1045,488),(1048,485),(1051,482),(1054,479),(1057,476),(1060,473),(1063,470),(1066,467),(1069,464),(1072,461),(1075,458),(1078,455),(1081,452),(1084,449),(1087,446),(1090,443),(1093,440),(1096,437),(1099,434),(1102,431),(1105,428)]
        self.path3v = [(655,755),(658,752),(661,749),(664,746),(667,743),(670,740),(673,737),(676,734),(679,731),(682,728),(685,725),(688,722),(691,719),(694,716),(697,713),(700,710),(703,707),(706,704),(709,701),(712,698),(715,695),(718,692),(721,689),(724,686),(727,683),(730,680),(733,677),(736,674),(739,671),(742,668),(745,665),(748,662),(751,659),(754,656),(757,653),(760,650),(763,647),(766,644),(769,641),(772,638),(775,635),(778,632),(781,629),(784,626),(787,623),(790,620),(793,617),(796,614),(799,611),(802,608),(805,605),(808,602),(811,599),(814,596),(817,593),(820,590),(823,587),(826,584),(829,581),(832,578),(835,575),(838,572),(841,569),(844,566),(847,563),(850,560),(853,557),(856,554),(859,551),(862,548),(865,545),(868,542),(871,539),(874,536),(877,533),(880,530),(883,527),(886,524),(889,521),(889,521),(889,521),(889,521),(889,521),(889,521),(892,521),(895,521),(898,521),(901,521),(904,521),(907,521),(910,521),(913,521),(916,521),(919,521),(922,521),(925,521),(928,521),(931,521),(934,521),(937,521),(940,521),(943,521),(946,521),(949,521),(952,521),(955,521),(958,521),(961,521),(964,521),(967,521),(970,521),(973,521),(976,521),(979,521),(982,521),(985,521),(988,521),(991,521),(994,521),(997,521),(1000,521),(1003,521),(1006,521),(1009,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1012,521),(1015,518),(1018,515),(1021,512),(1024,509),(1027,506),(1030,503),(1033,500),(1036,497),(1039,494),(1042,491),(1045,488),(1048,485),(1051,482),(1054,479),(1057,476),(1060,473),(1063,470),(1066,467),(1069,464),(1072,461),(1075,458),(1078,455),(1081,452),(1084,449),(1087,446),(1090,443),(1093,440),(1096,437),(1099,434),(1102,431),(1105,428),(1108,425),(1111,422),(1114,419),(1117,416),(1120,413),(1123,410),(1126,407),(1129,404),(1132,401),(1135,398),(1138,395),(1141,392),(1144,389),(1147,386),(1150,383),(1153,380),(1156,377),(1159,374),(1162,371),(1165,368),(1168,365),(1171,362),(1174,359),(1177,356),(1180,353),(1183,350),(1186,347)]
        self.path2d = [(655,755),(658,752),(661,749),(664,746),(667,743),(670,740),(673,737),(676,734),(679,731),(682,728),(685,725),(688,722),(691,719),(694,716),(697,713),(700,710),(703,707),(706,704),(709,701),(712,698),(715,695),(718,692),(721,689),(724,686),(727,683),(730,680),(733,677),(736,674),(739,671),(742,668),(745,665),(748,662),(751,659),(754,656),(757,653),(760,650)]
        self.path3d = [(655,755),(658,752),(661,749),(664,746),(667,743),(670,740)]        
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
                if self.x == 889 and self.y == 521 or self.x == 922 and self.y == 521:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 1")
                if self.x == 889 and self.y == 521 or self.x == 922 and self.y == 521:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 1")
                if self.x == 889 and self.y == 521 or self.x == 922 and self.y == 521:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2D")
                if self.x == 760 and self.y == 650:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 670 and self.y == 740:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 670 and self.y == 740:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2V")
                if self.x == 889 and self.y == 521 or self.x == 1012 and self.y == 521 or self.x == 1105 and self.y == 428:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 889 and self.y == 521 or self.x == 1012 and self.y == 521 or self.x == 1186 and self.y == 347:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 889 and self.y == 521 or self.x == 1012 and self.y == 521 or self.x == 1186 and self.y == 347:
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