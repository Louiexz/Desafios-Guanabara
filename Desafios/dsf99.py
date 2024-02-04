def maior(* num):
	numMaior = 0
	for v in num:
#	for a, v in enumerate(num)
#		if a == 0:
#			numMaior = 0
		if numMaior < v:
			numMaior = v
	print(f' O maior número dentre {num} foi o número:', numMaior)
	

maior(2, 3, 9, 10, 5, 18)
maior(2, 6, 8, 6, 1, 9)
#num = []
#while True:
#	qt = int(input('\033[37m\n Deseja quantos números? (0 para sair) '))
#	if qt == 0:
#		break
#	for c in range(0, qt):
#		num.append(int(input(f' Digite o {c+1}° número: ')))
#	print(f'\n	Analise dos números\n {num} foram informados {qt} valores ao todo.\n O maior número foi o', end= ' \033[m')
#	maior()
#.	num.clear()