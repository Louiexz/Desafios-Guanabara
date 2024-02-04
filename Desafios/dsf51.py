pt = int(input(' Digite o primeiro termo da PA: '))
r = int(input(' Digite a razão da PA: '))
print('='*30)
print('  Dez primeiros termos:\n')
decimo = pt + (10 - 1) * r
for c in range (pt, decimo + r, r):
	print(f' {c}', end=' ')
print(' Fim')