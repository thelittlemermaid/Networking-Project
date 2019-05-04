"""
War Card Game Server by: Ariel Inman & Alex Franklin
Because Suits do not matter in War, we only care about the value of each card
In the client we assign each card a RankValue from 0-12. (2-A).
Here is the list of how the RankValues correspond to each card:
2 - 0
3 - 1
4 - 2 
5 - 3
6 - 4
7 - 5
8 - 6
9 - 7
10 - 8
Jack - 9
Queen - 10
King - 11
Ace - 12
When the values are recieved from the Client, we print what the RankValue is for each card for easy comparison
"""

import socket
import ast

response = 0
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enter IP for current machine
server_socket.bind(('144.96.62.91', 8080))
server_socket.listen(5)
conn, address = server_socket.accept()

try:
    while True:
        # Prints once connection is made and Server recieves first card
        print("Server Listeningngngngng")
        # The values are a list from the array of the two cards that are sent
        values = conn.recv(8192).decode()
        # Converted from a string, back to a list
        convertedValues = ast.literal_eval(values)
        print('Data Recieved:', convertedValues)

        # Assign player card which is first
        playerValue = convertedValues[0]
        # Assign Server's Card which is second
        serverValue = convertedValues[1]

        # Displayed for debugging purposes to make sure that the correct card is sent
        # See above documentatiion for which values correspond to which cards
        print("Player:", playerValue)
        print("Server:", serverValue)

        # Compares the card rank values to determine the winner.
        if playerValue > serverValue:
            response = 1
        elif playerValue < serverValue:
            response = 2
        elif playerValue == serverValue:
            response = 3

        # Response will be sent back to Client to finish appending cards to winner's hand
        print("Response: ", response)
        conn.sendall(str(response).encode())
except SyntaxError:
    print("Game Over")