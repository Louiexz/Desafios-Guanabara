n = 0
n2 = 0
s = 0
print('\033[37m		Tabuada\n\n Obs: Digite um número negativo para sair')
while True:
	if n == 0:
		print()
		num = int(input('\033[33m Digite um número: '))
	if num < 0:
		print('\n\033[37m Programa encerrado\033[m')
		break
	n2 = 0
	print()
	while n2 != 10:
		n2 += 1
		s = num * n2
		print(f'\033[32m {num} x {n2} = {s} \033[m')