from database import add_contact, get_contacts, update_contact, delete_contact

from database import add_client, get_clients, update_client, delete_client, add_contact, get_contacts_by_client

def main():
    while True:
        print("\nMenu:")
        print("1. Ajouter un client")
        print("2. Voir les clients")
        print("3. Mettre à jour un client")
        print("4. Supprimer un client")
        print("5. Ajouter un contact à un client")
        print("6. Voir les contacts d'un client")
        print("7. Quitter")
        choix = input("Choisis une option : ")

        if choix == '1':
            name = input("Nom du client : ")
            address = input("Adresse : ")
            phone = input("Téléphone : ")
            add_client(name, address, phone)
            print("Client ajouté.")

        elif choix == '2':
            clients = get_clients()
            for client in clients:
                print(client)

        elif choix == '3':
            client_id = int(input("ID du client à mettre à jour : "))
            name = input("Nom : ")
            address = input("Adresse : ")
            phone = input("Téléphone : ")
            update_client(client_id, name, address, phone)
            print("Client mis à jour.")

        elif choix == '4':
            client_id = int(input("ID du client à supprimer : "))
            delete_client(client_id)
            print("Client supprimé.")

        elif choix == '5':
            client_id = int(input("ID du client : "))
            name = input("Nom du contact : ")
            email = input("Email : ")
            phone = input("Téléphone : ")
            add_contact(name, email, phone, client_id)
            print("Contact ajouté au client.")

        elif choix == '6':
            client_id = int(input("ID du client pour voir ses contacts : "))
            contacts = get_contacts_by_client(client_id)
            for contact in contacts:
                print(contact)

        elif choix == '7':
            print("À bientôt!")
            break

        else:
            print("Option invalide. Essaie encore.")

if __name__ == "__main__":
    main()
