from FGAme import *
import sys; sys.path.append('.')
from Ball import *

def AddTable(world):
	P1 = world.add.aabb(shape=(9, 300), pos=(36, 300),color='#5aa069', mass='inf')
	P2 = world.add.aabb(shape=(9, 300), pos=(765, 300),color='#5aa069', mass='inf')
	P3 = world.add.aabb(shape=(310, 9), pos=(225, 485),color='#5aa069', mass='inf')
	P4 = world.add.aabb(shape=(310, 9), pos=(576, 485),color='#5aa069', mass='inf')
	P5 = world.add.aabb(shape=(310, 9), pos=(225, 116),color='#5aa069', mass='inf')
	P6 = world.add.aabb(shape=(310, 9), pos=(576, 116),color='#5aa069', mass='inf')

	Pb1 = world.add.aabb(shape=(27, 289), pos=(17, 300),color='#a25541', mass='inf')
	Pb2 = world.add.aabb(shape=(27, 289), pos=(785, 300),color='#a25541', mass='inf')
	Pb3 = world.add.aabb(shape=(293, 27), pos=(223, 504),color='#a25541', mass='inf')
	Pb4 = world.add.aabb(shape=(293, 27), pos=(579, 504),color='#a25541', mass='inf')
	Pb5 = world.add.aabb(shape=(293, 27), pos=(223, 96),color='#a25541', mass='inf')
	Pb6 = world.add.aabb(shape=(293, 27), pos=(579, 96),color='#a25541', mass='inf')

def AddBalls(world, balls):
	positions = [(178, 0), (196, 10), (196, -10), (214,  15), (214, 0), (214, -15), (232, 20), (232, 10), (232, -10), (232, -20), (250, 0), (250, 20), (250, -20), (250, 40), (250, -40)]
	for position in positions:
		x,y = position
		balls.append(Ball(pos = pos.from_middle(x,y), color='random'))
	world.add(balls)
