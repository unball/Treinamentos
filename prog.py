#!/usr/bin/env python3
# -*- coding: utf-8 -*-

count = 0

while True:
	if (input("Quer continuar o programa? [y/n]\n") == 'y'):
		print('Você é demais! 👍🧠')
		count = count + 1
	else:
		if(count == 0):
			print('Seu chato 😡🧟...')
		else:
			print('Delícia!')
		break

#print(type(a))
