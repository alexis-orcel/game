import pygame
from projectile import Projectile


# creer une premiere classe qui va representer notre jeu
class player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 9
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/hell.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 433

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount


    def update_health_bar(self, surface):
        # dessiner notre jauge de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 5])
    def launch_projectile(self):
        # creer une nouvelle instance de la classe projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)


    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity
