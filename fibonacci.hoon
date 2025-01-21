|=
  n=@ud                                           ::  the input n
^-  @ud                                           ::  output type is @ud
=/  m=@                                           ::  module for calculation
  1.000.000.007
=/  id-matrix=(list (list @ud))                   ::  identity matrix
  ~[[1 0] [0 1]]
=/  fib-matrix=(list (list @ud))                  ::  transformation matrix
  ~[[1 1] [1 0]]
::
::  Power function using matrix multiplication
::
|%
++  mult-matrix                                  ::  matrix multiplication
  |=  [a=(list (list @ud)) b=(list (list @ud))]
  ^-  (list (list @ud))
  %+  turn  a
  |=  row=(list @ud)
  =/  b-transposed=(list (list @ud))
    ?:  =(~ b)  ~
    %-  flop
    %+  turn  i.b
    |=  col=@ud
    (turn b |=(r=(list @ud) (snag col r)))
  %+  turn  b-transposed
  |=  col=(list @ud)
  (reduce |=(x=(list @ud) (mod-add (dot-product x col) m)))
::
++  dot-product                                 ::  dot product of vectors
  |=  [a=(list @ud) b=(list @ud)]
  ^-  @ud
  |-  ^-  @ud
  ?:  |(?=(~ a) ?=(~ b))
    0
  (mod-add (mul i.a i.b) (mod (mul i.a i.b) m) $(a t.a, b t.b))
::
++  mod-add                                     ::  modular addition
  |=  [a=@ud b=@ud]
  ^-  @ud
  (mod (add a b) m)
::
++  power-matrix                                ::  exponentiate matrix
  |=  [m=(list (list @ud)) p=@ud]
  ^-  (list (list @ud))
  ?:  =(p 0)
    id-matrix
  ?:  =(p 1)
    m
  =/  half=(power-matrix m (div p 2))
  =/  half-mult=(mult-matrix half half)
  ?:  =(0 (mod p 2))
    half-mult
  (mult-matrix half-mult m)
--
::  Compute Fibonacci number
(power-matrix fib-matrix n)
