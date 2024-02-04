# Desafio 17

# primeiro jeito
#ca = float(input(' Cateto adjacente: '))
#co = float(input(' Cateto oposto: '))
#tg = (co ** 2 + ca ** 2) ** (1/2)
#print(f'A tagente do triangulo é {tg:.2f}')

#segundo jeito
from math import hypot
ca = float(input(' Cateto adjacente: '))
co = float(input(' Cateto oposto: '))
tg = hypot(co, ca)
print(f' A tagente do triangulo é {tg:.2f}')