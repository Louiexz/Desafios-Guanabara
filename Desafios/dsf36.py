casaValor = int(input(' Valor da casa: R$'))
salario = int(input(' Seu salário? R$'))
parcelaAno = int(input(' Quantos anos para pagar? '))
porcentagem = (salario * 30) / 100
parcelaMes = parcelaAno * 12
solucao = (casaValor / parcelaMes )
print('='*30)
print(' Valor da parcela por mes:',solucao)
if solucao <= porcentagem:
	print('\n\033[33m O empréstimo pode ser feito\033[m')
else:
	print('\n\033[33m Empréstimo cancelado\033[m')