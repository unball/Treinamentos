#!/urs/bin/env_python3
# -*- coding: utf:8 -*-

def func(fruta):
	return fruta + "banana", fruta + "pera"

def mostra_parametros(func_decorada):
	def nova_func(arg1, arg2):
		print("a:%i, b:%i" %(arg1, arg2))

		return (func_decorada(arg1, arg2))
		
	return nova_func




@mostra_parametros
def soma(a, b):
	return a + b

num = [1, 0, 0 , 1]
num2 = [1, 2, 3, 4]

print(num[0:2])
print(num[::-1])
print(num[::-2])
num.append(2)
print(num[:])
num.insert(2, 3)
print(num[:])
del num[3]
print(num[:])
num.remove(2)
print(num[:])


if 3 in num:
	print("tem")

num = num * 3
print(num[:])
num = [1, 0, 0 , 1]
num += num
print(num[:])
num = [1, 0, 0 , 1]
num = num + [1]
print(num[:])
num = [1, 0, 0 , 1]
num = num + num2
print(num[:])

lista = ['a', 'b', 'c', 'd']
lista.reverse()
print(lista[:])
lista.sort()
print(lista[:])
sorted(lista)
print(lista[:])

print(num.count(1))

nome = input("Digite seu nome:").split("a")
print(nome)

for i in range(0, 5):
	print(".")

ok = [x**2 for x in num]
print(ok)

su = soma(12, 13)
print(su)