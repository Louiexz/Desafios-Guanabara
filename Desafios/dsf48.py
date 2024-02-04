# Desafio 48
s = 0
s1 = 0
for a in range(0, 500, 3):
	if a % 2 != 0:
		s += 1
		s1 += a
print(f' A soma dos {s} número pares e múltiplos de 3 até 500 é: {s1}')