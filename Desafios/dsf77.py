palavra = 'arroz', 'feijao', 'carne', 'papa', 'salada', 'tomate', 'cebola', 'cuscuz','macarrao'
vogais = 'a', 'e', 'i', 'o', 'u',
for letra in palavra:
	print(f'\n\033[37m Na palavra {letra.upper()} temos vogal', end='  ')
	for vogal in vogais:
		if vogal in letra:
			print(vogal, end=' ')
# Jeito do Guanabara
#palavra = 'arroz', 'feijao', 'carne', 'papa', 'salada', 'tomate', 'cebola', 'cuscuz', 'macarrao'
#for p in palavra:
#	print(f'\033[37m\n Na palavra {p} temos vogal', end=' ')
#	for letra in p:
#		if letra.lower() in 'aeiou':
#			print(letra, end=' ')