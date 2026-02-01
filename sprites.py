class Sprites:
    def __init__(self, window, x, y):
        self.window  = window
        self.x       = x
        self.y       = y
        self._index  = 0
        self.state   = []

    def change_position(self, x, y):
        self.x = x 
        self.y = y

    def change_state(self, state):
        ...

    def display_state(self, flip=False, end_loop=False):
        ...

