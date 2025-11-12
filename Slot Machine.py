import string
# create character set
chars = list(string.ascii_letters + string.punctuation + string.digits + ' ')

#create shuffled keys for encryption

keys = chars.copy()
random.shuffle(keys)

def encrypt(message):
    encrypted_message = ""
    for char in message:
        if char in chars:
            index = chars.index(char)
            encrypted_message += keys[index]
        else:
            encrypted_message += char  #left the unknown chars unchanged
    return encrypted_message

def decrypt(message):
    decrypted_message = ""
    for char in message:
        if char in keys:
            index = keys.index(char)
            decrypted_message += chars[index]
        else:
            decrypted_message += char   #left the unknown chars unchanged
    return decrypted_message

def quit_program():
    print("**************************************")
    print("Thank you for using Encryption Program")
    print("**************************************")
    return False

# main loop

def main():
    running = True
    while running :

        options = input("Choose your option:\n 1 for Encryption\n 2 for Decryption\n 3 for Quit\n ").strip()

        if options == "1":
            print("Your encrypted message is: ", encrypt(input("Enter your message: ")))
        elif options == "2":
            print("Your decrypted message is: ", decrypt(input("Enter your message: ")))
        elif options == "3":
            running = quit_program()
        else:
            print("Invalid option. Please try again.")

while True:
    main()  # run one session
    again = input("\nDo you want to start again? (y/n): ").strip().lower()
    if again != "y":
        print("Okay, program terminated. Goodbye 👋")
        break












