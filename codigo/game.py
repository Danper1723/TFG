import pygame
import os
import sqlite3
import time  # Tiempo
import threading  # Tiempo
import random  # Numeros aleatorios

from moviepy.editor import *

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
from heroes.Asesina.img_asesina import Img_asesina
from heroes.Cicatrices.img_cicatrices import Img_cicatrices
from heroes.Robot.img_robot import Img_robot
from heroes.Elfa.img_elfa import Img_elfa

#IMPORTAR LOS VILLANOS
from villanos.Minato.img_minato import Img_minato
from villanos.Caballero.img_caballero import Img_caballero
from villanos.Leia.img_leia import Img_leia
from villanos.Sanadora.img_sanadora import Img_sanadora
from villanos.Sombrero.img_sombrero import Img_sombrero

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
        #pygame.display.flip()
        # screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(410, 405, 200, 57)
        button_2 = pygame.Rect(920, 464, 77, 100)
        if button_1.collidepoint((mx, my)):
            if click:
                if nombre != "" and correo != "":
                    cursor.execute('INSERT INTO usuarios values("' + nombre + '", "' + correo + '")')
                    conexion.commit()
                    conexion.close()
                game()  # CAMBIO - Meter dentro del if de arriba del SQL

        if button_2.collidepoint((mx, my)):
            if click:
                Tutorial()

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
            #pygame.draw.rect(screen, (255, 100, 20), button_2)

        pygame.display.flip()
        clock.tick(30)

def Tutorial():
    running = True
    while running:
        pygame.display.set_caption('Tutorial')
        clip = VideoFileClip('../tutorial/tutorial.mp4')
        clip.preview()
        running = False

        pygame.display.update()
        #mainClock.tick(60)

