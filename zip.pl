#!/usr/bin/env perl
use strict;
use warnings;

my @files = glob('bmp/*.bmp');
my $cnt = 0;

foreach my $f (@files) {
    `zip -9 $f.zip $f`;

    $cnt++;
    print( ("\b" x 40) . "$cnt / " . scalar(@files) );
}

print "\n";
