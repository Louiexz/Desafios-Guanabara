frase = str(input(' Digite uma frase/palavra: ')).strip().lower()
word = frase.split()
inverso = ''
junto = ''.join(word)
for letra in range(len(junto) -1, -1, -1):
	inverso += junto[letra]
print('='*40)
print(f'\n A palavra/frase {frase} ao contrário fica: {inverso}')
if inverso == junto:
	print('\n É um palídromo')
else:
	print('\n Não é um palídromo')