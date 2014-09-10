import socket
import threading
#---Sysvar---#
host='93.58.45.100'
port=80
buff=1024
nick=''
#------------#

class write(threading.Thread):
    def run(self):
        while 1:
            a=input('>>')
            if a!='':
                client.send(bytes(nick+': '+a,'UTF-8'))
            

class read(threading.Thread):
    def run(self):
        while 1:
            print('\n<<'+client.recv(1024).decode('UTF-8'))
            print('>>\b'),

nick=str(input('Insert nickname>>'))
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
writable=write()
readable=read()
writable.start()
readable.start()


