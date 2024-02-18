# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    # Listen for incoming connections
    serverSocket.listen(1)

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            try:
                # Open the client requested file.
                with open(filename[1:], 'rb') as f:
                    # This variable can store the headers you want to send for any valid request.
                    outputdata = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"

                    # Read the content of the requested file and append it to the response data.
                    outputdata += f.read()

                    # Send the content of the requested file to the client.
                    connectionSocket.sendall(outputdata)

            except FileNotFoundError:
                # If the file is not found, send a 404 Not Found response.
                response = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>"
                connectionSocket.sendall(response)

            # Close the connection socket
            connectionSocket.close()


        except Exception as e:
            # Send response message for invalid request due to the file not being found (404)
            response = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>"
            connectionSocket.sendall(response)

            # Close client socket
            connectionSocket.close()



                


if __name__ == "__main__":
    webServer(13331)
