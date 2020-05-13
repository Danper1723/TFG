import pygame
import os
import sqlite3
import time  # Tiempo
import threading  # Tiempo
import random  # Numeros aleatorios

# IMPORTA IMAGENES DE LOS MINIONS DE TOP
# ALIADOS
from minions.top.bueno.img_minion_bueno_top_1 import Img_minion_bueno_top_1
from minions.top.bueno.img_minion_bueno_top_2 import Img_minion_bueno_top_2
from minions.top.bueno.img_minion_bueno_top_3 import Img_minion_bueno_top_3

# ENEMIGOS
from minions.top.malo.img_minion_malo_top_1 import Img_minion_malo_top_1
from minions.top.malo.img_minion_malo_top_2 import Img_minion_malo_top_2
from minions.top.malo.img_minion_malo_top_3 import Img_minion_malo_top_3

# IMPORTA IMAGENES DE LOS MINIONS DE MID
# ALIADOS
from minions.mid.bueno.img_minion_bueno_mid_1 import Img_minion_bueno_mid_1
from minions.mid.bueno.img_minion_bueno_mid_2 import Img_minion_bueno_mid_2
from minions.mid.bueno.img_minion_bueno_mid_3 import Img_minion_bueno_mid_3

# ENEMIGOS
from minions.mid.malo.img_minion_malo_mid_1 import Img_minion_malo_mid_1
from minions.mid.malo.img_minion_malo_mid_2 import Img_minion_malo_mid_2
from minions.mid.malo.img_minion_malo_mid_3 import Img_minion_malo_mid_3

# IMPORTA IMAGENES DE LOS MINIONS DE BOT
# ALIADOS
from minions.bot.bueno.img_minion_bueno_bot_1 import Img_minion_bueno_bot_1
from minions.bot.bueno.img_minion_bueno_bot_2 import Img_minion_bueno_bot_2
from minions.bot.bueno.img_minion_bueno_bot_3 import Img_minion_bueno_bot_3

# ENEMIGOS
from minions.bot.malo.img_minion_malo_bot_1 import Img_minion_malo_bot_1
from minions.bot.malo.img_minion_malo_bot_2 import Img_minion_malo_bot_2
from minions.bot.malo.img_minion_malo_bot_3 import Img_minion_malo_bot_3

# IMPORTAR ACCIONES DE TORRES DE TOP
# DERECHA
from torres.top.accion_torre_top_1_derecha import Accion_torre_top_1_derecha
from torres.top.accion_torre_top_2_derecha import Accion_torre_top_2_derecha
# IZQUIERDA
from torres.top.accion_torre_top_1_izquierda import Accion_torre_top_1_izquierda
from torres.top.accion_torre_top_2_izquierda import Accion_torre_top_2_izquierda
# IMPORTAR ACCIONES DE TORRES DE MID
# DERECHA
from torres.mid.accion_torre_mid_1_derecha import Accion_torre_mid_1_derecha
from torres.mid.accion_torre_mid_2_derecha import Accion_torre_mid_2_derecha
# IZQUIERDA
from torres.mid.accion_torre_mid_1_izquierda import Accion_torre_mid_1_izquierda
from torres.mid.accion_torre_mid_2_izquierda import Accion_torre_mid_2_izquierda
# IMPORTAR ACCIONES DE TORRES DE BOT
# DERECHA
from torres.bot.accion_torre_bot_1_derecha import Accion_torre_bot_1_derecha
from torres.bot.accion_torre_bot_2_derecha import Accion_torre_bot_2_derecha
# IZQUIERDA
from torres.bot.accion_torre_bot_1_izquierda import Accion_torre_bot_1_izquierda
from torres.bot.accion_torre_bot_2_izquierda import Accion_torre_bot_2_izquierda

#IMPORTAR LOS HEROES
from heroes.Mrcalabaza.img_calabaza import Img_calabaza

from sonidos.sonidos import Sonidos

