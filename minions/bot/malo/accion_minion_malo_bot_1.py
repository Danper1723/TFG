import pygame
import math
class Accion_minion_malo_bot_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(1348,289),(1348,292),(1348,295),(1348,298),(1348,301),(1348,304),(1348,307),(1348,310),(1348,313),(1348,316),(1348,319),(1348,322),(1348,325),(1348,328),(1348,331),(1348,334),(1348,337),(1348,340),(1348,343),(1348,346),(1348,349),(1348,352),(1348,355),(1348,358),(1348,361),(1348,364),(1348,367),(1348,370),(1348,373),(1348,376),(1348,379),(1348,382),(1348,385),(1348,388),(1348,391),(1348,394),(1348,397),(1348,400),(1348,403),(1348,406),(1348,409),(1348,412),(1348,415),(1348,418),(1348,421),(1348,424),(1348,427),(1348,430),(1348,433),(1348,436),(1348,439),(1348,442),(1348,445),(1348,448),(1348,451),(1348,454),(1348,457),(1348,460),(1348,463),(1348,466),(1348,469),(1348,472),(1348,475),(1348,478),(1348,481),(1348,484),(1348,487),(1348,490),(1348,493),(1348,496),(1348,499),(1348,502),(1348,505),(1348,508),(1348,511),(1348,514),(1348,517),(1348,520),(1348,523),(1348,526),(1348,529),(1348,532),(1348,535),(1348,538),(1348,541),(1348,544),(1348,547),(1348,550),(1348,553),(1348,556),(1348,559),(1348,562),(1348,565),(1348,568),(1348,571),(1348,574),(1348,577),(1348,580),(1348,583),(1348,586),(1348,589),(1348,592),(1348,595),(1348,598),(1348,601),(1348,604),(1348,607),(1348,610),(1348,613),(1348,616),(1348,619),(1348,622),(1348,625),(1348,628),(1348,631),(1348,634),(1348,637),(1348,640),(1348,643),(1348,646),(1348,649),(1348,652),(1348,655),(1348,658),(1348,661),(1348,664),(1348,667),(1348,670),(1348,673),(1348,676),(1348,679),(1348,682),(1348,685),(1348,688),(1348,691),(1348,694),(1348,697),(1348,700),(1348,703),(1348,706),(1348,709),(1348,712),(1348,715),(1348,718),(1348,721),(1348,724),(1345,727),(1342,730),(1339,733),(1336,736),(1333,739),(1330,742),(1327,745),(1324,748)]
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

        if self.x == 1324 and self.y == 748:
            self.img = self.imgs3[self.contador_animacion]
        else:
            if self.x <= 1348 and self.y >= 724:
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