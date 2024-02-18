import desafio115 as dsf

escolha = 0

while escolha != 3:
    print('_'*35)
    print('    \033[32m-Menu de Registro-')
    print('*'*35)
    print('\033[37m 1 - Para usuários cadastrados')
    print(' 2 - Para cadastro de novo usuário')
    print(' 3 - Para finalizar o sistema')
    
    try:
        escolha = int(input('\n O que deseja ver? '))
        print('*'*35)
        
        if escolha == 1:
            dsf.fileReader()
        elif escolha == 2:
            dsf.registerUser()
     
    except ValueError:
         print('\n Algo errado. Repetindo informações...')