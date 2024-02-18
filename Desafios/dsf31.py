# Desafio 31
num = int(input('Digite os Km rodados na viagem: '))
if num <= 0:
	print('Nada a pagar')
elif num <= 200:
	print(f'Voce rodou {num} e deve pagar R${num * 0.50:.2f} de passagem')
else:
	print(f'Voce rodou {num} e deve pagar RS{num * 0.45:.2f} de passagem')
# Jeito do Guanabara
num = int(input('Qual a distancia da sua viagem? '))
preco = num * 0.50 if num <= 200 else num * 0.45
print(f'Ao percorrer uma viagem de {num}Km, voce deve pagar RS{preco:.2f} de passagem')