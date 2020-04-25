import pygame
import os
import sqlite3
import time #Tiempo
import threading #Tiempo

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

from pygame.constants import MOUSEBUTTONDOWN, K_ESCAPE, KEYDOWN, QUIT, RLEACCEL

pygame.init()
screen = pygame.display.set_mode((1024, 576))
pink = ((255,173,63))
magia = ((255,255,255))
COLOR_INACTIVE = (pink)
COLOR_ACTIVE = (magia)
FONT = pygame.font.Font(None, 32)

global nombre
nombre = ""
global correo
correo = ""
global cont
cont = 0
global validador
validador = 1
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False


    def handle_event(self, event):
        global nombre
        global correo
        global cont
        global validador
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if validador == 1:
                        print(self.text)
                        if cont == 0:
                            nombre = self.text
                            print(cont)
                            cont = 1
                        elif cont == 1:
                            correo = self.text
                            print(cont)
                            cont = 0
                            validador = 0
                        print(nombre)
                        print(correo)
                        self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)


    def update(self):
        # Resize the box if the text is too long.
        width = max(413, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



def cargar_imagen(nombre, transparente=False):
    try:
        imagen = pygame.image.load(nombre)

    except pygame.error as message:
        raise SystemExit(message)
    imagen = imagen.convert()
    if transparente:
        color = imagen.get_at((0, 0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen

def main():
    global nombre
    global correo

    conexion = sqlite3.connect('../datos.db')
    cursor = conexion.cursor()

    clock = pygame.time.Clock()
    input_box1 = InputBox(305, 179, 140, 34)
    input_box2 = InputBox(305, 309, 140, 34)
    input_boxes = [input_box1, input_box2]
    done = False


    while not done:

        fondo = cargar_imagen('imagenes/mainmenu.png')
        screen.blit(fondo, (0, 0))  # es para esto que nos sirvio poner en una
        # variable los datos de la pantalla
        pygame.display.flip()
        # screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(410, 405, 200, 57)
        if button_1.collidepoint((mx, my)):
            if click:
                if nombre != "" and correo != "":
                    cursor.execute('INSERT INTO usuarios values("' + nombre + '", "' + correo + '")')
                    conexion.commit()
                    conexion.close()
                game() #CAMBIO - Meter dentro del if de arriba del SQL

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        #screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)
            #pygame.draw.rect(screen, (0, 0, 0), button_1)

        pygame.display.flip()
        clock.tick(30)


def game():
    global segundosRonda  # Tiempo
    segundosRonda = 20
    global segundosPartida  # Tiempo
    segundosPartida = 0
    global minutosPartida  # Tiempo
    minutosPartida = 0

    class Game:

        def __init__(self):

            self.width = 1920  # TAMAÑO DE LA VENTANA
            self.height = 1080  # TAMAÑO DE LA VENTANA
            self.win = pygame.display.set_mode((self.width, self.height),
                                               pygame.FULLSCREEN)  # ESTA LINEA HACE QUE SE VEA EN PANTALLA COMPLETA
            self.torres = []
            self.subdito = [
                # TOP
                Img_minion_bueno_top_1(), Img_minion_bueno_top_2(), Img_minion_bueno_top_3(),
                Img_minion_malo_top_1(), Img_minion_malo_top_2(), Img_minion_malo_top_3(),
                # MID
                Img_minion_bueno_mid_1(), Img_minion_bueno_mid_2(), Img_minion_bueno_mid_3(),
                Img_minion_malo_mid_1(), Img_minion_malo_mid_2(), Img_minion_malo_mid_3(),
                # BOT
                Img_minion_bueno_bot_1(), Img_minion_bueno_bot_2(), Img_minion_bueno_bot_3(),
                Img_minion_malo_bot_1(), Img_minion_malo_bot_2(), Img_minion_malo_bot_3()
            ]
            self.dinero = 100

            self.background = pygame.image.load(os.path.join("..", "imagenes",
                                                             "Guia2.png"))  # INDICA LA RUTA DE LA IMAGEN, PRIMERAS COMILLAS LA CARPETA Y LAS SEGUNDAS EL ARCHIVO
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
            # -----
            self.torre_top_2_izquierda = None
            self.dib_torre_top_2_izquierda_viva = None
            self.dib_torre_top_2_izquierda_nada = None
            self.dib_torre_top_2_izquierda_rota = None
            self.cont_torre_top_2_izquierda = 0
            # MID
            # BOT
            self.torre_bot_1_derecha = None
            self.dib_torre_bot_1_derecha_viva = None
            self.dib_torre_bot_1_derecha_nada = None
            self.dib_torre_bot_1_derecha_rota = None
            self.cont_torre_bot_1_derecha = 0
            # -----
            self.torre_bot_2_derecha = None
            self.dib_torre_bot_2_derecha_viva = None
            self.dib_torre_bot_2_derecha_nada = None
            self.dib_torre_bot_2_derecha_rota = None
            self.cont_torre_bot_2_derecha = 0
            # -----
            self.torre_bot_1_izquierda = None
            self.dib_torre_bot_1_izquierda_viva = None
            self.dib_torre_bot_1_izquierda_nada = None
            self.dib_torre_bot_1_izquierda_rota = None
            self.cont_torre_bot_1_izquierda = 0
            # -----
            self.torre_bot_2_izquierda = None
            self.dib_torre_bot_2_izquierda_viva = None
            self.dib_torre_bot_2_izquierda_nada = None
            self.dib_torre_bot_2_izquierda_rota = None
            self.cont_torre_bot_2_izquierda = 0

            self.cont = 0
            self.dibT = None
            """# Tiempo
            self.segundosRonda = 0
            global segundosRonda # Tiempo
            segundosRonda = 0
            # ------"""

        def run(self):
            def cronoRonda():  # Tiempo funcion que sube 1 seg
                global segundosRonda
                segundosRonda = int(segundosRonda)
                if segundosRonda == 0:
                    segundosRonda = 20
                    return cronoRonda()
                else:
                    segundosRonda -= 1
                    time.sleep(1)
                    return cronoRonda()

            def cronoPartida():  # Tiempo funcion que sube 1 seg
                global segundosPartida
                segundosPartida = int(segundosPartida)
                global minutosPartida
                minutosPartida = int(minutosPartida)

                if segundosPartida == 59:
                    segundosPartida = -1
                    minutosPartida += 1
                    return cronoPartida()
                else:
                    segundosPartida += 1
                    time.sleep(1)
                    return cronoPartida()

            run = True
            clock = pygame.time.Clock()

            # -----------------------------
            self.b = Sonidos()
            self.b.backgroundPlay()
            # -----------------------------

            conexion = sqlite3.connect('../datos.db')
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

            pygame.font.init()  # Tiempo
            fuente = pygame.font.Font("../VT323-Regular.ttf", 55) #Tiempo

            hiloRonda = threading.Thread(target=cronoRonda, args=())  # Hilo que controla el tiempo de ronda
            hiloRonda.start()
            hiloPartida = threading.Thread(target=cronoPartida, args=())  # Hilo que controla el tiempo de ronda
            hiloPartida.start()
            while run:
                # self.torres()

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

                # for min in self.torres:
                # min.draw(self.win)

                # Tiempo
                # segundosRonda = self.segundosRonda
                global segundosRonda
                segundosRonda = str(segundosRonda)
                if int(segundosRonda) < 10:
                    sR = "0" + segundosRonda
                else:
                    sR = segundosRonda
                tRonda = fuente.render(sR, 0, (0, 0, 0))
                self.win.blit(tRonda, (1695, 745))

                global segundosPartida
                segundosPartida = str(segundosPartida)
                global minutosPartida
                minutosPartida = str(minutosPartida)
                if int(minutosPartida) < 10:
                    mP = "0" + minutosPartida
                else:
                    mP = minutosPartida
                if int(segundosPartida) < 10:
                    sP = "0" + segundosPartida
                else:
                    sP = segundosPartida
                temporizadorPartida = mP + ":" + sP
                tPartida = fuente.render(temporizadorPartida, 0, (0, 0, 0))
                self.win.blit(tPartida, (1665, 830))

                pygame.display.update()
                # ------

                self.draw()
            pygame.quit()

        def draw(self):
            if self.subdito[0].health >= 1:
                self.subdito[0].health = self.subdito[0].health - 1

            self.win.blit(self.background, (0, 0))

            conexion = sqlite3.connect('../datos.db')
            cursor = conexion.cursor()

            self.cont = self.cont + 1  # Esto sobra
            # Select TOP----------------------------------------------------------------------------------------------------
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
            # Select MID----------------------------------------------------------------------------------------------------
            # Select BOT----------------------------------------------------------------------------------------------------
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_1_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_1_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_1_derecha = r[0]
            print(self.torre_bot_1_derecha)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_2_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_2_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_2_derecha = r[0]
            print(self.torre_bot_2_derecha)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_1_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_1_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_1_izquierda = r[0]
            print(self.torre_bot_1_izquierda)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_2_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_2_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_2_izquierda = r[0]
            print(self.torre_bot_2_izquierda)
            #CAMBIO --------ESTO TIENE QUE IR FUERA---
            if self.cont == 50:
                cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_1_derecha"')
                conexion.commit()
                cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_2_derecha"')
                conexion.commit()
                cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_1_izquierda"')
                conexion.commit()
                cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_2_izquierda"')
                conexion.commit()
                cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_bot_1_derecha"')
                conexion.commit()
                cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_bot_2_derecha"')
                conexion.commit()
                cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_bot_1_izquierda"')
                conexion.commit()
                cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_bot_2_izquierda"')
                conexion.commit()
            conexion.close()
            # -----------
            # conexion.close()#CAMBIO - ESTO HAY QUE DES-COMENTARLO
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
                self.dib_torre_top_1_izquierda_viva = pygame.image.load(
                    "../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_top_1_izquierda_viva, (450, 350))
                self.cont_torre_top_1_izquierda = self.cont_torre_top_1_izquierda + 1
            elif not self.torre_top_1_izquierda and self.cont_torre_top_1_izquierda:
                self.dib_torre_top_1_izquierda_nada = pygame.image.load(
                    "../torres/torres/torre_top_izquierda_1_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_top_1_izquierda_nada, (450, 350))
                self.dib_torre_top_1_izquierda_rota = pygame.image.load(
                    "../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_top_1_izquierda_rota, (450, 350))
                self.cont_torre_top_1_izquierda = self.cont_torre_top_1_izquierda + 1

            if self.torre_top_2_izquierda and not self.cont_torre_top_2_izquierda:
                self.dib_torre_top_2_izquierda_viva = pygame.image.load(
                    "../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_top_1_izquierda_viva, (450, 610))
                self.cont_torre_top_2_izquierda = self.cont_torre_top_2_izquierda + 1
            elif not self.torre_top_2_izquierda and self.cont_torre_top_2_izquierda:
                self.dib_torre_top_2_izquierda_nada = pygame.image.load(
                    "../torres/torres/torre_top_izquierda_2_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_top_2_izquierda_nada, (450, 611))
                self.dib_torre_top_2_izquierda_rota = pygame.image.load(
                    "../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_top_2_izquierda_rota, (450, 610))
                self.cont_torre_top_2_izquierda = self.cont_torre_top_2_izquierda + 1

            # MID
            # BOT
            if self.torre_bot_1_derecha and not self.cont_torre_bot_1_derecha:
                self.dib_torre_bot_1_derecha_viva = pygame.image.load("../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_1_derecha_viva, (1435, 610))
                self.cont_torre_bot_1_derecha = self.cont_torre_bot_1_derecha + 1
            elif not self.torre_bot_1_derecha and self.cont_torre_bot_1_derecha:
                self.dib_torre_bot_1_derecha_nada = pygame.image.load(
                    "../torres/torres/torre_bot_derecha_1_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_1_derecha_nada, (1435, 616))
                self.dib_torre_bot_1_derecha_rota = pygame.image.load("../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_1_derecha_rota, (1435, 610))
                self.cont_torre_bot_1_derecha = self.cont_torre_bot_1_derecha + 1

            if self.torre_bot_2_derecha and not self.cont_torre_bot_2_derecha:
                self.dib_torre_bot_2_derecha_viva = pygame.image.load("../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_1_derecha_viva, (1435, 290))
                self.cont_torre_bot_2_derecha = self.cont_torre_bot_2_derecha + 1
            elif not self.torre_bot_2_derecha and self.cont_torre_bot_2_derecha:
                self.dib_torre_bot_2_derecha_nada = pygame.image.load(
                    "../torres/torres/torre_bot_derecha_2_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_2_derecha_nada, (1435, 295))
                self.dib_torre_bot_2_derecha_rota = pygame.image.load("../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_2_derecha_rota, (1435, 290))
                self.cont_torre_bot_2_derecha = self.cont_torre_bot_2_derecha + 1

            if self.torre_bot_1_izquierda and not self.cont_torre_bot_1_izquierda:
                self.dib_torre_bot_1_izquierda_viva = pygame.image.load(
                    "../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_1_izquierda_viva, (1089, 740))
                self.cont_torre_bot_1_izquierda = self.cont_torre_bot_1_izquierda + 1
            elif not self.torre_bot_1_izquierda and self.cont_torre_bot_1_izquierda:
                self.dib_torre_bot_1_izquierda_nada = pygame.image.load(
                    "../torres/torres/torre_bot_izquierda_1_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_1_izquierda_nada, (1089, 747))
                self.dib_torre_bot_1_izquierda_rota = pygame.image.load(
                    "../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_1_izquierda_rota, (1089, 740))
                self.cont_torre_bot_1_izquierda = self.cont_torre_bot_1_izquierda + 1

            if self.torre_bot_2_izquierda and not self.cont_torre_bot_2_izquierda:
                self.dib_torre_bot_2_izquierda_viva = pygame.image.load(
                    "../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_2_izquierda_viva, (801, 740))
                self.cont_torre_bot_2_izquierda = self.cont_torre_bot_2_izquierda + 1
            elif not self.torre_bot_2_izquierda and self.cont_torre_bot_2_izquierda:
                self.dib_torre_bot_2_izquierda_nada = pygame.image.load(
                    "../torres/torres/torre_bot_izquierda_2_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_2_izquierda_nada, (801, 751))
                self.dib_torre_bot_2_izquierda_rota = pygame.image.load(
                    "../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_bot_2_izquierda_rota, (801, 740))
                self.cont_torre_bot_2_izquierda = self.cont_torre_bot_2_izquierda + 1

            # -----------------------------------------------------------------------------------------------------------------------
            """
            #FUNCION PARA ESCRIBIR POR CONSOLA COORDENADAS
            for p in self.clicks:
                pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0)#PARTE 1º= ¿? / PARTE 2º= Color RGB / Parte 3º=¿? / PARTE 4º= PRIMER NUMERO TAMAÑO DEL CIRCULO SEGUNDO NUMERO TAMAÑO DEL BORDE
            """

            for min in self.subdito:
                min.draw(self.win)

            for min in self.torres:
                min.draw(self.win)

            # pygame.display.update() Este update esta ahora en donde se pinta el tiempo

    g = Game()
    g.run()

if __name__ == '__main__':
    main()
    pygame.quit()

