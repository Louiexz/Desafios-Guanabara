primeiro = float(input(' 1° número: '))
segundo = float(input(' 2° número: '))
terceiro = float(input(' 3° número: '))
quarto = float(input(' 4° número: '))
numeros = (primeiro, segundo, terceiro, quarto)
par = 0
print('\n Números digitados:',numeros)
print(f' O número 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
	print(f' Número 3 aparece primeiro na posição: {numeros.index(3)+1}°')
else:
	print(' Não houve número 3')
for c in numeros:
	if c % 2 == 0:
		par += 1
print(f' Números pares:',par)