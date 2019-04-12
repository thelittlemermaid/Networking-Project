import socket
import ast

response = 0
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))

while True:
    print("Server Listeningngngngng")
    server_socket.listen(30)
    conn, address = server_socket.accept()
    values = conn.recv(8192).decode()
    convertedValues = ast.literal_eval(values)
    print('Data Recieved:', convertedValues)

    playerValue = convertedValues[0]
    serverValue = convertedValues[1]

    print("Server:", serverValue)
    print("Player:", playerValue)

    if playerValue > serverValue:
        response = 1
    elif playerValue < serverValue:
        response = 2
    elif playerValue == serverValue:
        response = 3

    print(response)
    conn.send(str(response).encode())