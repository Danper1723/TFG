import pygame
import math
import random
import sqlite3
class Accion_minion_bueno_top_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 100  # Barra de vida
        self.max_health = 100  # Barra de vida
        self.vel = 3
        self.path = [(535,720),(535,717),(535,714),(535,711),(535,708),(535,705),(535,702),(535,699),(535,696),(535,693),(535,690),(535,687),(535,684),(535,681),(535,678),(535,675),(535,672),(535,669),(535,666),(535,663),(535,660),(535,657),(535,654),(535,651),(535,648),(535,645),(535,642),(535,639),(535,636),(535,633),(535,630),(535,627),(535,624),(535,621),(535,618),(535,615),(535,612),(535,609),(535,606),(535,603),(535,600),(535,597),(535,594),(535,591),(535,588),(535,585),(535,582),(535,579),(535,576),(535,573),(535,570),(535,567),(535,564),(535,561),(535,558),(535,555),(535,552),(535,549),(535,546),(535,543),(535,540),(535,537),(535,534),(535,531),(535,528),(535,525),(535,522),(535,519),(535,516),(535,513),(535,510),(535,507),(535,504),(535,501),(535,498),(535,495),(535,492),(535,489),(535,486),(535,483),(535,480),(535,477),(535,474),(535,471),(535,468),(535,465),(535,462),(535,459),(535,456),(535,453),(535,450),(535,447),(535,444),(535,441),(535,438),(535,435),(535,432),(535,429),(535,426),(535,423),(535,420),(535,417),(535,414),(535,411),(535,408),(535,405),(535,402),(535,399),(535,396),(535,393),(535,390),(535,387),(535,384),(535,381),(535,378),(535,375),(535,372),(535,369),(535,366),(535,363),(535,360),(535,357),(535,354),(535,351),(535,348),(535,345),(535,342),(535,339),(535,336),(535,333),(535,330),(535,327),(535,324),(535,321),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(538,315),(541,312),(544,309),(547,306),(550,303),(553,300),(556,297),(559,294)]
        
        self.path1 = [(535,720),(535,717),(535,714),(535,711),(535,708),(535,705),(535,702),(535,699),(535,696),(535,693),(535,690),(535,687),(535,684),(535,681),(535,678),(535,675),(535,672),(535,669),(535,666),(535,663),(535,660),(535,657),(535,654),(535,651),(535,648),(535,645),(535,642),(535,639),(535,636),(535,633),(535,630),(535,627),(535,624),(535,621),(535,618),(535,615),(535,612),(535,609),(535,606),(535,603),(535,600),(535,597),(535,594),(535,591),(535,588),(535,585),(535,582),(535,579),(535,576),(535,573),(535,570),(535,567),(535,564),(535,561),(535,558),(535,555),(535,552),(535,549),(535,546),(535,543),(535,540),(535,537),(535,534),(535,531),(535,528),(535,525),(535,522),(535,519),(535,516),(535,513),(535,510),(535,507),(535,504),(535,501),(535,498),(535,495),(535,492),(535,489),(535,486),(535,483),(535,480),(535,477),(535,474),(535,471),(535,468),(535,465),(535,462),(535,459),(535,456),(535,453),(535,450),(535,447),(535,444),(535,441),(535,438),(535,435),(535,432),(535,429),(535,426),(535,423),(535,420),(535,417),(535,414),(535,411),(535,408),(535,405),(535,402),(535,399),(535,396),(535,393),(535,390),(535,387),(535,384),(535,381),(535,378),(535,375),(535,372),(535,369),(535,366),(535,363),(535,360),(535,357),(535,354),(535,351),(535,348),(535,345),(535,342),(535,339),(535,336),(535,333),(535,330),(535,327),(535,324),(535,321),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(538,315),(541,312),(544,309),(547,306),(550,303),(553,300),(556,297),(559,294)]
        self.path2v = [(535,720),(535,717),(535,714),(535,711),(535,708),(535,705),(535,702),(535,699),(535,696),(535,693),(535,690),(535,687),(535,684),(535,681),(535,678),(535,675),(535,672),(535,669),(535,666),(535,663),(535,660),(535,657),(535,654),(535,651),(535,648),(535,645),(535,642),(535,639),(535,636),(535,633),(535,630),(535,627),(535,624),(535,621),(535,618),(535,615),(535,612),(535,609),(535,606),(535,603),(535,600),(535,597),(535,594),(535,591),(535,588),(535,585),(535,582),(535,579),(535,576),(535,573),(535,570),(535,567),(535,564),(535,561),(535,558),(535,555),(535,552),(535,549),(535,546),(535,543),(535,540),(535,537),(535,534),(535,531),(535,528),(535,525),(535,522),(535,519),(535,516),(535,513),(535,510),(535,507),(535,504),(535,501),(535,498),(535,495),(535,492),(535,489),(535,486),(535,483),(535,480),(535,477),(535,474),(535,471),(535,468),(535,465),(535,462),(535,459),(535,456),(535,453),(535,450),(535,447),(535,444),(535,441),(535,438),(535,435),(535,432),(535,429),(535,426),(535,423),(535,420),(535,417),(535,414),(535,411),(535,408),(535,405),(535,402),(535,399),(535,396),(535,393),(535,390),(535,387),(535,384),(535,381),(535,378),(535,375),(535,372),(535,369),(535,366),(535,363),(535,360),(535,357),(535,354),(535,351),(535,348),(535,345),(535,342),(535,339),(535,336),(535,333),(535,330),(535,327),(535,324),(535,321),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(538,315),(541,312),(544,309),(547,306),(550,303),(553,300),(556,297),(559,294),(562,291),(565,288),(568,285),(571,282),(574,279),(577,276),(580,273),(583,270),(586,267),(589,264),(592,261),(595,258),(598,255),(601,252),(604,249),(607,246),(610,243),(613,240),(616,237),(619,234),(622,231),(625,228),(628,225),(631,222),(634,219),(637,216),(640,213),(643,210),(646,207),(649,204),(652,201),(655,198),(658,195),(661,192),(664,189),(667,186),(670,183),(673,180),(676,177),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(682,174),(685,174),(688,174),(691,174),(694,174),(697,174),(700,174),(703,174),(706,174),(709,174),(712,174),(715,174),(718,174),(721,174),(724,174),(727,174),(730,174),(733,174),(736,174),(739,174),(742,174),(745,174),(748,174),(751,174),(754,174),(757,174),(760,174),(763,174),(766,174),(769,174),(772,174),(775,174),(778,174),(781,174),(784,174),(787,174),(790,174),(793,174),(796,174),(799,174),(802,174),(805,174),(808,174),(811,174),(814,174),(817,174),(820,174),(823,174),(826,174),(829,174),(832,174),(835,174),(838,174),(841,174),(844,174),(847,174),(850,174),(853,174),(856,174),(859,174),(862,174),(865,174),(868,174),(871,174),(874,174),(877,174),(880,174),(883,174),(886,174)]
        self.path3v = [(535,720),(535,717),(535,714),(535,711),(535,708),(535,705),(535,702),(535,699),(535,696),(535,693),(535,690),(535,687),(535,684),(535,681),(535,678),(535,675),(535,672),(535,669),(535,666),(535,663),(535,660),(535,657),(535,654),(535,651),(535,648),(535,645),(535,642),(535,639),(535,636),(535,633),(535,630),(535,627),(535,624),(535,621),(535,618),(535,615),(535,612),(535,609),(535,606),(535,603),(535,600),(535,597),(535,594),(535,591),(535,588),(535,585),(535,582),(535,579),(535,576),(535,573),(535,570),(535,567),(535,564),(535,561),(535,558),(535,555),(535,552),(535,549),(535,546),(535,543),(535,540),(535,537),(535,534),(535,531),(535,528),(535,525),(535,522),(535,519),(535,516),(535,513),(535,510),(535,507),(535,504),(535,501),(535,498),(535,495),(535,492),(535,489),(535,486),(535,483),(535,480),(535,477),(535,474),(535,471),(535,468),(535,465),(535,462),(535,459),(535,456),(535,453),(535,450),(535,447),(535,444),(535,441),(535,438),(535,435),(535,432),(535,429),(535,426),(535,423),(535,420),(535,417),(535,414),(535,411),(535,408),(535,405),(535,402),(535,399),(535,396),(535,393),(535,390),(535,387),(535,384),(535,381),(535,378),(535,375),(535,372),(535,369),(535,366),(535,363),(535,360),(535,357),(535,354),(535,351),(535,348),(535,345),(535,342),(535,339),(535,336),(535,333),(535,330),(535,327),(535,324),(535,321),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(535,318),(538,315),(541,312),(544,309),(547,306),(550,303),(553,300),(556,297),(559,294),(562,291),(565,288),(568,285),(571,282),(574,279),(577,276),(580,273),(583,270),(586,267),(589,264),(592,261),(595,258),(598,255),(601,252),(604,249),(607,246),(610,243),(613,240),(616,237),(619,234),(622,231),(625,228),(628,225),(631,222),(634,219),(637,216),(640,213),(643,210),(646,207),(649,204),(652,201),(655,198),(658,195),(661,192),(664,189),(667,186),(670,183),(673,180),(676,177),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(679,174),(682,174),(685,174),(688,174),(691,174),(694,174),(697,174),(700,174),(703,174),(706,174),(709,174),(712,174),(715,174),(718,174),(721,174),(724,174),(727,174),(730,174),(733,174),(736,174),(739,174),(742,174),(745,174),(748,174),(751,174),(754,174),(757,174),(760,174),(763,174),(766,174),(769,174),(772,174),(775,174),(778,174),(781,174),(784,174),(787,174),(790,174),(793,174),(796,174),(799,174),(802,174),(805,174),(808,174),(811,174),(814,174),(817,174),(820,174),(823,174),(826,174),(829,174),(832,174),(835,174),(838,174),(841,174),(844,174),(847,174),(850,174),(853,174),(856,174),(859,174),(862,174),(865,174),(868,174),(871,174),(874,174),(877,174),(880,174),(883,174),(886,174),(889,174),(892,174),(895,174),(898,174),(901,174),(904,174),(907,174),(910,174),(913,174),(916,174),(919,174),(922,174),(925,174),(928,174),(931,174),(934,174),(937,174),(940,174),(943,174),(946,174),(949,174),(952,174),(955,174),(958,174),(961,174),(964,174),(967,174),(970,174),(973,174),(976,174),(979,174),(982,174),(985,174),(988,174),(991,174),(994,174),(997,174),(1000,174),(1003,174),(1006,174),(1009,174),(1012,174),(1015,174),(1018,174),(1021,174),(1024,174),(1027,174),(1030,174),(1033,174),(1036,174),(1039,174),(1042,174),(1045,174),(1048,174),(1051,174),(1054,174),(1057,174)]
        self.path2d = [(535,720),(535,717),(535,714),(535,711),(535,708),(535,705),(535,702),(535,699),(535,696),(535,693),(535,690),(535,687),(535,684),(535,681),(535,678),(535,675),(535,672),(535,669),(535,666),(535,663),(535,660),(535,657),(535,654),(535,651),(535,648),(535,645),(535,642),(535,639),(535,636),(535,633),(535,630),(535,627),(535,624),(535,621),(535,618),(535,615),(535,612),(535,609),(535,606),(535,603),(535,600),(535,597)]
        self.path3d = [(535,720),(535,717),(535,714),(535,711),(535,708),(535,705)]
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
                if self.x == 559 and self.y == 294 or self.x == 535 and self.y == 318:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 559 and self.y == 294 or self.x == 535 and self.y == 318:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 559 and self.y == 294 or self.x == 535 and self.y == 318:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2D")
                if self.x == 535 and self.y == 597:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 535 and self.y == 705:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 535 and self.y == 705:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2V")
                if self.x == 535 and self.y == 318 or self.x == 679 and self.y == 174 or self.x == 886 and self.y == 174:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]


            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 535 and self.y == 318 or self.x == 679 and self.y == 174 or self.x == 1057 and self.y == 174:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 507 and self.y <= 315:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 535 and self.y == 318 or self.x == 679 and self.y == 174 or self.x == 1057 and self.y == 174:
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