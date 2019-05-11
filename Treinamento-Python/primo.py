primos = []

def p(x):
	if(x < 2):
		return False
	for i in range(2,int(x**0.5)):
		if(x % i == 0):
			return False
	primos.append(x)
	return True

def f(x):
	primos = [2]
	primosatestar = [2]
	if(x < 2):
		return []
	for n in range(2,x):
		primo = True
		for p in primos:
			if(n % p == 0):
				primo = False
		if(primo):
			primos.append(n)
	return primos

if __name__ == "__main__":
	print('Esse é o módulo principal')
