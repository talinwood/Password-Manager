# Password-Manager
Project Summary

This project is a local password manager developed in Python that allows users to store and manage website credentials in an encrypted vault. Users can add, view, and list password entries through a terminal-based interface. Password data is protected using a master password, with PBKDF2-HMAC-SHA256 used to derive an encryption key and AES-256-GCM used to encrypt and authenticate vault contents. The project is designed to keep stored credentials protected from someone who obtains the vault file, while detecting unauthorized modifications to encrypted data. The application uses JSON for data serialization and local file storage, with separate modules for password entries, management operations, encryption, and storage.

Architecture

The application is organized into separate modules so that password management, encryption, and file storage are handled independently.

flowchart TD
    A[User] --> B[main.py]
    B --> C[manager.py]
    C --> D[password_entry.py]
    C --> E[vault.py]
    E --> F[encryption.py]
    E --> G[storage.py]
    F --> H[PBKDF2-HMAC-SHA256]
    H --> I[AES-256-GCM]
    I --> G
    G --> J[(Encrypted Local Vault)]

General Workflow
The user interacts with the application through the terminal interface.
main.py receives the user's selections and input.
manager.py handles password-entry operations.
password_entry.py defines the structure of each password entry.
The vault workflow coordinates converting entries into data that can be encrypted and stored.
encryption.py derives an encryption key from the master password and encrypts or decrypts vault data.
storage.py handles reading and writing the encrypted vault file.

Folder Structure

Password-Manager/
│
├── PasswordManager/
│   ├── Tests/
│   │   ├── test_manager.py
│   │   └── test_vault.py
│   │
│   ├── encryption.py
│   ├── main.py
│   ├── manager.py
│   ├── password_entry.py
│   ├── storage.py
│   └── vault.py
│
├── README.md
└── DEMO.md

Main Files and Directories
File or Folder
Purpose
PasswordManager/
Contains the main application source code.
Tests/
Contains automated tests for application functionality.
test_manager.py
Tests password-entry management operations.
test_vault.py
Contains tests for vault functionality.
main.py
Provides the terminal-based user interface and application menu.
manager.py

Prerequisites
The following software and tools are needed to run and test the project:
Operating System: macOS, Windows, or Linux.
Python: Python 3.11 or compatible Python 3 version.
pip: Python package installer.
cryptography: Python library used for AES-GCM encryption.
pytest: Used to execute automated tests.
Git: Used to clone and manage the project repository.

Known Limitations
The application is a local prototype and has not undergone a professional security audit.
Security depends heavily on the strength and secrecy of the user's master password.
Malware, keyloggers, or an attacker with access to an unlocked computer may be able to access credentials.
Deleting or corrupting the local vault file can result in loss of stored credentials.
Password generation, clipboard auto-clearing, and automatic vault locking are not included in the confirmed core functionality.
The complete vault workflow should be tested end-to-end to verify that saving, loading, encryption, and decryption work together correctly.
The project does not currently provide cloud synchronization or account recovery.

Demonstration
For instructions on running the application and demonstrating its functionality, see:
DEMO.md