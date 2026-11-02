
from manager import add_entry, list_entries, view_entry


# Create an empty collection
entries = []


# Test adding entries
add_entry(
    entries,
    "google.com",
    "example@gmail.com",
    "password123"
)

add_entry(
    entries,
    "github.com",
    "developer123",
    "githubpassword"
)


# Test listing entries
results = list_entries(entries)

assert len(results) == 2
assert results[0]["website"] == "google.com"
assert results[1]["website"] == "github.com"


# Test viewing an entry
entry = view_entry(entries, 1)

assert entry.get_website() == "google.com"
assert entry.get_username() == "example@gmail.com"
assert entry.get_password() == "password123"


print("All manager tests passed!")
