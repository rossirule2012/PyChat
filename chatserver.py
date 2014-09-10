import select
import socket
import sys

#---Sysvar---#
host=''
port=80
pingback=10
buff=1024
#------------#
print('Creating server socket')
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Binding server')
server.bind((host,port))
print('Completed,starting chatting protocol')
server.listen(pingback)
input=[server]
output=[]
running=True
print('Protocol started on: ',port,'  '+socket.gethostname())
i=0

while True:
    try:
        inputready,outputready,exceptready=select.select(input,output,[])
    except ValueError as e:
        pass

    for s in inputready:

        if s==server:
            client,address=server.accept()
            i+=1
            print('Connected clients: ',i)
            input.append(client)
            output.append(client)
            
        else:
            
            try:
                data=s.recv(1024)
                
            except socket.error as e:
                pass
            except OsError:
                pass
            
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
                if s in input:
                    input.remove(s)
                    i-=1
server.close()
                
            
