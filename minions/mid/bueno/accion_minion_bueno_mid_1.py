import pygame
import math
import random
import sqlite3

class Accion_minion_bueno_mid_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 100  # Barra de vida
        self.max_health = 100  # Barra de vida
        self.vel = 3
        self.path = [(609,760),(612,757),(615,754),(618,751),(621,748),(624,745),(627,742),(630,739),(633,736),(636,733),(639,730),(642,727),(645,724),(648,721),(651,718),(654,715),(657,712),(660,709),(663,706),(666,703),(669,700),(672,697),(675,694),(678,691),(681,688),(684,685),(687,682),(690,679),(693,676),(696,673),(699,670),(702,667),(705,664),(708,661),(711,658),(714,655),(717,652),(720,649),(723,646),(726,643),(729,640),(732,637),(735,634),(738,631),(741,628),(744,625),(747,622),(750,619),(753,616),(756,613),(759,610),(762,607),(765,604),(768,601),(771,598),(774,595),(777,592),(780,589),(783,586),(786,583),(789,580),(792,577),(795,574),(798,571),(801,568),(804,565),(807,562),(810,559),(813,556),(816,553),(819,550),(822,547),(825,544),(828,541),(831,538),(834,535),(837,532),(840,529),(843,526),(846,523),(849,520),(852,517),(855,514),(858,511),(861,508),(864,505),(867,502),(870,499),(873,496),(876,493),(879,490),(882,490),(885,490),(888,490),(891,490),(894,490),(897,490),(900,490),(903,490),(906,490),(909,490),(912,490),(915,490),(918,490),(921,490)]
        
        self.path1 = [(609,760),(612,757),(615,754),(618,751),(621,748),(624,745),(627,742),(630,739),(633,736),(636,733),(639,730),(642,727),(645,724),(648,721),(651,718),(654,715),(657,712),(660,709),(663,706),(666,703),(669,700),(672,697),(675,694),(678,691),(681,688),(684,685),(687,682),(690,679),(693,676),(696,673),(699,670),(702,667),(705,664),(708,661),(711,658),(714,655),(717,652),(720,649),(723,646),(726,643),(729,640),(732,637),(735,634),(738,631),(741,628),(744,625),(747,622),(750,619),(753,616),(756,613),(759,610),(762,607),(765,604),(768,601),(771,598),(774,595),(777,592),(780,589),(783,586),(786,583),(789,580),(792,577),(795,574),(798,571),(801,568),(804,565),(807,562),(810,559),(813,556),(816,553),(819,550),(822,547),(825,544),(828,541),(831,538),(834,535),(837,532),(840,529),(843,526),(846,523),(849,520),(852,517),(855,514),(858,511),(861,508),(864,505),(867,502),(870,499),(873,496),(876,493),(879,490),(882,490),(885,490),(888,490),(891,490),(894,490),(897,490),(900,490),(903,490),(906,490),(909,490),(912,490),(915,490),(918,490),(921,490)]
        self.path2v = [(609,760),(612,757),(615,754),(618,751),(621,748),(624,745),(627,742),(630,739),(633,736),(636,733),(639,730),(642,727),(645,724),(648,721),(651,718),(654,715),(657,712),(660,709),(663,706),(666,703),(669,700),(672,697),(675,694),(678,691),(681,688),(684,685),(687,682),(690,679),(693,676),(696,673),(699,670),(702,667),(705,664),(708,661),(711,658),(714,655),(717,652),(720,649),(723,646),(726,643),(729,640),(732,637),(735,634),(738,631),(741,628),(744,625),(747,622),(750,619),(753,616),(756,613),(759,610),(762,607),(765,604),(768,601),(771,598),(774,595),(777,592),(780,589),(783,586),(786,583),(789,580),(792,577),(795,574),(798,571),(801,568),(804,565),(807,562),(810,559),(813,556),(816,553),(819,550),(822,547),(825,544),(828,541),(831,538),(834,535),(837,532),(840,529),(843,526),(846,523),(849,520),(852,517),(855,514),(858,511),(861,508),(864,505),(867,502),(870,499),(873,496),(876,493),(879,490),(882,490),(885,490),(888,490),(891,490),(894,490),(897,490),(900,490),(903,490),(906,490),(909,490),(912,490),(915,490),(918,490),(921,490),(924,490),(927,490),(930,490),(933,490),(936,490),(939,490),(942,490),(945,490),(948,490),(951,490),(954,490),(957,490),(960,490),(963,490),(966,490),(969,490),(972,490),(975,490),(978,490),(981,490),(984,490),(987,490),(990,490),(993,490),(996,490),(999,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1005,487),(1008,484),(1011,481),(1014,478),(1017,475),(1020,472),(1023,469),(1026,466),(1029,463),(1032,460),(1035,457),(1038,454),(1041,451),(1044,448)]
        self.path3d = [(609,760),(612,757),(615,754),(618,751),(621,748),(624,745),(627,742),(630,739),(633,736),(636,733),(639,730),(642,727),(645,724),(648,721),(651,718),(654,715),(657,712),(660,709),(663,706),(666,703),(669,700),(672,697),(675,694),(678,691),(681,688),(684,685),(687,682),(690,679),(693,676),(696,673),(699,670),(702,667),(705,664),(708,661),(711,658),(714,655),(717,652),(720,649),(723,646),(726,643),(729,640),(732,637),(735,634),(738,631),(741,628),(744,625),(747,622),(750,619),(753,616),(756,613),(759,610),(762,607),(765,604),(768,601),(771,598),(774,595),(777,592),(780,589),(783,586),(786,583),(789,580),(792,577),(795,574),(798,571),(801,568),(804,565),(807,562),(810,559),(813,556),(816,553),(819,550),(822,547),(825,544),(828,541),(831,538),(834,535),(837,532),(840,529),(843,526),(846,523),(849,520),(852,517),(855,514),(858,511),(861,508),(864,505),(867,502),(870,499),(873,496),(876,493),(879,490),(882,490),(885,490),(888,490),(891,490),(894,490),(897,490),(900,490),(903,490),(906,490),(909,490),(912,490),(915,490),(918,490),(921,490),(924,490),(927,490),(930,490),(933,490),(936,490),(939,490),(942,490),(945,490),(948,490),(951,490),(954,490),(957,490),(960,490),(963,490),(966,490),(969,490),(972,490),(975,490),(978,490),(981,490),(984,490),(987,490),(990,490),(993,490),(996,490),(999,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1002,490),(1005,487),(1008,484),(1011,481),(1014,478),(1017,475),(1020,472),(1023,469),(1026,466),(1029,463),(1032,460),(1035,457),(1038,454),(1041,451),(1044,448),(1047,445),(1050,442),(1053,439),(1056,436),(1059,433),(1062,430),(1065,427),(1068,424),(1071,421),(1074,418),(1077,415),(1080,412),(1083,409),(1086,406),(1089,403),(1092,400),(1095,397),(1098,394),(1101,391),(1104,388),(1107,385),(1110,382),(1113,379),(1116,376),(1119,373),(1122,370),(1125,367)]
        self.path2d = [(609,760),(612,757),(615,754),(618,751),(621,748),(624,745),(627,742),(630,739),(633,736),(636,733),(639,730),(642,727),(645,724),(648,721),(651,718),(654,715),(657,712),(660,709),(663,706),(666,703),(669,700),(672,697),(675,694),(678,691),(681,688),(684,685),(687,682),(690,679),(693,676),(696,673),(699,670),(702,667),(705,664),(708,661),(711,658),(714,655)]
        self.path3d = [(609,760),(612,757),(615,754),(618,751),(621,748),(624,745)]        
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
                if self.x == 921 and self.y == 490:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 921 and self.y == 490:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 921 and self.y == 490:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2D")
                if self.x == 714 and self.y == 655:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 624 and self.y == 745:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 624 and self.y == 745:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 2V")
                if self.x == 1002 and self.y == 490 or self.x == 1044 and self.y == 448:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 1002 and self.y == 490 or self.x == 1125 and self.y == 367:
                    self.img = self.imgs2[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
                print("FASE 3V")
                if self.x == 1002 and self.y == 490 or self.x == 1125 and self.y == 367:
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
            print("FASE 2D")
            self.path = self.path2d
        elif self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
            print("FASE 3D")
            self.path = self.path3d
        elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and not self.torre_mid_2_izquierda:
            print("FASE 3D")
            self.path = self.path3d
        elif not self.torre_mid_1_derecha and self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
            print("FASE 2V")
            self.path = self.path2v
        elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
            print("FASE 3V")
            self.path = self.path3v
        elif not self.torre_mid_1_derecha and not self.torre_mid_2_derecha and not self.torre_mid_1_izquierda and self.torre_mid_2_izquierda:
            print("FASE 3V")
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