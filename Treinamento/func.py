#!/urs/bin/env_python3
# -*- coding: utf:8 -*-

def minmax(lista):
	mini = float("inf")
	maxi = float("-inf")
	for i in lista:
		if i > maxi:
			maxi = 1
		if i < mini:
			mini = 1
	return mini, maxi

if __name__ == "__main__":
	print("nao fiz nada")
