from time import sleep

def contador():
	for c in range(inicio, fim, passo):
		print(c, end= ' ', flush=True)
		sleep(0.5)
	if passo - passo == 0 and passo + passo > 0:
		print(c+1, '-> Acabou')
	else:
		print(c-1, '-> Acabou')


inicio = 1; fim = 10; passo = 1
contador(); print()
inicio = 10; fim = 0; passo = -1
contador()
print('\n Agora é sua vez...\n')
inicio = int(input(' Onde a contagem inicia? '))
fim = int(input(' Onde a contagem acaba? '))
passo = int(input(' De quantos em quantos números? '))
print(); contador()