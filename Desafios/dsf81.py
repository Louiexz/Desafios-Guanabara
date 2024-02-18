lista = []
s = 0
escolha = 's'
while escolha != 'n':
	if escolha == 's':
		s += 1
		num = float(input(' Digite um número: '))
		lista.append(num)
	escolha = input(' Deseja continuar? [S/N] ').lower()
lista.sort(reverse= True)
print(f'\n Foram acrescentados {s} números a lista.'); print(f' A lista de forma decrescente:\n   {lista}')
if 5 in lista:
	print(' O número 5 está na lista!')
else:
	print(' O número 5 não está na lista!')