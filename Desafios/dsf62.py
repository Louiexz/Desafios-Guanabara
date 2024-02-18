print('\033[37m	Progressão Aritmetica\n')
primeiro = float(input(' Digite o primeiro número: '))
razao = float(input(' Digite a razão: '))
termo = 0
termoTotal = 10
print('=' * 30)
while True:
	while termo != termoTotal:
		termo += 1
		num = primeiro + (termo - 1) * razao
		print(f'\033[33m  {termo}°= {num}\033[m')
	print('='*30)
	termoTwo = int(input(' Mais quantos números? '))
	print()
	if termoTwo == 0:
		break
	elif termoTwo != 0:
		termoTotal += termoTwo
		while termo != termoTotal:
			termo += 1
			num = primeiro + (termo - 1) * razao
			print(f'\033[33m  {termo}°= {num}\033[m')