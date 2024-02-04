from datetime import date
anoAtual = date.today().year
s = 0
s2 = 0
for c in range(1, 8):
	print('='*30)
	ano = int(input(f'\033[33m Ano em que a {c}° pessoa nasceu? '))
	age = anoAtual - ano
	if age > 21:
		s += 1
	else:
		s2 += 1
print(f'\n\033[m\033[32m {s2} ainda são menores de idade\n')
print(f' {s} são maiores de idade\033[m')