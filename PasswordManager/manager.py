from password_entry import PasswordEntry

#Add a new password entry to the list of entries
def add_entry(entries, website, username, password):

    # Validate input
    if not website or not username or not password:
        raise ValueError("All fields are required.")
    
    # Create the new entry
    entry = PasswordEntry(website, username, password)

    # add new entry to the list
    entries.append(entry)

    return entry

#List all saved password entries
def list_entries(entries):
    results = []

    # Enumerate through the entries and create a list of dictionaries with entry details
    for index, entry in enumerate(entries, start=1):

        # Append the entry details to the results list
        results.append({
            "number": index,
            "website": entry.get_website(),
            "username": entry.get_username(),
        })

    return results

#View a specific password entry by its index
def view_entry(entries, entry_number):

    # Validate the entry number
    if entry_number < 1 or entry_number > len(entries):
        raise IndexError("Invalid entry number :(")
    
    # Return the entry at the specified index (adjusted for 0-based indexing)
    return entries[entry_number - 1]

# delete a password entry by its number
def delete_entry(entries, entry_number):

    # Validate the entry number
    if entry_number < 1 or entry_number > len(entries):
        raise IndexError("Invalid entry number :(")

    # remove and return the entry (with the 0 based indexing)
    return entries.pop(entry_number - 1)

# update the username and/or password of an entry
def update_entry(entries, entry_number, new_username, new_password):

    # Validate the entry number
    if entry_number < 1 or entry_number > len(entries):
        raise IndexError("Invalid entry number :(")

    entry = entries[entry_number - 1]

    # only change the fields that were filled in 
    if new_username:
        entry.set_username(new_username)

    if new_password:
        entry.set_password(new_password)

    return entry



