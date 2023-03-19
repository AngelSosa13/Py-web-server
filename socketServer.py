import socket

hostName  = ''         #Host
serverPort = 4040      #Exposed Port

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #Defines the socket
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     #Set the options parameters to the socket
listen_socket.bind((hostName, serverPort))                              #Pass binding the host and the exposed port
listen_socket.listen(1)                                                 #Starts the port
print(f'Serving HTTP on port {serverPort} ...')
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)                         #Socket attempting to receive data in a buffer size of 1024
    print(request_data.decode('utf-8'))

    http_response = b"""\
HTTP/1.1 200 OK

Hello World this is a Socket Server
"""
    client_connection.sendall(http_response)                            #Sending the data
    client_connection.close()                                           #closing connection