sistema = { 'nome': '',
				  	'media': 0 }
sistema['nome'] = input('\033[37m Digite seu nome: ').capitalize()
sistema['media'] = float(input(' Digite a média das suas notas: '))
print(f'\n Nome do aluno: {sistema["nome"]}\n Média do aluno: {sistema["media"]}')
if sistema['media'] >= 7 and sistema['media'] < 10:
	print('\033[32m Aluno aprovado\033[m')
elif sistema['media'] >= 5:
	print('\033[34m Aluno em recuperação\033[m')
elif sistema['media'] > -1:
	print('\033[31m Aluno reprovado\033[m')