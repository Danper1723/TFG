import pygame
import math
#from .minion_1 import Miniom_1 as per
#(507,315)
class Accion_minion_mid_3:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        #self.path = [(504,777),(504,774),(504,771),(504,768),(504,765),(504,762),(504,759),(504,756),(504,753),(504,750),(504,747),(504,744),(504,741),(504,738),(504,735),(504,732),(504,729),(504,726),(504,723),(504,720),(504,717),(504,714),(504,711),(504,708),(504,705),(504,702),(504,699),(504,696),(504,693),(504,690),(504,687),(504,684),(504,681),(504,678),(504,675),(504,672),(504,669),(504,666),(504,663),(504,660),(504,657),(504,654),(504,651),(504,648),(504,645),(504,642),(504,639),(504,636),(504,633),(504,630),(504,627),(504,624),(504,621),(504,618),(504,615),(504,612),(504,609),(504,606),(504,603),(504,600),(504,597),(504,594),(504,591),(504,588),(504,585),(504,582),(504,579),(504,576),(504,573),(504,570),(504,567),(504,564),(504,561),(504,558),(504,555),(504,552),(504,549),(504,546),(504,543),(504,540),(504,537),(504,534),(504,531),(504,528),(504,525),(504,522),(504,519),(504,516),(504,513),(504,510),(504,507),(504,504),(504,501),(504,498),(504,495),(504,492),(504,489),(504,486),(504,483),(504,480),(504,477),(504,474),(504,471),(504,468),(504,465),(504,462),(504,459),(504,456),(504,453),(504,450),(504,447),(504,444),(504,441),(504,438),(504,435),(504,432),(504,429),(504,426),(504,423),(504,420),(504,417),(504,414),(504,411),(504,408),(504,405),(504,402),(504,399),(504,396),(504,393),(504,390),(504,387),(504,384),(504,381),(504,378),(504,375),(504,372),(504,369),(504,366),(504,363),(504,360),(504,357),(504,354),(504,351),(504,348),(504,345),(504,342),(504,339),(504,336),(504,333),(504,330),(504,327),(504,324),(504,321),(504,318),(507,315),(510,312),(513,309),(516,306),(519,303),(522,300),(525,297),(528,294),(531,291),(534,288),(537,285),(540,282),(543,279),(546,276),(549,273),(552,270),(555,267),(558,264),(561,261),(564,258),(567,255),(570,252),(573,249),(576,246),(579,243),(582,240),(585,237),(588,234),(591,231),(594,228),(597,225),(600,222),(603,219),(606,216),(609,213),(612,210),(615,207),(618,204),(621,201),(624,198),(627,195),(630,192),(633,189),(636,186),(639,183),(642,180),(645,177),(648,174),(651,171),(654,168),(657,165),(660,162),(663,159),(666,156),(669,153),(672,150)]
        self.path = [(621,829),(624,826),(627,823),(630,820),(633,817),(636,814),(639,811),(642,808),(645,805),(648,802),(651,799),(654,796),(657,793),(660,790),(663,787),(666,784),(669,781),(672,778),(675,775),(678,772),(681,769),(684,766),(687,763),(690,760),(693,757),(696,754),(699,751),(702,748),(705,745),(708,742),(711,739),(714,736),(717,733),(720,730),(723,727),(726,724),(729,721),(732,718),(735,715),(738,712),(741,709),(744,706),(747,703),(750,700),(753,697),(756,694),(759,691),(762,688),(765,685),(768,682),(771,679),(774,676),(777,673),(780,670),(783,667),(786,664),(789,661),(792,658),(795,655),(798,652),(801,649),(804,646),(807,643),(810,640),(813,637),(816,634),(819,631),(822,628),(825,625),(828,622),(831,619),(834,616),(837,613),(840,610),(843,607),(846,604),(849,601),(852,598),(855,595),(858,592),(861,589),(864,586),(867,583),(870,580),(873,577),(876,574),(879,571),(882,568),(885,568)]#,(888,568)]
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

        if self.x == 885 and self.y == 568:
            self.img = self.imgs2[self.contador_animacion]
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