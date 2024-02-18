escolha = 's'; soma = 0; qt = 0
dados = { 'nome': [] }; nome = []; idade = []; homem = []; mulher = []; sexo = []

while True:
	
	if escolha == 's':
		nome.append((input(' Nome: ')).strip().capitalize())
		idade.append(int(input(' Idade: ')))
		soma += idade[qt]
		sexo.append(input(' Sexo: [M/F] ').upper().strip())
		
		if sexo[qt] == 'M':
			homem.append(nome[qt])
		elif sexo[qt] == 'F':
			mulher.append(nome[qt])
		
		qt += 1
	escolha = input('\n Deseja continuar? [S/N] ').lower()
	
	if escolha == 'n':
		dados['media'] = soma / qt
		break

dados['nome'] = nome; dados['idade'] = idade; dados['sexo'] = sexo
print(f'\n-- O grupo tem {qt} pessoas\n-- A média de idade é de {dados["media"]:.2f}\n-- As mulheres cadastradas foram: {mulher}')

for c, v in enumerate(idade):
	
	if c == 0:
		print(f'-- Pessoas com mais de {dados["media"]:.2f} anos')
	
	if v > dados['media']:
		print(f'\n -> Nome: {nome[c]}  -> Sexo: {sexo[c]}  -> Idade: {idade[c]}')