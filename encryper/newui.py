from tkinter import *
from cryptography.fernet import Fernet
from tkinter import filedialog
import tkinter as tk

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

def test():
    widthscale=window.winfo_width()/425
    widthscale=int(widthscale)
    buttonwidthscale=widthscale*40
    Button.configure(width=buttonwidthscale)
    print(widthscale)
    print(window.winfo_width())

Button =Button(window, width=40, fg= "#031A6B" , bg= "#05B2DC", activebackground= "#087CA7", text="New Key", command=test)
Button.grid(row=0, column=1)

window.mainloop()
##Loops the window to prevent the window from just "flashing once"