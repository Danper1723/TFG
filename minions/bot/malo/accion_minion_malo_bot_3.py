import pygame
import math
class Accion_minion_malo_bot_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(1400,289),(1400,292),(1400,295),(1400,298),(1400,301),(1400,304),(1400,307),(1400,310),(1400,313),(1400,316),(1400,319),(1400,322),(1400,325),(1400,328),(1400,331),(1400,334),(1400,337),(1400,340),(1400,343),(1400,346),(1400,349),(1400,352),(1400,355),(1400,358),(1400,361),(1400,364),(1400,367),(1400,370),(1400,373),(1400,376),(1400,379),(1400,382),(1400,385),(1400,388),(1400,391),(1400,394),(1400,397),(1400,400),(1400,403),(1400,406),(1400,409),(1400,412),(1400,415),(1400,418),(1400,421),(1400,424),(1400,427),(1400,430),(1400,433),(1400,436),(1400,439),(1400,442),(1400,445),(1400,448),(1400,451),(1400,454),(1400,457),(1400,460),(1400,463),(1400,466),(1400,469),(1400,472),(1400,475),(1400,478),(1400,481),(1400,484),(1400,487),(1400,490),(1400,493),(1400,496),(1400,499),(1400,502),(1400,505),(1400,508),(1400,511),(1400,514),(1400,517),(1400,520),(1400,523),(1400,526),(1400,529),(1400,532),(1400,535),(1400,538),(1400,541),(1400,544),(1400,547),(1400,550),(1400,553),(1400,556),(1400,559),(1400,562),(1400,565),(1400,568),(1400,571),(1400,574),(1400,577),(1400,580),(1400,583),(1400,586),(1400,589),(1400,592),(1400,595),(1400,598),(1400,601),(1400,604),(1400,607),(1400,610),(1400,613),(1400,616),(1400,619),(1400,622),(1400,625),(1400,628),(1400,631),(1400,634),(1400,637),(1400,640),(1400,643),(1400,646),(1400,649),(1400,652),(1400,655),(1400,658),(1400,661),(1400,664),(1400,667),(1400,670),(1400,673),(1400,676),(1400,679),(1400,682),(1400,685),(1400,688),(1400,691),(1400,694),(1400,697),(1400,700),(1400,703),(1400,706),(1400,709),(1400,712),(1400,715),(1400,718),(1400,721),(1400,724),(1400,727),(1400,730),(1400,733),(1400,736),(1400,739),(1397,742),(1394,745),(1391,748),(1388,751),(1385,754),(1382,757),(1379,760),(1376,763),(1373,766),(1370,769),(1367,772),(1364,775)]
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

        if self.x == 1364 and self.y == 775:
            self.img = self.imgs3[self.contador_animacion]
        else:
            if self.x <= 1400 and self.y >= 739:
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