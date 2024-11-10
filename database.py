import sqlite3

def create_connection():
    connection = sqlite3.connect('contacts.db')
    return connection

def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    # Création de la table clients
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            phone TEXT
        )
    ''')

    # Création de la table contacts avec une clé étrangère client_id
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            client_id INTEGER,
            FOREIGN KEY (client_id) REFERENCES clients (id)
        )
    ''')

    connection.commit()
    connection.close()

# Appeler cette fonction pour créer les tables lors du lancement du programme
create_tables()


def add_client(name, address, phone):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO clients (name, address, phone) VALUES (?, ?, ?)", (name, address, phone))
    connection.commit()
    connection.close()

def get_clients():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    connection.close()
    return clients

def update_client(client_id, name, address, phone):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE clients SET name = ?, address = ?, phone = ? WHERE id = ?", (name, address, phone, client_id))
    connection.commit()
    connection.close()

def delete_client(client_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    connection.commit()
    connection.close()

def add_contact(name, email, phone, client_id=None):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO contacts (name, email, phone, client_id) VALUES (?, ?, ?, ?)", (name, email, phone, client_id))
    connection.commit()
    connection.close()

def get_contacts_by_client(client_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts WHERE client_id = ?", (client_id,))
    contacts = cursor.fetchall()
    connection.close()
    return contacts

def get_contacts():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    connection.close()
    return contacts

def update_contact(contact_id, name, email, phone):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE contacts SET name = ?, email = ?, phone = ? WHERE id = ?", (name, email, phone, contact_id))
    connection.commit()
    connection.close()

def delete_contact(contact_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    connection.commit()
    connection.close()
