from tkinter import *
import os
from tkinter import messagebox

import pyqrcode

window = Tk()
window.title("QR code Generator")

Subject = StringVar()
SubEntry = Entry(window, textvariable=Subject)
SubEntry.grid(row=0, column=1, sticky=N + S + W + E)

Sub = Label(window, text="Enter Subject")
Sub.grid(row=0, column=0, sticky=N + S + W + E)

Fname = Label(window, text="Enter Filename")
Fname.grid(row=1, column=0, sticky=N + S + W + E)

name = StringVar()
name_in = Entry(window, textvariable=name)
name_in.grid(row=1, column=1, sticky=N + S + W + E)


def generator():
    if len(Subject.get()) != 0:
        global qr, photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showinfo('Please enter some Subject')
    try:
        showcode()
    except:
        pass


button = Button(window, text="Generate Code", width=20, command=generator)
button.grid(row=0, column=3, sticky=N + S + W + E)

imageLabel = Label(window)
imageLabel.grid(row=2, column=1, sticky=N + S + W + E)

subLabel = Label(window, text="")
subLabel.grid(row=1, column=3, sticky=N + S + W + E)


def showcode():
    imageLabel.config(image=photo)
    subLabel.config(text="QR Code of " + Subject.get())


def save():
    dir = os.getcwd() + "\\QR codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qr.png(os.path.join(dir, name.get() + ".png"), scale=8)
        else:
            messagebox.showinfo("Please Enter a filename")
    except:
        messagebox.showinfo("You need to generate a QR code first")


saveButton = Button(window, text="Save as a PNG", width=20, command=save)
saveButton.grid(row=1, column=3, sticky=N + S + W + E)

# responsive
Rows = 3
columns = 3
for row in range(Rows + 1):
    window.grid_rowconfigure(row, weight=1)
for col in range(columns + 1):
    window.grid_columnconfigure(col, weight=1)

window.mainloop()
