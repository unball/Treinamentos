#!/usr/bin/env python

# Representa um vetor
class Vetor:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.x = 0

# Representa uma area como um paralelepipedo definido por dois pontos no plano
# Tem um metodo que indica se a bola esta nessa area
class Area:
	def __init__(self, p1, p2):
		self.x1 = p1[0]
		self.x2 = p2[0]
		self.y1 = p1[1]
		self.y2 = p2[1]

#	def inside(self, bola):

# Classe que representa um robo no campo. Um robo contem um id ou indice
# Contem a posicao atual, a velocidade e o angulo que sao calculados
# usando a visao e IMU
class Robo:
	def __init__(self, id):
		self.id = id
		self.posicao = Vetor()
		self.velocidade = Vetor()
		self.angulo = 0

#	def getPosicao(self):
#	def getVelocidade(self):
#	def getAngulo(self):

# Classe que representa um robo do nosso time no campo
# A classe tambem deve ter metodos que criem trajetorias (linha reta ou A*) para um
# determinado ponto e obstaculos virtuais (no caso do A*)
# Essa classe tambem implementa movimentos gerais para todos os tipos de jogadores como movimentoChutar()
# A classe deve ter um valor que indica o tipo de jogador do robo como Goleiro, Zagueiro, ...
class NossoRobo(Robo):
	def __init__(self, tipo, id):
		self.tipo = tipo
		Robo.__init__(self, id)

#	def goTo(self, destino, tipoTrajetoria='reta', obstaculosVirtuais=None):
#	def movimentoChutar(self):
#	def tipoJogador(self):

# Classe que implemena movimentos especializados de um goleiro
class Goleiro:
	def __init__(self, gol):
		self.gol = gol

#	def movimentoGoleiro1(self, robo):

# Classe que implemena movimentos especializados de um atacante
class Atacante:
	def __init__(self):
		pass

#	def movimentoAtacante1(self, robo):
#	def movimentoAtacante2(self, robo):

# Classe que implementa movimentos especializados de um zagueiro
class Zagueiro:
	def __init__(self):
		pass

#	def movimentoZagueiro1(self, robo):

# Classe que representa a bola no campo.
# Deve ter getters para a posicao e velocidade da bola com base na visao
class Bola:
	def __init__(self):
		self.posicao = Vetor()
		self.velocidade = Vetor()

#	def getPosicao(self):
#	def getVelocidade(self):

# Classe que representa a area do gol no campo.
# Dado uma bola a classe tem um metodo que diz se ela esta dentro do gol
class Gol:
	def __init__(self):
		self.area = Area((0,0), (0,0))

#	def isGol(self, bola):

# Classe que representa uma pequena area no campo
class PequenaArea(Area):
	def __init__(self):
		Area.__init__(self, (0,0), (0,0))
		pass


# Classe que representa uma grande area no campo
class GrandeArea(Area):
	def __init__(self):
		Area.__init__(self, (0,0), (0,0))
		pass


# Classe que instancia os elementos do campo como gol, areas do campo,
# a bola e os robos
class Campo:
	def __init__(self):
		self.golAdversario = Gol()
		self.gol = Gol()
		self.pequenaAreaAdversaria = PequenaArea()
		self.pequenaArea = PequenaArea()
		self.grandeAreaAdversaria = GrandeArea()
		self.grandeArea = GrandeArea()
		self.bola = Bola()
		self.goleiro = NossoRobo(Goleiro, 0)
		self.atacantes = [NossoRobo(Atacante, i) for i in range(1,3)]
		self.zagueiros = [NossoRobo(Zagueiro, i) for i in range(3,5)]
		self.jogadoresAdversarios = [Robo(i) for i in range(5,10)]

# Classe mais abstrata, deve coordenar os movimentos dos robos em self.campo
# Obtem informacao de posicao, velocidade de self.campo e a partir disso define
# quais devem ser as acoes de cada robo.
class Estrategia:
	def __init__(self):
		self.campo = Campo()
		self.placar = (0,0)


e = Estrategia()
