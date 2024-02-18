numOne = int(input(' Digite um número: '))
numTwo = int(input(' Digite um número: '))
print('='*30)
if numOne > numTwo:
	print('\n\033[36m O primeiro número é maior\033[m')
elif numTwo > numOne:
	print('\n\033[36m O segundo número é maior\033[m')
else:
	print('\n\033[32m Os números são iguais\033[m')