extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onde', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input(' Um número: (de 0 a 20) '))
while escolha < 0 or escolha > 20:
	escolha = int(input(' Tente novamente. Digite um número: '))
if escolha > -1 or escolha < 21:
	print(f'\n O número {escolha} por extenso fica {extenso[escolha]}')