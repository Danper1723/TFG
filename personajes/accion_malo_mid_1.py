import pygame
import math
#from .minion_1 import Miniom_1 as per
#(507,315)
class Accion_malo_mid_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        #self.path = [(504,777),(504,774),(504,771),(504,768),(504,765),(504,762),(504,759),(504,756),(504,753),(504,750),(504,747),(504,744),(504,741),(504,738),(504,735),(504,732),(504,729),(504,726),(504,723),(504,720),(504,717),(504,714),(504,711),(504,708),(504,705),(504,702),(504,699),(504,696),(504,693),(504,690),(504,687),(504,684),(504,681),(504,678),(504,675),(504,672),(504,669),(504,666),(504,663),(504,660),(504,657),(504,654),(504,651),(504,648),(504,645),(504,642),(504,639),(504,636),(504,633),(504,630),(504,627),(504,624),(504,621),(504,618),(504,615),(504,612),(504,609),(504,606),(504,603),(504,600),(504,597),(504,594),(504,591),(504,588),(504,585),(504,582),(504,579),(504,576),(504,573),(504,570),(504,567),(504,564),(504,561),(504,558),(504,555),(504,552),(504,549),(504,546),(504,543),(504,540),(504,537),(504,534),(504,531),(504,528),(504,525),(504,522),(504,519),(504,516),(504,513),(504,510),(504,507),(504,504),(504,501),(504,498),(504,495),(504,492),(504,489),(504,486),(504,483),(504,480),(504,477),(504,474),(504,471),(504,468),(504,465),(504,462),(504,459),(504,456),(504,453),(504,450),(504,447),(504,444),(504,441),(504,438),(504,435),(504,432),(504,429),(504,426),(504,423),(504,420),(504,417),(504,414),(504,411),(504,408),(504,405),(504,402),(504,399),(504,396),(504,393),(504,390),(504,387),(504,384),(504,381),(504,378),(504,375),(504,372),(504,369),(504,366),(504,363),(504,360),(504,357),(504,354),(504,351),(504,348),(504,345),(504,342),(504,339),(504,336),(504,333),(504,330),(504,327),(504,324),(504,321),(504,318),(507,315),(510,312),(513,309),(516,306),(519,303),(522,300),(525,297),(528,294),(531,291),(534,288),(537,285),(540,282),(543,279),(546,276),(549,273),(552,270),(555,267),(558,264),(561,261),(564,258),(567,255),(570,252),(573,249),(576,246),(579,243),(582,240),(585,237),(588,234),(591,231),(594,228),(597,225),(600,222),(603,219),(606,216),(609,213),(612,210),(615,207),(618,204),(621,201),(624,198),(627,195),(630,192),(633,189),(636,186),(639,183),(642,180),(645,177),(648,174),(651,171),(654,168),(657,165),(660,162),(663,159),(666,156),(669,153),(672,150)]
        self.path = [(1244,242),(1241,245),(1238,248),(1235,251),(1232,254),(1229,257),(1226,260),(1223,263),(1220,266),(1217,269),(1214,272),(1211,275),(1208,278),(1205,281),(1202,284),(1199,287),(1196,290),(1193,293),(1190,296),(1187,299),(1184,302),(1181,305),(1178,308),(1175,311),(1172,314),(1169,317),(1166,320),(1163,323),(1160,326),(1157,329),(1154,332),(1151,335),(1148,338),(1145,341),(1142,344),(1139,347),(1136,350),(1133,353),(1130,356),(1127,359),(1124,362),(1121,365),(1118,368),(1115,371),(1112,374),(1109,377),(1106,380),(1103,383),(1100,386),(1097,389),(1094,392),(1091,395),(1088,398),(1085,401),(1082,404),(1079,407),(1076,410),(1073,413),(1070,416),(1067,419),(1064,422),(1061,425),(1058,428),(1055,431),(1052,434),(1049,437),(1046,440),(1043,443),(1040,446),(1037,449),(1034,452),(1031,455),(1028,458),(1025,461),(1022,464),(1019,467),(1016,470),(1013,473),(1010,476),(1007,479),(1004,482),(1001,485),(998,488),(995,491),(992,494),(989,497)]
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

        if self.x == 989 and self.y == 497:
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