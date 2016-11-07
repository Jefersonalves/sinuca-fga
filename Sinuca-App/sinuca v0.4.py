#import pygame, sys
#from pygame.locals import *

import sys; sys.path.append('.')
from library import *
from FGAme import *
import random
conf.set_framerate(60)

#Adicionando o fundo e a margem da tela:
Back = draw.Circle(800, pos=pos.from_middle(0, 0), color='#32cd32')
world.add(Back)
world.add.margin(3)

# Criando as bolas
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

# Criando as bordas da mesa
AddTable(world)

# Definindo a velocidade angular na bola A
# self.A.aboost(600)

# Definindo a constante de amortecimento
world.damping = 1.16

# Definindo as condições que as bolas são "encaçapadas"
@listen('frame-enter')
def ballh():
     if (A.y > 520) | (A.y < 85):
          A.pos = (200,300)
          A.vel = (0, 0)
     if (B.x > 790) | (B.x < 10) | (B.y > 520) | (B.y < 85):
          B.pos = (230,30)
          B.vel = (0, 0)
     if (C.x > 790) | (C.x < 10) | (C.y > 520) | (C.y < 85):
          C.pos = (265,30)
          C.vel = (0, 0)
     if (D.x > 790) | (D.x < 10) | (D.y > 520) | (D.y < 85):
          D.pos = (300,30)
          D.vel = (0, 0)
     if (E.x > 790) | (E.x < 10) | (E.y > 520) | (E.y < 85):
          E.pos = (335,30)
          E.vel = (0, 0)
     if (F.x > 790) | (F.x < 10) | (F.y > 520) | (F.y < 85):
          F.pos = (370,30)
          F.vel = (0, 0)
     if (G.x > 790) | (G.x < 10) | (G.y > 520) | (G.y < 85):
          G.pos = (405,30)
          G.vel = (0, 0)
     if (H.x > 790) | (H.x < 10) | (H.y > 520) | (H.y < 85):
          H.pos = (440,30)
          H.vel = (0, 0)
     if (I.x > 790) | (I.x < 10) | (I.y > 520) | (I.y < 85):
          I.pos = (475,30)
          I.vel = (0, 0)
     if (J.x > 790) | (J.x < 10) | (J.y > 520) | (J.y < 85):
          J.pos = (510,30)
          J.vel = (0, 0)
     if (L.x > 790) | (L.x < 10) | (L.y > 520) | (L.y < 85):
          L.pos = (545,30)
          L.vel = (0, 0)

# Definindo os controles para as ações do jogo

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


