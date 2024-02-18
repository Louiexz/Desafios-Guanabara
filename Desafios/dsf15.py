# Desafio 15
d = int(input('\033[36mDias alugado? \033[m'))
km = float(input('\033[36mQuilometros rodados? \033[m'))
vt = (d * 60) + (km * 0.15)
print(f'\033[32m\n O valor a pagar será de R${vt} por {d} dias e {km} quilometros rodados\033[m')