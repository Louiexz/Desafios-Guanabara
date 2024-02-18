# Desafio 12
pi = float(input('\033[0;35mPreço do produto: R$\033[m'))
s = float(input('\033[0;35mPorcentagem de desconto do produto: \033[m'))
pct = (pi * s / 100)
pd = pi - pct
print(f'\033[0;32mO produto que custa R${pi}, com desconto de {s}% é:\033[m \033[0;36mR${pd}\033[m')