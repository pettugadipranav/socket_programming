import socket

# 1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).
data_dict = {'Key1': 'computer','Key2': 'networks', 'Key3': 'routers', 'Key4': 'layers', 'Key5': 'sockets', 'Key6': 'switches'}
#data_dict = {}
serverIP = "10.0.1.2"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

dport = 12346

s.bind((serverIP, dport))
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
                    c.send(msg.encode())
                else:
                    msg = "HTTP/1.1 404 Not Found\r\n\r\nno key"
                    c.send(msg.encode())

            elif http_method == "PUT":
                url_parts = request_url.split('/')
                key = url_parts[2]
                val = url_parts[3]
                data_dict[key] = val
                c.send('HTTP/1.1 200 OK\r\n\r\nInserted successfully'.encode())

            elif http_method == "DELETE":
                url_parts = request_url.split('/')
                key = url_parts[2]
                if key in data_dict:
                    del data_dict[key]
                    c.send('HTTP/1.1 200 OK\r\n\r\nDeleted successfully'.encode())
                else:
                    c.send('HTTP/1.1 404 Not Found\r\n\r\nKey not found'.encode())
            
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