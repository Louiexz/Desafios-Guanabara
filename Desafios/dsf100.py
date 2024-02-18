from random import randint
from time import sleep
# AS PARTES VERDES NÃO SÃO ORIGINAIS DO DESAFIO

#saida = []; total = []; qt = []
#escolha = 's'
#while escolha != 'n':
numeros = []
def sorteio():
	for c in range(0, 10):
		num = randint(1, 10)
		print(f' {num}', end= ' ', flush= True)
		sleep(0.5)
		numeros.append(num)
	print('-> Acabou')
sorteio()


def somaPar():
	pares = 0
	resultado = 0
	par = []
	for pos, valor in enumerate(numeros):
		if valor % 2 == 0:
			resultado += valor
#			pares += 1
			pares = valor
			par.append(pares)
#		total.append(resultado)
#		qt.append(pares)
#	print(f' Soma dos {pares} números pares: {resultado}')
	print(f'\n Somando os números pares {par} temos: {resultado}')
#	saida.append(total[:]); saida.append(qt[:])
somaPar()
#	escolha = str(input(' Deseja continuar? [S/N] ')).lower()
#print(saida)