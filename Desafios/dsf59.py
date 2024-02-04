print('	Calculadora\n')
print(' Operações: \n [1] Somar\n [2] multiplicar\n [3] maior\n [4] novos números\n [5] sair do programa\n')
escolha = None
s = None
n1 = float(input(' Digite um número: '))
n2 = float(input(' Digite um número: '))
while escolha != '5':
	escolha = input('\n Escolha [1], [2], [3], [4] ou [5]: ')
	if escolha == '1':
		s = n1 + n2
		print('\n A soma dos números',s)
	elif escolha == '2':
		s = n1 * n2
		print(f'\n {n1} x {n2} = {s}')
	elif escolha == '3':
		if n1 > n2:
			print('\n O primeiro número é maior')
		else:
			print('\n O segundo número é maior')
	elif escolha == '4':
		n1 = float(input('\n 1° novo número: '))
		n2 = float(input(' 2° novo número: '))
	elif escolha != '5':
		print(' Opção inválida. ')