import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
def get_db_connection():
    conn = sqlite3.connect(nasa.db)
    return conn

# Insert a new contact into the database
def add_contact(category, name, email, phone):
    conn = get_db_connection()
    try:
        conn.execute('''
            INSERT INTO contacts (category, name, email, phone) 
            VALUES (?, ?, ?, ?);
        ''', (category, name, email, phone))
        conn.commit()
        print("Contact added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Contact with this email already exists.")
    finally:
        conn.close()

# Get user input for contact information
def get_contact_info():
    category = input("Enter category (student/public): ")
    name = input("Enter full name: ")
    email = input("Enter email address: ")
    phone = input("Enter phone number: ")
    return category, name, email, phone

if __name__ == '__main__':
    # Create the table if it doesn't already exist
    create_table()

    # Get contact info from user input
    category, name, email, phone = get_contact_info()

    # Insert the contact into the database
    add_contact(category, name, email, phone)
