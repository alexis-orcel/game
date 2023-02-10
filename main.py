import pygame
from game import game
pygame.init()


# generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer de charger l'arriere plan
background = pygame.image.load('assets/assetcyber (1).png')

# charger notre jeu
game = game()

running = True

# boucle tant que cette conditon est vrais
while running:

    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0,-200))

    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)


    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer le monstre de notre jeu
    for monster in game.all_monsters:
        monster.forward()

    monster.update_health_bar(screen)

    # appliquer l'ensemble des images de mon groupe de projectile
    game.player.all_projectiles.draw(screen)

    # appliquer l ensemble des images de mon groupe de monstre
    game.all_monsters.draw(screen)


    # verifier si le joueur souhaite aller a droite ou a gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.pressed)

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchee pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False







