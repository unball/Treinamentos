class Animal(object):
	a = 'atributo da classe'
	def __init__(self, nome):
		self.nome = nome
		self.__diasDeVida = 100
	def f(self):
		print("Sou um animal")
	def __str__(self):
		return "Sou instância da classe Animal e meu nome é " + self.nome

	def __lt__(self, other):
		return self.nome < other.nome

	def __add__(self, other):
		return Animal(self.nome+other.nome)

	@property
	def diasDeVida(self):
		return self.__diasDeVida

	@diasDeVida.setter
	def diasDeVida(self, diasDeVidaNovo):
		self.__diasDeVida = diasDeVidaNovo if self.__diasDeVida < diasDeVidaNovo else self.__diasDeVida
