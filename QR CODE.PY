import pyqrcode
import tkinter as tk
from tkinter import *

window = Tk()  
window.geometry('400x200')
window.title('QR Code Generator')

Label(window, text='Enter text to generate QR code:', font='Arial 15').pack()
s = tk.StringVar()
entry = Entry(window, textvariable=s, font='Arial 15')
entry.pack()

def create_qrcode():
    text = s.get()
    if text:
        qr = pyqrcode.create(text)
        qr.png('myqr.png', scale=6)
        Label(window, text='QR Code is created and saved successfully', fg='green').pack()
    else:
        Label(window, text='Please enter some text!', fg='red').pack()

Button(window, text='Generate QR Code', bg='pink', command=create_qrcode).pack()
window.mainloop()
