notaOne = float(input(' Sua 1° nota: '))
notaTwo = float(input(' Sua 2° nota: '))
solucao = (notaOne + notaTwo) / 2
print('='*30)
print('\n  Sua nota é',solucao)
if solucao < 5:
	print('\033[31m  Esta Reprovado\033[m')
elif solucao < 6.9:
	print('\033[36m  Esta de recuperação\033[m')
elif solucao > 6.9:
	print('\033[32m  Esta aprovado\033[m')