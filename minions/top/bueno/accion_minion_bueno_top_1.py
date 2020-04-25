import pygame
import math
class Accion_minion_bueno_top_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0

        self.vel = 3
        self.path = [(493,777),(493,774),(493,771),(493,768),(493,765),(493,762),(493,759),(493,756),(493,753),(493,750),(493,747),(493,744),(493,741),(493,738),(493,735),(493,732),(493,729),(493,726),(493,723),(493,720),(493,717),(493,714),(493,711),(493,708),(493,705),(493,702),(493,699),(493,696),(493,693),(493,690),(493,687),(493,684),(493,681),(493,678),(493,675),(493,672),(493,669),(493,666),(493,663),(493,660),(493,657),(493,654),(493,651),(493,648),(493,645),(493,642),(493,639),(493,636),(493,633),(493,630),(493,627),(493,624),(493,621),(493,618),(493,615),(493,612),(493,609),(493,606),(493,603),(493,600),(493,597),(493,594),(493,591),(493,588),(493,585),(493,582),(493,579),(493,576),(493,573),(493,570),(493,567),(493,564),(493,561),(493,558),(493,555),(493,552),(493,549),(493,546),(493,543),(493,540),(493,537),(493,534),(493,531),(493,528),(493,525),(493,522),(493,519),(493,516),(493,513),(493,510),(493,507),(493,504),(493,501),(493,498),(493,495),(493,492),(493,489),(493,486),(493,483),(493,480),(493,477),(493,474),(493,471),(493,468),(493,465),(493,462),(493,459),(493,456),(493,453),(493,450),(493,447),(493,444),(493,441),(493,438),(493,435),(493,432),(493,429),(493,426),(493,423),(493,420),(493,417),(493,414),(493,411),(493,408),(493,405),(493,402),(493,399),(493,396),(493,393),(493,390),(493,387),(493,384),(493,381),(493,378),(493,375),(493,372),(493,369),(493,366),(493,363),(493,360),(493,357),(493,354),(493,351),(493,348),(493,345),(493,342),(493,339),(493,336),(493,333),(493,330),(493,327),(493,324),(493,321),(493,318),(496,315),(499,312),(502,309),(505,306),(508,303),(511,300),(514,297),(517,294),(520,291),(523,288),(526,285),(529,282),(532,279),(535,276),(538,273),(541,270)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

        self.nombre = ""

        self.health = 100  # Barra de vida
        self.max_health = 100#Barra de vida

    def draw(self, win):
        self.nombre = self.id
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        """
        if self.x == 541 and self.y == 270:
            self.img = self.imgs3[self.contador_animacion]
        else:
            if self.x >= 507 and self.y <= 315:
                self.img = self.imgs2[self.contador_animacion]
                print("giro")
            else:
                self.img = self.imgs[self.contador_animacion]
            """
            SIRVE QUE EL MINION GIRE CUANDO LLEGUE A LA CURVA
            """

        self.contador_animacion += 1
        #ESTE IF REINICIARA EL CONTADOR DE ANIMACIONES PAR A SIMULAR EL MOVIMIENTO DE LA IMGANES
        if self.contador_animacion >= len(self.imgs):
            self.contador_animacion = 0

        win.blit(self.img, (self.x, self.y))
        #if

        self.mover()
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
        #TODA ESTA MIERDA ES PARA CALCULAR EL MOVIMIENTO ENTRE PUNTOS MEDIANTE EL TEOREMA DE PITAGORAS(VECTORES)
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

    def draw_health_bar(self, win):#Barra de vida
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """

        length = 25
        move_by = length / self.max_health
        health_bar = round(move_by * self.health)

        pygame.draw.rect(win, (255, 0, 0), (self.x - 15, self.y + 35, length, 5), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 15, self.y + 35, health_bar, 5), 0)