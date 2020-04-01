import pygame
import math
class Accion_minion_bueno_top_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(535,777),(535,774),(535,771),(535,768),(535,765),(535,762),(535,759),(535,756),(535,753),(535,750),(535,747),(535,744),(535,741),(535,738),(535,735),(535,732),(535,729),(535,726),(535,723),(535,720),(535,717),(535,714),(535,711),(535,708),(535,705),(535,702),(535,699),(535,696),(535,693),(535,690),(535,687),(535,684),(535,681),(535,678),(535,675),(535,672),(535,669),(535,666),(535,663),(535,660),(535,657),(535,654),(535,651),(535,648),(535,645),(535,642),(535,639),(535,636),(535,633),(535,630),(535,627),(535,624),(535,621),(535,618),(535,615),(535,612),(535,609),(535,606),(535,603),(535,600),(535,597),(535,594),(535,591),(535,588),(535,585),(535,582),(535,579),(535,576),(535,573),(535,570),(535,567),(535,564),(535,561),(535,558),(535,555),(535,552),(535,549),(535,546),(535,543),(535,540),(535,537),(535,534),(535,531),(535,528),(535,525),(535,522),(535,519),(535,516),(535,513),(535,510),(535,507),(535,504),(535,501),(535,498),(535,495),(535,492),(535,489),(535,486),(535,483),(535,480),(535,477),(535,474),(535,471),(535,468),(535,465),(535,462),(535,459),(535,456),(535,453),(535,450),(535,447),(535,444),(535,441),(535,438),(535,435),(535,432),(535,429),(535,426),(535,423),(535,420),(535,417),(535,414),(535,411),(535,408),(535,405),(535,402),(535,399),(535,396),(535,393),(535,390),(535,387),(535,384),(535,381),(535,378),(535,375),(535,372),(535,369),(535,366),(535,363),(535,360),(535,357),(535,354),(535,351),(535,348),(535,345),(535,342),(535,339),(535,336),(535,333),(535,330),(535,327),(535,324),(535,321),(535,318),(538,315),(541,312),(544,309),(547,306),(550,303),(553,300),(556,297),(559,294),(562,291),(565,288),(568,285)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

        self.nombre = ""

    def draw(self, win):
        self.nombre = self.id
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        """
        if self.x == 568 and self.y == 285:
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