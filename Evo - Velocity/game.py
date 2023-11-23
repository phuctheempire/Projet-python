import sys
import random
from world import World
from tools.graphic_tool import *


class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        # world
        self.world = World(10, 10, self.width, self.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(5)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
        self.world.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.world.draw(self.screen)

        draw_text(
            self.screen,
            'day={}'.format(self.world.day_count),
            25,
            (255, 255, 255),
            (10, 40)
        )

        self.world.tick_count += 1
        draw_text(
            self.screen,
            'tick={}'.format(self.world.tick_count),
            25,
            (255, 255, 255),
            (10, 10)
        )

        pg.display.flip()

