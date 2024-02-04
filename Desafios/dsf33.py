# Desafio 33
num = input('Digite tres números separados por espaço: ').split()
# Procurando o maior
if num[0] > num[1] and num[2]:
	print(f'O número {num[0]} é o maior')
elif num [1] > num[2] and num[0]:
	print(f'O número {num[1]} é o maior')
else:
	print(f'O número {num[2]} é o maior')
#procurando o menor
if num[0] < num[1] and num[2]:
	print(f'O número {num[0]} é o menor')
elif num[2] < num[1] and num[0]:
	print(f'O número {num[2]} é o menor')
else:
	print(f'O número {num[1]} é o menor')