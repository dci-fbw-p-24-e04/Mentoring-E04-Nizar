from bank_system import *

def main():
    while True:
        print("\n1. Add new client")
        print("2. Update existing client")
        print("3. Delete client")
        print("4. Display client")
        print("5. Display clients overview")
        print("6. Display total")
        print("t. Transfer Ca$h")
        print("d. Deposit")
        print("w Withdraw")
        print("q. Exit")
        clients = load_clients()
        option = input("\n Select an option : ")
        if option == '1':
            name = input('Enter the new client name: ')
            dob = input('Enter the client dob (yyyy-mm-dd): ')
            balance = float(input('Enter client balance: '))
            add_client(clients,name,dob,balance)
            print("Client added succesfully")
        elif option == '2':
            client_id = int(input('Enter cliend ID: '))
            display_client(clients,client_id)
            name = input('Enter new client name (Leave empty to keep current)')
            dob = input('Enter new client dob (yyyy-mm-dd) (Leave empty to keep current)')
            balance = input('Enter new client balance (Leave empty to keep current)') 
            if balance != "":
                balance = float(balance)
            update_client(clients,client_id,name,dob,balance)
        elif option == '3':
            client_id = int(input('Enter cliend ID: '))
            remove_client(clients,client_id)

        elif option == '4':
            client_id = int(input('Enter cliend ID: '))
            display_client(clients,client_id)

        elif option == '5':
            clients_overview(clients)
        elif option == '6':
            print(cs('Calculating...','green'))
            time.sleep(1)
            total = get_total_amount(clients)
            print("Total bank balance:", total)
        elif option=='t':
            client_send = int(input('Enter the sender ID: '))
            amount = float(input('Enter the amount: '))
            client_to = int(input('Enter the receiver ID: '))
            transfer_money(clients,client_send,client_to,amount)
        elif option == 'q':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()