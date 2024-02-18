# Desafio 22
nome = input(' Digite seu nome completo: ')
print(nome)
print(len(nome))
print('Seu nome em caps:',nome.upper())
print('Seu nome minúsculo:',nome.lower())
print(f'Seu nome tem ao todo',{len(nome) - nome.count(' ')},'letras')
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras')