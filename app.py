# sourcery skip: remove-dict-items

contacts = {}

while True:
    print('\n Contact Book Management App')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Edit Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contacts')
    print('7. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        name = input('Enter name: ')
        if name in contacts:
            print(f'Contact name {name} already exists')
        else:
            company = input('Enter your company: ')
            title = input('Enter your title: ')
            phone = input('Enter phone number: ')
            email = input('Enter email: ')
            contacts[name] = {'phone': phone,'company':company,'title':title, 'email': email}
            print('\nContact added successfully.')

    elif choice == '2':
        name = input('Enter contact name to views= ')
        if name in contacts:
            contact =contacts[name]
            print()
            print(f'Name: {name}')
            print(f'Phone: {phone}')
            print(f'Company: {company}')
            print(f'Title: {title}')
            print(f'Email: {email}')
            print()
        else:
            print(f'Contact name {name} does not exist')
            
    elif choice == '3':
        name = input('Enter contact name to edit: ')
        if name in contacts:
            phone = input('Enter new phone number: ')
            company = input('Enter new company: ')
            title = input('Enter new title: ')
            email = input('Enter new email: ')
            contacts[name] = {'phone': phone,'company':company,'title':title, 'email': email}   
        else:
            print(f'Contact name {name} does not exist')

    elif choice == '4':
        name = input('Enter contact name to delete: ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} deleted successfully.')
        else:
            print(f'Contact name {name} does not exist')

    elif choice == '5':
        search_name = input('Enter contact name to search: ')
        found = False
        for name, contact in contacts.items():
            if name.lower() == search_name.lower():
                print(f'Found your Contact Details- \nName: {name}\nPhone: {phone}\nCompany: {company}\nTitle: {title}\nEmail: {email}')
                found = True
        if not found:
            print(f'Contact name {search_name} does not found')
            
    elif choice == '6':
        print()
        print(f'Total contacts in your book: {len(contacts)}')

    elif choice == '7':
        print('--------------------------------------------------------------------------------------')
        print('                                    Exiting the program...                     ')
        break

    else:
        print(f'Invalid option - {choice}')
    
print("                       Thank you for using our contact book. Have a nice day!                                 ")
print('--------------------------------------------------------------------------------------')
        