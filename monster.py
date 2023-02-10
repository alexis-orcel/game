import pygame
import random


# creer une classe qui va gerer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0,3
        self.velocity = 1 + random.randint(0, 2)
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500

    def damage(self, amount):
        # infliger les degats
        self.health -= amount
        # verifier si son nouveau nombre de point de vie est inferieur ou egale a 0
        if self.health <= 0:
            # reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = 1 + random.randint(0, 2)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # dessiner notre jauge de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre entre en collision avec un joueur
        else:
            # infliger des degats
            self.game.player.damage(self.attack)











