def dado():
	while True:
		dinheiro = input('\033[37m Qual o preço? R$').replace(',', '.')
		
		try:
			dinheiro = float(dinheiro)
			if dinheiro == int(dinheiro) or dinheiro:
			
				return int(dinheiro)
		except (ValueError, TypeError):
			print(' Erro! Digite um valor válido.')