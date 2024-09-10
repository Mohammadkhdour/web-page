#  Name: mohammad Khdour - ID:1212517
#  Name: mohammad Ataya - ID: 1211555
#   Name: Hamza Alqam - ID:1211173
from socket import *
import re

#server
#define server port
serverPort = 6060
#define TCP server
serverSocket = socket(AF_INET, SOCK_STREAM)
# make binding with any ip address by ''
serverSocket.bind(('', serverPort))
# listen for requests
serverSocket.listen(1)
# print for the server is ready
print('The server is ready receive')
try:
    # open index.html file
    with open('main_en.html', 'r', encoding='utf-8') as file:
       hfile = file.read()

    # open arabic index.html file
    with open('main_ar.html', 'r', encoding='utf-8') as file0:
       hfile0 = file0.read()

    # open html file for display it
    with open('myForm.html', 'r',  encoding='utf-8') as file1:
       hfile1 = file1.read()

    # open css file for display it
    with open('style.css', 'r', encoding='utf-8') as file2:
       hfile2 = file2.read()

    # open image with png tybe
    with open('img/bzuLogo.png', 'rb') as file3:
       hfile3=file3.read()

    # open image with jpg tybe
    with open('img/bzuphoto.jpg', 'rb') as file4:
       hfile4 = file4.read()

    # open html for error page
    with open('error.html', 'r',   encoding='utf-8') as file5:
       hfile5 = file5.read()

    #open khdour photo
    with open('img/khdour.jpg', 'rb') as file6:
        hfile6 = file6.read()

    #open ataya photo
    with open('img/ataya.jpg', 'rb') as file7:
        hfile7 = file7.read()

    #open alqam photo
    with open('img/alqam.jpg', 'rb') as file8:
        hfile8 = file8.read()

except:pass

while True:

    # accept all requests
    connectionSocket, addr = serverSocket.accept()

    ip = addr[0]
    port = addr[1]
    print('Got connection from', "IP: " + ip + ", Port: " + str(port))

    # receve http reqeust and store it in sentence
    sentence = connectionSocket.recv(4096).decode()
    # we split the request to get the request line from user input
    match = re.split(pattern=" ",string=sentence)
    if len(match) < 2:
        continue
    response = match[1]
    # print http request in termanel
    print(f"*********************************{response}**********************************8")
    print(sentence)


    # for any of this we handle the request depinding on the url
    # for sending our html file
    if(response=="/" or response=="/index.html" or response=="/main_en.html" or response=="/en"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile.encode())

    # for sending arabic page
    elif(response=="/ar" or response=="/main_ar.html"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile0.encode())

    # for sending html file and display it as request
    elif(response=="/myForm.html" or response=="/myForm"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile1.encode())

    elif (response == "/.html"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/txt;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.sendall(hfile.encode())
    # for sending css code
    elif(response=="/.css" or response=="/style.css"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile2.encode())

    # for sending image with png type
    elif(response=="/.png" or response=="/img/bzuLogo.png"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile3)

    # for sending image with jpg type
    elif (response == "/.jpg" or response == "/img/bzuphoto.jpg"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile4)


    elif (response == "/khdour.jpg" or response == "/img/khdour.jpg"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile6)

    elif (response == "/ataya.jpg" or response == "/img/ataya.jpg"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile7)

    elif (response == "/alqam.jpg" or response == "/img/alqam.jpg"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile8)

        # opening stackoverflow website
    elif response == "/so":
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send('Content-Type: text/html; charset=utf-8\r\n'.encode())
        connectionSocket.send("Location:http://www.stackoverflow.com\r\n".encode())
        connectionSocket.send('\r\n'.encode())
        print("stackoverflow.com website successfully connected\r\n")

    # opening ritaj website
    elif response == "/itc":
        connectionSocket.send('HTTP/1.1 307 Temporary Redirect \r\n'.encode())
        connectionSocket.send('Content-Type: text/html; charset=utf-8\r\n'.encode())
        connectionSocket.send("Location:https://itc.birzeit.edu/login/index.php/\r\n".encode())
        connectionSocket.send('\r\n'.encode())
        print("itc.com website successfully connected\r\n")

    else:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile5.encode())
        connectionSocket.send(f'Got connection from, IP: {str(ip)},  Port:{str(port)} \r\n'.encode())




