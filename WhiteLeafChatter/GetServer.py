import tkinter as tk
from tkinter import *

    
def closeWindow(window):
    window.destroy()

def writeIP(entryField, window, confirmButton):
    confirmButton['state'] = DISABLED
    ipfile = open('tempip.txt', 'w')
    ip = entryField.get()
    ipfile.write(ip)
    ipfile.close()
    window.quit()

def getServerWindow():
    ServerWindow = tk.Tk()
    ServerWindow.title('Connect to Server')
    ServerWindow.geometry('450x150')
    ServerWindow.resizable(False, False)
    ServerWindow.option_add('*Font', 'Garamond 17')
    
    serverLabel = tk.Label(ServerWindow, text= 'Server IP')
    serverLabel.place(x= 25, y=25)
    
    ipEntryField = tk.Entry(ServerWindow, width=20)
    ipEntryField.place(x=150,y= 25)
    
    confirmButton = Button(ServerWindow, relief = RAISED, text='Connect', command= lambda: writeIP(ipEntryField, ServerWindow, confirmButton), padx=10)
    confirmButton.place(x=50, y=75)
    
    closeButton = Button(ServerWindow, relief=RAISED, text= 'Close', command=lambda: closeWindow(ServerWindow), padx=20)
    closeButton.place(x=200, y=75)
        
    ServerWindow.mainloop()