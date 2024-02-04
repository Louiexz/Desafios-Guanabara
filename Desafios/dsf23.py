# Desafio 23
num = int(input('Digite um número: '))
print('Analisando o número',num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
dm = num // 10000 % 10
cm = num // 100000 % 10
print('Centena de milhar:',cm)
print('Dezena de milhar:',dm)
#if num > 1000:
print('Unidade de milhar:',m)
#else :
	#print('Unidade de milhar: 0')
#if n  >= 100:
print('Unidade de centena:',c)
#else :
	#print('Unidade de centena: 0')
#if n >= 10:
print('Unidade de dezena:',d)
#else :
#	print('Unidade de dezena: 0')
print('Unidade',u)