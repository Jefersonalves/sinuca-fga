from FGAme import *

class Ball(Circle):
    def __init__(self, *args, **kwargs):
        Circle.__init__(self, *args, radius=22, mass='100', **kwargs)