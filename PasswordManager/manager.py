from password_entry import PasswordEntry

#Add a new password entry to the list of entries
def add_entry(entries, username, password, website):

    # Validate input
    if not website or not username or not password:
        raise ValueError("All fields are required.")
    
    # Check for duplicate entries
    entry = PasswordEntry(username, password, website)

    # Check if the entry already exists in the list
    entries.append(entry)

    return entry

#List all saved password entries
def list_entries(entries):
    results = []

    for index, entry in enumerate(entries, start=1):

        results.append({
            "number": index,
            "website": entry.get_website(),
            "username": entry.get_username(),
        })

    return results
