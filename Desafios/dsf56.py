# Desafio 56
s = 0
s1 = 0
maiorAge = 0
nomeVelho = 0
for c in range(1, 5):
	nome = str(input(f' Digite o da {c}° nome: ')).strip().capitalize()
	age = int(input(' Digite a idade: '))
	sexo = input(' Sexo: [M/F] ').strip().lower()
	print()
	s += age
	if c == 1 and sexo == 'm':
		maiorAge = age
		nomeVelho = nome
	if sexo == 'm' and age > maiorAge:
		maiorAge = age
		nomeVelho = nome
	if sexo == 'f' and age < 20:
		s1 += 1
print('\033[m','\n\033[32m A média de idade é:',s / 4)
print(f' {nomeVelho} é o homem mais velho e tem {maiorAge} anos de idade')
print(' Mulheres com menos de 20 anos:',s1,'\033[m')