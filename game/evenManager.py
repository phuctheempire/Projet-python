import pygame
import sys
from .bob import Bob

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


    def move_bob(self, keys):
        if keys[pygame.K_LEFT] and self.bob_x > 0:
            self.bob_x -= self.bob_speed
        if keys[pygame.K_RIGHT] and self.bob_x < self.width - self.bob_width:
            self.bob_x += self.bob_speed
        if keys[pygame.K_UP] and self.bob_y > 0:
            self.bob_y -= self.bob_speed
        if keys[pygame.K_DOWN] and self.bob_y < self.height - self.bob_height:
            self.bob_y += self.bob_speed

    def draw_bob(self):
        # Dessine Bob à sa position actuelle sur l'écran
        self.screen.blit(self.bob.image, (self.bob.x, self.bob.y))

