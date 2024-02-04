lista = []
for c in range(0,5):
	lista.append(int(input(f' Digite o número da posição {c}: ')))
#	numero = int(input(f' Digite o número da posição {c}: '))
#	lista.insert(c, numero)
maior = max(lista); menor = min(lista)
print('\n Números digitados:',lista)
print(' O maior número na lista:',maior,' posições:', end= ' ')
for i, v in enumerate(lista):
	if v == maior:
		print(i)
print('\n O menor número na lista:', menor,' posições:', end= ' ')
for a, b in enumerate(lista):
	if b == menor:
		print(a)		