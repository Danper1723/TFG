import pygame
import math
class Accion_minion_malo_bot_2:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(1375,323),(1375,326),(1375,329),(1375,332),(1375,335),(1375,338),(1375,341),(1375,344),(1375,347),(1375,350),(1375,353),(1375,356),(1375,359),(1375,362),(1375,365),(1375,368),(1375,371),(1375,374),(1375,377),(1375,380),(1375,383),(1375,386),(1375,389),(1375,392),(1375,395),(1375,398),(1375,401),(1375,404),(1375,407),(1375,410),(1375,413),(1375,416),(1375,419),(1375,422),(1375,425),(1375,428),(1375,431),(1375,434),(1375,437),(1375,440),(1375,443),(1375,446),(1375,449),(1375,452),(1375,455),(1375,458),(1375,461),(1375,464),(1375,467),(1375,470),(1375,473),(1375,476),(1375,479),(1375,482),(1375,485),(1375,488),(1375,491),(1375,494),(1375,497),(1375,500),(1375,503),(1375,506),(1375,509),(1375,512),(1375,515),(1375,518),(1375,521),(1375,524),(1375,527),(1375,530),(1375,533),(1375,536),(1375,539),(1375,542),(1375,545),(1375,548),(1375,551),(1375,554),(1375,557),(1375,560),(1375,563),(1375,566),(1375,569),(1375,572),(1375,575),(1375,578),(1375,581),(1375,584),(1375,587),(1375,590),(1375,593),(1375,596),(1375,599),(1375,602),(1375,605),(1375,608),(1375,611),(1375,614),(1375,617),(1375,620),(1375,623),(1375,626),(1375,629),(1375,632),(1375,635),(1375,638),(1375,641),(1375,644),(1375,647),(1375,650),(1375,653),(1375,656),(1375,659),(1375,662),(1375,665),(1375,668),(1375,671),(1375,674),(1375,677),(1375,680),(1375,683),(1375,686),(1375,689),(1375,692),(1375,695),(1375,698),(1375,701),(1375,704),(1375,707),(1375,710),(1375,713),(1375,716),(1375,719),(1375,722),(1375,725),(1375,728),(1375,731),(1375,734),(1375,737),(1372,740),(1369,743),(1366,746),(1363,749),(1360,752),(1357,755),(1354,758),(1351,761),(1348,764),(1345,767),(1342,770),(1339,773),(1336,776),(1333,779),(1330,782),(1327,785),(1324,788),(1321,791)]
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

        if self.x == 1321 and self.y == 791:
            self.img = self.imgs3[self.contador_animacion]
        else:
            if self.x <= 1375 and self.y >= 737:
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