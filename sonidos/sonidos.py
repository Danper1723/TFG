import pygame


class Sonidos:

    def __init__(self):
        pass

    def backgroundPlay(self):
        # ---------------------MUSICA----------------------------
        pygame.mixer.init()
        print("Musica ON!")
        self.fondo = pygame.mixer.music.load('../sonidos/-backgroundSound.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
        # --------------------------------------------------------

    def backgroundStop(self):
        # ---------------------MUSICA----------------------------
        pygame.mixer.init()
        print("Musica OFF!")
        pygame.mixer.music.stop()
        # --------------------------------------------------------
