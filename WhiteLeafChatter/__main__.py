import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import socket
from ctypes import windll
import GetServer

HEADER = 16
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'


def connectToServer(textbox):
    
    GetServer.getServerWindow()
    ip_file = open('tempip.txt', 'r')
    server = ip_file.read()
    ip_file.close()
    PORT = 5050
    SERVER = server
    ADDR = (SERVER, PORT)
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    textbox.config(state='normal')
    textbox.insert('end', f'\nYou have connected to {SERVER}')
    textbox.config(state='disabled')
    textbox.see('end')
    
    client.connect(ADDR)
    
def disconnectFromServer(textbox):
    ip_file = open('tempip.txt', 'r')
    server = ip_file.read()
    textbox.config(state='normal')
    textbox.insert('end', f'\nYou have disconnected from {server}')
    textbox.config(state='disabled')
    textbox.see('end')
    
    client.shutdown(2)
    client.close()

def sendMsg(entryField, textbox):
    msg = entryField.get()
    entryField.delete(0, 'end')
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    textbox.config(state='normal')
    textbox.insert('end', f'\nYou: {msg}')
    textbox.insert('end', f'\n{client.recv(2048).decode(FORMAT)}')
    textbox.config(state='disabled')
    textbox.see('end')

def ChatWindow():
    
    mainWindow = tk.Tk()
    mainWindow.title("White Leaf Chatter")
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

    sendButton = Button(mainWindow, relief=RAISED, text= 'Send', pady=0, font= 'garamond 17', padx=10, background='#ffffbb', command=lambda: sendMsg(entryField, textbox))
    sendButton.place(x= 650, y=500)

    connectButton = Button(mainWindow, relief=RAISED, text= 'Connect', font= 'garamond 17', background='#ffffbb', command=lambda: connectToServer(textbox))
    connectButton.place(y=40, x=350)
    
    disconnectButton = Button(mainWindow, relief=RAISED, text='Disconnect', font= 'garamond 17', background='#ffffbb', command= lambda: disconnectFromServer(textbox))
    disconnectButton.place(y=40, x=200)
    
    windll.shcore.SetProcessDpiAwareness(1)
    mainWindow.mainloop()


def main():
    ChatWindow()

if __name__ == '__main__':
    main()