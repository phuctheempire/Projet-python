class Environment:
    def __init__(self):
        self.tick = 0
        self.day = 0

    def next_step(self):
        self.tick += 1
        if self.tick == 100:
            self.day += 1
            self.tick = 0
