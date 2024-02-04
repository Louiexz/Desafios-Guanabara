lista = [0,0,0,0,0]
for c in range(0,5):
	num = float(input(' Digite um número: '))
	if num <=  lista[0]:
		lista.insert(0, num)
		print(' O valor foi posto na posicão 0')
	elif num >= lista[0] and num <= lista[1]:
		lista.insert(1, num)
		print(' O valor foi posto na posição 1')
	elif num >= lista[1] and num <= lista[2]:
		lista.insert(2, num)
		print(' O valor foi posto na posição 2')
	elif num >= lista[2] and num <= lista[3]:
		lista.insert(3, num)
		print(' O valor foi posto na posição 3')
	else:
		lista.insert(4, num)
		print(' O valor foi posto no fim da lista')
	lista.remove(0)
print('\n Os valores em ordem:',lista)