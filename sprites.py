from assets import NinjaSprite
from assets import ZombieSprite

from pygame import transform
from pygame import image

'''
TODO 1: Complete endloop functionality
TODO 2: Complete test with attack and throw
TODO 3: Plan the AI
TODO 4: Plan the senario or flow of game
'''

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

        self._loop_stack = []

    def change_position(self, x, y):
        self.x = x 
        self.y = y

    def change_state(self, state, endloop=False):

        if state == "idle":
            self.state = self.sprite.IDLE

        elif state == "run":
            self.state = self.sprite.RUN

        elif state == "throw":
            self.state = self.sprite.THROW
        
        if endloop:
            self._loop_stack.append({"state_name": state, "state_data": self.state})

        print(f"STATE: {state} | ENDLOOP: {endloop} | LOOP_STACK: {self._loop_stack}")

    def sprites_collide(self, other_sprite):
        ...

    def display_state(self, flip=False):
        try:
            self.state[self._index]
        except IndexError:
            self._index = 0
            print(f"EXCEPTION HERE: index is {self._index}, computing: {self.state}\n")

        finally:
            img = None
            if self._loop_stack:
                last_frame = len(self._loop_stack[0]["state_data"])
                img = image.load(f"{self.location}/{self._loop_stack[0]["state_data"][self._index]}")

                if self._index == last_frame - 1:
                    self._loop_stack.pop(0)
                    self._index = 0

            else:
                img = image.load(f"{self.location}/{self.state[self._index]}")
                
            resize = transform.scale(img, (img.get_width() * self.scale, img.get_height() * self.scale))
            self.window.blit(transform.flip(resize, flip, False), (self.x, self.y))

            if self._index == len(self.state) - 1 and self._loop_stack:
                self._index = 0
            self._index += 1

class Ninja(Sprites):
    def __init__(self, window, x, y, scale):
        super().__init__(window, x, y, scale, NinjaSprite, "./assets/protagonist/png")

class Zombie(Sprites):
    def __init__(self, window, x, y, scale):
        super().__init__(window, x, y, scale, ZombieSprite, "./assets/enemy/male")
