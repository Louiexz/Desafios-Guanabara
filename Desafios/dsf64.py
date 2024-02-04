quantidade = 0
soma = 0
num = None
while num != 999:
	num = int(input(' Digite um número: [999 para parar] '))
	if num != 999:
		soma += num
		quantidade += 1
print(f'\n\033[32m Foram digitados {quantidade} números e a soma deles deu {soma}\033[m')