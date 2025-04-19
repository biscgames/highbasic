var apples 4

: Print apple amnt
var applesConcat "I had "
operator applesConcat $apples " apples." +
println $applesConcat

macro getTwoApples
    in macro getTwoApples operator apples 2 +

macro getTwoApples

: Print apple amnt after running macro
var applesConcat "I got two, meaning I had "
operator applesConcat $apples " apples." +
println $applesConcat

macro getTwoApples

: Print apple amnt after running macro twice
var applesConcat "Then I got two more, I now have "
operator applesConcat $apples " apples." +
println $applesConcat