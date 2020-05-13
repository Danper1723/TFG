import sqlite3

import pygame


class Accion_torre_top_2_derecha:

    def __init__(self):
        self.nombre = "torre_top_2_derecha"
        self.health = 10
        self.max_health = 10
        self.x = 1120
        self.y = 2

    def draw_health_bar(self, win):  # Barra de vida
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """

        length = 25
        move_by = length / self.max_health
        health_bar = round(move_by * self.health)

        pygame.draw.rect(win, (255, 0, 0), (self.x + 5, self.y + 9, length, 5), 0)
        pygame.draw.rect(win, (0, 0, 0), (self.x + 5, self.y + 9, health_bar, 5), 0)

    def hit(self):
        """
        DEVUELVE SI EL SUBDITO HA SIDO GOLPEADO Y LE RESTA VIDA
        :return: BOOLEAN
        """

        self.health -= 5
        # self.health -= self.health

        if self.health <= 0:
            conexion = sqlite3.connect('../datos.db')
            cursor = conexion.cursor()
            cursor.execute('UPDATE torres SET estado = 0 WHERE nombre = "torre_top_2_derecha"')
            conexion.commit()
            conexion.close()