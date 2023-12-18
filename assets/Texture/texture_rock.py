import pygame

# Initialisation de pygame
pygame.init()

# Création de la fenêtre pygame (non nécessaire pour la texture, mais utile pour le contexte du jeu)
window = pygame.display.set_mode((800, 600))

# Chargement de l'image
rock_texture = pygame.image.load('rock.png')

# Obtenir les dimensions de l'image
rock_texture_rect = rock_texture.get_rect()

# Afficher l'image (à titre d'exemple, cela peut être différent selon votre utilisation)
window.blit(rock_texture, (0, 0))
pygame.display.flip()

# Attendre que l'utilisateur ferme la fenêtre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quitter pygame
pygame.quit()