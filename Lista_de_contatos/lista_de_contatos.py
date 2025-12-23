# Crie um programa que permita adicionar, listar e pesquisar contatos.

contacts_list = []

#Menu para apresentação das opções que o usuario tem!
def menu():
    global contacts_list
    print("===============================")
    print("   --> |(Contacts List)| <--   ")
    print("===============================")

    print("!You need to select ONE option!")
    print("===============================")
    print("[1] Add Contact")
    print("[2] Contact List")
    print("[3] Search with name")
    print("[4] Exit")
    print("===============================")

    while True: 
        try:
            option = int(input("type a number that you want: "))
            if option == 1:
                add_contacts(contacts_list)
            elif option == 2: 
                contacts(contacts_list)
            elif option == 3:
                search_contact(contacts_list)
            elif option == 4:
                print("!!! Bye Bye - See you soon !!!")
                break
            else:
                print("Invalid Option, please choose between 1 and 4.")
        except ValueError:
            print("Invalid Input, please type a Number.")


#Area de adição dos contatos para a lista! 
def add_contacts(contacts_list):
    print("--> | to add a contact you need (Name, Cellphone, E-mail) | <--")
    name = str(input("Contact Name: ")).lower()
    cellphone = int(input("Contact Number: "))
    email = str(input("Contact E-mail: ")).lower()
    print("!!!Contact add with succes!!!")

    new_contact = {
        "name": name,
        "cellphone": cellphone,
        "E-mail": email
    }

    contacts_list.append(new_contact)
    return contacts_list
#Area de Listagem dos contatos da lista! 
def contacts(contacts_list):
    if not contacts_list:
        print("No one contacts in the list..")
    else:
        print("===========================")
        print("==== Your contact list ====")
        print("===========================")
        for index, contact in enumerate(contacts_list):
            print(f"Contato #{index + 1}")
            print(f"Nome: {contact['name']}")
            print(f"Cellphone: {contact['cellphone']}")
            print(f"E-mail: {contact['E-mail']}")
            print("-----------------------------------")
#Area de procura dos contatos da lista!
def search_contact(contacts_list):
    contact_found = False
    search = str(input("Type a Name to search: ")).lower()
    
    print(">>>>Results of the search<<<<")
    print("--------------------")

    for contact in contacts_list:
        if search in contact["name"].lower():
            contact_found = True
            print(f"Nome: {contact['name']}")
            print("--------------------")
            print(f"Nome: {contact['name']}")
            print(f"Telefone: {contact['cellphone']}")
            print(f"E-mail: {contact['E-mail']}")
            print("--------------------")
    if not contact_found:
        print("No one conctact found in your list.")
        print("--------------------")

menu()
