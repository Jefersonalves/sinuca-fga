import sys; sys.path.append('.')
from library import *
from Ball import *
from WhiteBall import *
from FGAme import *
import random
conf.set_framerate(60)

#Adiciona o fundo e uma margem para a tela
conf.set_background('white', image="table10")
world.add.margin(0)

# Cria os limites para as bordas da mesa
AddTable(world)

# Adiciona as bolas
whiteBall = WhiteBall()
world.add(whiteBall)
balls = []
AddBalls(world, balls)

# Define o indicador do player da que fará a tacada
playerturn = world.add.circle(8, pos=(428, 576), color='green', mass = 'inf')

# Define a constante de amortecimento
world.damping = 0.85

# Define as condições que as bolas são encaçapadas
@listen('frame-enter')
def ballh():
     y = 258
     if ((whiteBall.x > 758) or (whiteBall.x < 42) or (whiteBall.y > 478) or (whiteBall.y < 122)):
          whiteBall.pos = (220,300)
          whiteBall.vel = (0, 0)
     for ball in balls:
          if ((ball.x > 758) or (ball.x < 42) or (ball.y > 478) or (ball.y < 122)):
               ball.pos = (y, 40)
               ball.vel = (0, 0)
               y = y + 20

# Definindo os controles para as ações do jogo
@listen('mouse-button-down', 'left')
def x_vel(pos):
     world.pause()
     world.line = draw.Segment(whiteBall.pos, pos)
     world.add(world.line)
     play("cuehit")

@listen('mouse-button-up', 'left')
def y_vel(pos):
     if (playerturn.pos == (428, 576)):
          playerturn.pos = (428, 553)
     else:
          playerturn.pos = (428, 576)
     world.line.linewidth = '0'
     whiteBall.vel = (pos)
     whiteBall.vel -= (whiteBall.pos)
     whiteBall.vel *= 2
     world.resume()

@listen('key-down', 'e')
def exit1():
     exit()

run()
