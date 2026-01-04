import random
import string

def generate_password():
    length = int(input("Enter password length: "))
    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)

def main():
    while True:
        print("1. Generate Password")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            generate_password()
        elif choice == "2":
            break
        else:
            print("Invalid option")

main()
