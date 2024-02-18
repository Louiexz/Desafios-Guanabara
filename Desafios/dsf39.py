year = int(input('\033[33m Nasceu em que ano? \033[m'))
print('='*30)
age = 2022 - year
if age < 18:
	print(f' Ainda vai se alistar\n   Faltam {18 - age} anos')
elif age == 18:
	print(' Hora de se alistar')
else:
	print(f' Cuidado! Passou {age - 18} anos do tempo de alistamento')