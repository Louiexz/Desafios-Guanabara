def docs():
	'''metade(num=0):
		-> Função que retorna metade de um número
		:param num: Número de sua preferencia
		:param return: Número dividido por dois
			
		diminuir(num=0, porcentagem=0):
		-> Função que retorna o número menos uma quantidade em porcentagem
		:param porcentagem: Número em porcentagem a ser retirado
		:param return: Número multiplicado pela porcentagem dividido por cem menos o número
		
		dobro(num=0):
		-> Função que retorna o dobro de um número
		:param return: Número multiplicado por dois
		
		aumentar(num=0, porcentagem=0):
		-> Função que retorna um número e seu acrescimo em porcentagem
		:param return: Número multiplicado pela porcentagem dividido por cem mais o número
		
		moeda(preco=0, formatar= 'N'):
			-> Função para formatação de valores
			:para return: Retorna ou não o valor formatado
		
		resumo(dinheiro, aumento, diminuicao, formatar):
			-> Funcão que dá o retorno de todos os valores atribuídos anteriormente
	'''
	
	
def aumentar(
							num,
							porcentagem=0
							):
	
	if porcentagem >= 0 and porcentagem <= 100:
		acrescimo = (num * porcentagem / 100) + num
		return acrescimo
		
		
#def fatorial(
#						num
#						):
#	f = 1
#	for c in range(num, num+1):
#		f *= c

	
def dobro(
					num
					):
	dobrado = num * 2
	return dobrado

		
def diminuir(num, porcentagem=0):
	
	if porcentagem >= 0 and porcentagem <= 100:
		decrescimo = num - (num * porcentagem / 100)
		return decrescimo


def metade(
						num
						):
	banda = num / 2
	return banda
	
	
def moeda(
					preco=0,
					formatar= 'N'
					):
	if formatar == 'S':
		return f'	R${preco:10.2f}'.replace('.', ',')
	else:
		return preco


def resumo(
						dinheiro,
						aumento,
						diminuicao,
						formatar
						):
	print('\n', '~'*40, '\n	Resumo dos valores aproximados\n', '~'*40)
	print(f'\n Número dobrado: {moeda(dobro(dinheiro), formatar)}')
	print(f' + {aumento}%: {moeda(aumentar(dinheiro, aumento), formatar)}')
	print(f' - {diminuicao}%: {moeda(diminuir(dinheiro, diminuicao), formatar)}')
	print(f' Metade do número: {moeda(metade(dinheiro), formatar)}\033[m')
