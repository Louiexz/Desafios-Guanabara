# Desafio 19
import random
nome1 = input('Nome do aluno(a): ')
nome2= input('Nome do aluno(a): ')
nome3 = input('Nome do aluno(a): ')
nome4 = input('Nome do aluno(a): ')
num = random.randint(1, 4)
if num == 1:
 	print('\nO(A) escolhido(a) foi',nome1)
elif num == 2:
 	print('\nO(A) escolhido(a) foi',nome2)
elif num  == 3:
 	print('\nO(A) escolhido(a) foi',nome3)
elif num == 4:
 	print('\nO(A) escolhido(a) foi',nome4)