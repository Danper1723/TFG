import pygame
import math
import random
import sqlite3
class Accion_minion_bueno_top_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 200  # Barra de vida
        self.max_health = 200  # Barra de vida
        self.vel = 3
        self.path = [(493,720),(493,717),(493,714),(493,711),(493,708),(493,705),(493,702),(493,699),(493,696),(493,693),(493,690),(493,687),(493,684),(493,681),(493,678),(493,675),(493,672),(493,669),(493,666),(493,663),(493,660),(493,657),(493,654),(493,651),(493,648),(493,645),(493,642),(493,639),(493,636),(493,633),(493,630),(493,627),(493,624),(493,621),(493,618),(493,615),(493,612),(493,609),(493,606),(493,603),(493,600),(493,597),(493,594),(493,591),(493,588),(493,585),(493,582),(493,579),(493,576),(493,573),(493,570),(493,567),(493,564),(493,561),(493,558),(493,555),(493,552),(493,549),(493,546),(493,543),(493,540),(493,537),(493,534),(493,531),(493,528),(493,525),(493,522),(493,519),(493,516),(493,513),(493,510),(493,507),(493,504),(493,501),(493,498),(493,495),(493,492),(493,489),(493,486),(493,483),(493,480),(493,477),(493,474),(493,471),(493,468),(493,465),(493,462),(493,459),(493,456),(493,453),(493,450),(493,447),(493,444),(493,441),(493,438),(493,435),(493,432),(493,429),(493,426),(493,423),(493,420),(493,417),(493,414),(493,411),(493,408),(493,405),(493,402),(493,399),(493,396),(493,393),(493,390),(493,387),(493,384),(493,381),(493,378),(493,375),(493,372),(493,369),(493,366),(493,363),(493,360),(493,357),(493,354),(493,351),(493,348),(493,345),(493,342),(493,339),(493,336),(493,333),(493,330),(493,327),(493,324),(493,321),(493,318),(493,315),(493,312),(493,309),(493,306),(493,303),(493,300),(493,297),(493,294),(493,291),(493,288),(496,285),(499,282),(502,279),(505,276),(508,273),(511,270),(514,267),(517,264),(520,261),(523,258),(526,255)]
        
        self.path1 = [(493,720),(493,717),(493,714),(493,711),(493,708),(493,705),(493,702),(493,699),(493,696),(493,693),(493,690),(493,687),(493,684),(493,681),(493,678),(493,675),(493,672),(493,669),(493,666),(493,663),(493,660),(493,657),(493,654),(493,651),(493,648),(493,645),(493,642),(493,639),(493,636),(493,633),(493,630),(493,627),(493,624),(493,621),(493,618),(493,615),(493,612),(493,609),(493,606),(493,603),(493,600),(493,597),(493,594),(493,591),(493,588),(493,585),(493,582),(493,579),(493,576),(493,573),(493,570),(493,567),(493,564),(493,561),(493,558),(493,555),(493,552),(493,549),(493,546),(493,543),(493,540),(493,537),(493,534),(493,531),(493,528),(493,525),(493,522),(493,519),(493,516),(493,513),(493,510),(493,507),(493,504),(493,501),(493,498),(493,495),(493,492),(493,489),(493,486),(493,483),(493,480),(493,477),(493,474),(493,471),(493,468),(493,465),(493,462),(493,459),(493,456),(493,453),(493,450),(493,447),(493,444),(493,441),(493,438),(493,435),(493,432),(493,429),(493,426),(493,423),(493,420),(493,417),(493,414),(493,411),(493,408),(493,405),(493,402),(493,399),(493,396),(493,393),(493,390),(493,387),(493,384),(493,381),(493,378),(493,375),(493,372),(493,369),(493,366),(493,363),(493,360),(493,357),(493,354),(493,351),(493,348),(493,345),(493,342),(493,339),(493,336),(493,333),(493,330),(493,327),(493,324),(493,321),(493,318),(493,315),(493,312),(493,309),(493,306),(493,303),(493,300),(493,297),(493,294),(493,291),(493,288),(496,285),(499,282),(502,279),(505,276),(508,273),(511,270),(514,267),(517,264),(520,261),(523,258),(526,255)]
        self.path2v = [(493,720),(493,717),(493,714),(493,711),(493,708),(493,705),(493,702),(493,699),(493,696),(493,693),(493,690),(493,687),(493,684),(493,681),(493,678),(493,675),(493,672),(493,669),(493,666),(493,663),(493,660),(493,657),(493,654),(493,651),(493,648),(493,645),(493,642),(493,639),(493,636),(493,633),(493,630),(493,627),(493,624),(493,621),(493,618),(493,615),(493,612),(493,609),(493,606),(493,603),(493,600),(493,597),(493,594),(493,591),(493,588),(493,585),(493,582),(493,579),(493,576),(493,573),(493,570),(493,567),(493,564),(493,561),(493,558),(493,555),(493,552),(493,549),(493,546),(493,543),(493,540),(493,537),(493,534),(493,531),(493,528),(493,525),(493,522),(493,519),(493,516),(493,513),(493,510),(493,507),(493,504),(493,501),(493,498),(493,495),(493,492),(493,489),(493,486),(493,483),(493,480),(493,477),(493,474),(493,471),(493,468),(493,465),(493,462),(493,459),(493,456),(493,453),(493,450),(493,447),(493,444),(493,441),(493,438),(493,435),(493,432),(493,429),(493,426),(493,423),(493,420),(493,417),(493,414),(493,411),(493,408),(493,405),(493,402),(493,399),(493,396),(493,393),(493,390),(493,387),(493,384),(493,381),(493,378),(493,375),(493,372),(493,369),(493,366),(493,363),(493,360),(493,357),(493,354),(493,351),(493,348),(493,345),(493,342),(493,339),(493,336),(493,333),(493,330),(493,327),(493,324),(493,321),(493,318),(493,315),(493,312),(493,309),(493,306),(493,303),(493,300),(493,297),(493,294),(493,291),(493,288),(496,285),(499,282),(502,279),(505,276),(508,273),(511,270),(514,267),(517,264),(520,261),(523,258),(526,255),(529,252),(532,249),(535,246),(538,243),(541,240),(544,237),(547,234),(550,231),(553,228),(556,225),(559,222),(562,219),(565,216),(568,213),(571,210),(574,207),(577,204),(580,201),(583,198),(586,195),(589,192),(592,189),(595,186),(598,183),(601,180),(604,177),(607,174),(610,171),(613,168),(616,165),(619,162),(622,159),(625,156),(628,153),(631,150),(634,147),(637,144),(640,141),(643,138),(646,135),(649,132),(652,129),(655,126),(658,126),(661,126),(664,126),(667,126),(670,126),(673,126),(676,126),(679,126),(682,126),(685,126),(688,126),(691,126),(694,126),(697,126),(700,126),(703,126),(706,126),(709,126),(712,126),(715,126),(718,126),(721,126),(724,126),(727,126),(730,126),(733,126),(736,126),(739,126),(742,126),(745,126),(748,126),(751,126),(754,126),(757,126),(760,126),(763,126),(766,126),(769,126),(772,126),(775,126),(778,126),(781,126),(784,126),(787,126),(790,126),(793,126),(796,126),(799,126),(802,126),(805,126),(808,126),(811,126),(814,126),(817,126),(820,126),(823,126),(826,126),(829,126),(832,126),(835,126),(838,126),(841,126),(844,126),(847,126),(850,126),(853,126),(856,126),(859,126),(862,126),(865,126),(868,126),(871,126),(874,126),(877,126),(880,126),(883,126),(886,126)]
        self.path3v = [(493,720),(493,717),(493,714),(493,711),(493,708),(493,705),(493,702),(493,699),(493,696),(493,693),(493,690),(493,687),(493,684),(493,681),(493,678),(493,675),(493,672),(493,669),(493,666),(493,663),(493,660),(493,657),(493,654),(493,651),(493,648),(493,645),(493,642),(493,639),(493,636),(493,633),(493,630),(493,627),(493,624),(493,621),(493,618),(493,615),(493,612),(493,609),(493,606),(493,603),(493,600),(493,597),(493,594),(493,591),(493,588),(493,585),(493,582),(493,579),(493,576),(493,573),(493,570),(493,567),(493,564),(493,561),(493,558),(493,555),(493,552),(493,549),(493,546),(493,543),(493,540),(493,537),(493,534),(493,531),(493,528),(493,525),(493,522),(493,519),(493,516),(493,513),(493,510),(493,507),(493,504),(493,501),(493,498),(493,495),(493,492),(493,489),(493,486),(493,483),(493,480),(493,477),(493,474),(493,471),(493,468),(493,465),(493,462),(493,459),(493,456),(493,453),(493,450),(493,447),(493,444),(493,441),(493,438),(493,435),(493,432),(493,429),(493,426),(493,423),(493,420),(493,417),(493,414),(493,411),(493,408),(493,405),(493,402),(493,399),(493,396),(493,393),(493,390),(493,387),(493,384),(493,381),(493,378),(493,375),(493,372),(493,369),(493,366),(493,363),(493,360),(493,357),(493,354),(493,351),(493,348),(493,345),(493,342),(493,339),(493,336),(493,333),(493,330),(493,327),(493,324),(493,321),(493,318),(493,315),(493,312),(493,309),(493,306),(493,303),(493,300),(493,297),(493,294),(493,291),(493,288),(496,285),(499,282),(502,279),(505,276),(508,273),(511,270),(514,267),(517,264),(520,261),(523,258),(526,255),(529,252),(532,249),(535,246),(538,243),(541,240),(544,237),(547,234),(550,231),(553,228),(556,225),(559,222),(562,219),(565,216),(568,213),(571,210),(574,207),(577,204),(580,201),(583,198),(586,195),(589,192),(592,189),(595,186),(598,183),(601,180),(604,177),(607,174),(610,171),(613,168),(616,165),(619,162),(622,159),(625,156),(628,153),(631,150),(634,147),(637,144),(640,141),(643,138),(646,135),(649,132),(652,129),(655,126),(658,126),(661,126),(664,126),(667,126),(670,126),(673,126),(676,126),(679,126),(682,126),(685,126),(688,126),(691,126),(694,126),(697,126),(700,126),(703,126),(706,126),(709,126),(712,126),(715,126),(718,126),(721,126),(724,126),(727,126),(730,126),(733,126),(736,126),(739,126),(742,126),(745,126),(748,126),(751,126),(754,126),(757,126),(760,126),(763,126),(766,126),(769,126),(772,126),(775,126),(778,126),(781,126),(784,126),(787,126),(790,126),(793,126),(796,126),(799,126),(802,126),(805,126),(808,126),(811,126),(814,126),(817,126),(820,126),(823,126),(826,126),(829,126),(832,126),(835,126),(838,126),(841,126),(844,126),(847,126),(850,126),(853,126),(856,126),(859,126),(862,126),(865,126),(868,126),(871,126),(874,126),(877,126),(880,126),(883,126),(886,126),(889,126),(892,126),(895,126),(898,126),(901,126),(904,126),(907,126),(910,126),(913,126),(916,126),(919,126),(922,126),(925,126),(928,126),(931,126),(934,126),(937,126),(940,126),(943,126),(946,126),(949,126),(952,126),(955,126),(958,126),(961,126),(964,126),(967,126),(970,126),(973,126),(976,126),(979,126),(982,126),(985,126),(988,126),(991,126),(994,126),(997,126),(1000,126),(1003,126),(1006,126),(1009,126),(1012,126),(1015,126),(1018,126),(1021,126),(1024,126),(1027,126),(1030,126),(1033,126),(1036,126),(1039,126),(1042,126),(1045,126),(1048,126),(1051,126),(1054,126),(1057,126)]
        self.path2d = [(493,720),(493,717),(493,714),(493,711),(493,708),(493,705),(493,702),(493,699),(493,696),(493,693),(493,690),(493,687),(493,684),(493,681),(493,678),(493,675),(493,672),(493,669),(493,666),(493,663),(493,660),(493,657),(493,654),(493,651),(493,648),(493,645),(493,642),(493,639),(493,636),(493,633),(493,630),(493,627),(493,624),(493,621),(493,618),(493,615),(493,612),(493,609),(493,606),(493,603),(493,600),(493,597)]
        self.path3d = [(493,720),(493,717),(493,714),(493,711),(493,708),(493,705)]
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
                if self.x == 526 and self.y == 255:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 496 and self.y <= 294:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 526 and self.y == 255:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 496 and self.y <= 294:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 1")
                if self.x == 526 and self.y == 255:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 496 and self.y <= 294:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2D")
                if self.x == 493 and self.y == 597:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 493 and self.y == 705:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and not self.torre_top_1_izquierda and not self.torre_top_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 493 and self.y == 705:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 2V")
                if self.x == 886 and self.y == 126:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 496 and self.y <= 294:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 1057 and self.y == 126:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 496 and self.y <= 294:
                        self.img = self.imgs2[self.contador_animacion]
                    else:
                        self.img = self.imgs[self.contador_animacion]

            elif not self.torre_top_1_derecha and not self.torre_top_2_derecha and not self.torre_top_1_izquierda and self.torre_top_2_izquierda:
                print("FASE 3V")
                if self.x == 1057 and self.y == 126:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x >= 496 and self.y <= 294:
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

        pygame.draw.rect(win, (255, 0, 0), (self.x - 0, self.y - 5, length, 5), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 0, self.y - 5, health_bar, 5), 0)

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