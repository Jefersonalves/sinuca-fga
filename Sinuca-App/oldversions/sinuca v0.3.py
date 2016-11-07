#import pygame, sys
#from pygame.locals import *
from FGAme import *

#Adicionando o fundo da tela:

Back = draw.Circle(800, pos=pos.from_middle(0, 0), color='#32cd32')
#Test = draw.image('Snake_head2.png', pos = (400, 300))
world.add([Back])

world.add.margin(3)
        # Criando as bolas

#A = world.add.circle(25, pos=pos.from_middle(-330, 0), vel = (200, 35), color='grey')

A = world.add.circle(25, pos=pos.from_middle(-330, 0), color='white', mass='200')
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



#M = world.add.regular_poly(3, 3, pos=pos.from_middle(-500, 0), color='random', mass='100')

# Criando as bordas da mesa
P1 = world.add.aabb(shape=(10, 360), pos=(10, 300), mass='inf')
P2 = world.add.aabb(shape=(10, 360), pos=(790, 300), mass='inf')
P3 = world.add.aabb(shape=(310, 10), pos=(210, 520), mass='inf')
P4 = world.add.aabb(shape=(310, 10), pos=(580, 520), mass='inf')
P5 = world.add.aabb(shape=(310, 10), pos=(210, 80), mass='inf')
P6 = world.add.aabb(shape=(310, 10), pos=(580, 80), mass='inf')
PB = world.add.aabb(shape=(400, 5), pos=(400, 60), mass='inf')
PBa = world.add.aabb(shape=(5, 60), pos=(200, 32), mass='inf')
PBb = world.add.aabb(shape=(5, 60), pos=(600, 32), mass='inf')




        # self.A.line = draw.Segment(50, 50)
    
        # Definindo a velocidade angular na bola A
        # self.A.aboost(600)

# Definindo a constante de amortecimento
world.damping = 0.38

        #listen('mouse-button-down', function=self.A.move, args=(0, 0))
        #on('mouse-button-down', 'left').do(self.A.imove)

#@listen('mouse-button-down', 'left')
#def add_circle(pos):
#     world.pause()
#     world.circle = Circle(28, pos=pos, vel = (2000, 0), color='grey')
#     world.line = draw.Segment(pos, pos)
#     world.add([world.circle, world.line])

#@listen('mouse-long-press', 'left')
#def set_circle_velocity(pos):
#     world.line.end = (pos, pos)

#@listen('mouse-button-up', 'left')
#def launch_circle(pos):
#     world.resume()
#     world.remove(world.line)
#     world.circle.vel = 4 * world.line.direction
    
        #Definindo os controles do jogo: 
        #listen('long-press', 'down', function=self.A.move, args=(0, -5))
        #listen('long-press', 'up', function=self.A.move, args=(0, 5))
        #listen('long-press', 'left', function=self.A.move, args=(-5, 0))
        #listen('long-press', 'right', function=self.A.move, args=(5, 0)) 

        #Definindo os controles do jogo:
#@listen('key-down', 'space')
#def move_right():
#     A.vel = (220, 0)

@listen('frame-enter')
def ballh():
     if (A.y > 520) | (A.y < 80):
          A.pos = (200,300)
          A.vel = (0, 0)
     if (B.x > 790) | (B.x < 10) | (B.y > 520) | (B.y < 80):
          B.pos = (230,30)
          B.vel = (0, 0)
     if (C.x > 790) | (C.x < 10) | (C.y > 520) | (C.y < 80):
          C.pos = (265,30)
          C.vel = (0, 0)
     if (D.x > 790) | (D.x < 10) | (D.y > 520) | (D.y < 80):
          D.pos = (300,30)
          D.vel = (0, 0)
     if (E.x > 790) | (E.x < 10) | (E.y > 520) | (E.y < 80):
          E.pos = (335,30)
          E.vel = (0, 0)
     if (F.x > 790) | (F.x < 10) | (F.y > 520) | (F.y < 80):
          F.pos = (370,30)
          F.vel = (0, 0)
     if (G.x > 790) | (G.x < 10) | (G.y > 520) | (G.y < 80):
          G.pos = (405,30)
          G.vel = (0, 0)
     if (H.x > 790) | (H.x < 10) | (H.y > 520) | (H.y < 80):
          H.pos = (440,30)
          H.vel = (0, 0)
     if (I.x > 790) | (I.x < 10) | (I.y > 520) | (I.y < 80):
          I.pos = (475,30)
          I.vel = (0, 0)
     if (J.x > 790) | (J.x < 10) | (J.y > 520) | (J.y < 80):
          J.pos = (510,30)
          J.vel = (0, 0)
     if (L.x > 790) | (L.x < 10) | (L.y > 520) | (L.y < 80):
          L.pos = (545,30)
          L.vel = (0, 0)


coord = (-400, -300)
coord2 = (400,300)
coord3 = (0, 0)

@listen('mouse-button-down', 'left')
def x_vel(pos):
     world.pause()
     aux = (pos)
     world.line = draw.Segment(A.pos, pos)
     world.add(world.line)
    
@listen('mouse-button-up', 'left')
def y_vel(pos):
     world.line.linewidth = '0'
     A.vel = (pos)
     A.vel -= (A.pos)
     A.vel *= 4
     world.resume()

@listen('key-down', 'e')
def exit1():
     exit()

run()



