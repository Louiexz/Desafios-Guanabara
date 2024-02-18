# Desafio 26
frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra "A" aparece:',frase.count('a'), 'vezes')
print('O "A" aparece primeiramente em', frase.find('a')+1)
print('A última vez que o "A" aparece é:', frase.rfind('a')+1)