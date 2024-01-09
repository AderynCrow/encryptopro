import tkinter as tk
from tkinter import *
from cryptography.fernet import Fernet
from tkinter import filedialog
import tkinter as tk
##Import of Tkinter module

window = Tk()
##Creates the size of the window
window.title("encrypter")
window.geometry("425x125")


for i in range(3):
    window.columnconfigure(i, weight=1, minsize=30)
    window.rowconfigure(i, weight=1, minsize=30)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED
        )
        frame.grid(row=i, column=j)

##Adds a title to the Windows GUI for the window
window.configure(bg="#05B2DC")

def enc():
    inputfile = filedialog.askopenfilename()
    outputfile = inputfile + ".encpy"
    data = open(inputfile, "rb").read()
    f = open(outputfile, "wb")
    key = KeyInput.get()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    f.write(encrypted)
def dec():
    inputfile = filedialog.askopenfilename()
    outputfile = inputfile.replace(".encpy", "")
    data = open(inputfile, "rb").read()
    f = open(outputfile, "wb")
    key = KeyInput.get()
    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)
    f.write(encrypted)
def newkey():
    KeyInput.delete(first=0, last=100)
    key = Fernet.generate_key()
    KeyInput.insert(0, key)

KeyInput = Entry(window, width=54, bg="#5EE0F1", fg= "#031A6B", selectbackground="#031A6B", selectforeground="#5EE0F1")
KeyInput.insert(0, "Enter Key or get new one")
KeyInput.grid(row=0, column=0)
key= KeyInput.get()

KeyButton = Button(window, fg= "#031A6B" , bg= "#05B2DC", activebackground= "#087CA7", text="New Key", command=newkey)
KeyButton.grid(row=0, column=1)

enceyptButton = Button(window, fg= "#031A6B" , bg= "#05B2DC", activebackground= "#087CA7", width=46, text= "Encrypt File",command=enc)
enceyptButton.grid(row=1, column=0)

decryptButton = Button(window, fg= "#031A6B" , bg= "#05B2DC", activebackground= "#087CA7", width=46, text="Decrypt File", command=dec)
decryptButton.grid(row=2, column=0)


window.mainloop()
##Loops the window to prevent the window from just "flashing once"