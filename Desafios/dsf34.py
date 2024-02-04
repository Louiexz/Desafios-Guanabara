# Desafio 34
salario = float(input('Salário do funcionário: R$'))
if salario > 1250:
	print(f'Seu salário terá aumento de 10% e ficará R${salario + (salario / 10):.2f}')
else:
	print(f'Seu salário terá aumento de 15% e ficará R${salario + ((salario * 15) / 100):.2f}')