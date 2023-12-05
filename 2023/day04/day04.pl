#!/usr/bin/env perl

use warnings;
use strict;
use POSIX;

sub extract_winning {
    my ($line)  = @_;
    my @spl     = split /[:,|]/, $line;
    my @winning = $spl[1] =~ /(\d+)/g;
    my @mycards = $spl[2] =~ /(\d+)/g;
    my %winning_hash;
    foreach my $num (@winning) {
        $winning_hash{$num} = 1;
    }
    my @intersection = grep { $winning_hash{$_} } @mycards;
    return @intersection;
}

sub readlines {
    my ($filename) = @_;
    open my $file, '<', $filename or die "Could not open $filename: $!";
    my @lines = map { $_ } <$file>;
    return @lines;
}

sub part1 {
    my (@lines) = @_;
    my $sum = 0;
    foreach my $line (@lines) {
        my @nums = extract_winning($line);
        my $len  = scalar @nums;
        $sum += floor( 2**( $len - 1 ) );
    }
    print $sum;
}

sub part2 {
    my (@lines) = @_;
    my @howmany = (1) x scalar @lines;
    my $sum     = 0;
    foreach my $i ( 0 .. $#lines ) {
        my @nums = extract_winning( $lines[$i] );
        my $len  = scalar @nums;
        foreach ( 0 .. $howmany[$i] - 1 ) {
            foreach my $j ( 0 .. $#nums ) { $howmany[ $i + $j + 1 ] += 1; }
        }
        $sum += $howmany[$i];
    }
    print $sum;
}

my @lines = readlines( $ENV{INPUT} );

part1(@lines);
print "\n";
part2(@lines);
