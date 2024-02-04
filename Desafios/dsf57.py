sexo = 'm'
sexo2 = 'f'
escolha = str(input('\033[33m Digite seu sexo [M/F]: ')).lower()
print()
while escolha != sexo and escolha != sexo2:
	escolha = str(input(' Dado ínvalido.\n Digite seu sexo novamente [M/F]: ')).lower()	
print('\033[m')