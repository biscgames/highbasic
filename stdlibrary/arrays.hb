module
module "stdlibrary/iterate.hb"

var variableName "array"
var arrayLength 8
var arrayInit 0

macro createArrLengthVariable
    in macro createArrLengthVariable var nameConcat $!emptyline
    in macro createArrLengthVariable concat nameConcat $variableName "Length"
    in macro createArrLengthVariable var $nameConcat $arrayLength
macro createElementIndex
    in macro createElementIndex var nameConcat $!emptyline
    in macro createElementIndex concat nameConcat $variableName "Index" $cnt
    in macro createElementIndex var $nameConcat $arrayInit
    in macro createElementIndex operator cnt 1 +

var loopEnd $arrayLength
macro loop
    in macro loop macro createElementIndex
macro onLoopEnd
    macro createArrLengthVariable

macro initalizeArr
    var cnt 0
    in macro initalizeArr del macro createElementIndex r
        in macro initalizeArr in macro createElementIndex var nameConcat $!emptyline
        in macro initalizeArr in macro createElementIndex concat nameConcat $variableName "Index" $cnt
        in macro initalizeArr in macro createElementIndex var $nameConcat $arrayInit
        in macro initalizeArr in macro createElementIndex operator cnt 1 +
    in macro initalizeArr del macro createArrLengthVariable r
        in macro initalizeArr in macro createArrLengthVariable var nameConcat $!emptyline
        in macro initalizeArr in macro createArrLengthVariable concat nameConcat $variableName "Length"
        in macro initalizeArr in macro createArrLengthVariable var $nameConcat $arrayLength
    var loopEnd $arrayLength
    macro startLoop
    macro createArrLengthVariable