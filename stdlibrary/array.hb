module
var arrLength 0
var variableName "array"
var arrInit 0
macro arrays$createIndex
macro arrays$initalizeArrayLength
macro arrays$initalizeArray
in macro arrays$initalizeArray var _arrCnt 0
in macro arrays$initalizeArray del macro arrays$createIndex r
in macro arrays$initalizeArray in macro arrays$createIndex var nameConcat $variableName
in macro arrays$initalizeArray in macro arrays$createIndex concat nameConcat ":" $_arrCnt
in macro arrays$initalizeArray in macro arrays$createIndex var $nameConcat $arrInit
in macro arrays$initalizeArray in macro arrays$createIndex operator _arrCnt 1 +
in macro arrays$initalizeArray del macro arrays$initalizeArrayLength r
in macro arrays$initalizeArray in macro arrays$initalizeArrayLength var nameConcat $variableName
in macro arrays$initalizeArray in macro arrays$initalizeArrayLength concat nameConcat ":length"
in macro arrays$initalizeArray in macro arrays$initalizeArrayLength var $nameConcat $_arrCnt
in macro arrays$initalizeArray iterate 0 $arrLength arrays$createIndex
