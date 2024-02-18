ano = int(input('  Ano que nasceu: '))
idade = 2022 - ano
print('='*30)
print('\033[32m')
if idade < 9:
	print(' Classificação: Mirim')
elif idade < 14:
	print(' Classificação: Infantil')
elif idade < 19:
	print(' Classificação: Junior')
elif idade < 20:
	print(' Classificação: Sénior')
else:
	print(' Classificação: Master')
print('\033[m')