print('     BANGU X MADUREIRA     ')
print('='*40)
gols = int(input('Quantos gols Bamgu fez? '))
gols2 = int(input('Quantos gols Madureira fez? '))
print()
if gols > gols2:
	df = gols - gols2
	print('Diferença:',df)
	if df <=3:
		print('Status: Partida Normal')
	else:
		print('Status: Goleada')
elif gols2 > gols:
	df = gols2 - gols
	print('Diferença:',df)
	if df <=3:
		print('Status: Partida Normal')
	else:
		print('Status: Goleada')
else:
	print('Diferença: 0')
	print('Status: Empate')