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
        self.dibT = None
        self.background = pygame.image.load(os.path.join("..", "imagenes", "Guia.png"))  # INDICA LA RUTA DE LA IMAGEN, PRIMERAS COMILLAS LA CARPETA Y LAS SEGUNDAS EL ARCHIVO
        # self.background = pygame.transform.scale(self.background,(self.width,self.height)) #ESTA SENTENCIA HARA QUE LA IMAGEN DE FONDO SE ESCALE AL TAMAÑO DE LA VENTANA, DE MOMENTO NO ES NECESARIO LO DEJAMOS COMO ANOTACION POR SI ACASO
        self.clicks = []

        self.cont = 0
        self.torreta = None
        self.dib_torre_top_1_viva = None
        self.dib_torre_top_1_nada = None
        self.dib_torre_top_1_rota = None
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
        cursor.execute('INSERT INTO torres VALUES("torre_top_1", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_top_2", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_top_3", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_top_4", 1)')
        conexion.commit()

        cursor.execute('INSERT INTO torres VALUES("torre_mid_1", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_mid_2", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_mid_3", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_mid_4", 1)')
        conexion.commit()

        cursor.execute('INSERT INTO torres VALUES("torre_bot_1", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_bot_2", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_bot_3", 1)')
        conexion.commit()
        cursor.execute('INSERT INTO torres VALUES("torre_bot_4", 1)')
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

        cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_1"')
        resul = cursor.fetchall()

        if self.cont == 50:
            cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_1"')
            conexion.commit()
        for r in resul:
            self.torreta = r[0]
        print(self.torreta)
        conexion.close()
        # self.torreta = self.torres[0].viva # tiene que ser el estado actuial de CADA torre

        if self.torreta:
            self.dib_torre_top_1_viva = pygame.image.load("../torres/torres/torre_viva.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_viva, (770, 5))
        else:
            self.dib_torre_top_1_nada = pygame.image.load(
                "../torres/torres/torre_top_derecha_1_vacia.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_nada, (770, 9))
            self.dib_torre_top_1_rota = pygame.image.load("../torres/torres/torre_rota.png").convert_alpha()
            self.background.blit(self.dib_torre_top_1_rota, (770, 5))

        if self.torreta:
            self.dibT = pygame.image.load("../torres/torres/torre_viva.png")
        else:
            self.dibT = pygame.image.load("../torres/torres/torre_muerta.png")
        self.dibT = self.background.blit(self.dibT, (1120, 5))

        if self.torreta:
            self.dibT = pygame.image.load("../torres/torres/torre_viva.png")
        else:
            self.dibT = pygame.image.load("../torres/torres/torre_muerta.png")
        self.dibT = self.background.blit(self.dibT, (450, 350))

        if self.torreta:
            self.dibT = pygame.image.load("../torres/torres/torre_viva.png")
        else:
            self.dibT = pygame.image.load("../torres/torres/torre_muerta.png")
        self.dibT = self.background.blit(self.dibT, (450, 610))
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
