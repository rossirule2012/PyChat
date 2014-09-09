import select
import socket
import sys

#---Sysvar---#
host=''
port=80
pingback=10
buff=1024
#------------#

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(pingback)
input=[server]
output=[]
running=True
i=0

while True:
    inputready,outputready,exceptready=select.select(input,output,[])

    for s in inputready:

        if s==server:
            client,address=server.accept()
            i+=1
            print('Connected clients: ',i)
            input.append(client)
            output.append(client)

        elif s==sys.stdin:
            j=sys.stdin.readline()
            running=False

        else:
            
            try:
                data=s.recv(1024)
                
            except socket.error as e:
                s.close()
                input.remove(s)
                i-=1
                output.remove(s)
            
            if data:
                print(data)
                for a in outputready:

                    if a!=s:
                            try:
                                a.send(data)
                            except socket.error as e:
                                print(e)
                                break
                        
                            
            else:
                s.close()
                input.remove(s)
                i-=1
server.close()
                
            
