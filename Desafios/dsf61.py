print('\033[37m	Progressão Aritmetica\n')
primeiro = float(input(' Digite o primeiro número: '))
razao = float(input(' Digite a razão: '))
termo = 0
print('=' * 30)
while True:
	termo += 1
	num = primeiro + (termo - 1) * razao
	print(f'\033[33m  {termo}°= {num}\033[m')
	if termo >= 10:
		break