from pygame.constants import MOUSEBUTTONDOWN, K_ESCAPE, KEYDOWN, QUIT, RLEACCEL

pygame.init()
screen = pygame.display.set_mode((1024, 576))
pink = ((255, 173, 63))
magia = ((255, 255, 255))
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
        width = max(413, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
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
                game()  # CAMBIO - Meter dentro del if de arriba del SQL

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

        # screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)
            # pygame.draw.rect(screen, (0, 0, 0), button_1)

        pygame.display.flip()
        clock.tick(30)


def game():
    global segundosRonda  # Tiempo
    segundosRonda = 20
    segundosRonda = 5
    global segundosPartida  # Tiempo
    segundosPartida = 0
    global minutosPartida  # Tiempo
    minutosPartida = 0

    #

    class Game:

        def __init__(self):

            self.width = 1920  # TAMAÑO DE LA VENTANA
            self.height = 1080  # TAMAÑO DE LA VENTANA
            self.win = pygame.display.set_mode((self.width, self.height),
                                               pygame.FULLSCREEN)  # ESTA LINEA HACE QUE SE VEA EN PANTALLA COMPLETA
            self.torres = [
                # TOP
                Accion_torre_top_1_derecha(), Accion_torre_top_2_derecha(), Accion_torre_top_1_izquierda(),
                Accion_torre_top_2_izquierda(),
                # MID
                Accion_torre_mid_1_derecha(), Accion_torre_mid_2_derecha(), Accion_torre_mid_1_izquierda(),
                Accion_torre_mid_2_izquierda(),
                # BOT
                Accion_torre_bot_1_derecha(), Accion_torre_bot_2_derecha(), Accion_torre_bot_1_izquierda(),
                Accion_torre_bot_2_izquierda()
            ]
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
            self.heroe = [
                Img_calabaza()
            ]
            self.villano = [

            ]
            self.dinero = 100

            self.background = pygame.image.load(os.path.join("..", "imagenes",
                                                             "Guia.png"))  # INDICA LA RUTA DE LA IMAGEN, PRIMERAS COMILLAS LA CARPETA Y LAS SEGUNDAS EL ARCHIVO
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
            self.torre_mid_1_derecha = None
            self.dib_torre_mid_1_derecha_viva = None
            self.dib_torre_mid_1_derecha_nada = None
            self.dib_torre_mid_1_derecha_rota = None
            self.cont_torre_mid_1_derecha = 0
            # -----
            self.torre_mid_2_derecha = None
            self.dib_torre_mid_2_derecha_viva = None
            self.dib_torre_mid_2_derecha_nada = None
            self.dib_torre_mid_2_derecha_rota = None
            self.cont_torre_mid_2_derecha = 0
            # -----
            self.torre_mid_1_izquierda = None
            self.dib_torre_mid_1_izquierda_viva = None
            self.dib_torre_mid_1_izquierda_nada = None
            self.dib_torre_mid_1_izquierda_rota = None
            self.cont_torre_mid_1_izquierda = 0
            # -----
            self.torre_mid_2_izquierda = None
            self.dib_torre_mid_2_izquierda_viva = None
            self.dib_torre_mid_2_izquierda_nada = None
            self.dib_torre_mid_2_izquierda_rota = None
            self.cont_torre_mid_2_izquierda = 0
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
            #PELEAS
            self.buenosTop = 300
            self.malosTop = 300
            self.buenosMid = 300
            self.malosMid = 300
            self.buenosBot = 300
            self.malosBot = 300

            self.peleaTop = 0
            self.peleaMid = 0
            self.peleaBot = 0

            #COLISIONES
            self.reset_cont = 1
                # Mr.Calbaza
            self.bCalColTop = False
            self.bCalColMid = False
            self.bCalColBot = False

            self.cont_top = 0
            self.cont_mid = 0
            self.cont_bot = 0

        def run(self):
            def cronoRonda():  # Tiempo funcion que sube 1 seg
                global segundosRonda
                segundosRonda = int(segundosRonda)
                if segundosRonda == 0:
                    for sub in self.subdito:
                        sub.estado_partida()
                    for her in self.heroe:
                        her.estado_partida()
                    if self.subdito[15].estado:
                        segundosRonda = 60
                        self.reset_cont = 1
                    else:
                        if self.reset_cont:
                            self.bCalColTop = False
                            self.bCalColMid = False
                            self.bCalColBot = False


                            self.cont_top = 0
                            self.cont_mid = 0
                            self.cont_bot = 0
                            self.reset_cont = 0
                        segundosRonda = 20
                        segundosRonda = 5
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
            fuente = pygame.font.Font("../VT323-Regular.ttf", 55)  # Tiempo
            fuenteHealth = pygame.font.Font("../VT323-Regular.ttf", 30) # Vida personajes

            hiloRonda = threading.Thread(target=cronoRonda, args=())  # Hilo que controla el tiempo de ronda
            hiloRonda.start()
            hiloPartida = threading.Thread(target=cronoPartida, args=())  # Hilo que controla el tiempo de ronda
            hiloPartida.start()

            # Variables para arrastrar a Mr.Clabaza
            mCalabazaRect = pygame.rect.Rect(317, 189, 32, 32)
            mCalabazaImg = pygame.image.load(os.path.join("..", "heroes/imagenes/Mr.calabaza/", "calabaza.png"))  # Carga imagen grande mr.Calabaza
            rectangle_draging_Mcalabaza = False

            # Zona de colision top
            rectColTop = pygame.rect.Rect(482, 635, 100, 100)
            colisionTopImg = pygame.image.load(os.path.join("..", "imagenes/", "portal_top.png"))  # Carga imagen zona de colision top

            # Zona de colision mid
            rectColMid = pygame.rect.Rect(575, 643, 100, 100)
            colisionMidImg = pygame.image.load(os.path.join("..", "imagenes/", "portal_mid.png"))  # Carga imagen zona de colision mid

            # Zona de colision bot
            rectColBot = pygame.rect.Rect(625, 865, 157, 91)
            colisionBotImg = pygame.image.load(os.path.join("..", "imagenes/", "portal_bot.png"))  # Carga imagen zona de colision bot

            # ---Terminan las variables de arrastrar heroes
            while run:
                # Mover a Mr.Calabaza
                if not self.subdito[15].estado:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if mCalabazaRect.collidepoint(event.pos):
                                    rectangle_draging_Mcalabaza = True
                                    mouse_x, mouse_y = event.pos
                                    offset_x = mCalabazaRect.x - mouse_x
                                    offset_y = mCalabazaRect.y - mouse_y
                        elif event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:
                                print("aqui")
                                rectangle_draging_Mcalabaza = False
                        elif event.type == pygame.MOUSEMOTION:
                            if rectangle_draging_Mcalabaza:
                                print("esto no falla->", event.pos)
                                mouse_x, mouse_y = event.pos
                                mCalabazaRect.x = mouse_x + offset_x
                                mCalabazaRect.y = mouse_y + offset_y

                if self.subdito[15].estado:
                    mCalabazaRect = pygame.rect.Rect(317, 189, 32, 32)  # Crear el rect de Mr.Calabaza
                    rectCal = pygame.draw.rect(self.win, (255, 255, 255), mCalabazaRect, -1)  # Rect que envuelve a Mr.Calabaza

                else:
                    rectCal = pygame.draw.rect(self.win, (255, 255, 255), mCalabazaRect, -1)  # Rect que envuelve a Mr.Calabaza

                    # Zonas de colisiones
                    self.win.blit(colisionTopImg, rectColTop)  # Dibuja el sprite de colision top con su rect
                    self.win.blit(colisionMidImg, rectColMid)  # Dibuja el sprite de colision mid con su rect
                    self.win.blit(colisionBotImg, rectColBot)  # Dibuja el sprite de colision bot con su rect

                # Heroes para arrastrar
                self.win.blit(mCalabazaImg, rectCal)  # Dibujar el sprite grande de Mr.Calabaza con su rect

                # Colisiones de Mr.Calabaza
                if not self.bCalColTop:
                    if rectCal.colliderect(rectColTop):  # Colision con rect en top
                        if self.cont_top <= 2:
                            self.cont_top += 1
                            self.heroe[0].posicion = self.cont_top
                            #self.heroe[0].posicion = 2#
                            self.heroe[0].linea = "top"
                            self.bCalColTop = True

                if not self.bCalColMid:
                    if rectCal.colliderect(rectColMid):  # Colision con rect en mid
                        if self.cont_mid <= 2:
                            self.cont_mid += 1
                            self.heroe[0].posicion = self.cont_mid
                            #self.heroe[0].posicion = 2#
                            self.heroe[0].linea = "mid"
                            self.bCalColMid = True

                if not self.bCalColBot:
                    if rectCal.colliderect(rectColBot):  # Colision con rect en bot
                        if self.cont_bot <= 2:
                            self.cont_bot += 1
                            self.heroe[0].posicion = self.cont_bot
                            #self.heroe[0].posicion = 2#
                            self.heroe[0].linea = "bot"
                            self.bCalColBot = True



                # ----Se acaba mover heroes a las lineas

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
                    # for d in to_del:
                        # self.subdito.remove(d)

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

                # Dibujar vida minions
                    # Buneos TOP
                vidaBT1 = str(self.subdito[0].health)  # 2º
                if int(vidaBT1) < 10:
                    vidaBT1 = "00" + str(vidaBT1)
                elif int(vidaBT1) < 100:
                    vidaBT1 = "0" + str(vidaBT1)
                healthBt1 = fuenteHealth.render(vidaBT1, 0, (0, 0, 0))
                self.win.blit(healthBt1, (110, 207))

                vidaBT2 = str(self.subdito[1].health)  # 1º
                if int(vidaBT2) < 10:
                    vidaBT2 = "00" + str(vidaBT2)
                elif int(vidaBT2) < 100:
                    vidaBT2 = "0" + str(vidaBT2)
                healthBt2 = fuenteHealth.render(vidaBT2, 0, (0, 0, 0))
                self.win.blit(healthBt2, (110, 172))

                vidaBT3 = str(self.subdito[2].health)  # 3º
                if int(vidaBT3) < 10:
                    vidaBT3 = "00" + str(vidaBT3)
                elif int(vidaBT3) < 100:
                    vidaBT3 = "0" + str(vidaBT3)
                healthBt3 = fuenteHealth.render(vidaBT3, 0, (0, 0, 0))
                self.win.blit(healthBt3, (110, 242))
                    # Buenos MID
                vidaBM1 = str(self.subdito[6].health)  # 2º
                if int(vidaBM1) < 10:
                    vidaBM1 = "00" + str(vidaBM1)
                elif int(vidaBM1) < 100:
                    vidaBM1 = "0" + str(vidaBM1)
                healthBm1 = fuenteHealth.render(vidaBM1, 0, (0, 0, 0))
                self.win.blit(healthBm1, (110, 394))

                vidaBM2 = str(self.subdito[7].health)  # 1º
                if int(vidaBM2) < 10:
                    vidaBM2 = "00" + str(vidaBM2)
                elif int(vidaBM2) < 100:
                    vidaBM2 = "0" + str(vidaBM2)
                healthBm2 = fuenteHealth.render(vidaBM2, 0, (0, 0, 0))
                self.win.blit(healthBm2, (110, 359))

                vidaBM3 = str(self.subdito[8].health)  # 3º
                if int(vidaBM3) < 10:
                    vidaBM3 = "00" + str(vidaBM3)
                elif int(vidaBM3) < 100:
                    vidaBM3 = "0" + str(vidaBM3)
                healthBm3 = fuenteHealth.render(vidaBM3, 0, (0, 0, 0))
                self.win.blit(healthBm3, (110, 429))
                    # Buenos BOT
                vidaBB1 = str(self.subdito[12].health)  # 2º
                if int(vidaBB1) < 10:
                    vidaBB1 = "00" + str(vidaBB1)
                elif int(vidaBB1) < 100:
                    vidaBB1 = "0" + str(vidaBB1)
                healthBb1 = fuenteHealth.render(vidaBB1, 0, (0, 0, 0))
                self.win.blit(healthBb1, (110, 582))

                vidaBB2 = str(self.subdito[13].health)  # 1º
                if int(vidaBB2) < 10:
                    vidaBB2 = "00" + str(vidaBB2)
                elif int(vidaBB2) < 100:
                    vidaBB2 = "0" + str(vidaBB2)
                healthBb2 = fuenteHealth.render(vidaBB2, 0, (0, 0, 0))
                self.win.blit(healthBb2, (110, 547))

                vidaBB3 = str(self.subdito[14].health)  # 3º
                if int(vidaBB3) < 10:
                    vidaBB3 = "00" + str(vidaBB3)
                elif int(vidaBB3) < 100:
                    vidaBB3 = "0" + str(vidaBB3)
                healthBb3 = fuenteHealth.render(vidaBB3, 0, (0, 0, 0))
                self.win.blit(healthBb3, (110, 617))

                pygame.display.update()#Este es el update general NO SE TOCA

                # ------

                self.draw()
            pygame.quit()

        def draw(self):

            self.win.blit(self.background, (0, 0))

            conexion = sqlite3.connect('../datos.db')
            cursor = conexion.cursor()

            self.cont = self.cont + 1  # Esto sobra
            # Select TOP------------------------------------------------------------------------------------------------
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_1_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_1_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_top_1_derecha = r[0]
            # print(self.torre_top_1_derecha)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_2_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_2_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_top_2_derecha = r[0]
            # print(self.torre_top_2_derecha)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_1_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_1_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_top_1_izquierda = r[0]
            # print(self.torre_top_1_izquierda)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_2_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_top_2_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_top_2_izquierda = r[0]
            # print(self.torre_top_2_izquierda)
            # Select MID------------------------------------------------------------------------------------------------
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_mid_1_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_mid_1_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_mid_1_derecha = r[0]
            # print(self.torre_mid_1_derecha)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_mid_2_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_mid_2_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_mid_2_derecha = r[0]
            # print(self.torre_mid_2_derecha)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_mid_1_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_mid_1_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_mid_1_izquierda = r[0]
            # print(self.torre_mid_1_izquierda)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_top_2_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_mid_2_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_mid_2_izquierda = r[0]
            # print(self.torre_mid_2_izquierda)
            # Select BOT------------------------------------------------------------------------------------------------
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_1_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_1_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_1_derecha = r[0]
            # print(self.torre_bot_1_derecha)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_2_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_2_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_2_derecha = r[0]
            # print(self.torre_bot_2_derecha)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_1_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_1_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_1_izquierda = r[0]
            # print(self.torre_bot_1_izquierda)
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_2_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_2_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_2_izquierda = r[0]
            # print(self.torre_bot_2_izquierda)
            conexion.close()
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
            if self.torre_mid_1_derecha and not self.cont_torre_mid_1_derecha:
                self.dib_torre_mid_1_derecha_viva = pygame.image.load("../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_1_derecha_viva, (985, 350))
                self.cont_torre_mid_1_derecha = self.cont_torre_mid_1_derecha + 1
            elif not self.torre_mid_1_derecha and self.cont_torre_mid_1_derecha:
                self.dib_torre_mid_1_derecha_nada = pygame.image.load(
                    "../torres/torres/torre_mid_derecha_1_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_1_derecha_nada, (985, 351))
                self.dib_torre_mid_1_derecha_rota = pygame.image.load("../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_1_derecha_rota, (985, 350))
                self.cont_torre_mid_1_derecha = self.cont_torre_mid_1_derecha + 1

            if self.torre_mid_2_derecha and not self.cont_torre_mid_2_derecha:
                self.dib_torre_mid_2_derecha_viva = pygame.image.load(
                    "../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_2_derecha_viva, (1150, 195))
                self.cont_torre_mid_2_derecha = self.cont_torre_mid_2_derecha + 1
            elif not self.torre_mid_2_derecha and self.cont_torre_mid_2_derecha:
                self.dib_torre_mid_2_derecha_nada = pygame.image.load(
                    "../torres/torres/torre_mid_derecha_2_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_2_derecha_nada, (1150, 209))
                self.dib_torre_mid_2_derecha_rota = pygame.image.load(
                    "../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_2_derecha_rota, (1150, 195))
                self.cont_torre_mid_2_derecha = self.cont_torre_mid_2_derecha + 1

            if self.torre_mid_1_izquierda and not self.cont_torre_mid_1_izquierda:
                self.dib_torre_mid_1_izquierda_viva = pygame.image.load(
                    "../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_1_izquierda_viva, (800, 415))
                self.cont_torre_mid_1_izquierda = self.cont_torre_mid_1_izquierda + 1
            elif not self.torre_mid_1_izquierda and self.cont_torre_mid_1_izquierda:
                self.dib_torre_mid_1_izquierda_nada = pygame.image.load(
                    "../torres/torres/torre_mid_izquierda_1_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_1_izquierda_nada, (800, 405))
                self.dib_torre_mid_1_izquierda_rota = pygame.image.load(
                    "../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_1_izquierda_rota, (800, 415))
                self.cont_torre_mid_1_izquierda = self.cont_torre_mid_1_izquierda + 1

            if self.torre_mid_2_izquierda and not self.cont_torre_mid_2_izquierda:
                self.dib_torre_mid_2_izquierda_viva = pygame.image.load(
                    "../torres/torres/torre_viva.png").convert_alpha()
                self.background.blit(self.dib_torre_top_1_izquierda_viva, (640, 575))
                self.cont_torre_mid_2_izquierda = self.cont_torre_mid_2_izquierda + 1
            elif not self.torre_mid_2_izquierda and self.cont_torre_mid_2_izquierda:
                self.dib_torre_mid_2_izquierda_nada = pygame.image.load(
                    "../torres/torres/torre_mid_izquierda_2_vacia.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_2_izquierda_nada, (640, 588))
                self.dib_torre_mid_2_izquierda_rota = pygame.image.load(
                    "../torres/torres/torre_rota.png").convert_alpha()
                self.background.blit(self.dib_torre_mid_2_izquierda_rota, (640, 575))
                self.cont_torre_mid_2_izquierda = self.cont_torre_mid_2_izquierda + 1

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

            # ----------------------------------------------------------------------------------------------------------
            """
            #FUNCION PARA ESCRIBIR POR CONSOLA COORDENADAS
            for p in self.clicks:
                pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0)#PARTE 1º= ¿? / PARTE 2º= Color RGB / Parte 3º=¿? / PARTE 4º= PRIMER NUMERO TAMAÑO DEL CIRCULO SEGUNDO NUMERO TAMAÑO DEL BORDE
            """
            # PELEAS TOP
            if self.subdito[0].x == 526 and self.subdito[3].x == 597:
                # FASE 1
                if self.buenosTop > 0 and self.malosTop > 0:
                    self.peleaTop = 1
                    # TURNO DE LOS BUENOS
                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(3, 6))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  # For turno heroes
                        if her.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    # TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(0, 3))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""

            elif self.subdito[0].y == 597 and self.subdito[3].y == 470:
                # FASE 2V - Malos
                # FASE 2D - Buenos
                if self.buenosTop > 0 and self.malosTop > 0:
                    self.peleaTop = 1
                    # TURNO DE LOS BUENOS
                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(3, 6))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  # For turno heroes
                        if her.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    # TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(0, 3))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""

            elif self.subdito[0].y == 705 and self.subdito[3].y == 611:
                # FASE 3V - Malos
                # FASE 3D - Buenos
                if self.buenosTop > 0 and self.malosTop > 0:
                    self.peleaTop = 1
                    # TURNO DE LOS BUENOS
                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(3, 6))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  # For turno heroes
                        if her.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    # TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(0, 3))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""

            elif self.subdito[0].x == 886 and self.subdito[3].x == 1005:
                # FASE 2D - Malos
                # FASE 2V - Buenos
                if self.buenosTop > 0 and self.malosTop > 0:
                    self.peleaTop = 1
                    # TURNO DE LOS BUENOS
                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(3, 6))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  # For turno heroes
                        if her.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    # TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(0, 3))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""

            elif self.subdito[0].x == 1057 and self.subdito[3].x == 1185:
                # FASE 3D - Malos
                # FASE 3V - Buenos
                if self.buenosTop > 0 and self.malosTop > 0:
                    self.peleaTop = 1
                    # TURNO DE LOS BUENOS
                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(3, 6))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  # For turno heroes
                        if her.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    # TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(0, 3))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "top":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[2].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""
            sumaHerTop = 0
            for her in self.heroe:
                if her.linea == "top":
                    sumaHerTop = sumaHerTop + her.health
            sumaVilTop = 0
            """for vil in self.villano:
                if vil.linea == "top":
                    sumVilTop = sumVilTop + vil.health"""

            self.buenosTop = self.subdito[0].health + self.subdito[1].health + self.subdito[2].health + sumaHerTop
            self.malosTop = self.subdito[3].health + self.subdito[4].health + self.subdito[5].health + sumaVilTop
            print(self.buenosTop, "-", self.malosTop)
            if self.peleaTop:
                if self.buenosTop > 0 and self.malosTop <= 0:
                    if self.torre_top_1_derecha:
                        self.torres[0].hit()
                        self.peleaTop = 0
                    elif self.torre_top_2_derecha:
                        self.torres[1].hit()
                        self.peleaTop = 0
                elif self.buenosTop <= 0 and self.malosTop > 0:
                    if self.torre_top_1_izquierda:
                        self.torres[2].hit()
                        self.peleaTop = 0
                    elif self.torre_top_2_izquierda:
                        self.torres[3].hit()
                        self.peleaTop = 0
            # PELEAS MID
            # PELEAS BOT
            if self.subdito[12].x == 1246 and self.subdito[15].x == 1324:
                # FASE 1
                if self.buenosBot > 0 and self.malosBot > 0:
                    self.peleaBot = 1
                    #TURNO DE LOS BUENOS
                    for i in range(3): #For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3)) #1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(15, 18))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  #For turno heroes
                        if her.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    #TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(12, 15))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""

            elif self.subdito[12].x == 895 and self.subdito[15].x == 991:
                # FASE 2V - Malos
                # FASE 2D - Buenos
                if self.buenosBot > 0 and self.malosBot > 0:
                    self.peleaBot = 1
                    # TURNO DE LOS BUENOS
                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(15, 18))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  # For turno heroes
                        if her.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    # TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(12, 15))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""
            elif self.subdito[12].x == 685 and self.subdito[15].x == 796:
                # FASE 3V - Malos
                # FASE 3D - Buenos
                if self.buenosBot > 0 and self.malosBot > 0:
                    self.peleaBot = 1
                    # TURNO DE LOS BUENOS
                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(15, 18))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  # For turno heroes
                        if her.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    # TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(12, 15))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""
            elif self.subdito[12].y == 602 and self.subdito[15].y == 484:
                # FASE 2D - Malos
                # FASE 2V - Buenos
                if self.buenosBot > 0 and self.malosBot > 0:
                    self.peleaBot = 1
                    # TURNO DE LOS BUENOS
                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(15, 18))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  # For turno heroes
                        if her.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    # TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(12, 15))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""
            elif self.subdito[12].y == 431 and self.subdito[15].y == 304:
                # FASE 3D - Malos
                # FASE 3V - Buenos
                if self.buenosBot > 0 and self.malosBot > 0:
                    self.peleaBot = 1
                    # TURNO DE LOS BUENOS
                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                            if n == 1:
                                atacarA = random.choice(range(15, 18))
                                print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                    salir = False
                            elif n == 2:
                                """atacarA = random.choice(range(0, len(self.heroe)))
                                if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                    self.villano[atacarA].hit()
                                    salir = False"""

                    for her in self.heroe:  # For turno heroes
                        if her.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= her.dano
                                        salir = False
                                    if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                        salir = False
                                elif n == 2:
                                    """atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                        self.villano[atacarA].health -= her.dano
                                        salir = False"""

                    # TURNO DE LOS MALOS

                    for i in range(3):  # For turno minions
                        salir = True
                        while salir:
                            n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                            if n == 1:
                                atacarA = random.choice(range(12, 15))
                                if self.subdito[atacarA].health > 0:
                                    self.subdito[atacarA].hit()
                                    salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[
                                    14].health <= 0:
                                    salir = False
                            elif n == 2:
                                atacarA = random.choice(range(0, len(self.heroe)))
                                if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                    self.heroe[atacarA].hit()
                                    salir = False

                    """for vil in self.villano:  # For turno villanos
                        if vil.linea == "bot":
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    if self.subdito[atacarA].health > 0:
                                        self.subdito[atacarA].health -= vil.dano
                                        salir = False
                                if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                    salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                        self.heroe[atacarA].health -= vil.dano
                                        salir = False"""
            sumaHerBot = 0
            for her in self.heroe:
                if her.linea == "bot":
                    sumaHerBot = sumaHerBot + her.health
            sumaVilBot = 0
            """for vil in self.villano:
                if vil.linea == "bot":
                    sumaVilBot = sumaVilBot + vil.health"""

            self.buenosBot = self.subdito[12].health + self.subdito[13].health + self.subdito[14].health + sumaHerBot
            print(len(self.subdito))
            print(self.subdito[15].id)
            print(self.subdito[16].id)
            print(self.subdito[17].id)
            self.malosBot = self.subdito[15].health + self.subdito[16].health + self.subdito[17].health + sumaVilBot
            print(self.buenosBot, "-", self.malosBot)
            if self.peleaBot:
                if self.buenosBot > 0 and self.malosBot <= 0:
                    if self.torre_bot_1_derecha:
                        print("paso a pegar a bot", self.malosBot)
                        self.torres[8].hit()
                        self.peleaBot = 0
                    elif self.torre_bot_2_derecha:
                        self.torres[9].hit()
                        self.peleaBot = 0
                elif self.buenosBot <= 0 and self.malosBot > 0:
                    if self.torre_bot_1_izquierda:
                        self.torres[10].hit()
                        self.peleaBot = 0
                    elif self.torre_bot_2_izquierda:
                        self.torres[11].hit()
                        self.peleaBot = 0

            print("Vida m1", self.subdito[15].health, self.subdito[15].x)
            print("Vida m2", self.subdito[16].health)
            print("Vida m3", self.subdito[17].health)
            print("Vida b1", self.subdito[12].health, self.subdito[12].x)
            print("Vida b2", self.subdito[13].health, self.subdito[13].x)
            print("Vida b3", self.subdito[14].health)

            # ----------

            for min in self.subdito:
                min.draw(self.win)

            for her in self.heroe:
                her.draw(self.win)
                print("pos", her.posicion, "linea", her.linea)

            for tor in self.torres:
                tor.draw_health_bar(self.win)
            # pygame.display.update() Este update esta ahora en donde se pinta el tiempo

    g = Game()
    g.run()


if __name__ == '__main__':
    main()
    pygame.quit()
