from FGAme import *

class WhiteBall(Circle):
    def __init__(self, *args, **kwargs):
        Circle.__init__(self, *args, radius=11, pos=pos.from_middle(-330, 0), mass='200', color='white', **kwargs)