def static_vars(**kwargs):
	def decorate(func):
		print('O decorador é executado no início do programa')
		for k in kwargs:
			setattr(func, k, kwargs[k])
		return func
	return decorate


@static_vars(x=0)
def f():
	f.x=f.x+1
	return f.x
