import pygame as pg
from entities.Bob import Bob
TILE_SIZE = 64


def draw_text(screen, text, size, colour, pos):
    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect(topleft=pos)

    screen.blit(text_surface, text_rect)


def load_images():
    block = pg.image.load("graphics/block.png").convert_alpha()
    bob = pg.image.load("graphics/bob.png").convert_alpha()

    return {
        "block": block,
        "bob": bob
    }


def draw_bob(screen, bob: Bob):
    render_pos = bob.world.world[bob.x][bob.y]["render_pos"]
    screen.blit(bob.image,
                (render_pos[0] + bob.world.width / 2,
                 render_pos[1] + TILE_SIZE))

    # Calculate the width of the energy bar based on the energy level
    bar_width = int((bob.energy / bob.energy_max) * 50)  # Adjust the multiplier as needed

    # Draw the energy bar above the Bob
    pg.draw.rect(screen, (0, 255, 0), (render_pos[0] + bob.world.width / 2 + TILE_SIZE / 2,
                                       render_pos[1] + TILE_SIZE * 1.25,
                                       bar_width, 5))

    # draw velocity
    velocity_text = f"Vel: {bob.effective_velocity:.2f} VelBuf: {bob.velocity_buffer}"  # Format the velocity
    # to two decimal places
    draw_text(screen,
              velocity_text,
              12,
              (255, 255, 255),
              (render_pos[0] + bob.world.width / 2 + TILE_SIZE / 2,
               render_pos[1] + TILE_SIZE * 1)
              )
