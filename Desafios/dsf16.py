# Desafio 16
# formas de fazer

# from math import floor
# num = int(input('Digite um número que não seja inteiro: '))
#print(f' A parte inteira de {num} é {floor(num)}')

# from math import trunc 
#num = int(input('Digite um número que não seja inteiro: '))
#print(f' A parte inteira de {num} é {trunc(num)}')

num = float(input('\033[37mDigite um número que não seja inteiro: \033[m'))
print(f'\n\033[31m A parte inteira de {num} é {int(num)}\033[m')