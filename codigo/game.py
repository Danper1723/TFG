import pygame
import os
import sqlite3

#IMPORTA IMAGENES DE LOS MINIONS DE TOP
    #ALIADOS
from minions.top.bueno.img_minion_bueno_top_1 import Img_minion_bueno_top_1
from minions.top.bueno.img_minion_bueno_top_2 import Img_minion_bueno_top_2
from minions.top.bueno.img_minion_bueno_top_3 import Img_minion_bueno_top_3

    #ENEMIGOS
from minions.top.malo.img_minion_malo_top_1 import Img_minion_malo_top_1
from minions.top.malo.img_minion_malo_top_2 import Img_minion_malo_top_2
from minions.top.malo.img_minion_malo_top_3 import Img_minion_malo_top_3

#IMPORTA IMAGENES DE LOS MINIONS DE MID
    #ALIADOS
from minions.mid.bueno.img_minion_bueno_mid_1 import Img_minion_bueno_mid_1
from minions.mid.bueno.img_minion_bueno_mid_2 import Img_minion_bueno_mid_2
from minions.mid.bueno.img_minion_bueno_mid_3 import Img_minion_bueno_mid_3

    #ENEMIGOS
from minions.mid.malo.img_minion_malo_mid_1 import Img_minion_malo_mid_1
from minions.mid.malo.img_minion_malo_mid_2 import Img_minion_malo_mid_2
from minions.mid.malo.img_minion_malo_mid_3 import Img_minion_malo_mid_3

#IMPORTA IMAGENES DE LOS MINIONS DE BOT
    #ALIADOS
from minions.bot.bueno.img_minion_bueno_bot_1 import Img_minion_bueno_bot_1
from minions.bot.bueno.img_minion_bueno_bot_2 import Img_minion_bueno_bot_2
from minions.bot.bueno.img_minion_bueno_bot_3 import Img_minion_bueno_bot_3

    #ENEMIGOS
from minions.bot.malo.img_minion_malo_bot_1 import Img_minion_malo_bot_1
from minions.bot.malo.img_minion_malo_bot_2 import Img_minion_malo_bot_2
from minions.bot.malo.img_minion_malo_bot_3 import Img_minion_malo_bot_3


from sonidos.sonidos import Sonidos

from torres.img_torre_top_1 import Img_torre_top_1


