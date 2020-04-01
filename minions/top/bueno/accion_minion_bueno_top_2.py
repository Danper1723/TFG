import pygame
import math
class Accion_minion_bueno_top_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(516,747),(516,744),(516,741),(516,738),(516,735),(516,732),(516,729),(516,726),(516,723),(516,720),(516,717),(516,714),(516,711),(516,708),(516,705),(516,702),(516,699),(516,696),(516,693),(516,690),(516,687),(516,684),(516,681),(516,678),(516,675),(516,672),(516,669),(516,666),(516,663),(516,660),(516,657),(516,654),(516,651),(516,648),(516,645),(516,642),(516,639),(516,636),(516,633),(516,630),(516,627),(516,624),(516,621),(516,618),(516,615),(516,612),(516,609),(516,606),(516,603),(516,600),(516,597),(516,594),(516,591),(516,588),(516,585),(516,582),(516,579),(516,576),(516,573),(516,570),(516,567),(516,564),(516,561),(516,558),(516,555),(516,552),(516,549),(516,546),(516,543),(516,540),(516,537),(516,534),(516,531),(516,528),(516,525),(516,522),(516,519),(516,516),(516,513),(516,510),(516,507),(516,504),(516,501),(516,498),(516,495),(516,492),(516,489),(516,486),(516,483),(516,480),(516,477),(516,474),(516,471),(516,468),(516,465),(516,462),(516,459),(516,456),(516,453),(516,450),(516,447),(516,444),(516,441),(516,438),(516,435),(516,432),(516,429),(516,426),(516,423),(516,420),(516,417),(516,414),(516,411),(516,408),(516,405),(516,402),(516,399),(516,396),(516,393),(516,390),(516,387),(516,384),(516,381),(516,378),(516,375),(516,372),(516,369),(516,366),(516,363),(516,360),(516,357),(516,354),(516,351),(516,348),(516,345),(516,342),(516,339),(516,336),(516,333),(516,330),(516,327),(516,324),(516,321),(516,318),(519,315),(522,312),(525,309),(528,306),(531,303),(534,300),(537,297),(540,294),(543,291),(546,288),(549,285),(552,282),(555,279),(558,276),(561,273),(564,270),(567,267),(570,264),(573,261),(576,258),(579,255)]
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

        if self.x == 579 and self.y == 255:
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