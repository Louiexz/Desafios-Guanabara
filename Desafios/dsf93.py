tabela = { 'jogador': '',
					'gols': [],
					'total': 0 }

gols = []

tabela['jogador'] = input('\033[37m Nome: ').capitalize().strip()
tabela['partidas'] = int(input(f' Partidas jogadas por {tabela["jogador"]}: '))

for c in range (0, tabela['partidas']):
	gols.append(int(input(f' Quantidade de gols na partida {c+1}: ')))
	tabela['total'] += gols[c]

tabela['gols'] = gols

print('='*35,f'\n {tabela} \n','='*35)
print(f' Nome do jogador: {tabela["jogador"]}\n Gols marcados: {tabela["gols"]}\n Total de gols: {tabela["total"]}\n','='*35)
print(f' O jogador {tabela["jogador"]} jogou {tabela["partidas"]}\n')

for a in range(0, tabela['partidas']):
	print(f'	-> Na partida {a+1}, fez {gols[a]} gols')

print(f'\n Marcou um total de {tabela["total"]} gols\033[m')