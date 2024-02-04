filename = 'register_file.json'

def registerUser():
    global filename    
    active = True
    
    while active:
        nome = input(' Nome do usuário: ').strip().title()
        
        try:
            idade = int(input(' Idade do usuário: '))
            active = False
        
        except ValueError:
            print(' Dado inválido.')
    
    with open(filename, 'a') as file_objct:
        file_objct.write('\n')
        file_objct.write(f'{nome},{idade}')
        
        print('\n\033[32m Dados cadastrados.\033[m')

def fileReader():
         with open(filename) as f_obj:
             print('\033[33m   Usuários Cadastrados\n')
             print(' Nome          Idade\033[m\n')
             
             for line in f_obj:
                 if line.strip():
                     line = (line.split(','))
                     # or line = eval(line)
                     print(f' {line[0]:<12} {line[1].strip()} anos')
