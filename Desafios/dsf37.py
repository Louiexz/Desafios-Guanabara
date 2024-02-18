num = int(input('\033[36m Digite um número: '))
print('='*30)
print('   Digite [1] para binário\n   Digite [2] para octal\n   Digite [3] para hexadecimal\033[m')
print('='*30)
conversor = input('\033[32m Qual a conversão? [1], [2] ou [3]: ')
if conversor == '1':
	print(f'\n O número em binário é {bin(num)[2:]}')
elif conversor == '2':
	print(f'\n O número em octal é {oct(num)[2:]}')
elif conversor == '3':
		print(f'\n O número em hexadecimal é {hex(num)[2:]}')
else:
	print(' Error')
print('\033[m')