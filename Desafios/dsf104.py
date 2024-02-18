def leiaInt(msg):
	''' leiaInt(msg):
		 -> Função para validar números inteiros
		:param msg: Mensagem do input
	'''
	active = True
	while active:
	    try:
	        numero = input(msg)
	        if int(numero):
	            print(f' {numero} é um número inteiro')
	            active = False
	    except ValueError:
	        print('\033[31m Erro! Não é um número inteiro\033[m\n')


def leiaFloat(msg):
	''' leiaFloat(msg):
		 -> Função para validar números inteiros
		:param msg: Mensagem do input
	'''
	active = True
	while active:
	    try:
	        numero = input(msg)
	        if float(numero):
	            print(f' {numero} é um número flutuante')
	            active = False
	    except ValueError:
	        print('\033[31m Erro! Não é um número Flutuante\033[m\n')


leiaInt(' Digite um número: '); print()
leiaFloat(' Digite um número: ')