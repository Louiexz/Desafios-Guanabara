def fatorial(num=0, show=False):
	''' fatorial(n, show=False)
		>>> Calcula fatorial de um número
		:para num: O número a ser calculado
		:para show: Mostra ou não a conta
		:return: Retorna o valor Fatorial de um número '''
	multi = num
	print(f'\033[37m {num}! =', end= ' ')
	for c in range(num, 0, -1):
		if c != num:
			multi *= c
		if show == True:
			if c != 1:
				print(c, end= ' x ') 
			if c == 1:
				print(c, end= ' = ')
				
	return multi


#help(fatorial)
print(fatorial(5, True))

#fatorar = int(input(' Digite um número inteiro: '))
#escolha = str(input(' Aparecer o processo: [S/N] ')).upper()
#print()
#if escolha == 'S':
#	hidden = True
#	print('1 =', fatorial(fatorar, hidden))
#else:
#	hidden = False
#	print(fatorar, escolha)