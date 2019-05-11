#!/usr/bin/env python3
#-*- coding: utf-8 -*-
class Plantas (object):
	nome = 'Plantas'
	"""docstring for Plantas """
	def __init__(self, raiz, folha):
		self.raiz = raiz
		self.folha = folha
		self.mostra_info()
	def mostra_info(self):
		print('Plantinha')
	def tamanho_planta (self):
		return self.folha - self.raiz
	def __str__(self):
		return 'Plantinha de tamanho: %s' %self.tamanho_planta ()
	def __gt__(self, other):
		return self.folha > other.folha

	@property
	def folha(self):
		return self.__folha
		
	@folha.setter
	def folha(self, nfolha):
		self.__folha = -folha if nfolha < 0 else folha