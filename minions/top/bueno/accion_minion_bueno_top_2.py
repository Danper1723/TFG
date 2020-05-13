import pygame
import math
import random
import sqlite3
class Accion_minion_bueno_top_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 100  # Barra de vida
        self.max_health = 100  # Barra de vida
        self.vel = 3
        self.path = [(516,687),(516,684),(516,681),(516,678),(516,675),(516,672),(516,669),(516,666),(516,663),(516,660),(516,657),(516,654),(516,651),(516,648),(516,645),(516,642),(516,639),(516,636),(516,633),(516,630),(516,627),(516,624),(516,621),(516,618),(516,615),(516,612),(516,609),(516,606),(516,603),(516,600),(516,597),(516,594),(516,591),(516,588),(516,585),(516,582),(516,579),(516,576),(516,573),(516,570),(516,567),(516,564),(516,561),(516,558),(516,555),(516,552),(516,549),(516,546),(516,543),(516,540),(516,537),(516,534),(516,531),(516,528),(516,525),(516,522),(516,519),(516,516),(516,513),(516,510),(516,507),(516,504),(516,501),(516,498),(516,495),(516,492),(516,489),(516,486),(516,483),(516,480),(516,477),(516,474),(516,471),(516,468),(516,465),(516,462),(516,459),(516,456),(516,453),(516,450),(516,447),(516,444),(516,441),(516,438),(516,435),(516,432),(516,429),(516,426),(516,423),(516,420),(516,417),(516,414),(516,411),(516,408),(516,405),(516,402),(516,399),(516,396),(516,393),(516,390),(516,387),(516,384),(516,381),(516,378),(516,375),(516,372),(516,369),(516,366),(516,363),(516,360),(516,357),(516,354),(516,351),(516,348),(516,345),(516,342),(516,339),(516,336),(516,333),(516,330),(516,327),(516,324),(516,321),(516,318),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(519,312),(522,309),(525,306),(528,303),(531,300),(534,297),(537,294),(540,291),(543,288),(546,285),(549,282),(552,279),(555,276),(558,273),(561,270),(564,267),(567,264),(570,261),(573,258),(576,255)]
        
        self.path1 = [(516,687),(516,684),(516,681),(516,678),(516,675),(516,672),(516,669),(516,666),(516,663),(516,660),(516,657),(516,654),(516,651),(516,648),(516,645),(516,642),(516,639),(516,636),(516,633),(516,630),(516,627),(516,624),(516,621),(516,618),(516,615),(516,612),(516,609),(516,606),(516,603),(516,600),(516,597),(516,594),(516,591),(516,588),(516,585),(516,582),(516,579),(516,576),(516,573),(516,570),(516,567),(516,564),(516,561),(516,558),(516,555),(516,552),(516,549),(516,546),(516,543),(516,540),(516,537),(516,534),(516,531),(516,528),(516,525),(516,522),(516,519),(516,516),(516,513),(516,510),(516,507),(516,504),(516,501),(516,498),(516,495),(516,492),(516,489),(516,486),(516,483),(516,480),(516,477),(516,474),(516,471),(516,468),(516,465),(516,462),(516,459),(516,456),(516,453),(516,450),(516,447),(516,444),(516,441),(516,438),(516,435),(516,432),(516,429),(516,426),(516,423),(516,420),(516,417),(516,414),(516,411),(516,408),(516,405),(516,402),(516,399),(516,396),(516,393),(516,390),(516,387),(516,384),(516,381),(516,378),(516,375),(516,372),(516,369),(516,366),(516,363),(516,360),(516,357),(516,354),(516,351),(516,348),(516,345),(516,342),(516,339),(516,336),(516,333),(516,330),(516,327),(516,324),(516,321),(516,318),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(519,312),(522,309),(525,306),(528,303),(531,300),(534,297),(537,294),(540,291),(543,288),(546,285),(549,282),(552,279),(555,276),(558,273),(561,270),(564,267),(567,264),(570,261),(573,258),(576,255)]
        self.path2v = [(516,687),(516,684),(516,681),(516,678),(516,675),(516,672),(516,669),(516,666),(516,663),(516,660),(516,657),(516,654),(516,651),(516,648),(516,645),(516,642),(516,639),(516,636),(516,633),(516,630),(516,627),(516,624),(516,621),(516,618),(516,615),(516,612),(516,609),(516,606),(516,603),(516,600),(516,597),(516,594),(516,591),(516,588),(516,585),(516,582),(516,579),(516,576),(516,573),(516,570),(516,567),(516,564),(516,561),(516,558),(516,555),(516,552),(516,549),(516,546),(516,543),(516,540),(516,537),(516,534),(516,531),(516,528),(516,525),(516,522),(516,519),(516,516),(516,513),(516,510),(516,507),(516,504),(516,501),(516,498),(516,495),(516,492),(516,489),(516,486),(516,483),(516,480),(516,477),(516,474),(516,471),(516,468),(516,465),(516,462),(516,459),(516,456),(516,453),(516,450),(516,447),(516,444),(516,441),(516,438),(516,435),(516,432),(516,429),(516,426),(516,423),(516,420),(516,417),(516,414),(516,411),(516,408),(516,405),(516,402),(516,399),(516,396),(516,393),(516,390),(516,387),(516,384),(516,381),(516,378),(516,375),(516,372),(516,369),(516,366),(516,363),(516,360),(516,357),(516,354),(516,351),(516,348),(516,345),(516,342),(516,339),(516,336),(516,333),(516,330),(516,327),(516,324),(516,321),(516,318),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(519,312),(522,309),(525,306),(528,303),(531,300),(534,297),(537,294),(540,291),(543,288),(546,285),(549,282),(552,279),(555,276),(558,273),(561,270),(564,267),(567,264),(570,261),(573,258),(576,255),(579,252),(582,249),(585,246),(588,243),(591,240),(594,237),(597,234),(600,231),(603,228),(606,225),(609,222),(612,219),(615,216),(618,213),(621,210),(624,207),(627,204),(630,201),(633,198),(636,195),(639,192),(642,189),(645,186),(648,183),(651,180),(654,177),(657,174),(660,171),(663,168),(666,165),(669,162),(672,159),(675,156),(678,153),(681,150),(684,147),(684,147),(684,147),(684,147),(687,147),(690,147),(693,147),(696,147),(699,147),(702,147),(705,147),(708,147),(711,147),(714,147),(717,147),(720,147),(723,147),(726,147),(729,147),(732,147),(735,147),(738,147),(741,147),(744,147),(747,147),(750,147),(753,147),(756,147),(759,147),(762,147),(765,147),(768,147),(771,147),(774,147),(777,147),(780,147),(783,147),(786,147),(789,147),(792,147),(795,147),(798,147),(801,147),(804,147),(807,147),(810,147),(813,147),(816,147),(819,147),(822,147),(825,147),(828,147),(831,147),(834,147),(837,147),(840,147),(843,147),(846,147),(849,147),(852,147),(855,147),(858,147),(861,147),(864,147),(867,147),(870,147),(873,147),(876,147),(879,147),(882,147),(885,147),(888,147),(891,147),(894,147),(897,147),(900,147),(903,147),(906,147),(909,147),(912,147),(915,147),(918,147),(921,147),(924,147),(927,147)]
        self.path3v = [(516,687),(516,684),(516,681),(516,678),(516,675),(516,672),(516,669),(516,666),(516,663),(516,660),(516,657),(516,654),(516,651),(516,648),(516,645),(516,642),(516,639),(516,636),(516,633),(516,630),(516,627),(516,624),(516,621),(516,618),(516,615),(516,612),(516,609),(516,606),(516,603),(516,600),(516,597),(516,594),(516,591),(516,588),(516,585),(516,582),(516,579),(516,576),(516,573),(516,570),(516,567),(516,564),(516,561),(516,558),(516,555),(516,552),(516,549),(516,546),(516,543),(516,540),(516,537),(516,534),(516,531),(516,528),(516,525),(516,522),(516,519),(516,516),(516,513),(516,510),(516,507),(516,504),(516,501),(516,498),(516,495),(516,492),(516,489),(516,486),(516,483),(516,480),(516,477),(516,474),(516,471),(516,468),(516,465),(516,462),(516,459),(516,456),(516,453),(516,450),(516,447),(516,444),(516,441),(516,438),(516,435),(516,432),(516,429),(516,426),(516,423),(516,420),(516,417),(516,414),(516,411),(516,408),(516,405),(516,402),(516,399),(516,396),(516,393),(516,390),(516,387),(516,384),(516,381),(516,378),(516,375),(516,372),(516,369),(516,366),(516,363),(516,360),(516,357),(516,354),(516,351),(516,348),(516,345),(516,342),(516,339),(516,336),(516,333),(516,330),(516,327),(516,324),(516,321),(516,318),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(516,315),(519,312),(522,309),(525,306),(528,303),(531,300),(534,297),(537,294),(540,291),(543,288),(546,285),(549,282),(552,279),(555,276),(558,273),(561,270),(564,267),(567,264),(570,261),(573,258),(576,255),(579,252),(582,249),(585,246),(588,243),(591,240),(594,237),(597,234),(600,231),(603,228),(606,225),(609,222),(612,219),(615,216),(618,213),(621,210),(624,207),(627,204),(630,201),(633,198),(636,195),(639,192),(642,189),(645,186),(648,183),(651,180),(654,177),(657,174),(660,171),(663,168),(666,165),(669,162),(672,159),(675,156),(678,153),(681,150),(684,147),(684,147),(684,147),(684,147),(687,147),(690,147),(693,147),(696,147),(699,147),(702,147),(705,147),(708,147),(711,147),(714,147),(717,147),(720,147),(723,147),(726,147),(729,147),(732,147),(735,147),(738,147),(741,147),(744,147),(747,147),(750,147),(753,147),(756,147),(759,147),(762,147),(765,147),(768,147),(771,147),(774,147),(777,147),(780,147),(783,147),(786,147),(789,147),(792,147),(795,147),(798,147),(801,147),(804,147),(807,147),(810,147),(813,147),(816,147),(819,147),(822,147),(825,147),(828,147),(831,147),(834,147),(837,147),(840,147),(843,147),(846,147),(849,147),(852,147),(855,147),(858,147),(861,147),(864,147),(867,147),(870,147),(873,147),(876,147),(879,147),(882,147),(885,147),(888,147),(891,147),(894,147),(897,147),(900,147),(903,147),(906,147),(909,147),(912,147),(915,147),(918,147),(921,147),(924,147),(927,147),(930,147),(933,147),(936,147),(939,147),(942,147),(945,147),(948,147),(951,147),(954,147),(957,147),(960,147),(963,147),(966,147),(969,147),(972,147),(975,147),(978,147),(981,147),(984,147),(987,147),(990,147),(993,147),(996,147),(999,147),(1002,147),(1005,147),(1008,147),(1011,147),(1014,147),(1017,147),(1020,147),(1023,147),(1026,147),(1029,147),(1032,147),(1035,147),(1038,147),(1041,147),(1044,147),(1047,147),(1050,147),(1053,147),(1056,147),(1059,147),(1062,147),(1065,147),(1068,147),(1071,147),(1074,147),(1077,147),(1080,147),(1083,147),(1086,147),(1089,147),(1092,147),(1095,147),(1098,147)]
        self.path2d = [(516,687),(516,684),(516,681),(516,678),(516,675),(516,672),(516,669),(516,666),(516,663),(516,660),(516,657),(516,654),(516,651),(516,648),(516,645),(516,642),(516,639),(516,636),(516,633),(516,630),(516,627),(516,624),(516,621),(516,618),(516,615),(516,612),(516,609),(516,606),(516,603),(516,600),(516,597),(516,594),(516,591),(516,588),(516,585),(516,582),(516,579),(516,576),(516,573),(516,570),(516,567),(516,564)]
        self.path3d = [(516,687),(516,684),(516,681),(516,678),(516,675),(516,672)]
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
        self.torre_top_1_izquierdau = 1
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
                if self.x == 576 and self.y == 255 or self.x == 516 and self.y == 315:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 576 and self.y == 255 or self.x == 516 and self.y == 315:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 576 and self.y == 255 or self.x == 516 and self.y == 315:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2D")
                if self.x == 516 and self.y == 564:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 516 and self.y == 672:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 516 and self.y == 672:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2V")
                if self.x == 516 and self.y == 315 or self.x == 684 and self.y == 147 or self.x == 927 and self.y == 147:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 516 and self.y == 315 or self.x == 684 and self.y == 147 or self.x == 1098 and self.y == 147:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 516 and self.y == 315 or self.x == 684 and self.y == 147 or self.x == 1098 and self.y == 147:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
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
            self.path = self.path2d
        elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
            print("FASE 3V")
            self.path = self.path3d
        elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
            print("FASE 3V")
            self.path = self.path3d
        elif not self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
            print("FASE 2D")
            self.path = self.path2v
        elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
            print("FASE 3D")
            self.path = self.path3v
        elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
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

        pygame.draw.rect(win, (255, 0, 0), (self.x - 0, self.y - 5, length, 5), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 0, self.y - 5, health_bar, 5), 0)

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