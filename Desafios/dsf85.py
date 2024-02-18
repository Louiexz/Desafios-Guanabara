numeros= []; par = []; impar = []
for c in range(1, 8):
	num = float(input(f' Digite o {c}° número: '))
	if num % 2 == 0:
		par.append(num)
	else:
		impar.append(num)
impar.sort(); par.sort()
numeros.append(par[:]); numeros.append(impar[:])
print(f'\n Números pares digitados: {numeros[0]}\n Números ímpares digitados: {numeros[1]}')