# Desafio 50 soma de seis números pares
s = 0
for c in range(1,7):
	num = int(input(f'  Digite o {c}° número inteiro: '))
	if num % 2 == 0:
		s += num
print('\n  A soma dos números pares é',s)