from FGAme import *

class Sinuca(World):

   # @listen('mouse-button-down', 'left')
   # def add_circle(self, pos):
   #     self.pause()
   #     self.circle = Circle(28, pos=pos, vel = (2000, 0), color='grey')
   #     self.line = draw.Segment(pos, pos)
   #     self.add([self.circle, self.line])   

    def init(self):

        # Criando as bolas
        self.A = Circle(25, pos=pos.from_middle(-330, 0), vel = (2000, 35), color='grey')
        self.B = Circle(22, pos=pos.from_middle(140, 0), color='red')
        self.C = Circle(22, pos=pos.from_middle(180, 20), color='red')
        self.D = Circle(22, pos=pos.from_middle(180, -20), color='red')
        self.E = Circle(22, pos=pos.from_middle(220,  30), color='red')
        self.F = Circle(22, pos=pos.from_middle(220, 0), color='red')
        self.G = Circle(22, pos=pos.from_middle(220, -30), color='red')
        self.H = Circle(22, pos=pos.from_middle(260, 40), color='red')
        self.I = Circle(22, pos=pos.from_middle(260, 20), color='red')
        self.J = Circle(22, pos=pos.from_middle(260, -20), color='red')
        self.L = Circle(22, pos=pos.from_middle(260, -40), color='red')

      # Criando as bordas da mesa
        P1 = world.add.aabb(shape=(10, 360), pos=(10, 300), mass='inf')
        P2 = world.add.aabb(shape=(10, 360), pos=(790, 300), mass='inf')
        P3 = world.add.aabb(shape=(310, 10), pos=(210, 520), mass='inf')
        P4 = world.add.aabb(shape=(310, 10), pos=(580, 520), mass='inf')
        P5 = world.add.aabb(shape=(310, 10), pos=(210, 80), mass='inf')
        P6 = world.add.aabb(shape=(310, 10), pos=(580, 80), mass='inf')

      # Adicionando-os a simulacao
        self.add([P1, P2, P3, P4, P5, P6, self.A, self.B, self.C, self.D, self.E , self.F, self.G, self.H , self.I, self.J, self.L])        #self.A.line = draw.Segment(50, 50)
    
      # Definindo a velocidade angular na bola A
      # self.A.aboost(600)

        # Definindo a constante de amortecimento
        self.damping = 0.38

if __name__ == '__main__':
    world = Sinuca()
    world.run()
