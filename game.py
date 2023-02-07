import pygame
from player import player

# creer une seconde classe qui va representer notre jeu
class game:

    def __init__(self):
       # genere notre joueur
        self.player = player()
        self.pressed = {}


