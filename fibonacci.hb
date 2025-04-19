: Variable Setup
var a 0
var b 1
var iterationCnt 2
var maxCnt 32

: Fibonacci Setup
macro fiboStep
    in macro fiboStep var temp $a
    in macro fiboStep operator temp $b +
    in macro fiboStep var a $b
    in macro fiboStep var b $temp
    in macro fiboStep println $b
    in macro fiboStep operator iterationCnt 1 +
    in macro fiboStep unlessInt iterationCnt $maxCnt macro fiboStep

: Run Fibonacci macro
macro fiboStep