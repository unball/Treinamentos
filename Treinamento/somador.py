#!/urs/bin/env_python3
# -*- coding: utf:8 -*-
def static_vars(**kwargs):
	def decorate(func):
		for k in kwargs:
			setattr(func, k, kwargs[k])
		return func
	return decorate




@static_vars(arg=0)
def contador():
	cont = contador.arg
	contador.arg += 1
	return cont

while(True):
	som = contador()
	if som == 100:
		break
	print(som)
