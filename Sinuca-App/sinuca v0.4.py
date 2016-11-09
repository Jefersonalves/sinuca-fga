import sys; sys.path.append('.')
from library import *
from FGAme import *
import random
conf.set_framerate(60)

#Adiciona o fundo e a margem da tela
Back = draw.Circle(800, pos=pos.from_middle(0, 0), color='#32cd32')
world.add(Back)
world.add.margin(3)

# Cria as bordas da mesa
AddTable(world)

# Adiciona as bolas
whiteBall = world.add.circle(25, pos=pos.from_middle(-330, 0), color='white', mass='200')
balls = []
AddBalls(world, balls)

# Define a constante de amortecimento
world.damping = 1.16


# Define as condições que as bolas são encaçapadas
@listen('frame-enter')
def ballh():
     y = 230
     if (whiteBall.y > 520) | (whiteBall.y < 85):
          whiteBall.pos = (200,300)
          whiteBall.vel = (0, 0)
     for ball in balls:
          if (ball.x > 790) | (ball.x < 10) | (ball.y > 520) | (ball.y < 85):
             ball.pos = (y,30)
             ball.vel = (0, 0) 
             y = y + 35 

# Definindo os controles para as ações do jogo
@listen('mouse-button-down', 'left')
def x_vel(pos):
     world.pause()
     aux = (pos)
     world.line = draw.Segment(whiteBall.pos, pos)
     world.add(world.line)
    
@listen('mouse-button-up', 'left')
def y_vel(pos):
     world.line.linewidth = '0'
     whiteBall.vel = (pos)
     whiteBall.vel -= (whiteBall.pos)
     whiteBall.vel *= 4
     world.resume()

@listen('key-down', 'e')
def exit1():
     exit()

run()


