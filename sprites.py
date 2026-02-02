from assets import NinjaSprite
from assets import ZombieSprite

from pygame import transform
from pygame import image

class Sprites:
    def __init__(self, window, x, y, scale, sprite, location):
        self.window  = window
        self.x       = x
        self.y       = y
        self.scale   = scale
        self._index  = 0
        self.sprite = sprite
        self.state   = sprite.IDLE
        self.location = location

    def change_position(self, x, y):
        self.x = x 
        self.y = y

    def change_state(self, state):
        if state == "idle":
            self.state = self.sprite.IDLE

        elif state == "run":
            self.state = self.sprite.RUN

    def display_state(self, flip=False, end_loop=False):
        try:
            self.state[self._index]
        except IndexError:
            self._index = 0
        finally:
            img = image.load(f"{self.location}/{self.state[self._index]}")
            resize = transform.scale(img, (img.get_width() * self.scale, img.get_height() * self.scale))
            self.window.blit(transform.flip(resize, flip, False), (self.x, self.y))

            if self._index == len(self.state) - 1:
                self._index = 0
            self._index += 1

class Ninja(Sprites):
    def __init__(self, window, x, y, scale):
        super().__init__(window, x, y, scale, NinjaSprite, "./assets/protagonist/png")

class Zombie(Sprites):
    def __init__(self, window, x, y, scale):
        super().__init__(window, x, y, scale, ZombieSprite, "./assets/enemy/male")
