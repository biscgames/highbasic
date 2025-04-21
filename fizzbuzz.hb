num cnt 0
var loopEnd 20
macro loop
    : Initalize
    in macro loop operator cnt 1 +
    in macro loop var fizz $cnt
    in macro loop var buzz $cnt
    in macro loop operator fizz 3 %
    in macro loop operator buzz 5 %

    : Print
    in macro loop equalInt fizz 0 print "Fizz"
    in macro loop equalInt buzz 0 print "Buzz"
    in macro loop unlessInt buzz 0 unlessInt fizz 0 print $cnt
    in macro loop print $!newline
iterate 0 $loopEnd loop
