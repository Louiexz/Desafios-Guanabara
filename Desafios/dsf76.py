myTupla = ('Computador', 12000, 'Celular', 2000, 'Playstation', 5000, 'Monitor', 1500)
print('	Lista de Preços')
print(f'\n {myTupla[0]}.........R${myTupla[1]}\n {myTupla[2]}............R$ {myTupla[3]}\n {myTupla[4]}........R$ {myTupla[5]}\n {myTupla[6]}............R$ {myTupla[7]}\n')
#jeito do guanaba
for pos in range(0, len(myTupla)):
	if pos % 2 == 0:
		print(f' {myTupla[pos]:.<30}', end ='')
	else:
		print(f'R${myTupla[pos]:>7.2f}')