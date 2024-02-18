from random import randint
from time import sleep
from operator import itemgetter

jogo = { 'jogador_1': randint(1, 6),
				'jogador_2': randint(1, 6),
				'jogador_3': randint(1, 6),
				'jogador_4': randint(1, 6) }

for c in range(1, 5):
	sleep(0.5)
	print(f' O jogador número {c} tirou o número:', end= ' '); print(jogo.get(f'jogador_{c}'))

print('\n	Ranking dos jogadores\n')
ordem = sorted(jogo.items(), key=itemgetter(1), reverse= True)

for a, v in enumerate(ordem):
	sleep(0.5)
	print(f' O {v[0]} tirou {a+1}° lugar com o número {v[1]}', end= '\n')