# Desafio 55
print(' Analisador de pesos\n')
maior = 0
menor = 0
for p in range(1, 6):
	peso = float(input(f' Digite o peso da {p}° pessoa: '))
	if p == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso
print(f'\n O maior peso foi {maior}Kg')
print(f' O menor peso foi {menor}Kg')