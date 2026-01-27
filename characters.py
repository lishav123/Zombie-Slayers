
from pygame import image

from assets import NinjaSprite

class Ninja:
    def __init__(self, window, x, y):
        self.ninja_sprite = NinjaSprite()
        self.current_state = self.ninja_sprite.idle
        self.x = x
        self.y = y
        self.window = window
        self._index = 0

    def update_position(self, x, y):
        self.x += x
        self.y += y

    def update_state(self, state):
        if state == "idle":
            self.current_state = self.ninja_sprite.idle

        if state == "run":
            self.current_state = self.ninja_sprite.run

    def display_state(self):
        self.window.blit(image.load(f"./assets/protagonist/png/{self.current_state[self._index]}"), (self.x, self.y))

        if self._index == len(self.current_state) - 1:
            self._index = 0
        self._index += 1
