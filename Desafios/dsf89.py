dado = [[],[],[]]
escolha = 's'; num = 0; aluno = None
while True:
	if escolha == 's':
		dado[0].append((input('\n\033[37m Nome do aluno: ').capitalize()))
		for c in range(1, 2):
			dado[1].append(float(input(f' Digite a {c}° nota: ')))
			c += 1
			dado[2].append(float(input(f' Digite a {c}° nota: ')))
	escolha = input('\n Deseja continuar? [S/N] ').lower().strip()
	if escolha == 'n':
		while num != len(dado[0]):
			if num == 0:
				print('\n No.   Nome	Média\n\n', end= '')
			print(f' {num:^3} {dado[0][num]:^8} {(dado[1][num] + dado[2][num]) / 2:^5}')
			num += 1
		break
while True:
	aluno = int(input('\n Deseja ver a nota de qual aluno? (-1 para sair) '))
	if aluno == -1:
		break
	if aluno > -1 and aluno < len(dado[0]):
		print(f'\n Nota do aluno: {dado[0][aluno]}\n Primeira nota: {dado[1][aluno]}\n Segunda nota: {dado[2][aluno]}\033[m')