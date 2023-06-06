#!/bin/python3
"""
The Lab-93 API Hub offers a singular dissemination point for passing
data from the back end to the front via REST API.
"""


from socket import socket, AF_INET, SOCK_STREAM
from socket import error as SocketError
from json import loads
from time import sleep


class apiHub:
    """
    The API Hub provides a centralized socket server for passing information
    from any python processes running in the background to any front-end service
    requesting said information.  This socket server mediates communication between
    the back end and the front end by acting as a persistent state machine that other
    live clients can refer to when visualizing data on the Lab-93 network.
    """

    def __init__( self, host, port ):

        # Establish an instance of the socket.socket object.
        with socket(AF_INET, SOCK_STREAM) as self.server:

            # Bind the server to our preferred host and port combination.
            self.server.bind( (host, port) )

            # Tell the server to begin listening.
            self.server.listen()

            # Accept all connections and set them aside for future reference.
            self.conn, self.addr = self.server.accept()


            with self.conn:
                while True:

                    # Recieve incoming transmission in chunks of 10-24 bytes.
                    data = self.conn.recv(1024)

                    # Break the loop if the client is done sending.
                    if not data: break

                    # If any information was actually recieved, re-transmit.
                    if len(data) > 0: self.conn.sendall(data)

