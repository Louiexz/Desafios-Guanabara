from datetime import date

dados = { 'nome': '' }
dados['nome'] = input(' Digite seu nome: ').capitalize().strip()
nasci = float(input(' Ano que nasceu? '))
dados['idade'] = int(date.today().year - nasci)
dados['ct'] = int(input(' Número da carteira de trabalho: '))
print(f'\n Nome: {dados["nome"]}\n Idade: {dados["idade"]}\n Carteira de trabalho: {dados["ct"]}')

if dados['ct'] != 0:
	dados['iniciocontrato'] = int(input(' Ano do ínicio de contrato: '))
	dados['salario'] = int(input(' Seu sálario: '))
	dados['aposento'] = 35 - (date.today().year - dados['iniciocontrato']) + dados['idade']
	print(f' Ano de contratação : {dados["iniciocontrato"]}\n Salário: R${dados["salario"]:.2f}\n Vai se aposentar com: {dados["aposento"]} anos')