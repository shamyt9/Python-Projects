🔐 Python Password Manager (File-Based)

This project is a simple file-based password manager built using Python.
It demonstrates how credentials can be securely stored using hashing and managed using JSON files, focusing on core concepts like file handling, data persistence, and basic security.

🚀 Project Overview

The Password Manager allows you to:
Store website credentials (website, username, password)
Secure passwords using SHA-256 hashing
Save credentials in a structured JSON file
Retrieve and display stored credential data
Automatically create the data file if it does not exist

This project is designed for learning purposes and helps understand how password storage systems work internally.

🛠️ Technologies & Libraries Used
Library	Purpose
os	File existence checking
json	Storing credentials in structured format
hashlib	Password hashing using SHA-256
getpass	Secure password input (future extension)
🔒 Security Approach

Passwords are never stored in plain text
Each password is converted into a SHA-256 hash
Hashing ensures one-way security (passwords cannot be decrypted)

Example:
mypassword → 34819d7beeabbc..

📂 Data Storage Format

Credentials are stored in passwords.json:

{
    "example.com": {
        "username": "user123",
        "password": "hashed_password_here"
    }
}

📌 Key Functions

hash_password() – Hashes passwords securely
load_data() – Loads or initializes the JSON data file
save_password() – Stores credentials safely
show_data() – Displays stored entries
get_password() – Retrieves hashed password for a website

🎯 Learning Outcomes

Understanding password hashing vs encryption
Working with JSON for persistent storage
File handling using Python
Implementing basic security best practices
Structuring a small real-world Python project

⚠️ Disclaimer

This project is intended for educational purposes only.
It is not a full-featured or production-ready password manager.

🔮 Future Enhancements

Master password authentication
Password verification instead of display
Password strength validation
CLI menu-based interaction
Encryption for stored data
Delete / update credentials

🧠 One-Line Summary (Resume-Ready)

Built a Python-based password manager using JSON storage and SHA-256 hashing to securely store and manage credentials.
