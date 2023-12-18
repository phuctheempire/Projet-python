import pygame
import sys
from Prototype.N.game.bob import Bob

class EvenManager:
    def __init__(self, screen, clock, world):
        pygame.init()
        self.screen = screen
        self.clock = clock
        self.world = world
        self.width, self.height = self.screen.get_size()
        pygame.display.set_caption("EvenManager - Déplacement de Bob")

        tile = self.world.world[5][5]
        self.bob = Bob(tile, self.world)


    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Gestion des événements de la souris
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Événement de clic de souris
                    mouse_x, mouse_y = pygame.mouse.get_pos()


            keys = pygame.key.get_pressed()
            self.move_bob(keys)
            self.screen.fill((0, 0, 0))  # Vous pouvez remplir avec une couleur différente si nécessaire

            self.draw_bob()
            pygame.display.flip()

            clock.tick(60)

    def update_grid(self, keys):
        if keys[pygame.K_LEFT]:
            self.move_grid("left")
        elif keys[pygame.K_RIGHT]:
            self.move_grid("right")
        elif keys[pygame.K_UP]:
            self.move_grid("up")
        elif keys[pygame.K_DOWN]:
            self.move_grid("down")

    def move_grid(self, direction):
        # Logique pour déplacer la grille dans la direction spécifiée
        if direction in ["up", "down", "left", "right"]:
            # Logique pour déplacer la grille dans la direction spécifiée
            # Vous pouvez adapter cette logique en fonction des besoins spécifiques de votre jeu
            if direction == "up":
                self.world.world = list(zip(*self.world.world[::-1]))
            elif direction == "down":
                self.world.world = list(zip(*self.world.world[::-1]))[::-1]
            elif direction == "left":
                self.world.world = [list(row[::-1]) for row in self.world.world]
            elif direction == "right":
                self.world.world = [list(row[::-1]) for row in self.world.world][::-1]


