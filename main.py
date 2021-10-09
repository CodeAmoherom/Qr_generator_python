from tkinter import *
import os
from tkinter import messagebox

import pyqrcode

window = Tk()
window.title("QR code Generator")

def generator():
    if len(Subject.get())!=0 :
        global qr,photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showinfo('Please enter some Subject')






Subject = StringVar()
SubEntry = Entry(window, textvariable=Subject)
SubEntry.grid(row=0, column=1, sticky=N+S+W+E)