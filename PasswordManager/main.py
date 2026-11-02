from manager import add_entry, list_entries, view_entry

#display main menu
def display_menu():
    print("\n==============================")
    print("       PASSWORD MANAGER")
    print("==============================")
    print("1. Add Password")
    print("2. View Password")
    print("3. List Passwords")
    print("4. Exit")
    print("==============================")

#Add a new password
def add_password(entries):
    
    print("\n--- Add New Password ---")

    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        add_entry(entries, website, username, password)
        print("\nPassword entry added successfully!")
    except ValueError as error:
        print(f"Error: {error}")

#View existing password
def view_password(entries):
    
    print("\n--- View Password ---")
    
    if not entries:
        print("No passwords saved yet.")
        return
    
    list_passwords(entries)
    
    try:
        number = int(input("\nSelect an entry number: "))

        entry = view_entry(entries, number)

        print("\nWebsite:", entry.get_website())
        print("Username:", entry.get_username())
        print("Password:", entry.get_password())

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except IndexError as error:
        print(f"Error: {error}")

#Display all saved websites
def list_passwords(entries):

    print("\n--- Saved Passwords ---")

    results = list_entries(entries)

    if not results:
        print("No passwords saved yet.")
        return

    for result in results:
        print(f"{result['number']}. {result['website']} - {result['username']}")
    