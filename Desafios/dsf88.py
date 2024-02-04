from random import randint
ajuste = 0; jogo = []
print('\033[m	--Mega sena--')
quantidadeJogos = int(input('\n Quantos jogos voce quer? '))
print('~'*30)
while ajuste != quantidadeJogos:
	jogos = []
	for c in range(0, 6):
		jogos.append(randint(1, 60))
	jogo.append(jogos[:])
	print(f'Jogo número {ajuste}: {jogo[ajuste]}\033[m')
	ajuste += 1