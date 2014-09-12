from tkinter import *
from tkinter import ttk
import socket
import threading

#---Sysvar---#
host='93.58.45.100'
port=80
buff=1024
nick=''
b=None
c=None
started=True
#------------#

class logger():
    def draw(self):
        self.logframe=Tk()
        labelsframe=Frame(self.logframe)
        logname=ttk.Label(labelsframe,text='Nickname')
        self.logname_val=ttk.Entry(labelsframe)
        logbutton=ttk.Button(self.logframe,text='Connect',command=self.log)
        logname.grid(row=0,column=0)
        self.logname_val.grid(row=0,column=1)
        labelsframe.pack()
        logbutton.pack()
        self.logframe.mainloop()

    def log(self):
        global host,port,buff,b,c
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((host,port))
        s=self.logname_val.get()
        self.logframe.destroy()
        c=reader(client)
        c.start()
        b=chat(s,client)
        b.draw()
        

        

class chat():
    def __init__(self,s,client):
        self.conn=s
        self.client=client
    
    def draw(self):
        
        self.chatframe=Tk()
        labelsframe=Frame(self.chatframe)
        chatsend=ttk.Button(labelsframe,text='Send',command=self.send)
        self.chatexit=ttk.Button(labelsframe,text='Exit',command=self.exit)
        self.chatcontents=Text(self.chatframe,width=20,height=10,state=DISABLED)
        self.uptext('Logged as '+self.conn)
        self.chatentry=ttk.Entry(labelsframe)
        self.chatentry.grid(row=0,column=0)
        chatsend.grid(row=0,column=1)
        self.chatexit.grid(row=1,column=1)
        self.chatcontents.pack(side=TOP)
        labelsframe.pack(side=BOTTOM)
        self.chatframe.mainloop()

    def uptext(self,test):
        self.chatcontents.configure(state=NORMAL)
        self.chatcontents.insert(END,test+'\n')
        self.chatcontents.configure(state=DISABLED)

    def send(self):
        self.client.send(bytes(self.conn+': '+self.chatentry.get(),'UTF-8'))
        self.uptext('User: '+self.chatentry.get())

    def exit(self):
        c.stop()
        self.client.send(bytes('exit','UTF-8'))
        self.client.close()
        print('Done')
        self.chatframe.destroy()
        sys.exit()

class reader(threading.Thread):
    def __init__(self,client):
        self.started=True
        threading.Thread.__init__(self)
        print('started')
        self.client=client

    def run(self):
        global b
        while self.started:
            try:
                data=self.client.recv(1024)
                if data:
                    text=data.decode('UTF-8')
                    print(text)
                    b.uptext(text)
            except socket.error:
                self.started=False
                return
        return
    def stop(self):
        self.started=False
        
        
        
        
a=logger()
a.draw()
