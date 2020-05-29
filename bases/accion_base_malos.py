
import pygame


class Accion_base_malos:

    def __init__(self):
        self.nombre = "Base_malos"
        self.health = 100
        self.max_health = 100
        self.x = 1352
        self.y = 131


    def draw_health_bar(self, win):  # Barra de vida
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """

        length = 70
        move_by = length / self.max_health
        health_bar = round(move_by * self.health)

        pygame.draw.rect(win, (255, 0, 0), (self.x + 5, self.y + 5, length, 10), 0)
        pygame.draw.rect(win, (158, 18, 228), (self.x + 5, self.y + 5, health_bar, 10), 0)

    def hit(self):
        """
        DEVUELVE SI EL SUBDITO HA SIDO GOLPEADO Y LE RESTA VIDA
        :return: BOOLEAN
        """

        self.health -= 5
        #self.health -= self.health
        print("Se pega a base malos")
        if self.health <= 0:
            self.health = 0
