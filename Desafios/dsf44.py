preco = float(input(' Preço do produto: R$'))
print('\n Formas de pagamento:\n   dinheiro/cheque [1]\n   1x no cartão [2]\n   2x no cartão [3]\n   3x ou mais no cartão [4]\n')
pagamento = input(' Escolha [1] [2] [3] ou [4] ')
print('='*30)
if pagamento == '1':
	preco -= (preco / 10)
	print(' 10% de desconto: Preço final',preco)
elif pagamento == '2':
	preco = preco - (preco * 5 / 100)
	print(' 5% de desconto: Preço final',preco)
elif pagamento == '3':
	print(' Preço normal:',preco)
elif pagamento == '4':
	preco2 = (preco * 20) / 100 + preco
	print(f' 20% de acrescimo: Preço final',preco2)