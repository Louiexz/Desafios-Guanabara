from datetime import date

def voto(situacao):
	''' voto(situacao):
		-> Função para calcular idade, e analisar a situação eleitoral de alguém.
		:param situacao: Ano em que nasceu
		'''
	idade = date.today().year - situacao
	if idade < 18:
		print(f' Com {idade} anos: Não pode votar')
	elif idade >= 18 and idade < 70:
		print(f' Com {idade} anos: O voto é obrigatório')
	elif idade >= 70:
		print(f' Com {idade} anos: Voto opcional')
		
voto(int(input(' Ano em que nasceu? ')))
print()	