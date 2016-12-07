from FGAme import *

class Ball(Circle):
    def __init__(self, *args, **kwargs):
        Circle.__init__(self, *args, radius=10, mass='130', **kwargs)
