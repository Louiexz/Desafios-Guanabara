from random import randint

def helper():
	parametro = None
	while True:
		parametro = str(input('\033[41m Deseja ter a doc de qual função ou libraria? (Fim = parar) ')).strip().lower()
		if parametro == 'fim':
			break
		inicio = f'Aqui está a doc de {parametro.upper()}'
		print('', '~' * (len(inicio)+4), f'\n   {inicio}\n','~' * (len(inicio)+4))
		print(f'\033[{randint(42, 46)}m')
		help(parametro)
	

helper()