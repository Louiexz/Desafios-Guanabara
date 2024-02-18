peso = float(input('\033[33m Seu peso: (Kg)'))
altura = float(input(' Sua altura: (m) '))
print('\033[m')
solucao = peso / (altura ** 2)
print('='*30)
print(f' Seu IMC é: {solucao}\n')
if solucao < 18.5:
	print('\033[35m Abaixo do peso\033[m')
elif solucao < 25:
	print('\033[32m Peso ideal\033[m')
elif solucao < 30:
	print('\033[35m Sobrepeso\033[m')
elif solucao < 40:
	print('\033[31m Obesidade\033[m')
else:
	print('\033[31m Obesidade mórbida\033[m')