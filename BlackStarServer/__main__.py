import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import socket
import threading
from ctypes import windll

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


def handle_client(conn, addr, textbox):
    textbox.config(state='normal')
    textbox.insert('end', f'\n[NEW CONNECTION] {addr} connected.')
    textbox.config(state='disabled')
    textbox.see('end')
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            textbox.config(state='normal')
            textbox.insert('end', f'\n[{addr}] {msg}')
            textbox.config(state='disabled')
            textbox.see('end')
            conn.send("[SERVER] Message Received.".encode(FORMAT))
        else:
            connected= False
    
    threadCount = threading.active_count() -3
    textbox.config(state='normal')
    textbox.insert('end', f'\n[ACTIVE CONNECTIONS] {threadCount}')
    textbox.config(state='disabled')
    textbox.see('end')    
    conn.close()

def startNow(textbox, server):
    server.listen()
    textbox.config(state='normal')
    textbox.insert('end', f"\n[LISTENING] Server is listening on {SERVER}")
    textbox.config(state='disabled')
    textbox.see('end')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, textbox))
        thread.start()
        threadCount = threading.active_count() -2
        textbox.config(state='normal')
        textbox.insert('end', f'\n[ACTIVE CONNECTIONS] {threadCount}')
        textbox.config(state='disabled')
        textbox.see('end')

def StartServer(textbox, serverStartButton, server):
    serverStartButton['state'] = DISABLED
    textbox.config(state='normal')
    textbox.insert('end', '\n[STARTING] Server is starting ...')
    textbox.config(state='disabled')
    textbox.see('end')
    
    threadTkinter = threading.Thread(target=startNow, args=(textbox, server))
    threadTkinter.daemon = True
    threadTkinter.start()

def StopServer(textbox, serverStartButton):
    serverStartButton['state'] = NORMAL
    textbox.config(state='normal')
    textbox.insert('end', '\n[SHUTTING DOWN] Stopping the server ...')
    textbox.config(state='disabled')
    textbox.see('end')

def serverWindow():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    mainWindow = tk.Tk()
    mainWindow.title("Black Star Server")
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

    text = "[PROGRAM MESSAGE] Welcome\n"
    message = f'CURRENT SERVER: {SERVER} NAMED {socket.gethostname()}'
    textbox = Text(mainWindow, width = 50, height= 10, background='#ffffee')
    textbox.place(x=50, y=100)
    textbox.insert('end', text)
    textbox.insert('end', message)
    textbox.config(state='disabled')
    scrollbar.config(command=textbox.yview)

    stopServerButton = Button(mainWindow, relief=RAISED, text= 'Stop Server', font= 'garamond 17', padx=10, background='#ffffbb', command=lambda: StopServer(textbox, startServerButton))
    stopServerButton.place(x= 200, y=500)

    startServerButton = Button(mainWindow, relief=RAISED, text= 'Start Server', font= 'garamond 17', background='#ffffbb', command=lambda: StartServer(textbox, startServerButton, server))
    startServerButton.place(x=50, y=500)

    windll.shcore.SetProcessDpiAwareness(1)
    mainWindow.mainloop()

def main():
    serverWindow()

if __name__ == '__main__':
    main()