qt = 0
soma = 0
print('\033[37m	Soma de números\n \nObs: Digite 999 para finalizar\n')
while True:
	num = int(input('\033[36m Digite um número: '))
	if num == 999:
		break
	qt += 1
	soma += num
print(f'\033[33m\n Soma dos {qt} números: \033[32m{soma}\033[m')