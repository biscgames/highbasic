module
module "stdlibrary/iterate.hb"

num cnt 0

var loopEnd 32
macro loop
    in macro loop operator cnt 2 +
    in macro loop println $cnt
macro startLoop