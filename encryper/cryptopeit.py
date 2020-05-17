from cryptography.fernet import Fernet
from tkinter import filedialog
import tkinter as tk
#making the root window and then closing it to not be distracting
rootwindow = tk.Tk()
rootwindow.withdraw()
print('''Welcome to the CRYPTO
We encrypt everything you want!
We can Generate a key for you or you can Provide us with one!''')
key = input('Provide key: ("new" to generate automatically)> ')
if key.lower() == "new" or key.lower() == "" \
                                          "":
    # Generating new key if user has none
    key = Fernet.generate_key()
    print(key.decode("ascii"))
print('type "help" for help')
command = input("> ")
while command.lower() != "quit":
    if command.lower() == "help":
        print('''key - generate new key or take existing
show key - show current key
enc - choose a file to encrypt
dec - chose a file to decrypt
quit - exit the programm''')
    elif command.lower() == "key":
        key = input('Provide key: ("new" to generate automatically)> ')
        if key.lower() == "new":
            # Generating new key if user has none
            key = Fernet.generate_key()
            print(key.decode("ascii"))
    elif command.lower() == "enc":
        # Encrypting a File the User specifies
        print("Input file Path for next step")
        inputfile = filedialog.askopenfilename()
        outputfile = inputfile + ".encpy"
        data = open(inputfile, "rb").read()
        f = open(outputfile, "wb")
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        f.write(encrypted)
        print(outputfile + ' Is now the encrypted file!')
    elif command.lower() == "dec":
        # Default: Decrypting File the user specifies
        print("Input file Path for next step")
        inputfile = filedialog.askopenfilename()
        outputfile = inputfile.replace(".encpy", "")
        data = open(inputfile, "rb").read()
        f = open(outputfile, "wb")
        fernet = Fernet(key)
        encrypted = fernet.decrypt(data)
        f.write(encrypted)
        print(outputfile + ' Is now the decrypted file!')
    elif command.lower() == "show key":
        print(key.decode("ascii"))
    else:
        print("Unkown command; please try again")
    command = input("> ")