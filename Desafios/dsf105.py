def notas(dados=[], situacao=True):
	''' notas(dados=[], situacao=bool):
		-> Função para calcular notas e retornar os resultados.
		:param dados=[]: Lista com as notas recebidas;
		:param situacao: True ou False para situação geral da turma.
	'''
	sistema = {}
	sistema['total'] = len(dados)
	sistema['maior'] = max(dados)
	sistema['menor'] = min(dados)
	sistema['média'] = sum(dados) / len(dados)
	if situacao == True:
		if sistema['média'] >= 6:
			notaGeral = 'Boa'
		elif sistema['média'] >= 5:
			notaGeral = 'Mediana'
		else:
			notaGeral = 'Péssima'
		sistema['situação'] = notaGeral
	return sistema


# MELHORIAS POSSÍVEIS
#dados = []
#situacao = str(input(' Deseja mostrar a situação da sala? [S/N] ')).upper()
#if situacao == 'S':
#	situacao = True
#alunos = int(input('\n Quantos alunos vão ser cadastrados? '))
#for c in range(0, len(dados)):
#	dados.append(float(input(f' Digite a nota do {c+1}° aluno: ')))
#print(notas(dados, situacao))

#help(notas)
print(notas(dados=[8, 6, 6, 7], situacao=True))