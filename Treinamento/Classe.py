#!/urs/bin/env_python3
# -*- coding: utf:8 -*-

class Fruta():
	def __init__(self, nome, peso, doce, agrotoxico = 0):
		self.nome = nome
		self.peso = peso
		self.doce = doce
		self.__agrotoxico = agrotoxico

	def __str__(self):
		return "A fruta %s tem peso %f e docura %f" %(self.nome, self.peso, self.doce)

	def __ge__(self, other):
		return self.peso >= other.peso

	def agrotoxico(self):
		veneno = 0
		veneno = 1 if self.__agrotoxico > 5 else 0
		if veneno == 1:
			print("envenenado")
		else
			print("fruta segura")