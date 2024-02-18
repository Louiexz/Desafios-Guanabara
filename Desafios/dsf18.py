# Desafio 18
from math import cos,sin,tan,radians
ang = int(input('Digite o angulo do seu triangulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print(f' O cosseno de {ang} é: {cos:.2f} \n O seno de {ang} é: {sen:.2f} \n A tangente de {ang} é: {tg:.2f}')