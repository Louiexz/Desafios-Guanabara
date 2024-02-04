# Desafio 29
velocity = int(input('Digite a velocidade: '))
if velocity > 80:
	multa = (-1*(80 - velocity)) * 7
	print(f'Voce foi em R${multa:.2f} multado por excesso de velocidade')
else:
	print('Boa viagem!')