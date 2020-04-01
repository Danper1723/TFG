import pygame
import math
class Accion_minion_bueno_mid_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(584,785),(587,782),(590,779),(593,776),(596,773),(599,770),(602,767),(605,764),(608,761),(611,758),(614,755),(617,752),(620,749),(623,746),(626,743),(629,740),(632,737),(635,734),(638,731),(641,728),(644,725),(647,722),(650,719),(653,716),(656,713),(659,710),(662,707),(665,704),(668,701),(671,698),(674,695),(677,692),(680,689),(683,686),(686,683),(689,680),(692,677),(695,674),(698,671),(701,668),(704,665),(707,662),(710,659),(713,656),(716,653),(719,650),(722,647),(725,644),(728,641),(731,638),(734,635),(737,632),(740,629),(743,626),(746,623),(749,620),(752,617),(755,614),(758,611),(761,608),(764,605),(767,602),(770,599),(773,596),(776,593),(779,590),(782,587),(785,584),(788,581),(791,578),(794,575),(797,572),(800,569),(803,566),(806,563),(809,560),(812,557),(815,554),(818,551),(821,548),(824,545),(827,542),(830,539),(833,536),(836,533),(839,530),(842,527),(845,524),(848,521),(851,518),(854,515),(857,512),(860,509),(863,506),(866,503),(869,500),(872,500),(875,500),(878,500),(881,500),(884,500)]
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

        if self.x == 884 and self.y == 500:
            self.img = self.imgs2[self.contador_animacion]
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