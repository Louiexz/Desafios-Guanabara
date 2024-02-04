qt = 0
s1 = 0
maior = 0
menor = 10 ** 5
resposta = 's'
while resposta != 'n':
	num = int(input(' Digite um número: '))
	qt += 1
	s1 += num
	if maior < num:
		maior = num
	if num < menor:
		menor = num
	resposta = input(' Deseja continuar? [S/N] ').lower()
print(f'\n\033[33m A média dos {qt} números foi {s1 / qt}')
print(f' O maior número foi {maior} e o menor foi {menor}\033[m')