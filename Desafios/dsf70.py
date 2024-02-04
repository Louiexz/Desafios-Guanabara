menorPreco = 10 ** 5
soma = 0
qt = 0
produtoMenor = 0
print('\033[33m	Analisando compras')
while True:
	nomeProduto = input('\n Qual o nome do produto: ').strip().capitalize()
	precoP = float(input(' Qual o preço? R$'))
	fim = input(' Quer continuar? [S/N] ').lower()
	if precoP > 1000:
		qt += 1
	soma += precoP
	if precoP < menorPreco:
		menorPreco = precoP
		produtoMenor = nomeProduto
	if fim == 'n':
		print(f'\n\033[37m O total gasto foi de R${soma:.2f}')
		print(f' Produtos por mais de R$1000: {qt}')
		print(f' O nome do produto mais barato é: {produtoMenor} custando R${menorPreco} \033[m')
		break	