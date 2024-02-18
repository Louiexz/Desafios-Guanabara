s1 = 0
s2 = 0
s3 = 0
print('\033[37m	Cadastro de pessoas')
while True:
	age = 0
	gender = None
	age = int(input('\n  Sua idade: '))
	gender = input('  Seu sexo [M/F]: ').lower()
	if age > 0 and age > 18:
		s1 += 1
	if gender == 'm':
		s2 += 1
	if age < 20 and gender == 'f':
		s3 += 1
	fim = input('\n Deseja continuar? [S/N]: ').lower()
	if fim == 'n':
		print('\n\033[33m  Pessoas com mais de 18 anos:',s1)
		print('  Homens cadastrados:',s2)
		print('  Mulheres com menos de 20 anos:',s3,'\033[m')
		break