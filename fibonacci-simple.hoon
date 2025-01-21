%.  10
::  A gate to compute Fibonacci numbers
|=  a=@ud  :: Input is an unsigned decimal (natural number)
^-  @ud    :: Output is also an unsigned decimal
=/  f  |=  [b=@ud c=@ud d=@ud]  :: Internal gate to carry out recursion
    ?:  =(c a)
      d
    $(c (add c 1), d (add b d), b d)
(f 0 0 1)  :: Initialize recursion
