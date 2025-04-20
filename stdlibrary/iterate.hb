module

var loopCnt 0
var loopEnd 0

macro startLoop
    in macro startLoop macro loop
    in macro startLoop operator loopCnt 1 +
    in macro startLoop unlessInt loopCnt $loopEnd macro startLoop
    in macro startLoop equalInt loopCnt $loopEnd macro onLoopEnd

: EXAMPLE USAGE:
: 
: module stdlibrary/iterate.hb
: var loopEnd 32
: var message "Hello, World!"
: macro loop
:     in macro loop println $message
: macro startLoop