size = 3
client_list = [None] * size

def add_client_linear():
    global client_list
    global size
    for _ in range(size):
        if None in client_list:
            client_id = int(input("client id: "))
            name = input("client name: ")
            telephone = input("client telephone: ")
            client_details = [client_id, name, telephone]

            index = client_id % size
            # Inserting record using linear probing in case of collision
            for i in range(size):
                if client_list[index] == None:
                    client_list[index] = client_details
                    print("adding data", index, client_details)
                    break
                else:
                    index = (index + 1) % size
        else:
            print("Maximum number of clients reached.")
            break

def add_client_quadratic():
    global client_list
    global size
    for _ in range(size):
        if None in client_list:
            client_id = int(input("client id: "))
            name = input("client name: ")
            telephone = input("client telephone: ")
            client_details = [client_id, name, telephone]

            index = client_id % size
            i = 1
            # Inserting record using quadratic probing in case of collision
            while client_list[index] is not None:
                index = (index + i ** 2) % size
                i += 1
                
            client_list[index] = client_details
            print("adding data", index, client_details)
        else:
            print("Maximum number of clients reached.")
            break

def search_client():
    client_id = int(input("client id: "))
    index = client_id % size
    for i in range(size):
        if client_list[index] is not None:
            if client_list[index][0] == client_id:
                print("client is found at index ", index, client_list[index])
                return
        index = (index + 1) % size
    print("client not found")

def delete_client():
    client_id = int(input("client id: "))
    index = client_id % size
    for i in range(size):
        if client_list[index] is not None:
            if client_list[index][0] == client_id:
                client_list[index] = None
                print("client deleted")
                return
        index = (index + 1) % size
    print("client not found")

def display_menu():
    print("\nMenu:")
    print("1. Add Client (Linear Probing)")
    print("2. Add Client (Quadratic Probing)")
    print("3. Search Client")
    print("4. Delete Client")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_client_linear()
    elif choice == '2':
        add_client_quadratic()
    elif choice == '3':
        search_client()
    elif choice == '4':
        delete_client()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
