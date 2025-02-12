import re
def main():
    
    contacts = {}

    while True:
        print('---------------------------------------------------------------------------------------------------------------')
        print('Contact Book Management App')
        print('---------------------------------------------------------------------------------------------------------------')
        print("\n")  
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
                Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
                if Pattern.match(phone):
                    contacts[name] = {'phone': phone,'company':company,'title':title}
                else:
                    print('Invalid phone number')
                    main()
                email = input('Enter email: ')
                valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
                if valid:
                    contacts[name] = {'phone': phone,'company':company,'title':title, 'email': email}
                    print("Successfully added contact phone book")
                else:
                    print('Invalid email address')
                    main()
                
        elif choice == '2':
            name = input('Enter contact name to views= ')
            if name in contacts:
                contact =contacts[name]
                print(" ")
                print("_______________________________________________________________________________________________________________")
                print(f'Name: {name}')
                print(f'Phone: {phone}')
                print(f'Company: {company}')
                print(f'Title: {title}')
                print(f'Email: {email}')
                print("_______________________________________________________________________________________________________________")
                print("\n")  
            else:
                print(f'Contact name {name} does not exist')
                
        elif choice == '3':
            name = input('Enter contact name to edit: ')
            if name in contacts:
                phone = input('Enter new phone number: ')
                Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
                if Pattern.match(phone):
                    contacts[name] = {'phone': phone,'company':company,'title':title}
                else:
                    print('Invalid phone number')
                    main()
                company = input('Enter new company: ')
                title = input('Enter new title: ')
                email = input('Enter new email: ')
                valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
                if valid:
                    contacts[name] = {'phone': phone,'company':company,'title':title, 'email': email}
                    print("Successfully updated contact")
                else:
                    print('Invalid email address')
                    main()
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
            print('---------------------------------------------------------------------------------------------------------------')
            print('                                      Exiting the program...                     ')
            break

        else:
            print(f'Invalid option - {choice}')
        
    print("                       Thank you for using our contact book. Have a nice day!                                 ")
    print('---------------------------------------------------------------------------------------------------------------')

main()