class Game:
    def __init__(self):

        self.width = 1920  # TAMAÑO DE LA VENTANA
        self.height = 1080  # TAMAÑO DE LA VENTANA
        self.win = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)  # ESTA LINEA HACE QUE SE VEA EN PANTALLA COMPLETA
        self.torres = [Img_torre_top_1()]
        self.subdito = [
                        #TOP
                        Img_minion_bueno_top_1(), Img_minion_bueno_top_2(), Img_minion_bueno_top_3(),
                        Img_minion_malo_top_1(), Img_minion_malo_top_2(),Img_minion_malo_top_3(),
                        #MID
                        Img_minion_bueno_mid_1(), Img_minion_bueno_mid_2(), Img_minion_bueno_mid_3(),
                        Img_minion_malo_mid_1(), Img_minion_malo_mid_2(), Img_minion_malo_mid_3(),
                        #BOT
                        Img_minion_bueno_bot_1(), Img_minion_bueno_bot_2(), Img_minion_bueno_bot_3(),
                        Img_minion_malo_bot_1(), Img_minion_malo_bot_2(), Img_minion_malo_bot_3()
                        ]
        self.dinero = 100

        self.background = pygame.image.load(os.path.join("..", "imagenes", "Guia.png"))  # INDICA LA RUTA DE LA IMAGEN, PRIMERAS COMILLAS LA CARPETA Y LAS SEGUNDAS EL ARCHIVO
        # self.background = pygame.transform.scale(self.background,(self.width,self.height)) #ESTA SENTENCIA HARA QUE LA IMAGEN DE FONDO SE ESCALE AL TAMAÑO DE LA VENTANA, DE MOMENTO NO ES NECESARIO LO DEJAMOS COMO ANOTACION POR SI ACASO
        self.clicks = []

        # TOP
        self.torre_top_1_derecha = None
        self.dib_torre_top_1_derecha_viva = None
        self.dib_torre_top_1_derecha_nada = None
        self.dib_torre_top_1_derecha_rota = None
        self.cont_torre_top_1_derecha = 0
        # -----
        self.torre_top_2_derecha = None
        self.dib_torre_top_2_derecha_viva = None
        self.dib_torre_top_2_derecha_nada = None
        self.dib_torre_top_2_derecha_rota = None
        self.cont_torre_top_2_derecha = 0
        # -----
        self.torre_top_1_izquierda = None
        self.dib_torre_top_1_izquierda_viva = None
        self.dib_torre_top_1_izquierda_nada = None
        self.dib_torre_top_1_izquierda_rota = None
        self.cont_torre_top_1_izquierda = 0
        self.cont = 0
        self.dibT = None
        # -----
        self.torre_top_2_izquierda = None
        self.dib_torre_top_2_izquierda_viva = None
        self.dib_torre_top_2_izquierda_nada = None
        self.dib_torre_top_2_izquierda_rota = None
        self.cont_torre_top_2_izquierda = 0
        # MID
        # BOT

        self.cont = 0
        self.dibT = None

    def run(self):
        run = True
        clock = pygame.time.Clock()

        # -----------------------------
        self.b = Sonidos()
        self.b.backgroundPlay()
        # -----------------------------

        conexion = sqlite3.connect('../prueba.db')
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM torres')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_top_1_derecha", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_top_2_derecha", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_top_1_izquierda", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_top_2_izquierda", 1)')
        conexion.commit()

        cursor.execute('INSERT INTO torres VALUES("torre_mid_1_derecha", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_mid_2_derecha", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_mid_1_izquierda", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_mid_2_izquierda", 1)')
        conexion.commit()

        cursor.execute('INSERT INTO torres VALUES("torre_bot_1_derecha", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_bot_2_derecha", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_bot_1_izquierda", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_bot_2_izquierda", 1)')
        conexion.commit()
        conexion.close()

        while run:
            #self.torres()

            # pygame.time.delay(50)
            pygame.time.delay(25)
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    # self.clicks.append(pos)
                    # print(self.clicks)#IMPRIME POR CONSOLA LA LISTA DE CORDENADAS PULSADAS

                # bucle que lanza enemigos
                to_del = []

                for en in self.subdito:
                    if en.x < -5:
                        to_del.append(en)
                # bucle que elimina enemigos de la pantalla
                for d in to_del:
                    self.subdito.remove(d)

            #for min in self.torres:
                #min.draw(self.win)

            self.draw()
        pygame.quit()

    def draw(self):

        self.win.blit(self.background, (0, 0))
