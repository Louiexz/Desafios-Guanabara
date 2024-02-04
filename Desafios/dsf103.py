def ficha():
	global nome, gols
	if nome.isalpha() is False:
		nome = '<Desconhecido>'
	if gols.isnumeric() is False:
		gols = 0
	print(f'\n O jogador {nome} fez {gols} gols')


nome = str(input(' Nome do jogador: ')).capitalize().strip()
gols = input(' Gols feitos: ').strip()
ficha()