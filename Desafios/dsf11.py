# Desafio 11
p_l = float(input('\033[0;32mLargura da parede:\033[m '))
p_a = float(input('\033[0;32mAltura da parede:\033[m '))
area = p_l * p_a
tinta = area / 2
print('\033[0;36mVai gastar',tinta,'litros de tinta\033[m')