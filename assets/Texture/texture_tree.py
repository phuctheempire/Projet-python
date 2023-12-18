import pygame

# Initialisation de pygame
pygame.init()

# Création de la fenêtre pygame (non nécessaire pour la texture, mais utile pour le contexte du jeu)
window = pygame.display.set_mode((800, 600))

# Chargement de l'image
tree_texture = pygame.image.load('tree.png')

# Obtenir les dimensions de l'image
tree_texture_rect = tree_texture.get_rect()

# Afficher l'image (à titre d'exemple, cela peut être différent selon votre utilisation)
window.blit(tree_texture, (0, 0))
pygame.display.flip()

# Attendre que l'utilisateur ferme la fenêtre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quitter pygame
pygame.quit()
