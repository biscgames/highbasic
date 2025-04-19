var correct 4
readln "What's 2+2?: " answer

var concat ""
equalInt answer $correct var concat "Correct!"
unlessInt answer $correct var concat "Incorrect!"

println $concat