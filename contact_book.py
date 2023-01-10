contact_book = []
first = 0

# menu/intro
def menu():
    global first
    if first == 0:
        print("Welcome to your contact book!")
        first += 1
    action = int(input("""
what do you want to do?
1: Add contact
2: Remove contact
3: Access contact    
4: List all contacts
5: Quit
"""))
    while action < 1 or action > 5:
        action = int(input("Please select an option above"))

    if action == 1:
        print("Please enter the following information :")
        name = input('\nName (required): ')
        phone_num = input("Phone number (required): ")
        email = input("Email: ")
        address = input("Address: ")
        add(name, phone_num, email, address)
    elif action == 2:
        name = input("Contact name: ")
        remove(name)
    elif action == 3:
        name = input("Contact name: ")
        access(name)
    elif action == 4:
        list_contacts()
    elif action == 5:
        quit()

# adds contact to contact_book
def add(name, phone_num, email=None, address=None):
    if email == '':
        email = None
    if address == '':
        address = None
    contact_book.append([name, phone_num, email, address])
    menu()

# removes contact from contact_book
def remove(name):
    for contact in contact_book:
        if name == contact[0]:
            contact_book.remove(contact)
    menu()

# shows certain contact and allows choice to edit the contact
def access(name):
    match = 0
    for contact in contact_book:
        if name == contact[0]:
            match = 1
            print("Name: " + contact[0])
            print("Phone number: " + contact[1])
            if contact[2] != None:
                print("Email address: " + contact[2])
            if contact[3] != None:
                print("Adrress: " + contact[3])
    
    if match == 1:
        edit_choice = int(input("""\nDo you want to edit this contact?
1: yes
2: no
"""))
        if edit_choice == 1:
            edit(name)
    else:
        print("No matches were found.")
    menu()

# gets index of certain contact name in contact_book
def get_index(name):
        index = 0
        for contact in contact_book:
            if contact[0] == name:
                return index
            index += 1

# allows user to edit contact that was accessed
def edit(name):
    global contact_book
    edit_choice = int(input("""
What would you like to edit?
1: Name
2: Phone number
3: Email address
4: Address
"""))
    print("\nCurrent: " + contact_book[get_index(name)][edit_choice - 1])
    contact_book[get_index(name)][edit_choice - 1] = input("Type new: ")
    menu()

def list_contacts():
    for contact in contact_book:
        print(contact)
    menu()

menu()