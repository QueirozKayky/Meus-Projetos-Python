#Area do menu para seleção das opções!
def menu():
    print('~~~~~~~~~~~~~~')
    print('|App de Notas|')
    print('~~~~~~~~~~~~~~')
    print('!Select one option!')
    print('-------------------')
    print('[1] Write Note.')
    print('[2] See notes.')
    print('[3] Delete Notes.')
    print('[4] Exit.')
    print('-------------------')
    while True:
        try:
            option = int(input('Option number: '))
            if option ==1:
                write_notes()
            elif option ==2:
                see_notes()
            elif option ==3: 
                delete_notes()
            elif option ==4:
                print('!Bye, bye!')
                break
            else:
                print('--------------------------------------')
                print("please select a number btween 1 and 4.")
                print('--------------------------------------')
        except:
            print('!!! Invalid input, type a number to continue!!! ')

def write_notes():
    #pega a nota do usuario.
    notes = str(input('Write your note: '))

    #Abre o arquivo e armazena a conexão em uma variavel.
    file = open('notas.txt', 'a')

    #Usa o objeto Write no objeto do arquivo, uma unica vez.
    file.write(notes + '\n') #Adiciona a nota e adiciona uma linha.

    #Fecha o arquivo (sempre). 
    file.close()

def see_notes():
    try:
        with open ('notas.txt', 'r') as file:
            print('-----------------------------')
            print(">>Hey, here it's your notes<<")
            print('-----------------------------')
        
            content = file.read()
            print(content)
    except:
        if  FileNotFoundError:
            print('-----------------------------')
            print('Ops, you need to create a note \n to see what in inside...')
            print('-----------------------------')

def delete_notes():
    all_notes =[]

    try:
        with open('notas.txt', 'r') as file:
            all_notes = file.readlines()
    except FileNotFoundError:
        print('You dont have notes here...')
        return
    
    for index, notes in enumerate(all_notes):
        print(f"[{index + 1}] {notes}", end = '')
    
    try:
        user_option = int(input('\n Delete Note (type a number):  '))
    except ValueError:
        print("Wrong input, please type a number!!!")
        return

    if 0 < user_option <= len(all_notes):
        all_notes.pop(user_option - 1)
    else:
        print('You need to select a number of the list!')

    #salvar a lista para atualizar ela! 
    try:
        with open('notas.txt', 'w') as file:
            for note in all_notes:
                file.write(note)
    
            print('-----------------------------------')
            print("Notes Deleted with succes!!! ")
            print('-----------------------------------')

    except Exception as e:
        # Um tratamento de erro genérico caso algo dê errado na escrita
        print(f"Error when save the file: {e}")
    
menu()