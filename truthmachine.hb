: If input is equal to 1, print 1 128 times
var maxCnt 128
var printCnt 0
readln "" num
macro truthMachine
    in macro truthMachine println "1"
    in macro truthMachine operator printCnt 1 +
    in macro truthMachine unlessInt printCnt $maxCnt macro truthMachine
equalInt num 1 macro truthMachine