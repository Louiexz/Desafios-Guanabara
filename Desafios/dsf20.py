# Desafio 20
from random import shuffle
n1 = input('Aluno(a): ')
n2 = input('Aluno(a): ')
n3 = input('Aluno(a): ')
n4 = input('Aluno(a): ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem da apresentação será:\n', lista)