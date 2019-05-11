#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#x = input('Escreva:\n')

def tamanho(letras):
    return len(letras), 2*len(letras)

def nada():
    numeros = []
    x = 0
    print(numeros)

    while len(numeros) < 6:
        numeros.append(x)
        x = x + 1

    print(x)
    numeros.append(2)
    print(numeros)

    while 2 in numeros:
        numeros.remove(2)

    print(numeros)

    numeros + [2]

    numeros.reverse()

    sorted(numeros)
    a = 'ioiii'
    print(a)
    print(numeros)
    _,tam2 = tamanho(numeros)
    print(tam2)

def mostra_argumentos(func_decorada):
    def funcao(arg1, arg2):
        print('primeiro: %f, segundo: %f'% (arg1,arg2))
        return func_decorada
    return funcao

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(a = 0)
def soma(b):
    soma.a += b
    return soma.a

class Comidas:
    def __init__(self, nome, cor, quantidade, animal):
        self.nome = nome
        self.cor = cor
        self.quantidade = quantidade
        self.mostra_nome_e_cor()
        self.juliana_gosta()
        self.__animal = animal
    
    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, newx):
        self.__animal = -animal if newx < 0 else animal

    def mostra_nome_e_cor(self):
        print('A cor de %s é %s'% (self.nome, self.cor))
    def juliana_gosta(self):
        if self.nome == 'banana' or self.nome == 'mamão':
            return True
        else:
            return False        
    def __str__(self):
        return 'Tem'
    def __gt__(self, other):
        return self.quantidade > other.quantidade
    def __lt__(self, other):
        return self.quantidade < other.quantidade
    def __add__(self,other):
        return self.quantidade + other.quantidade 




    
        


if __name__ == "__main__":
    print("não fiz nada")    

