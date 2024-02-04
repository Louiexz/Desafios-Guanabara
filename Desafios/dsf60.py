print('	Fatorial\n')
n = int(input(' Qual o número: '))
resultado = 1
count = 1
print(f'\n{n}! =')
while count <= n:
	resultado *= count
	count += 1
	print(count-1, end = ' x ')
print('1 =',resultado)