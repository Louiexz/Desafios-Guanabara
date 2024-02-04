print('	Banco Guanaba')
print('='*30)
while True:
	valor = int(input(' Valor que será sacado: '))
	r1 = int(valor / 50)
	r2 = int((valor % 50) / 20)
	r3 = int(((valor % 50) % 20) / 10)
	r4 = int((((valor % 50) % 20) % 10) / 1)
	print(f'\n Cédulas retornadas:\n')
	if r1 != 0:
		print(f' Cédulas de R$50: {r1}')
	if r2 != 0:
		print(f' Cédulas de R$20: {r2}')
	if r3 != 0:
		print(f' Cédulas de R$10: {r3}')
	if r4 != 0:
		print(f' Cédulas de R$1: {r4}')
	break
	print('='*30)
	print('  Volte sempre ao Banco Guanaba!')