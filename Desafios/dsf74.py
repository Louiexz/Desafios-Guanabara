from random import randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('  Números sorteados:')
for c in numero:
	print(' ',c, end=' ')
print('\n\n O maior número foi:',max(numero)); print(' O menor número foi:',min(numero))