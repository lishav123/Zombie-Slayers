
from pygame import image
from pygame import transform

from assets import NinjaSprite

class Ninja:
    def __init__(self, window, x, y, scale):
        self.ninja_sprite = NinjaSprite()
        self.current_state = self.ninja_sprite.idle
        self.x = x
        self.y = y
        self.window = window
        self._index = 0
        self.scale = scale

    def update_position(self, x, y):
        self.x += x
        self.y += y

    def update_state(self, state):
        if state == "idle":
            self.current_state = self.ninja_sprite.idle

        if state == "run":
            self.current_state = self.ninja_sprite.run

    def display_state(self):
        img = image.load(f"./assets/protagonist/png/{self.current_state[self._index]}")
        self.window.blit(
            transform.scale(img, (img.get_width() * self.scale,
                                 img.get_height() * self.scale)), (self.x, self.y))

        if self._index == len(self.current_state) - 1:
            self._index = 0
        self._index += 1

class BackgroundParallex:
    def __init__(self, window, x, y, scale):
        self.background = "./assets/background/Background.png"
        self.x = x
        self.y = y
        self.scale = scale
        self.window = window

    def update_position(self, x, y):
        self.x += x
        self.y += y

    def load_state(self):
        img = image.load(self.background)
        self.resize_image = transform.scale(img, (img.get_width() * self.scale, img.get_height() * self.scale))

    def parallex(self, velocity):
        self.window.blit(self.resize_image, (self.x, self.y))
        self.window.blit(self.resize_image, (self.x + self.resize_image.get_width(), self.y))
        self.window.blit(self.resize_image, (self.x - self.resize_image.get_width(), self.y))

        if self.x + self.resize_image.get_width() <= 0 and velocity < 0:
            self.x = 0

        if self.x > self.resize_image.get_width() and velocity > 0:
            self.x = 0

        self.x += velocity
