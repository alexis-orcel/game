import pygame
from player import player
from monster import Monster

# creer une seconde classe qui va representer notre jeu
class game:

    def __init__(self):
       # genere notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = player(self)
        self.all_players.add(self.player)
       # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)


