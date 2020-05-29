import sqlite3

import pygame


class Accion_torre_bot_1_izquierda:

    def __init__(self):
        self.nombre = "torre_bot_1_izquierda"
        self.health = 10
        self.max_health = 10
        self.x = 1089
        self.y = 740

    def draw_health_bar(self, win):  # Barra de vida
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """

        length = 25
        move_by = length / self.max_health
        health_bar = round(move_by * self.health)

        pygame.draw.rect(win, (255, 0, 0), (self.x + 5, self.y + 5, length, 5), 0)
        pygame.draw.rect(win, (0, 0, 0), (self.x + 5, self.y + 5, health_bar, 5), 0)

    def hit(self):
        """
        DEVUELVE SI EL SUBDITO HA SIDO GOLPEADO Y LE RESTA VIDA
        :return: BOOLEAN
        """

        self.health -= 1

        if self.health <= 0:
            conexion = sqlite3.connect('../datos.db')
            cursor = conexion.cursor()
            cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_bot_1_izquierda"')
            conexion.commit()
            conexion.close()
            self.health = 0
            pygame.mixer.init()
            effect = pygame.mixer.Sound('../sonidos/sonidos_torres/muerte_torre.wav')
            effect.set_volume(0.01)
            effect.play()