def mostra_parametros(func_decorada):
	def nova_func(*arg1):
#		print('a:%i b:%i' % (arg1, arg2))
		print(arg1)
		return func_decorada(*arg1)
	return nova_func

@mostra_parametros
def soma(a, b):
	return a+b

@mostra_parametros
def outrafuncao(a,b,c):
	return a+b+c
