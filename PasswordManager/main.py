
import os
from getpass import getpass # hides password typing in
from manager import add_entry, list_entries, view_entry, delete_entry, update_entry
from vault import save_entries, load_entries

# vault file lives in the same folder as main.py
VAULT_FILE = os.path.join(os.path.dirname(__file__), "vault.json")

#display main menu
def display_menu():
    print("\n==============================")
    print("       PASSWORD MANAGER")
    print("==============================")
    print("1. Add Password")
    print("2. View Password")
    print("3. List Passwords")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Exit")
    print("==============================")


#Add a new password
def add_password(entries):
    
    print("\n--- Add New Password ---")

    website = input("Enter website: ")
    username = input("Enter username: ")
    password = getpass("Enter password: ")

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


#Update an existing password
def update_password(entries):

    print("\n--- Update Password ---")

    if not entries:
        print("No passwords have been saved yet.")
        return

    list_passwords(entries)

    try:
        number = int(input("\nSelect an entry number: "))
        new_username = input("New username (leave blank to keep): ")
        new_password = getpass("New password (leave blank to keep): ")

        entry = update_entry(entries, number, new_username, new_password)
        print(f"\n{entry.get_website()} updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except IndexError as e:
        print(f"Error: {e}")


#Delete a password
def delete_password(entries):

    print("\n--- Delete Password ---")

    if not entries:
        print("No passwords saved yet.")
        return

    list_passwords(entries)

    try:
        number = int(input("\nSelect an entry number: "))
        entry = delete_entry(entries, number)
        print(f"\n{entry.get_website()} deleted successfully!")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
    except IndexError as e:
        print(f"Error: {e}")



# creating a new vault or unlocking the preexisting one
# returns the entries and master_password, or None if it fails
def unlock_vault():

    if not os.path.exists(VAULT_FILE):
        print("\nNo vault was found. Creating a new one.")
        print("Tip: use at least 12 characters with uppercase, lowercase, numbers, and special characters.\n")

        # keep asking until the passwords match and aren't empty
        while True:
            master_pass = getpass("Create the master password: ")
            confirm = getpass("Confirm the master password: ")

            if master_pass and master_pass == confirm:
                break

            print("Passwords didn't match or they were empty. Please try again.\n")

        entries = []
        save_entries(VAULT_FILE, entries, master_pass)
        print("\nVault successfully created!")
        return entries, master_pass

    # the vault does exist so try to unlock it
    master_pass = getpass("Enter master password: ")
    try:
        entries = load_entries(VAULT_FILE, master_pass)
    except ValueError as e:
        print(f"Error: {e}")
        return None, None

    print("Vault unlocked!")
    return entries, master_pass

#Main program loop
def main():

    # unlock or create vault before showing the menu
    entries, master_pass = unlock_vault()
    if entries is None:
        return

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            add_password(entries)
            save_entries(VAULT_FILE, entries, master_pass)
        elif choice == "2":
            view_password(entries)
        elif choice == "3":
            list_passwords(entries)
        elif choice == "4":
            update_password(entries)
            save_entries(VAULT_FILE, entries, master_pass)
        elif choice == "5":
            delete_password(entries)
            save_entries(VAULT_FILE, entries, master_pass)
        elif choice == "6":
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()