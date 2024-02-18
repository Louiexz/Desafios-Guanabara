num = int(input(' Digite um número: '))
print('\n   Tabuada do',num)
print('='*30)
for c in range(1, 11):
	print(f'    {num} x {c} =',num * c)
	c += 1