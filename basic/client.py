import socket

serverIP = "10.0.1.2"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 12346

s.connect((serverIP, port))
print("Connection established with server")

while True:
    try:
        req = str(input("Enter request method: "))

        if req == "End":
            print("Closing Program as per input")
            s.send('End'.encode())
            break
        
        if req == "PUT":
            key = str(input("Enter key: "))
            val = str(input("Enter val: "))
            st = req + "  /assignment2/" + key + "/" + val + "  HTTP/1.1\r\n\r\n"

        elif req == "GET":
            key = str(input("Enter key: "))
            st = req + "  /assignment2?request=" + key + "  HTTP/1.1\r\n\r\n"

        elif req == "DELETE":
            key = str(input("Enter key: "))
            st = req + "  /assignment2/" + key + "  HTTP/1.1\r\n\r\n"
        else:
            st = req
            
        print("Request: ", st)
        s.send(st.encode())
        recvmsg=s.recv(1024).decode()
        if(recvmsg=='socketerror'):
            print("socketerror at server")
            break
        print('Client received ' + recvmsg)

    except socket.error as e:
        print("Connection closed: ", e)
        s.send('error'.encode())
        break
    except KeyboardInterrupt:
        print("\nConnection closed")
        s.send('keyboardInterrupt'.encode())
        break

s.close()