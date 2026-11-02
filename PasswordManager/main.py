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