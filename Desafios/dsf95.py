dados = []

while True:
	gols = []
	tabela = { 'jogador': '',
						'total': 0 }
	tabela['jogador'] = input('\033[37m\n Nome: (Para prosseguir: digite -1) ').capitalize().strip()
	
	if tabela['jogador'] == '-1':
		break
	tabela['partidas'] = int(input(f' Partidas jogadas: '))
	
	for c in range (0, tabela['partidas']):
		gols.append(int(input(f' Quantidade de gols na partida {c+1}: ')))
		tabela['total'] += gols[c]
	tabela['gols'] = gols[:]; dados.append(tabela)

for c, v in enumerate(dados):

	if c == 0:
		print(' cod  nome	gols	total')
	print(f' {c}    {v["jogador"]:^2}	{v["gols"]}	{v["total"]:^3}')

while True:
	analise = int(input('\n Código do jogador: (-1 para sair) ')); print()
	
	if analise == -1:
		break
	
	if analise > -1 and analise <= len(dados):
		num = dados[analise]["partidas"]
		
		for jogo in range(0, num):
		
			if jogo == 0:
				print(f'-- Jogador {dados[analise]["jogador"]}:')
			print(f' No jogo {jogo+1} fez {dados[analise]["gols"][jogo]} gols')		