from FGAme import *

def AddTable(world):
     P1 = world.add.aabb(shape=(10, 360), pos=(10, 300), mass='inf')
     P2 = world.add.aabb(shape=(10, 360), pos=(790, 300), mass='inf')
     P3 = world.add.aabb(shape=(310, 10), pos=(210, 520), mass='inf')
     P4 = world.add.aabb(shape=(310, 10), pos=(580, 520), mass='inf')
     P5 = world.add.aabb(shape=(310, 10), pos=(210, 80), mass='inf')
     P6 = world.add.aabb(shape=(310, 10), pos=(580, 80), mass='inf')
     PB = world.add.aabb(shape=(400, 5), pos=(400, 60), mass='inf')
     PBa = world.add.aabb(shape=(5, 60), pos=(200, 32), mass='inf')
     PBb = world.add.aabb(shape=(5, 60), pos=(600, 32), mass='inf')

def AddBalls(world, balls):
	balls.append(Circle(22, pos=pos.from_middle(140, 0), color='random', mass='100'))
	balls.append(Circle(22, pos=pos.from_middle(180, 20), color='random', mass='100'))
	balls.append(Circle(22, pos=pos.from_middle(180, -20), color='random', mass='100'))
	balls.append(Circle(22, pos=pos.from_middle(220,  30), color='random', mass='100'))
	balls.append(Circle(22, pos=pos.from_middle(220, 0), color='random', mass='100'))
	balls.append(Circle(22, pos=pos.from_middle(220, -30), color='random', mass='100'))
	balls.append(Circle(22, pos=pos.from_middle(260, 40), color='random', mass='100'))
	balls.append(Circle(22, pos=pos.from_middle(260, 20), color='random', mass='100'))
	balls.append(Circle(22, pos=pos.from_middle(260, -20), color='random', mass='100'))
	balls.append(Circle(22, pos=pos.from_middle(260, -40), color='random', mass='100'))
	world.add(balls)