def game():
    global segundosRonda  # Tiempo
    segundosRonda = 20
    #segundosRonda = 5
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
                Img_calabaza(), Img_asesina(), Img_cicatrices(), Img_robot(), Img_elfa()
            ]
            self.villano = [
                Img_minato(), Img_caballero(), Img_leia(), Img_sanadora(), Img_sombrero()
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
                # Asesina
            self.bAseColTop = False
            self.bAseColMid = False
            self.bAseColBot = False
                # Cicatrices
            self.bCicColTop = False
            self.bCicColMid = False
            self.bCicColBot = False
                # Robot
            self.bRobColTop = False
            self.bRobColMid = False
            self.bRobColBot = False
                # Elfa
            self.bElfColTop = False
            self.bElfColMid = False
            self.bElfColBot = False

            self.cont_top = 0
            self.cont_mid = 0
            self.cont_bot = 0

            # Variables para arrastrar a Mr.Clabaza
            self.mCalabazaRect = None
            self.mCalabazaImg = None
            self.rectangle_draging_Mcalabaza = None
            # Variables para arrastrar a Asesina
            self.asesinaRect = None
            self.asesinaImg = None
            self.rectangle_draging_Asesina = None
            # Variables para arrastrar a Cicatrices
            self.cicatricesRect = None
            self.cicatricesImg = None
            self.rectangle_draging_Cicatrices = None
            # Variables para arrastrar a Robot
            self.robotRect = None
            self.robotImg = None
            self.rectangle_draging_Robot = None
            # Variables para arrastrar a Elfa
            self.elfaRect = None
            self.elfaImg = None
            self.rectangle_draging_Elfa = None

            # Zona de colision top
            self.rectColTop = None
            self.colisionTopImg = None

            # Zona de colision mid
            self.rectColMid = None
            self.colisionMidImg = None

            # Zona de colision bot
            self.rectColBot = None
            self.colisionBotImg = None

            self.rectCal = None
            self.rectAse = None
            self.rectCic = None
            self.rectRob = None
            self.rectElf = None

            self.comprobacion_ia = True

            self.comPeleaTop = True
            self.comPeleaMid = True
            self.comPeleaBot = True

        def run(self):
            global click

            def cronoRonda():  # Tiempo funcion que sube 1 seg
                global segundosRonda
                segundosRonda = int(segundosRonda)
                if segundosRonda == 0:
                    for sub in self.subdito:
                        sub.estado_partida()
                    for her in self.heroe:
                        her.estado_partida()
                    for vil in self.villano:
                        vil.estado_partida()
                    if self.subdito[15].estado:
                        segundosRonda = 60
                        self.reset_cont = 1
                        self.peleaTop = 1
                        self.peleaMid = 1
                        self.peleaBot = 1
                        self.comPeleaTop = True
                        self.comPeleaMid = True
                        self.comPeleaBot = True
                    else:
                        if self.reset_cont:
                            # Mr.Calabaza
                            self.bCalColTop = False
                            self.bCalColMid = False
                            self.bCalColBot = False
                            # Asesina
                            self.bAseColTop = False
                            self.bAseColMid = False
                            self.bAseColBot = False
                            # Cicatrices
                            self.bCicColTop = False
                            self.bCicColMid = False
                            self.bCicColBot = False
                            # Robot
                            self.bRobColTop = False
                            self.bRobColMid = False
                            self.bRobColBot = False
                            # Elfa
                            self.bElfColTop = False
                            self.bElfColMid = False
                            self.bElfColBot = False


                            self.cont_top = 0
                            self.cont_mid = 0
                            self.cont_bot = 0
                            self.reset_cont = 0

                        self.comprobacion_ia = True
                        segundosRonda = 20
                        #segundosRonda = 5
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

            self.conexion_Bd()

            pygame.font.init()

            hiloRonda = threading.Thread(target=cronoRonda, args=())  # Hilo que controla el tiempo de ronda
            hiloRonda.start()
            hiloPartida = threading.Thread(target=cronoPartida, args=())  # Hilo que controla el tiempo de ronda
            hiloPartida.start()

            self.cargar_Heroes()

            # ---Terminan las variables de arrastrar heroes
            while run:

                if not self.subdito[15].estado:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                                # Mover a Mr.Calabaza
                                if self.mCalabazaRect.collidepoint(event.pos):
                                    self.rectangle_draging_Mcalabaza = True
                                    mouse_x, mouse_y = event.pos
                                    offset_x = self.mCalabazaRect.x - mouse_x
                                    offset_y = self.mCalabazaRect.y - mouse_y
                                # Mover a Asesina
                                if self.asesinaRect.collidepoint(event.pos):
                                    self.rectangle_draging_Asesina = True
                                    mouse_x, mouse_y = event.pos
                                    offset_x = self.asesinaRect.x - mouse_x
                                    offset_y = self.asesinaRect.y - mouse_y
                                # Mover a Cicatrices
                                if self.cicatricesRect.collidepoint(event.pos):
                                    self.rectangle_draging_Cicatrices = True
                                    mouse_x, mouse_y = event.pos
                                    offset_x = self.cicatricesRect.x - mouse_x
                                    offset_y = self.cicatricesRect.y - mouse_y
                                # Mover a Robot
                                if self.robotRect.collidepoint(event.pos):
                                    self.rectangle_draging_Robot = True
                                    mouse_x, mouse_y = event.pos
                                    offset_x = self.robotRect.x - mouse_x
                                    offset_y = self.robotRect.y - mouse_y
                                # Mover a Elfa
                                if self.elfaRect.collidepoint(event.pos):
                                    self.rectangle_draging_Elfa = True
                                    mouse_x, mouse_y = event.pos
                                    offset_x = self.elfaRect.x - mouse_x
                                    offset_y = self.elfaRect.y - mouse_y
                        elif event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:
                                print("aqui")
                                # Mover a Mr.Calabaza
                                if self.rectangle_draging_Mcalabaza:
                                    self.rectangle_draging_Mcalabaza = False
                                # Mover a Asesina
                                if self.rectangle_draging_Asesina:
                                    self.rectangle_draging_Asesina = False
                                # Mover a Cicatrices
                                if self.rectangle_draging_Cicatrices:
                                    self.rectangle_draging_Cicatrices = False
                                # Mover a Robot
                                if self.rectangle_draging_Robot:
                                    self.rectangle_draging_Robot = False
                                # Mover a Elfa
                                if self.rectangle_draging_Elfa:
                                    self.rectangle_draging_Elfa = False
                        elif event.type == pygame.MOUSEMOTION:
                            # Mover a Mr.Calabaza
                            if self.rectangle_draging_Mcalabaza:
                                print("esto no falla->", event.pos)
                                mouse_x, mouse_y = event.pos
                                self.mCalabazaRect.x = mouse_x + offset_x
                                self.mCalabazaRect.y = mouse_y + offset_y
                            # Mover a Asesina
                            if self.rectangle_draging_Asesina:
                                print("esto no falla->", event.pos)
                                mouse_x, mouse_y = event.pos
                                self.asesinaRect.x = mouse_x + offset_x
                                self.asesinaRect.y = mouse_y + offset_y
                            # Mover a Cicatrices
                            if self.rectangle_draging_Cicatrices:
                                print("esto no falla->", event.pos)
                                mouse_x, mouse_y = event.pos
                                self.cicatricesRect.x = mouse_x + offset_x
                                self.cicatricesRect.y = mouse_y + offset_y
                            # Mover a Robot
                            if self.rectangle_draging_Robot:
                                print("esto no falla->", event.pos)
                                mouse_x, mouse_y = event.pos
                                self.robotRect.x = mouse_x + offset_x
                                self.robotRect.y = mouse_y + offset_y
                            # Mover a Elfa
                            if self.rectangle_draging_Elfa:
                                print("esto no falla->", event.pos)
                                mouse_x, mouse_y = event.pos
                                self.elfaRect.x = mouse_x + offset_x
                                self.elfaRect.y = mouse_y + offset_y

                if self.subdito[15].estado:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True

                mx, my = pygame.mouse.get_pos()
                button_1 = pygame.Rect(1855, 1017, 50, 60)
                # pygame.draw.rect(screen, (0, 0, 0), button_1)
                if button_1.collidepoint((mx, my)):
                    if click:
                        pygame.quit()
                        sys.exit()

                button_2 = pygame.Rect(1765, 1012, 65, 60)
                # pygame.draw.rect(screen, (0, 0, 0), button_2)
                if button_2.collidepoint((mx, my)):
                    if click:
                        # pygame.quit()
                        self.b.backgroundStop()

                click = False

                self.movimiento_Heroes()

                self.colisiones_Heroes()

                if self.comprobacion_ia:
                    self.comprobacion_ia = False
                    self.ia()

                # pygame.time.delay(50)
                pygame.time.delay(25)
                clock.tick(30)
                """for event in pygame.event.get():
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
                        # self.subdito.remove(d)"""

                # for min in self.torres:
                # min.draw(self.win)

                self.escribir_Tiempo()

                self.escribir_Vida_Buenos()
                self.escribir_Vida_Malos()

                self.escribir_Vida_Villanos()

                pygame.display.update()#Este es el update general NO SE TOCA

                # ------

                self.draw()
            pygame.quit()

        def draw(self):
            global click

            self.win.blit(self.background, (0, 0))

            self.conexion_Bd_Torres()

            # TOP
            self.dibujar_Torres_Top()

            # MID
            self.dibujar_Torres_Mid()

            # BOT
            self.dibujar_Torres_Bot()

            # PELEAS TOP
            self.peleas_Top()

            # PELEAS MID
            self.peleas_Mid()

            # PELEAS BOT
            self.peleas_Bot()

            for min in self.subdito:
                min.draw(self.win)

            for her in self.heroe:
                her.draw(self.win)

            for vil in self.villano:
                vil.draw(self.win)

            for tor in self.torres:
                tor.draw_health_bar(self.win)

        def conexion_Bd(self):
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

        def cargar_Heroes(self):
            # Variables para arrastrar a Mr.Clabaza
            self.mCalabazaRect = pygame.rect.Rect(317, 189, 32, 32)
            self.mCalabazaImg = pygame.image.load(
                os.path.join("..", "heroes/imagenes/Mr.calabaza/", "calabaza.png"))  # Carga imagen grande Mr.Calabaza
            self.rectangle_draging_Mcalabaza = False
            # Variables para arrastrar a Asesina
            self.asesinaRect = pygame.rect.Rect(319, 291, 32, 32)
            self.asesinaImg = pygame.image.load(
                os.path.join("..", "heroes/imagenes/Asesina/", "asesina.png"))  # Carga imagen grande Asesina
            self.rectangle_draging_Asesina = False
            # Variables para arrastrar a Cicatrices
            self.cicatricesRect = pygame.rect.Rect(317, 393, 32, 32)
            self.cicatricesImg = pygame.image.load(
                os.path.join("..", "heroes/imagenes/Cicatrices/", "cicatrices.png"))  # Carga imagen grande Cicatrices
            self.rectangle_draging_Cicatrices = False
            # Variables para arrastrar a Robot
            self.robotRect = pygame.rect.Rect(317, 494, 32, 32)
            self.robotImg = pygame.image.load(
                os.path.join("..", "heroes/imagenes/Robot/", "robot.png"))  # Carga imagen grande Cicatrices
            self.rectangle_draging_Robot = False
            # Variables para arrastrar a Elfa
            self.elfaRect = pygame.rect.Rect(318, 598, 32, 32)
            self.elfaImg = pygame.image.load(
                os.path.join("..", "heroes/imagenes/Elfa/", "elfa.png"))  # Carga imagen grande Elfa
            self.rectangle_draging_Elfa = False

            # Zona de colision top
            self.rectColTop = pygame.rect.Rect(482, 635, 100, 100)
            self.colisionTopImg = pygame.image.load(
                os.path.join("..", "imagenes/", "portal_top.png"))  # Carga imagen zona de colision top

            # Zona de colision mid
            self.rectColMid = pygame.rect.Rect(575, 643, 100, 100)
            self.colisionMidImg = pygame.image.load(
                os.path.join("..", "imagenes/", "portal_mid.png"))  # Carga imagen zona de colision mid

            # Zona de colision bot
            self.rectColBot = pygame.rect.Rect(625, 865, 157, 91)
            self.colisionBotImg = pygame.image.load(
                os.path.join("..", "imagenes/", "portal_bot.png"))  # Carga imagen zona de colision bot

        def movimiento_Heroes(self):
            if self.subdito[15].estado:
                self.mCalabazaRect = pygame.rect.Rect(317, 189, 32, 32)  # Crear el rect de Mr.Calabaza
                self.rectCal = pygame.draw.rect(self.win, (255, 255, 255), self.mCalabazaRect, -1)  # Rect que envuelve a Mr.Calabaza
                self.asesinaRect = pygame.rect.Rect(319, 291, 32, 32)  # Crear el rect de Asesina
                self.rectAse = pygame.draw.rect(self.win, (255, 255, 255), self.asesinaRect, -1)  # Rect que envuelve a Asesina
                self.cicatricesRect = pygame.rect.Rect(317, 393, 32, 32)  # Crear el rect de Cicatrices
                self.rectCic = pygame.draw.rect(self.win, (255, 255, 255), self.cicatricesRect, -1)  # Rect que envuelve a Cicatrices
                self.robotRect = pygame.rect.Rect(317, 494, 32, 32)  # Crear el rect de Robot
                self.rectRob = pygame.draw.rect(self.win, (255, 255, 255), self.robotRect, -1)  # Rect que envuelve a Robot
                self.elfaRect = pygame.rect.Rect(317, 599, 32, 32)  # Crear el rect de Elfa
                self.rectElf = pygame.draw.rect(self.win, (255, 255, 255), self.elfaRect, -1)  # Rect que envuelve a Elfa

            else:
                self.rectCal = pygame.draw.rect(self.win, (255, 255, 255), self.mCalabazaRect, -1)  # Rect que envuelve a Mr.Calabaza
                self.rectAse = pygame.draw.rect(self.win, (255, 255, 255), self.asesinaRect, -1)  # Rect que envuelve a Asesina
                self.rectCic = pygame.draw.rect(self.win, (255, 255, 255), self.cicatricesRect, -1)  # Rect que envuelve a Cicatrices
                self.rectRob = pygame.draw.rect(self.win, (255, 255, 255), self.robotRect, -1)  # Rect que envuelve a Robot
                self.rectElf = pygame.draw.rect(self.win, (255, 255, 255), self.elfaRect, -1)  # Rect que envuelve a Elfa

                # Zonas de colisiones
                self.win.blit(self.colisionTopImg, self.rectColTop)  # Dibuja el sprite de colision top con su rect
                self.win.blit(self.colisionMidImg, self.rectColMid)  # Dibuja el sprite de colision mid con su rect
                self.win.blit(self.colisionBotImg, self.rectColBot)  # Dibuja el sprite de colision bot con su rect

                # Heroes para arrastrar
            self.win.blit(self.mCalabazaImg, self.rectCal)  # Dibujar el sprite grande de Mr.Calabaza con su rect
            self.win.blit(self.asesinaImg, self.rectAse)  # Dibujar el sprite grande de Asesina con su rect
            self.win.blit(self.cicatricesImg, self.rectCic)  # Dibujar el sprite grande de Cicatrices con su rect
            self.win.blit(self.robotImg, self.rectRob)  # Dibujar el sprite grande de Robot con su rect
            self.win.blit(self.elfaImg, self.rectElf)  # Dibujar el sprite grande de Elfa con su rect

        def colisiones_Heroes(self):
            # Colisiones de Mr.Calabaza
            if not self.bCalColTop:
                if self.rectCal.colliderect(self.rectColTop):  # Colision con rect en top
                    if self.cont_top <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[0].linea == "mid":
                            if self.heroe[0].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[0].posicion == 2:
                            self.cont_mid = 1
                        if self.heroe[0].linea == "bot":
                            if self.heroe[0].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[0].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_top += 1
                        self.heroe[0].posicion = self.cont_top
                        # self.heroe[0].posicion = 2#
                        self.heroe[0].linea = "top"
                        self.bCalColTop = True

            if not self.bCalColMid:
                if self.rectCal.colliderect(self.rectColMid):  # Colision con rect en mid
                    if self.cont_mid <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[0].linea == "top":
                            if self.heroe[0].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[0].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[0].linea == "bot":
                            if self.heroe[0].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[0].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_mid += 1
                        self.heroe[0].posicion = self.cont_mid
                        # self.heroe[0].posicion = 2#
                        self.heroe[0].linea = "mid"
                        self.bCalColMid = True

            if not self.bCalColBot:
                if self.rectCal.colliderect(self.rectColBot):  # Colision con rect en bot
                    if self.cont_bot <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[0].linea == "top":
                            if self.heroe[0].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[0].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[0].linea == "mid":
                            if self.heroe[0].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[0].posicion == 2:
                            self.cont_mid = 1
                        # ----------------
                        self.cont_bot += 1
                        self.heroe[0].posicion = self.cont_bot
                        # self.heroe[0].posicion = 2#
                        self.heroe[0].linea = "bot"
                        self.bCalColBot = True

            # Colisiones de Asesina
            if not self.bAseColTop:
                if self.rectAse.colliderect(self.rectColTop):  # Colision con rect en top
                    if self.cont_top <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[1].linea == "mid":
                            if self.heroe[1].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[1].posicion == 2:
                            self.cont_mid = 1
                        if self.heroe[1].linea == "bot":
                            if self.heroe[1].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[1].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_top += 1
                        self.heroe[1].posicion = self.cont_top
                        # self.heroe[0].posicion = 2#
                        self.heroe[1].linea = "top"
                        self.bAseColTop = True

            if not self.bAseColMid:
                if self.rectAse.colliderect(self.rectColMid):  # Colision con rect en mid
                    if self.cont_mid <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[1].linea == "top":
                            if self.heroe[1].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[1].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[1].linea == "bot":
                            if self.heroe[1].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[1].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_mid += 1
                        self.heroe[1].posicion = self.cont_mid
                        # self.heroe[0].posicion = 2#
                        self.heroe[1].linea = "mid"
                        self.bAseColMid = True

            if not self.bAseColBot:
                if self.rectAse.colliderect(self.rectColBot):  # Colision con rect en bot
                    if self.cont_bot <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[1].linea == "top":
                            if self.heroe[1].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[1].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[1].linea == "mid":
                            if self.heroe[1].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[1].posicion == 2:
                            self.cont_mid = 1
                        # ----------------
                        self.cont_bot += 1
                        self.heroe[1].posicion = self.cont_bot
                        # self.heroe[0].posicion = 2#
                        self.heroe[1].linea = "bot"
                        self.bAseColBot = True

            # Colisiones de Cicatrices
            if not self.bCicColTop:
                if self.rectCic.colliderect(self.rectColTop):  # Colision con rect en top
                    if self.cont_top <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[2].linea == "mid":
                            if self.heroe[2].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[2].posicion == 2:
                            self.cont_mid = 1
                        if self.heroe[2].linea == "bot":
                            if self.heroe[2].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[2].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_top += 1
                        self.heroe[2].posicion = self.cont_top
                        # self.heroe[0].posicion = 2#
                        self.heroe[2].linea = "top"
                        self.bCicColTop = True

            if not self.bCicColMid:
                if self.rectCic.colliderect(self.rectColMid):  # Colision con rect en mid
                    if self.cont_mid <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[2].linea == "top":
                            if self.heroe[2].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[2].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[2].linea == "bot":
                            if self.heroe[2].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[2].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_mid += 1
                        self.heroe[2].posicion = self.cont_mid
                        # self.heroe[0].posicion = 2#
                        self.heroe[2].linea = "mid"
                        self.bCicColMid = True

            if not self.bCicColBot:
                if self.rectCic.colliderect(self.rectColBot):  # Colision con rect en bot
                    if self.cont_bot <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[2].linea == "top":
                            if self.heroe[2].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[2].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[2].linea == "mid":
                            if self.heroe[1].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[1].posicion == 2:
                            self.cont_mid = 1
                        # ----------------
                        self.cont_bot += 1
                        self.heroe[2].posicion = self.cont_bot
                        # self.heroe[0].posicion = 2#
                        self.heroe[2].linea = "bot"
                        self.bCicColBot = True

            # Colisiones de Robot
            if not self.bRobColTop:
                if self.rectRob.colliderect(self.rectColTop):  # Colision con rect en top
                    if self.cont_top <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[3].linea == "mid":
                            if self.heroe[3].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[3].posicion == 2:
                            self.cont_mid = 1
                        if self.heroe[3].linea == "bot":
                            if self.heroe[3].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[3].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_top += 1
                        self.heroe[3].posicion = self.cont_top
                        # self.heroe[0].posicion = 2#
                        self.heroe[3].linea = "top"
                        self.bRobColTop = True

            if not self.bRobColMid:
                if self.rectRob.colliderect(self.rectColMid):  # Colision con rect en mid
                    if self.cont_mid <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[3].linea == "top":
                            if self.heroe[3].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[3].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[3].linea == "bot":
                            if self.heroe[3].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[3].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_mid += 1
                        self.heroe[3].posicion = self.cont_mid
                        # self.heroe[0].posicion = 2#
                        self.heroe[3].linea = "mid"
                        self.bRobColMid = True

            if not self.bRobColBot:
                if self.rectRob.colliderect(self.rectColBot):  # Colision con rect en bot
                    if self.cont_bot <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[3].linea == "top":
                            if self.heroe[3].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[3].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[3].linea == "mid":
                            if self.heroe[3].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[3].posicion == 2:
                            self.cont_mid = 1
                        # ----------------
                        self.cont_bot += 1
                        self.heroe[3].posicion = self.cont_bot
                        # self.heroe[0].posicion = 2#
                        self.heroe[3].linea = "bot"
                        self.bRobColBot = True

            # Colisiones de Elfa
            if not self.bElfColTop:
                if self.rectElf.colliderect(self.rectColTop):  # Colision con rect en top
                    if self.cont_top <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[4].linea == "mid":
                            if self.heroe[4].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[4].posicion == 2:
                            self.cont_mid = 1
                        if self.heroe[4].linea == "bot":
                            if self.heroe[4].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[4].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_top += 1
                        self.heroe[4].posicion = self.cont_top
                        # self.heroe[0].posicion = 2#
                        self.heroe[4].linea = "top"
                        self.bElfColTop = True

            if not self.bRobColMid:
                if self.rectElf.colliderect(self.rectColMid):  # Colision con rect en mid
                    if self.cont_mid <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[4].linea == "top":
                            if self.heroe[4].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[4].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[4].linea == "bot":
                            if self.heroe[4].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "bot":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_bot = 1
                        elif self.heroe[4].posicion == 2:
                            self.cont_bot = 1
                        # ----------------
                        self.cont_mid += 1
                        self.heroe[4].posicion = self.cont_mid
                        # self.heroe[0].posicion = 2#
                        self.heroe[4].linea = "mid"
                        self.bElfColMid = True

            if not self.bElfColBot:
                if self.rectElf.colliderect(self.rectColBot):  # Colision con rect en bot
                    if self.cont_bot <= 2:
                        # Reiniciar las posiciones al cambiar hero de linea
                        if self.heroe[4].linea == "top":
                            if self.heroe[4].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "top":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_top = 1
                        elif self.heroe[4].posicion == 2:
                            self.cont_top = 1
                        if self.heroe[4].linea == "mid":
                            if self.heroe[4].posicion == 1:
                                for her in self.heroe:
                                    if her.linea == "mid":
                                        if her.posicion == 2:
                                            her.posicion = 1
                                self.cont_mid = 1
                        elif self.heroe[4].posicion == 2:
                            self.cont_mid = 1
                        # ----------------
                        self.cont_bot += 1
                        self.heroe[4].posicion = self.cont_bot
                        # self.heroe[0].posicion = 2#
                        self.heroe[4].linea = "bot"
                        self.bElfColBot = True
            # ----Se acaba mover heroes a las lineas

        def escribir_Tiempo(self):
            fuente = pygame.font.Font("../VT323-Regular.ttf", 55)  # Tiempo
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

        def escribir_Vida_Buenos(self):
            fuenteHealth = pygame.font.Font("../VT323-Regular.ttf", 30)  # Vida personajes
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

        def escribir_Vida_Malos(self):
            fuenteHealth = pygame.font.Font("../VT323-Regular.ttf", 30)  # Vida personajes
            # Dibujar vida minions
            # Buneos TOP
            vidaBT1 = str(self.subdito[3].health)  # 2º
            if int(vidaBT1) < 10:
                vidaBT1 = "00" + str(vidaBT1)
            elif int(vidaBT1) < 100:
                vidaBT1 = "0" + str(vidaBT1)
            healthBt1 = fuenteHealth.render(vidaBT1, 0, (0, 0, 0))
            self.win.blit(healthBt1, (1830, 207))

            vidaBT2 = str(self.subdito[4].health)  # 1º
            if int(vidaBT2) < 10:
                vidaBT2 = "00" + str(vidaBT2)
            elif int(vidaBT2) < 100:
                vidaBT2 = "0" + str(vidaBT2)
            healthBt2 = fuenteHealth.render(vidaBT2, 0, (0, 0, 0))
            self.win.blit(healthBt2, (1830, 172))

            vidaBT3 = str(self.subdito[5].health)  # 3º
            if int(vidaBT3) < 10:
                vidaBT3 = "00" + str(vidaBT3)
            elif int(vidaBT3) < 100:
                vidaBT3 = "0" + str(vidaBT3)
            healthBt3 = fuenteHealth.render(vidaBT3, 0, (0, 0, 0))
            self.win.blit(healthBt3, (1830, 242))
            # Buenos MID
            vidaBM1 = str(self.subdito[9].health)  # 2º
            if int(vidaBM1) < 10:
                vidaBM1 = "00" + str(vidaBM1)
            elif int(vidaBM1) < 100:
                vidaBM1 = "0" + str(vidaBM1)
            healthBm1 = fuenteHealth.render(vidaBM1, 0, (0, 0, 0))
            self.win.blit(healthBm1, (1830, 394))

            vidaBM2 = str(self.subdito[10].health)  # 1º
            if int(vidaBM2) < 10:
                vidaBM2 = "00" + str(vidaBM2)
            elif int(vidaBM2) < 100:
                vidaBM2 = "0" + str(vidaBM2)
            healthBm2 = fuenteHealth.render(vidaBM2, 0, (0, 0, 0))
            self.win.blit(healthBm2, (1830, 359))

            vidaBM3 = str(self.subdito[11].health)  # 3º
            if int(vidaBM3) < 10:
                vidaBM3 = "00" + str(vidaBM3)
            elif int(vidaBM3) < 100:
                vidaBM3 = "0" + str(vidaBM3)
            healthBm3 = fuenteHealth.render(vidaBM3, 0, (0, 0, 0))
            self.win.blit(healthBm3, (1830, 429))
            # Buenos BOT
            vidaBB1 = str(self.subdito[15].health)  # 2º
            if int(vidaBB1) < 10:
                vidaBB1 = "00" + str(vidaBB1)
            elif int(vidaBB1) < 100:
                vidaBB1 = "0" + str(vidaBB1)
            healthBb1 = fuenteHealth.render(vidaBB1, 0, (0, 0, 0))
            self.win.blit(healthBb1, (1830, 582))

            vidaBB2 = str(self.subdito[16].health)  # 1º
            if int(vidaBB2) < 10:
                vidaBB2 = "00" + str(vidaBB2)
            elif int(vidaBB2) < 100:
                vidaBB2 = "0" + str(vidaBB2)
            healthBb2 = fuenteHealth.render(vidaBB2, 0, (0, 0, 0))
            self.win.blit(healthBb2, (1830, 547))

            vidaBB3 = str(self.subdito[17].health)  # 3º
            if int(vidaBB3) < 10:
                vidaBB3 = "00" + str(vidaBB3)
            elif int(vidaBB3) < 100:
                vidaBB3 = "0" + str(vidaBB3)
            healthBb3 = fuenteHealth.render(vidaBB3, 0, (0, 0, 0))
            self.win.blit(healthBb3, (1830, 617))

        def escribir_Vida_Villanos(self):
            fuenteHealth = pygame.font.Font("../VT323-Regular.ttf", 23)  # Vida villanos
            vidaMinato = str(self.villano[0].health)  # 3º
            if int(vidaMinato) < 10:
                vidaMinato = "00" + str(vidaMinato)
            elif int(vidaMinato) < 100:
                vidaMinato = "0" + str(vidaMinato)
            vidaMinato = fuenteHealth.render(vidaMinato, 0, (0, 0, 0))
            self.win.blit(vidaMinato, (1532, 377))

        def conexion_Bd_Torres(self):
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

        def dibujar_Torres_Top(self):
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

        def dibujar_Torres_Mid(self):
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

        def dibujar_Torres_Bot(self):
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

        def peleas_Top(self):
            if self.subdito[0].x == 526 and self.subdito[3].x == 597:
                # FASE 1
                if self.peleaTop:
                    if self.buenosTop > 0 and self.malosTop > 0:
                        self.peleaTop = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                        5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

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
                                        if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                            5].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health  - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "top":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(0, 3))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[0].y == 597 and self.subdito[3].y == 470:
                # FASE 2V - Malos
                # FASE 2D - Buenos
                if self.peleaTop:
                    if self.buenosTop > 0 and self.malosTop > 0:
                        self.peleaTop = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                        5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

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
                                        if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                            5].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "top":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(0, 3))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[0].y == 705 and self.subdito[3].y == 611:
                # FASE 3V - Malos
                # FASE 3D - Buenos
                if self.peleaTop:
                    if self.buenosTop > 0 and self.malosTop > 0:
                        self.peleaTop = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                        5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

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
                                        if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                            5].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "top":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(0, 3))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[0].x == 886 and self.subdito[3].x == 1005:
                # FASE 2D - Malos
                # FASE 2V - Buenos
                if self.peleaTop:
                    if self.buenosTop > 0 and self.malosTop > 0:
                        self.peleaTop = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                        5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

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
                                        if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                            5].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "top":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(0, 3))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[0].x == 1057 and self.subdito[3].x == 1185:
                # FASE 3D - Malos
                # FASE 3V - Buenos
                if self.peleaTop:
                    if self.buenosTop > 0 and self.malosTop > 0:
                        self.peleaTop = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(3, 6))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                        5].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

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
                                        if self.subdito[3].health <= 0 and self.subdito[4].health <= 0 and self.subdito[
                                            5].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "top":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(0, 3))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "top":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(0, 3))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[0].health <= 0 and self.subdito[1].health <= 0 and self.subdito[
                                        2].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "top":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False
            sumaHerTop = 0
            for her in self.heroe:
                if her.linea == "top":
                    sumaHerTop = sumaHerTop + her.health
            sumaVilTop = 0
            for vil in self.villano:
                if vil.linea == "top":
                    sumaVilTop = sumaVilTop + vil.health

            self.buenosTop = self.subdito[0].health + self.subdito[1].health + self.subdito[2].health + sumaHerTop
            self.malosTop = self.subdito[3].health + self.subdito[4].health + self.subdito[5].health + sumaVilTop

            print(self.buenosTop, "-", self.malosTop)
            if self.peleaTop:
                if self.buenosTop > 0 and self.malosTop == 0:
                    if self.torre_top_1_derecha:
                        self.torres[0].hit()
                        self.peleaTop = 0
                    elif self.torre_top_2_derecha:
                        self.torres[1].hit()
                        self.peleaTop = 0
                elif self.buenosTop == 0 and self.malosTop > 0:
                    if self.torre_top_1_izquierda:
                        self.torres[2].hit()
                        self.peleaTop = 0
                    elif self.torre_top_2_izquierda:
                        self.torres[3].hit()
                        self.peleaTop = 0

        def peleas_Mid(self):
            if self.subdito[6].x == 921 and self.subdito[9].x == 952:
                # FASE 1
                if self.peleaMid:
                    if self.buenosMid > 0 and self.malosMid > 0:
                        self.peleaMid = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(9, 12))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and self.subdito[
                                        11].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    print(atacarA)
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

                        for her in self.heroe:  # For turno heroes
                            if her.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(9, 12))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= her.dano
                                            salir = False
                                        if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and self.subdito[
                                            11].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                            self.villano[atacarA].health -= her.dano - int((
                                                        (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(6, 9))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[
                                        8].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(6, 9))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[8].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                        (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[6].y == 655 and self.subdito[9].y == 559:
                # FASE 2V - Malos
                # FASE 2D - Buenos
                if self.peleaMid:
                    if self.buenosMid > 0 and self.malosMid > 0:
                        self.peleaMid = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(9, 12))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and self.subdito[
                                        11].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    print(atacarA)
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

                        for her in self.heroe:  # For turno heroes
                            if her.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(9, 12))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= her.dano
                                            salir = False
                                        if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and \
                                                self.subdito[
                                                    11].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(6, 9))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[
                                        8].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(6, 9))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[
                                        8].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[6].y == 745 and self.subdito[9].y == 715:
                # FASE 3V - Malos
                # FASE 3D - Buenos
                if self.peleaMid:
                    if self.buenosMid > 0 and self.malosMid > 0:
                        self.peleaMid = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(9, 12))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and self.subdito[
                                        11].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    print(atacarA)
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

                        for her in self.heroe:  # For turno heroes
                            if her.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(9, 12))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= her.dano
                                            salir = False
                                        if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and \
                                                self.subdito[
                                                    11].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(6, 9))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[
                                        8].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(6, 9))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[
                                        8].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[6].x == 1044 and self.subdito[9].x == 1135:
                # FASE 2D - Malos
                # FASE 2V - Buenos
                if self.peleaMid:
                    if self.buenosMid > 0 and self.malosMid > 0:
                        self.peleaMid = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(9, 12))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and self.subdito[
                                        11].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    print(atacarA)
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

                        for her in self.heroe:  # For turno heroes
                            if her.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(9, 12))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= her.dano
                                            salir = False
                                        if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and \
                                                self.subdito[
                                                    11].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(6, 9))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[
                                        8].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(6, 9))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[
                                        8].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[6].x == 1125 and self.subdito[9].x == 1219:
                # FASE 3D - Malos
                # FASE 3V - Buenos
                if self.peleaMid:
                    if self.buenosMid > 0 and self.malosMid > 0:
                        self.peleaMid = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(9, 12))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and self.subdito[
                                        11].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    print(atacarA)
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

                        for her in self.heroe:  # For turno heroes
                            if her.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(9, 12))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= her.dano
                                            salir = False
                                        if self.subdito[9].health <= 0 and self.subdito[10].health <= 0 and \
                                                self.subdito[
                                                    11].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "mid":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(6, 9))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[
                                        8].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "mid":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(6, 9))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[6].health <= 0 and self.subdito[7].health <= 0 and self.subdito[
                                        8].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "mid":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            sumaHerMid = 0
            for her in self.heroe:
                if her.linea == "mid":
                    sumaHerMid = sumaHerMid + her.health
            sumaVilMid = 0
            for vil in self.villano:
                if vil.linea == "mid":
                    sumaVilMid = sumaVilMid + vil.health

            self.buenosMid = self.subdito[6].health + self.subdito[7].health + self.subdito[8].health + sumaHerMid
            self.malosMid = self.subdito[9].health + self.subdito[10].health + self.subdito[11].health + sumaVilMid
            print(self.buenosMid, "-", self.malosMid)
            if self.peleaMid:
                if self.buenosMid > 0 and self.malosMid == 0:
                    if self.torre_mid_1_derecha:
                        self.torres[4].hit()
                        self.peleaMid = 0
                    elif self.torre_mid_2_derecha:
                        self.torres[5].hit()
                        self.peleaMid = 0
                elif self.buenosMid == 0 and self.malosMid > 0:
                    if self.torre_mid_1_izquierda:
                        self.torres[6].hit()
                        self.peleaMid = 0
                    elif self.torre_mid_2_izquierda:
                        self.torres[7].hit()
                        self.peleaMid = 0

        def peleas_Bot(self):
            if self.subdito[12].x == 1246 and self.subdito[15].x == 1324:
                # FASE 1
                if self.peleaBot:
                    if self.comPeleaBot:
                        if self.buenosBot > 0 and self.malosBot > 0:
                            self.peleaBot = 1
                            #TURNO DE LOS BUENOS
                            turnosBuenos = 0
                            for i in range(3): # For turno minions
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3)) # 1 ataca a minion 2 ataca a villano
                                    if n == 1:
                                        atacarA = random.choice(range(15, 18))
                                        print("ataco a", self.subdito[atacarA].id, "que tiene", self.subdito[atacarA].health)
                                        if self.subdito[atacarA].health > 0:
                                            if turnosBuenos < 2:
                                                dano = random.choice(range(10, 14))
                                                self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                                turnosBuenos += 1
                                            elif turnosBuenos == 2:
                                                dano = random.choice(range(15, 19))
                                                self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            salir = False
                                        if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[17].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                            if turnosBuenos < 2:
                                                dano = random.choice(range(10, 14))
                                                self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                                turnosBuenos += 1
                                            elif turnosBuenos == 2:
                                                dano = random.choice(range(15, 19))
                                                self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                        (dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

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
                                            atacarA = random.choice(range(0, len(self.villano)))
                                            if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                                self.villano[atacarA].health -= her.dano - int((
                                                        (her.dano * self.villano[atacarA].armadura) / 100))
                                                salir = False

                            # TURNO DE LOS MALOS
                            turnoMalos = 0
                            for i in range(3):  # For turno minions
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(12, 15))
                                        if self.subdito[atacarA].health > 0:
                                            if turnoMalos < 2:
                                                dano = random.choice(range(10, 14))
                                                self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                                turnoMalos += 1
                                            elif turnoMalos == 2:
                                                dano = random.choice(range(15, 19))
                                                self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            salir = False
                                        if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                            if turnoMalos < 2:
                                                dano = random.choice(range(10, 14))
                                                self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                        (dano * self.heroe[atacarA].armadura) / 100))
                                                turnoMalos += 1
                                            elif turnoMalos == 2:
                                                dano = random.choice(range(15, 19))
                                                self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                        (dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

                            for vil in self.villano:  # For turno villanos
                                if vil.linea == "bot":
                                    salir = True
                                    while salir:
                                        n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                        if n == 1:
                                            atacarA = random.choice(range(12, 15))
                                            if self.subdito[atacarA].health > 0:
                                                self.subdito[atacarA].health -= vil.dano
                                                salir = False
                                        if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[14].health <= 0:
                                            salir = False
                                        elif n == 2:
                                            atacarA = random.choice(range(0, len(self.heroe)))
                                            if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                                self.heroe[atacarA].health -= vil.dano - int((
                                                        (vil.dano * self.heroe[atacarA].armadura) / 100))
                                                salir = False

            elif self.subdito[12].x == 895 and self.subdito[15].x == 991:
                # FASE 2V - Malos
                # FASE 2D - Buenos
                if self.peleaBot:
                    if self.buenosBot > 0 and self.malosBot > 0:
                        self.peleaBot = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[
                                        17].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

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
                                        if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and \
                                                self.subdito[17].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(12, 15))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[
                                        14].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "bot":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(12, 15))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[
                                        14].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[12].x == 685 and self.subdito[15].x == 796:
                # FASE 3V - Malos
                # FASE 3D - Buenos
                if self.peleaBot:
                    if self.buenosBot > 0 and self.malosBot > 0:
                        self.peleaBot = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[
                                        17].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

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
                                        if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and \
                                                self.subdito[17].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(12, 15))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[
                                        14].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "bot":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(12, 15))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[
                                        14].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[12].y == 602 and self.subdito[15].y == 484:
                # FASE 2D - Malos
                # FASE 2V - Buenos
                if self.peleaBot:
                    if self.buenosBot > 0 and self.malosBot > 0:
                        self.peleaBot = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[
                                        17].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

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
                                        if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and \
                                                self.subdito[17].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(12, 15))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[
                                        14].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "bot":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(12, 15))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[
                                        14].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False

            elif self.subdito[12].y == 431 and self.subdito[15].y == 304:
                # FASE 3D - Malos
                # FASE 3V - Buenos
                if self.peleaBot:
                    if self.buenosBot > 0 and self.malosBot > 0:
                        self.peleaBot = 1
                        # TURNO DE LOS BUENOS
                        turnosBuenos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a villano
                                if n == 1:
                                    atacarA = random.choice(range(15, 18))
                                    print("ataco a", self.subdito[atacarA].id, "que tiene",
                                          self.subdito[atacarA].health)
                                    if self.subdito[atacarA].health > 0:
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and self.subdito[
                                        17].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.villano)))
                                    if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                        if turnosBuenos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.villano[atacarA].health = self.subdito[atacarA].health - dano
                                            turnosBuenos += 1
                                        elif turnosBuenos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.villano[atacarA].health = self.villano[atacarA].health - int((
                                                    (dano * self.villano[atacarA].armadura) / 100))
                                        salir = False

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
                                        if self.subdito[15].health <= 0 and self.subdito[16].health <= 0 and \
                                                self.subdito[17].health <= 0:
                                            salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.villano)))
                                        if self.villano[atacarA].health > 0 and self.villano[atacarA].linea == "bot":
                                            self.villano[atacarA].health -= her.dano - int((
                                                    (her.dano * self.villano[atacarA].armadura) / 100))
                                            salir = False

                        # TURNO DE LOS MALOS
                        turnoMalos = 0
                        for i in range(3):  # For turno minions
                            salir = True
                            while salir:
                                n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                if n == 1:
                                    atacarA = random.choice(range(12, 15))
                                    if self.subdito[atacarA].health > 0:
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.subdito[atacarA].health = self.subdito[atacarA].health - dano
                                        salir = False
                                    if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[
                                        14].health <= 0:
                                        salir = False
                                elif n == 2:
                                    atacarA = random.choice(range(0, len(self.heroe)))
                                    if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                        if turnoMalos < 2:
                                            dano = random.choice(range(10, 14))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                            turnoMalos += 1
                                        elif turnoMalos == 2:
                                            dano = random.choice(range(15, 19))
                                            self.heroe[atacarA].health = self.heroe[atacarA].health - int((
                                                    (dano * self.heroe[atacarA].armadura) / 100))
                                        salir = False

                        for vil in self.villano:  # For turno villanos
                            if vil.linea == "bot":
                                salir = True
                                while salir:
                                    n = random.choice(range(1, 3))  # 1 ataca a minion 2 ataca a heroe
                                    if n == 1:
                                        atacarA = random.choice(range(12, 15))
                                        if self.subdito[atacarA].health > 0:
                                            self.subdito[atacarA].health -= vil.dano
                                            salir = False
                                    if self.subdito[12].health <= 0 and self.subdito[13].health <= 0 and self.subdito[
                                        14].health <= 0:
                                        salir = False
                                    elif n == 2:
                                        atacarA = random.choice(range(0, len(self.heroe)))
                                        if self.heroe[atacarA].health > 0 and self.heroe[atacarA].linea == "bot":
                                            self.heroe[atacarA].health -= vil.dano - int((
                                                    (vil.dano * self.heroe[atacarA].armadura) / 100))
                                            salir = False
            sumaHerBot = 0
            for her in self.heroe:
                if her.linea == "bot":
                    sumaHerBot = sumaHerBot + her.health
            sumaVilBot = 0
            for vil in self.villano:
                if vil.linea == "bot":
                    sumaVilBot = sumaVilBot + vil.health

            self.buenosBot = self.subdito[12].health + self.subdito[13].health + self.subdito[14].health + sumaHerBot
            self.malosBot = self.subdito[15].health + self.subdito[16].health + self.subdito[17].health + sumaVilBot

            if self.peleaBot:
                if self.buenosBot > 0 and self.malosBot == 0:
                    if self.torre_bot_1_derecha:
                        print("paso a pegar a bot", self.malosBot)
                        self.torres[8].hit()
                        self.peleaBot = 0
                    elif self.torre_bot_2_derecha:
                        self.torres[9].hit()
                        self.peleaBot = 0
                elif self.buenosBot == 0 and self.malosBot > 0:
                    if self.torre_bot_1_izquierda:
                        self.torres[10].hit()
                        self.peleaBot = 0
                    elif self.torre_bot_2_izquierda:
                        self.torres[11].hit()
                        self.peleaBot = 0

        def ia(self):
            contador_top = 0
            contador_mid = 0
            contador_bot = 0

            for vil in self.villano:
                colocar = False
                while True:
                    n = random.choice(range(1, 4))

                    if n == 1:
                        contador_top = contador_top + 1
                        if contador_top == 1:
                            vil.linea = "top"
                            vil.posicion = 1
                            colocar = True
                        else:
                            if contador_top == 2:
                                vil.linea = "top"
                                vil.posicion = 2
                                colocar = True

                    if n == 2:
                        contador_mid = contador_mid + 1
                        if contador_mid == 1:
                            vil.linea = "mid"
                            vil.posicion = 1
                            colocar = True
                        else:
                            if contador_mid == 2:
                                vil.linea = "mid"
                                vil.posicion = 2
                                colocar = True

                    if n == 3:
                        contador_bot = contador_bot + 1
                        if contador_bot == 1:
                            vil.linea = "bot"
                            vil.posicion = 1
                            colocar = True
                        else:
                            if contador_bot == 2:
                                vil.linea = "bot"
                                vil.posicion = 2
                                colocar = True

                    if colocar:
                        break

    g = Game()
    g.run()

if __name__ == '__main__':
    main()
    pygame.quit()
