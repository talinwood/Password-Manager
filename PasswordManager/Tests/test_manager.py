
from manager import add_entry, list_entries, view_entry


def test_add_and_list_entries():

    entries = []

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

    results = list_entries(entries)

    assert len(results) == 2
    assert results[0]["website"] == "google.com"
    assert results[1]["website"] == "github.com"


def test_view_entry():

    entries = []

    add_entry(
        entries,
        "google.com",
        "example@gmail.com",
        "password123"
    )

    entry = view_entry(entries, 1)

    assert entry.get_website() == "google.com"
    assert entry.get_username() == "example@gmail.com"
    assert entry.get_password() == "password123"


def test_invalid_entry_number():

    entries = []

    try:
        view_entry(entries, 1)
        assert False, "Expected IndexError"

    except IndexError:
        pass
