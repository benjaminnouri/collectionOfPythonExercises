from cryptography.fernet import Fernet

# Function to generate and save the encryption key to a file
def write_key():
    key = Fernet.generate_key()  # Generate a new key
    with open("./mykey.key", "wb") as f:
        f.write(key)  # Write the key to a file

# Function to load the encryption key from a file
def load_key():
    try:
        with open("./mykey.key", "rb") as f:
            key = f.read()  # Read the key from the file
            return key
    except FileNotFoundError:  # If the file does not exist, generate a new key
        write_key()
        return load_key()

# Load the encryption key
key = load_key()
fernet = Fernet(key)  # Create a Fernet object for encryption/decryption using the key

# Function to add a new username and encrypted password to the file
def add_pass(username, password):
    encrypted_pass = fernet.encrypt(password.encode()).decode()  # Encrypt the password
    with open("./passwords.txt", "a") as f:
        f.write(f"{username}|{encrypted_pass}\n")  # Save the username and encrypted password
    print("Password added!")

# Function to view saved usernames and passwords (decrypt passwords)
def view_pass():
    try:
        with open("./passwords.txt", "r") as f:
            for line in f:
                username, encrypted_pass = line.strip().split('|')  # Split username and encrypted password
                password = fernet.decrypt(encrypted_pass.encode()).decode()  # Decrypt the password
                print(f"USER: {username} | PASSWORD: {password}")  # Display username and decrypted password
    except FileNotFoundError:
        print("No passwords found.")

# Main loop to handle user input for viewing or adding passwords
while True:
    user_input = input("Enter the mode (v: view, a: add, q: quit): ").lower()

    if user_input == "v":
        print("Your passwords are as follows:")
        view_pass()  # View saved passwords
    elif user_input == "a":
        print("Let's add a new username-password pair.")
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        add_pass(username, password)  # Add new username-password pair
    elif user_input == "q":
        break  # Exit the loop
    else:
        print("Invalid mode! Please choose 'v', 'a', or 'q'.")
