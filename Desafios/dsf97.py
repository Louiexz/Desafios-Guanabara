def escreva():
	print('\n','~' * (len(msg) + 4) ,f' \n   {msg}\n','~'* (len(msg) + 4))


escolha = 'n'
while escolha != 's':
	msg = input('\n Digite uma frase: ').strip()
	escreva()
	escolha = input('\n Deseja sair? [S/N] ').lower().strip()