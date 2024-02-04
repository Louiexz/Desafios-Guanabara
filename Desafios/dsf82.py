lista = []; pares = []; impar = []
escolha = 's'
while escolha != 'n':
	if escolha == 's':
		num = float(input(' Digite um número: '))
		lista.append(num)
		if num % 2 == 0:
			pares.append(num)
		else:
			impar.append(num)
	escolha = input(' Continuar? [S/N] ')
print(f'\n Lista dos números digitados {lista}\n Lista dos números pares {pares}\n Lista dos números ímpares {impar}')