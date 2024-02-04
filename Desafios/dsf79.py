escolha = 's'
lista = []
c = 0
while escolha != 'n':
	if escolha == 's':
		numero = float(input('\n Digite um número: '))
		s = lista.count(numero)+1
		if s <= 1:
			lista.insert(c, numero)
			c += 1
		else:
			print('O número já existe na lista')
	escolha = input('\n Deseja continuar? [S/N] ').lower().strip()
lista.sort()
print('\n Números válidos digitados: ',lista)