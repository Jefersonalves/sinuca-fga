#import pygame, sys
#from pygame.locals import *
from FGAme import *

world.add.margin(3)

        # Criando as bolas

#A = world.add.circle(25, pos=pos.from_middle(-330, 0), vel = (200, 35), color='grey')

A = world.add.circle(25, pos=pos.from_middle(-330, 0), color='grey', mass='200')
B = world.add.circle(22, pos=pos.from_middle(140, 0), color='random', mass='100')
C = world.add.circle(22, pos=pos.from_middle(180, 20), color='random', mass='100')
D = world.add.circle(22, pos=pos.from_middle(180, -20), color='random', mass='100')
E = world.add.circle(22, pos=pos.from_middle(220,  30), color='random', mass='100')
F = world.add.circle(22, pos=pos.from_middle(220, 0), color='random', mass='100')
G = world.add.circle(22, pos=pos.from_middle(220, -30), color='random', mass='100')
H = world.add.circle(22, pos=pos.from_middle(260, 40), color='random', mass='100')
I = world.add.circle(22, pos=pos.from_middle(260, 20), color='random', mass='100')
J = world.add.circle(22, pos=pos.from_middle(260, -20), color='random', mass='100')
L = world.add.circle(22, pos=pos.from_middle(260, -40), color='random', mass='100')

# Criando as bordas da mesa
P1 = world.add.aabb(shape=(10, 360), pos=(10, 300), mass='inf')
P2 = world.add.aabb(shape=(10, 360), pos=(790, 300), mass='inf')
P3 = world.add.aabb(shape=(310, 10), pos=(210, 520), mass='inf')
P4 = world.add.aabb(shape=(310, 10), pos=(580, 520), mass='inf')
P5 = world.add.aabb(shape=(310, 10), pos=(210, 80), mass='inf')
P6 = world.add.aabb(shape=(310, 10), pos=(580, 80), mass='inf')

        # Adicionando-os a simulacao
        #self.add([P1, P2, P3, P4, P5, P6, self.A, self.B, self.C, self.D, self.E , self.F, self.G, self.H , self.I, self.J, self.L])
        # self.A.line = draw.Segment(50, 50)
    
        # Definindo a velocidade angular na bola A
        # self.A.aboost(600)

        # Definindo a constante de amortecimento
        #self.damping = 0.38

        #@listen('mouse-button-down', 'left')
        #def add_circle(self, pos):
        #     self.pause()
        #     self.circle = Circle(28, pos=pos, vel = (2000, 0), color='grey')
        #     self.line = draw.Segment(pos, pos)
        #     self.add([self.circle, self.line])
     
        #listen('mouse-button-down', function=self.A.move, args=(0, 0))
        #on('mouse-button-down', 'left').do(self.A.imove)

#on('long-press', 'right').do(A.move, 0, -5).do(B.move, 0,-5)

@listen('mouse-button-down', 'left')
def add_circle(pos):
     world.pause()
     world.circle = Circle(28, pos=pos, vel = (2000, 0), color='grey')
     world.line = draw.Segment(pos, pos)
     world.add([world.circle, world.line])

@listen('mouse-long-press', 'left')
def set_circle_velocity(pos):
     world.line.end = (pos, pos)

@listen('mouse-button-up', 'left')
def launch_circle(pos):
     world.resume()
     world.remove(world.line)
     world.circle.vel = 4 * world.line.direction
    
        #Definindo os controles do jogo: 
        #listen('long-press', 'down', function=self.A.move, args=(0, -5))
        #listen('long-press', 'up', function=self.A.move, args=(0, 5))
        #listen('long-press', 'left', function=self.A.move, args=(-5, 0))
        #listen('long-press', 'right', function=self.A.move, args=(5, 0)) 

        #[NAO FUNCIONA] Definindo os controles do jogo:
@listen('key-down', 'space')
def move_right():
     A.vel = (220, 0)


run()



