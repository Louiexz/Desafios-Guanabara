# Desafio 35
print('   Classificando triangulos\n')
r1 = float(input(' Primeiro segmento: '))
r2 = float(input(' Segundo segmento: '))
r3 = float(input(' Terceito segmento: '))
print('='*30)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print(' Podem formar um triangulo', end='')
	if r1 == r2 == r3:
		print(' equilátero')
	elif r1 != r2 != r3:
		print(' escaleno')
	else:
		print(' isósceles')
else:
	print(' Não podem formar um triangulo')