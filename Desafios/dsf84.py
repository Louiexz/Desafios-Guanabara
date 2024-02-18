escolha = 's'; qt = 0
dados = []; leve = []; pesado = []; nomes = []
while escolha != 'n':
	if escolha == 's':
		nome = str(input('\033[37m Seu nome: ')).capitalize()
		nomes.append(nome)
		qt += 1
		dados.append(float(input(' Seu peso: ')))
	escolha = input('Deseja continuar? [S/N] ')
for a, p in enumerate(dados):
	if p == min(dados):
		menorPeso = p
		leve.append(nomes[a][:])
	elif p == max(dados):
		maiorPeso = p
		pesado.append(nomes[a][:])
dados.append(leve[:]); dados.append(pesado[:])
print(f'\n Pessoas cadastradas: {qt} pessoas\n A pessoa mais leve é {leve} com {menorPeso}Kg \n A mais pesada é: {pesado} com {maiorPeso}Kg\033[m')