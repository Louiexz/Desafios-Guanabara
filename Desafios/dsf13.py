# Desafio 13
s = float(input('\033[0;33mSeu salario: R$\033[m'))
r = float(input('\033[0;33mValor do reajuste: \033[m'))
sn = s + (s * r / 100)
print(f'\033[0;32mGanhava R${s:.2f} com {r} de reajuste passou a ganhar: R${sn:.2f}\033[m')