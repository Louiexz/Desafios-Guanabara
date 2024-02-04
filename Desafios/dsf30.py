# Desafio 30
num = int(input('Digite um número: '))
if num == 0:
	print(f'{num} é um número neutro')
elif num % 2 == 0:
	print(f'{num} é um número par')
else:
	print(f'{num} é um número ímpar')
# Jeito do Guanabara
num = int(input('Digite um número: '))
r = num % 2
if r == 0:
	print(num,'é par')
else:
	print(num,'é impar')