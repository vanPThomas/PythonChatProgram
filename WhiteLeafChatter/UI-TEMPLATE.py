import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

mainWindow = tk.Tk()
mainWindow.title("Test Window")
mainWindow.geometry('800x600')
mainWindow.option_add('*Font', 'Garamond 23')
mainWindow.resizable(False, False)
image1 = Image.open("wtf_bak.jpg")
testimg = ImageTk.PhotoImage(image1)

scrollbar = Scrollbar(mainWindow)
scrollbar.pack(side=RIGHT, fill= Y)

label1 = tk.Label(image=testimg)
label1.image = testimg
label1.place(x=-2, y=-2)

entryField = tk.Entry(mainWindow, width= 40, background='#ffffee')
entryField.place(x=50, y=500)
text = "[PROGRAM MESSAGE] Welcome\n[PROGRAM MESSAGE] Press the 'Connect' Button to connect to a server"
textbox = Text(mainWindow, width = 50, height= 10, background='#ffffee')
textbox.place(x=50, y=100)
textbox.insert('end', text)
textbox.config(state='disabled')
scrollbar.config(command=textbox.yview)

sendButton = Button(mainWindow, relief=RAISED, text= 'Send', pady=0, font= 'garamond 17', padx=10, background='#ffffbb')
sendButton.place(x= 650, y=500)

connectButton = Button(mainWindow, relief=RAISED, text= 'Connect', font= 'garamond 17', background='#ffffbb')
connectButton.place(y=40, x=350)

mainWindow.mainloop()