#Torres TOP-------------------------------------------------------------------------------------------------------------

        conexion = sqlite3.connect('../prueba.db')
        cursor = conexion.cursor()

        self.cont = self.cont + 1

        # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_1_derecha
        cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_1_derecha"')
        resul = cursor.fetchall()
        for r in resul:
            self.torre_top_1_derecha = r[0]
        print(self.torre_top_1_derecha)
        # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_2_derecha
        cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_2_derecha"')
        resul = cursor.fetchall()
        for r in resul:
            self.torre_top_2_derecha = r[0]
        print(self.torre_top_2_derecha)
        # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_1_izquierda
        cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_1_izquierda"')
        resul = cursor.fetchall()
        for r in resul:
            self.torre_top_1_izquierda = r[0]
        print(self.torre_top_1_izquierda)
        # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_2_izquierda
        cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_2_izquierda"')
        resul = cursor.fetchall()
        for r in resul:
            self.torre_top_2_izquierda = r[0]
        print(self.torre_top_2_izquierda)
        # conexion.close()#ESTO HAY QUE DES-COMENTARLO

        # --------ESTO TIENE QUE IR FUERA
        if self.cont == 50:
            cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_1_derecha"')
            conexion.commit()
            cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_2_derecha"')
            conexion.commit()
            cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_1_izquierda"')
            conexion.commit()
            cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_2_izquierda"')
            conexion.commit()
        conexion.close()
        # -----------
        # self.torreta = self.torres[0].viva # tiene que ser el estado actuial de CADA torre
        # TOP
        if self.torre_top_1_derecha and not self.cont_torre_top_1_derecha:
            self.dib_torre_top_1_derecha_viva = pygame.image.load("../torres/torres/torre_viva.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_derecha_viva, (770, 5))
            self.cont_torre_top_1_derecha = self.cont_torre_top_1_derecha + 1
        elif not self.torre_top_1_derecha and self.cont_torre_top_1_derecha:
            self.dib_torre_top_1_derecha_nada = pygame.image.load(
                "../torres/torres/torre_top_derecha_1_vacia.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_derecha_nada, (770, 9))
            self.dib_torre_top_1_derecha_rota = pygame.image.load("../torres/torres/torre_rota.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_derecha_rota, (770, 5))
            self.cont_torre_top_1_derecha = self.cont_torre_top_1_derecha + 1

        if self.torre_top_2_derecha and not self.cont_torre_top_2_derecha:
            self.dib_torre_top_2_derecha_viva = pygame.image.load("../torres/torres/torre_viva.png").convert_alpha()
            self.background.blit(self.dib_torre_top_2_derecha_viva, (1120, 5))
            self.cont_torre_top_2_derecha = self.cont_torre_top_2_derecha + 1
        elif not self.torre_top_2_derecha and self.cont_torre_top_2_derecha:
            self.dib_torre_top_2_derecha_nada = pygame.image.load(
                "../torres/torres/torre_top_derecha_2_vacia.png").convert_alpha()
            self.background.blit(self.dib_torre_top_2_derecha_nada, (1120, 15))
            self.dib_torre_top_2_derecha_rota = pygame.image.load("../torres/torres/torre_rota.png").convert_alpha()
            self.background.blit(self.dib_torre_top_2_derecha_rota, (1120, 5))
            self.cont_torre_top_2_derecha = self.cont_torre_top_2_derecha + 1

        if self.torre_top_1_izquierda and not self.cont_torre_top_1_izquierda:
            self.dib_torre_top_1_izquierda_viva = pygame.image.load("../torres/torres/torre_viva.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_izquierda_viva, (450, 350))
            self.cont_torre_top_1_izquierda = self.cont_torre_top_1_izquierda + 1
        elif not self.torre_top_1_izquierda and self.cont_torre_top_1_izquierda:
            self.dib_torre_top_1_izquierda_nada = pygame.image.load(
                "../torres/torres/torre_top_izquierda_1_vacia.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_izquierda_nada, (450, 350))
            self.dib_torre_top_1_izquierda_rota = pygame.image.load("../torres/torres/torre_rota.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_izquierda_rota, (450, 350))
            self.cont_torre_top_1_izquierda = self.cont_torre_top_1_izquierda + 1

        if self.torre_top_2_izquierda and not self.cont_torre_top_2_izquierda:
            self.dib_torre_top_2_izquierda_viva = pygame.image.load("../torres/torres/torre_viva.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_izquierda_viva, (450, 610))
            self.cont_torre_top_2_izquierda = self.cont_torre_top_2_izquierda + 1
        elif not self.torre_top_2_izquierda and self.cont_torre_top_2_izquierda:
            self.dib_torre_top_2_izquierda_nada = pygame.image.load(
                "../torres/torres/torre_top_izquierda_2_vacia.png").convert_alpha()
            self.background.blit(self.dib_torre_top_2_izquierda_nada, (450, 611))
            self.dib_torre_top_2_izquierda_rota = pygame.image.load("../torres/torres/torre_rota.png").convert_alpha()
            self.background.blit(self.dib_torre_top_2_izquierda_rota, (450, 610))
            self.cont_torre_top_2_izquierda = self.cont_torre_top_2_izquierda + 1

        # MID
        # BOT
#-----------------------------------------------------------------------------------------------------------------------
        """
        #FUNCION PARA ESCRIBIR POR CONSOLA COORDENADAS
        for p in self.clicks:
            pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0)#PARTE 1º= ¿? / PARTE 2º= Color RGB / Parte 3º=¿? / PARTE 4º= PRIMER NUMERO TAMAÑO DEL CIRCULO SEGUNDO NUMERO TAMAÑO DEL BORDE
        """

        for min in self.subdito:
            min.draw(self.win)

        for min in self.torres:
            min.draw(self.win)

        pygame.display.update()




g = Game()
g.run()
