from FGAme import *
import sys; sys.path.append('.')
from Ball import *

def AddTable(world):
	world.add.aabb(shape=(20, 360), pos=(10, 300), mass='inf')
	world.add.aabb(shape=(20, 360), pos=(790, 300), mass='inf')
	world.add.aabb(shape=(310, 20), pos=(210, 520), mass='inf')
	world.add.aabb(shape=(310, 20), pos=(580, 520), mass='inf')
	world.add.aabb(shape=(310, 20), pos=(210, 80), mass='inf')
	world.add.aabb(shape=(310, 20), pos=(580, 80), mass='inf')

def AddPlacar(world):
	world.add.aabb(shape=(400, 5), pos=(400, 60), mass='inf')
	world.add.aabb(shape=(5, 60), pos=(200, 32), mass='inf')
	world.add.aabb(shape=(5, 60), pos=(600, 32), mass='inf')

def AddBalls(world, balls):
	positions = [(140, 0), (180, 20), (180, -20), (220,  30), (220, 0), (220, -30), (260, 40), (260, 20), (260, -20), (260, -40)]
	for position in positions:
		x,y = position
		balls.append(Ball(pos = pos.from_middle(x,y), color='random'))
	world.add(balls)