module "stdlibrary/arrays.hb"
nick macro arrays$initalizeArray initArr

var arrLength 8
var variableName "fruits"
var arrInit "Fruit"

macro initArr

var indexCnt 0
macro loopForArr
    in macro loopForArr var nameConcat "fruits"
    in macro loopForArr concat nameConcat ":" $indexCnt
    in macro loopForArr var $nameConcat "Apple"
    in macro loopForArr operator indexCnt 1 +
iterate 0 4 loopForArr

var indexCnt 0
del macro loopForArr r
    in macro loopForArr var nameConcat "fruits"
    in macro loopForArr concat nameConcat ":" $indexCnt
    in macro loopForArr println $$nameConcat
    in macro loopForArr operator indexCnt 1 +
iterate 0 8 loopForArr
