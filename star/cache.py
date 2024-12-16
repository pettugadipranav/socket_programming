import socket

# 1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).
#data_dict = {'1': 'computer','2': 'networks', '3': 'osi', '4': 'layers', '5': 'sockets', '6': 'switches', '7': 'routers'}
data_dict = {'Key1':'computer'}
cacheIP = "10.0.1.2"
serverIP = "10.0.1.3"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

dport = 12346

s.bind((cacheIP, dport))
print("socket binded to %s" % (dport))

s.listen(5)
print("socket is listening")

while True:
    
    try:
        c, addr = s.accept()
        print('Got connection from client', addr)
        while True:
            recvmsg = c.recv(1024).decode()
            if recvmsg == "End" or recvmsg == 'error' or recvmsg == 'keyboardInterrupt':
                print('connection is closing for client', addr)
                break

            parts = recvmsg.split()
            # Extract the HTTP method (GET, POST, etc.)
            http_method = parts[0]
            request_url = parts[1]

            if http_method == "GET":
                key = request_url.split("=")[1]
                if key in data_dict:
                    msg = "HTTP/1.1 200 OK\r\n\r\n" + data_dict[key]
                    print("Cache has the key :" + key)
                    c.send(msg.encode())

                else:
                    #If we can`t find key here open socket to server
                    proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    port = 12346
                    proxy.connect((serverIP, port))

                    proxy.send(recvmsg.encode())
                    proxy_recvmsg = proxy.recv(1024).decode()
                    proxy.close()
                    recv_code = proxy_recvmsg.split()[1]
                    recv_value = proxy_recvmsg.split()[3]
                    #After finding in server add it to cache too
                    if recv_code == "200":
                        data_dict[key] = recv_value
                        print("value added :" + key + " :: " + data_dict[key])
                        c.send(proxy_recvmsg.encode())
                    elif recv_code == "404":
                        c.send(proxy_recvmsg.encode())
                    

            elif http_method == "PUT":
                #Create new socket to connect to server and put there
                proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                port = 12346
                proxy.connect((serverIP, port))
                proxy.send(recvmsg.encode())
                #After recieving the response send to client 
                proxy_recvmsg = proxy.recv(1024).decode()
                proxy.close()
                c.send(proxy_recvmsg.encode())
 
            elif http_method == "DELETE":
                #First check in cache if there delete it 
                url_parts = request_url.split('/')
                key = url_parts[2]
                if key in data_dict:
                    del data_dict[key]
                
                #Create new socket to connect to server to delete there too
                proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                port = 12346
                proxy.connect((serverIP, port))
                proxy.send(recvmsg.encode())
                #After recieving the response send to client 
                proxy_recvmsg = proxy.recv(1024).decode()
                proxy.close()
                c.send(proxy_recvmsg.encode())
            
            else:
            	c.send('HTTP/1.1 400 Bad Request\r\n\r\n'.encode())

        c.close()
        
    except socket.error as e:
        print("Error: ", e)
        c.send("socketerror".encode())
        c.close()
    except KeyboardInterrupt:
        print("\nConnection closed")
        break
s.close()