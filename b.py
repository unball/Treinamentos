def minmax(lista):
	min = float('inf')
	max = float('-inf')
	for i in lista:
		if(i > max):
			max = i
		if(i < min):
			min = i
	return min,max
