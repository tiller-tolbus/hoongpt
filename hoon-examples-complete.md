# Hoon Examples Complete Documentation

---
# _index.md

---

+++
title = "Examples"
description = "Additional Hoon challenges and explication"
weight = 100
insert_anchor_links = "right"
+++

Hoon language examples and exercises.

{% grid %}

  {% iconcard
    title="Competitive Programming"
    description="Various exercises."
    href="/language/hoon/examples/competitive"
    small=true
  /%}

  {% iconcard
    title="Gleichniszahlenreihe"
    description="Challenge: the look-and-say sequence."
    href="/language/hoon/examples/gleichniszahlenreihe"
    small=true
  /%}

  {% iconcard
    title="Rhonda Numbers"
    description="Challenge: compute Rhonda Numbers."
    href="/language/hoon/examples/rhonda"
    small=true
  /%}

  {% iconcard
    title="Roman Numerals"
    description="Challenge: printing and parsing roman numerals."
    href="/language/hoon/examples/roman"
    small=true
  /%}

  {% iconcard
    title="Solitaire Cipher"
    description="Challenge: solitaire encryption cipher."
    href="/language/hoon/examples/solitaire"
    small=true
  /%}

  {% iconcard
    title="Water Between Towers"
    description="Challenge: fill convex areas of a tower with water."
    href="/language/hoon/examples/water-towers"
    small=true
  /%}

  {% iconcard
    title="ABC Blocks"
    description="Challenge: spell words with blocks."
    href="/language/hoon/examples/abc-blocks"
    small=true
  /%}

  {% iconcard
    title="Luhn Number"
    description="Challenge: compute Luhn numbers."
    href="/language/hoon/examples/luhn-number"
    small=true
  /%}

  {% iconcard
    title="Emirp"
    description="Challenge: compute primes whose reverses are also primes."
    href="/language/hoon/examples/emirp"
    small=true
  /%}

  {% iconcard
    title="Restore IPs"
    description="Challenge: restore IP addresses that have lost their dots."
    href="/language/hoon/examples/restore-ip"
    small=true
  /%}

  {% iconcard
    title="Islands"
    description="Challenge: find the size of the biggest island in a 2D grid."
    href="/language/hoon/examples/islands"
    small=true
    
  /%}

  {% iconcard
    title="Minimum Path Sum"
    description="Challenge: find the least expensive path through a 2D grid."
    href="/language/hoon/examples/min-path"
    small=true
    
  /%}

    {% iconcard
    title="Phone Letters"
    description="Challenge: return the strings that can be represented by numbers in a phonepad."
    href="/language/hoon/examples/phone-letters"
    small=true
    
  /%}

{% /grid %}



# abc-blocks.md

---

+++
title = "ABC Blocks"
weight = 70
+++

## Challenge: ABC Blocks

You are given a collection of blocks with two letters of the alphabet on each block. A complete alphabet is guaranteed among all sides of the blocks. You would like to check if a given word can be written with the provided set of blocks.

An example set of blocks:
```
 (F E)
 (A W)
 (Q V)
 (B M)
 (X H)
 (N P)
 (I Z)
 (G U)
 (S R)
 (K Y)
 (T L)
 (O C)
 (J D)
 (A N)
 (O B)
 (E R)
 (F S)
 (L Y)
 (P C)
 (Z M)
```

Your task for this challenge is to write a generator `abc-blocks`. It takes a cell of two arguments. The first argument is a `(list (pair @t @t))` which represents the input set of blocks. The second argument is a `@t` which represents the word that you'd like to check.

Your generator should first check if the input blocks cover all letters of the alphabet. If not, the generator should fail (possibly returning an error message). It should also check if the input word only has alphabetical characters (no spaces, numbers, or special characters). Otherwise it should fail. Then, it should check whether the word can be spelled with the blocks, either returning a `%.y` or `%.n`. It should not care about case, for the blocks or for the word.

Example usage:
```
> +abc-blocks [[['a', 'b'] ['c' 'd'] ['e' 'f'] ~] 'fad']
dojo: naked generator failure

> +abc-blocks [[['a', 'b'] ['c' 'd'] ['e' 'f'] ['g' 'h'] ['i' 'j'] ['k' 'l'] ['m' 'n'] ['o' 'p'] ['q' 'r'] ['s' 't'] ['u 'v'] ['w' 'x] ['y' z] ~] '12%-3']
dojo: naked generator failure

> +abc-blocks [[['a', 'B'] ['C' 'd'] ['e' 'F'] ['G' 'h'] ['i' 'J'] ['K' 'l'] ['m' 'N'] ['o' 'P'] ['Q' 'r'] ['s' 'T'] ['U 'v'] ['w' 'X'] ['y' Z'] ~] 'cat']
%.y

> +abc-blocks [[['a', 'B'] ['C' 'd'] ['e' 'F'] ['G' 'h'] ['i' 'J'] ['K' 'l'] ['m' 'N'] ['o' 'P'] ['Q' 'r'] ['s' 'T'] ['U 'v'] ['w' 'X'] ['y' Z'] ~] 'CAT']
%.y

> +abc-blocks [[['a', 'B'] ['C' 'd'] ['e' 'F'] ['G' 'h'] ['i' 'J'] ['K' 'l'] ['m' 'N'] ['o' 'P'] ['Q' 'r'] ['s' 'T'] ['U 'v'] ['w' 'X'] ['y' Z'] ~] 'BAT']
%.n
```

##  Unit Tests

Following a principle of test-driven development, we compose a series of tests which allow us to rigorously check for expected behavior.

```hoon
/+  *test
/=  abc-blocks  /gen/abc-blocks
|%
::  test for failure of incomplete alphabet
::
++  test-01
  =/  blocks  `(list (pair @t @t))`[['a' 'b'] ['c' 'd'] ['e' 'f'] ['g' 'h'] ['i' 'j'] ['k' 'l'] ['m' 'n'] ['o' 'p'] ['q' 'q'] ['s' 't'] ['u' 'v'] ['w' 'x'] ['y' 'z'] ~]
  =/  word  `@t`'foo'
  %-  expect-fail  |.  (abc-blocks blocks word)
++  test-02
  =/  blocks  `(list (pair @t @t))`[['a' 'b'] ['c' 'd'] ['e' 'f'] ['g' 'h'] ['i' 'j'] ['k' 'l'] ['m' 'n'] ['q' 'r'] ['s' 't'] ['u' 'v'] ['w' 'x'] ['y' 'z'] ~]
  =/  word  `@t`'foo'
  %-  expect-fail  |.  (abc-blocks blocks word)
++  test-03
  =/  blocks  `(list (pair @t @t))`[['A' 'B'] ['C' 'D'] ['E' 'F'] ['G' 'H'] ['I' 'J'] ['K' 'L'] ['M' 'N'] ['O' 'P'] ['Q' 'R'] ['S' 'A'] ['U' 'V'] ['W' 'X'] ['Y' 'Z'] ~]
  =/  word  `@t`'foo'
  %-  expect-fail  |.  (abc-blocks blocks word)
++  test-04
  =/  blocks  `(list (pair @t @t))`[['A' 'B'] ['C' 'D'] ['e' 'f'] ['G' 'H'] ['I' 'J'] ['K' 'L'] ['M' 'N'] ['O' 'P'] ['Q' 'R'] ['S' 'A'] ['U' 'V'] ['W' 'X'] ['Y' 'Z'] ['A' 'B'] ['j' 'x']~]
  =/  word  `@t`'foo'
  %-  expect-fail  |.  (abc-blocks blocks word)
++  test-05
  =/  blocks  `(list (pair @t @t))`[['F' 'M'] ['W' 'S'] ['I' 'B'] ['Q' 'K'] ['Z' 'H'] ['G' 'L'] ['U' 'J'] ['V' 'A'] ['C' 'T'] ['R' 'O'] ['P' 'N'] ['E' 'Y'] ~]
  =/  word  `@t`'foo'
  %-  expect-fail  |.  (abc-blocks blocks word)
::  test for failure of input word
::
++  test-06
  =/  blocks  `(list (pair @t @t))`[['F' 'M'] ['W' 'S'] ['I' 'B'] ['D' 'X'] ['Q' 'K'] ['Z' 'H'] ['G' 'L'] ['U' 'J'] ['V' 'A'] ['C' 'T'] ['R' 'O'] ['P' 'N'] ['E' 'Y'] ~]
  =/  word  `@t`'foo bar'
  %-  expect-fail  |.  (abc-blocks blocks word)
++  test-07
  =/  blocks  `(list (pair @t @t))`[['F' 'M'] ['W' 'S'] ['I' 'B'] ['D' 'X'] ['Q' 'K'] ['Z' 'H'] ['G' 'L'] ['U' 'J'] ['V' 'A'] ['C' 'T'] ['R' 'O'] ['P' 'N'] ['E' 'Y'] ~]
  =/  word  `@t`'foo1bar'
  %-  expect-fail  |.  (abc-blocks blocks word)
++  test-08
  =/  blocks  `(list (pair @t @t))`[['F' 'M'] ['W' 'S'] ['I' 'B'] ['D' 'X'] ['Q' 'K'] ['Z' 'H'] ['G' 'L'] ['U' 'J'] ['V' 'A'] ['C' 'T'] ['R' 'O'] ['P' 'N'] ['E' 'Y'] ~]
  =/  word  `@t`'foo!bar'
  %-  expect-fail  |.  (abc-blocks blocks word)
::  test for success with various capitalizations and alphabets
::
++  test-09
  =/  blocks  `(list (pair @t @t))`[['F' 'M'] ['W' 'S'] ['I' 'B'] ['D' 'X'] ['Q' 'K'] ['Z' 'H'] ['G' 'L'] ['U' 'J'] ['V' 'A'] ['C' 'T'] ['R' 'O'] ['P' 'N'] ['E' 'Y'] ~]
  =/  word  `@t`'TRAP'
  %+  expect-eq
    !>  %.y
    !>  (abc-blocks blocks word)
++  test-10
  =/  blocks  `(list (pair @t @t))`[['F' 'M'] ['W' 'S'] ['I' 'B'] ['D' 'X'] ['Q' 'K'] ['Z' 'H'] ['G' 'L'] ['U' 'J'] ['V' 'A'] ['C' 'T'] ['R' 'O'] ['P' 'N'] ['E' 'Y'] ~]
  =/  word  `@t`'trap'
  %+  expect-eq
    !>  %.y
    !>  (abc-blocks blocks word)
++  test-11
  =/  blocks  `(list (pair @t @t))`[['F' 'M'] ['W' 'S'] ['I' 'B'] ['D' 'X'] ['Q' 'K'] ['Z' 'H'] ['G' 'L'] ['U' 'J'] ['V' 'A'] ['C' 'T'] ['R' 'O'] ['P' 'N'] ['E' 'Y'] ~]
  =/  word  `@t`'tRaP'
  %+  expect-eq
    !>  %.y
    !>  (abc-blocks blocks word)
++  test-12
  =/  blocks  `(list (pair @t @t))`[['f' 'm'] ['w' 's'] ['i' 'b'] ['d' 'x'] ['q' 'k'] ['z' 'h'] ['g' 'l'] ['u' 'j'] ['v' 'a'] ['c' 't'] ['r' 'o'] ['p' 'n'] ['e' 'y'] ~]
  =/  word  `@t`'TRAP'
  %+  expect-eq
    !>  %.y
    !>  (abc-blocks blocks word)
++  test-13
  =/  blocks  `(list (pair @t @t))`[['f' 'm'] ['w' 's'] ['i' 'b'] ['d' 'x'] ['q' 'k'] ['z' 'h'] ['g' 'l'] ['u' 'j'] ['v' 'A'] ['c' 't'] ['R' 'o'] ['p' 'n'] ['e' 'y'] ~]
  =/  word  `@t`'trap'
  %+  expect-eq
    !>  %.y
    !>  (abc-blocks blocks word)
++  test-14
  =/  blocks  `(list (pair @t @t))`[['f' 'm'] ['w' 's'] ['i' 'b'] ['d' 'x'] ['q' 'k'] ['z' 'h'] ['g' 'l'] ['u' 'j'] ['v' 'A'] ['c' 't'] ['R' 'o'] ['p' 'n'] ['e' 'y'] ['x' 'y'] ['a' 'b'] ~]
  =/  word  `@t`'fsixqhgjvtrnyyb'
  %+  expect-eq
    !>  %.y
    !>  (abc-blocks blocks word)
::  test for being unable to make a word
::
++  test-15
  =/  blocks  `(list (pair @t @t))`[['f' 'm'] ['w' 's'] ['i' 'b'] ['d' 'x'] ['q' 'k'] ['z' 'h'] ['g' 'l'] ['u' 'j'] ['v' 'A'] ['c' 't'] ['R' 'o'] ['p' 'n'] ['e' 'y'] ['x' 'y'] ['a' 'b'] ~]
  =/  word  `@t`'fsixqhgjvtrnyyyb'
  %+  expect-eq
    !>  %.n
    !>  (abc-blocks blocks word)
++  test-16
  =/  blocks  `(list (pair @t @t))`[['f' 'm'] ['w' 's'] ['i' 'b'] ['d' 'x'] ['q' 'k'] ['z' 'h'] ['g' 'l'] ['u' 'j'] ['v' 'A'] ['c' 't'] ['R' 'o'] ['p' 'n'] ['e' 'y'] ['x' 'y'] ['a' 'b'] ~]
  =/  word  `@t`'fsixqhgujvtrnyyb'
  %+  expect-eq
    !>  %.n
    !>  (abc-blocks blocks word)
++  test-17
  =/  blocks  `(list (pair @t @t))`[['f' 'm'] ['w' 's'] ['i' 'b'] ['d' 'x'] ['q' 'k'] ['z' 'h'] ['g' 'l'] ['u' 'j'] ['v' 'A'] ['c' 't'] ['R' 'o'] ['p' 'n'] ['e' 'y'] ['x' 'y'] ['a' 'b'] ~]
  =/  word  `@t`'AAA'
  %+  expect-eq
    !>  %.n
    !>  (abc-blocks blocks word)
++  test-18
  =/  blocks  `(list (pair @t @t))`[['A' 'B'] ['C' 'D'] ['E' 'F'] ['G' 'H'] ['I' 'J'] ['K' 'L'] ['M' 'N'] ['O' 'P'] ['Q' 'R'] ['S' 'T'] ['U' 'V'] ['W' 'X'] ['Y' 'Z'] ~]
  =/  word  `@t`'AGENTT'
  %+  expect-eq
    !>  %.n
    !>  (abc-blocks blocks word)
++  test-19
  =/  blocks  `(list (pair @t @t))`[['A' 'B'] ['C' 'D'] ['E' 'F'] ['G' 'H'] ['I' 'J'] ['K' 'L'] ['M' 'N'] ['O' 'P'] ['Q' 'R'] ['S' 'T'] ['U' 'V'] ['W' 'X'] ['Y' 'Z'] ['S' 'T'] ~]
  =/  word  `@t`'AGENTtT'
  %+  expect-eq
    !>  %.n
    !>  (abc-blocks blocks word)
++  test-20
  =/  blocks  `(list (pair @t @t))`[['A' 'Z'] ['A' 'Z'] ['F' 'M'] ['W' 'S'] ['I' 'B'] ['D' 'X'] ['Q' 'K'] ['Z' 'H'] ['G' 'L'] ['U' 'J'] ['V' 'A'] ['C' 'T'] ['R' 'O'] ['P' 'N'] ['E' 'Y'] ~]
  =/  word  `@t`'ZAZAZ'
  %+  expect-eq
    !>  %.n
    !>  (abc-blocks blocks word)
--
```

##  Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2023.6.  They are made available under the MIT License and CC0.  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_By ~dozreg-toplud.  In the process, he found and fixed a bug in the implementation of `++curr`._

```hoon
::  +abc-blocks: a solution to the HSL challenge #2
::
::    https://github.com/tamlut-modnys/template-hsl-abc-blocks
::    Takes a cell of arguments [blocks=(list (pair @t @t)) word=@t],
::    produces a flag.
::    Crashes if the alphabet is not represented in the blocks, or if there are
::    non-alphabetical characters in the blocks or in the word.
::    Produces %.y if the word can be written with the given list of blocks,
::    %.n otherwise
::
::    Solving this challenge revealed a bug in ++curr implementation! Refer to
::    the bottom of the file.
::
|^
::  Main part:
::
|=  [blocks=(list (pair @t @t)) word=@t]
^-  ?
=/  word-tape=tape  (trip word)
::  Convert input values to lowercase
::
=.  word-tape  (cass word-tape)
=.  blocks
  %+  turn
    blocks
  |=  [a=@t b=@t]
  ^-  (pair @t @t)
  :-  (crip (cass (trip a)))
  (crip (cass (trip b)))
::  Define alphabet
::
=/  alphabet=(set @t)  (silt "abcdefghijklmnopqrstuvwxyz")
::  Assert: only alphabetical characters in the blocks
::
?.  %+  levy
      blocks
    |=  [a=@t b=@t]
    ^-  ?
    &((~(has in alphabet) a) (~(has in alphabet) b))
  ~_  leaf+"non-alphabetical character in blocks"
  !!
::  Assert: only alphabetical characters in the word
::
?.  %+  levy
      word-tape
    |=  =cord
    ^-  ?
    (~(has in alphabet) cord)
  ~_  leaf+"non-alphabetical character in word"
  !!
::  Assert: complete alphabet among the blocks
::
?.  ::  Iterate for block list indices i:
    ::
    =+  i=0
    |-  ^-  ?
    ::  if the alphabet set is empty, then the blocks contain all the letters
    ::
    ?:  =(~ alphabet)
      %.y
    ::  else, if we reached the end of the block list, then the opposite is true
    ::
    ?:  =(i (lent blocks))
      %.n
    ::  else, delete letters on a block from the alphabet and continue
    ::
    =+  [a b]=(snag i blocks)
    $(i +(i), alphabet (~(del in (~(del in alphabet) b)) a))
  ~_  leaf+"not complete alphabet in blocks"
  !!
::  check if we can compose the word with the blocks
::
(check blocks word-tape)
::
::  Helping functions
::  ++check: checks if the word can be composed with the given blocks
::
++  check
  |=  [blocks=(list (pair @t @t)) word=tape]
  ^-  ?
  ::  Self-reference
  ::
  =*  this-gate  ..$
  ::  The word can be composed if it's empty, ...
  ::
  ?~  word  %.y
  ::  ... or if the list of indices of blocks that contain i.word is not empty
  ::  and t.word can be composed with at least one list of the blocks made by
  ::  removing one of the blocks that contain i.word.
  ::
  ::  Logical OR on a list (%.n if the list is empty)
  ::
  %+  lien
    ::  (list of lists of blocks made by removing one block that contains
    ::  i.word for each such block)
    ::
    %+  turn
      ::  (list of block indices that contain i.word)
      ::
      (find-in-blocks i.word blocks)
    ::  (gate that removes a block from a list of blocks by an index)
    ::
    (curr (curr oust blocks) 1)
  ::  (gate that applies ++check to a given list of blocks and t.word)
  ::
  (curr this-gate t.word)
::  ++  find-in-blocks: returns a list of block indices that contain
::  a given letter
::
++  find-in-blocks
  |=  [letter=@t blocks=(list (pair @t @t))]
  ^-  (list @)
  =+  i=0
  =|  =(list @)
  ::  Iterate over elements of blocks
  ::
  |-
  ?~  blocks
    list
  ::  If a block contains the letter, append its index to the list
  ::
  =?  list  |(=(letter -:i.blocks) =(letter +:i.blocks))  (snoc list i)
  $(i +(i), blocks t.blocks)
::  ++curr: rewrite ++curr from stdlib because the original has a bug
::  (https://github.com/urbit/urbit/issues/6655)
::
++  curr
  |*  [a=$-(^ *) c=*]
  |*  b=_,.+<-.a
  (a b c)
::
--
```

### Solution #2

_By ~bantus-follus_

```hoon
|=  [blocks=(list (pair @t @t)) word=@t]
=<
=/  alphacheck  (alphabet-check merged-blocks)
?.  (character-check word)
    ~|  "Input word contains invalid characters."  !!
=/  spellcheck  (spell-check word)
spellcheck
|%
++  alphabet  "abcdefghijklmnopqrstuvwxyz"
::
::  merges all blocks into a single tape
++  merged-blocks  (merge blocks)
::
::  turns all blocks into individual tapes
++  tape-blocks    (turn (turn (turn (turn blocks pair-to-list) crip) trip) cass)
++  merge
    |=  blocks=(list (pair @t @t))
    ^-  tape
        (cass (trip (crip `(list @t)`(zing (turn blocks pair-to-list)))))
::
::  converts each pair to a (list @t)
++  pair-to-list
            |=  input=(pair @t @t)
            ^-  (list @t)
                [-:input +:input ~]
::
::  checks if input blocks cover all letters of the alphabet
++  alphabet-check
    |=  input=tape
    ^-  ?
        =/  i  0
        |-
        ?:  =(i 26)
            %.y
        ?~  (find [(snag i alphabet)]~ input)
            ~|  "Full alphabet not found. {<(snag i alphabet)>} not in blocks"  !!
        $(i +(i))
::
::  checks if input word has valid chaaracters. %.y means all characters are valid
++  character-check
    |=  word=@t
    ^-  ?
        =/  i  0
        =/  tapeword  (cass (trip word))
        |-
        ?:  =(+(i) (lent tapeword))
            %.y
        ?~  (find [(snag i tapeword)]~ alphabet)
            %.n
        $(i +(i))
::
::  checks if the word can be spelled using the input blocks
++  spell-check
    |=  word=@t
    ^-  ?
        =/  tapeword     (cass (trip word))
        =/  tape-blocks  tape-blocks
        =/  i  0
        =/  letter  (snag i tapeword)
        |-
        ?:  =(+(i) (lent tapeword))
            =/  blockcheck  (check-blocks [tape-blocks letter])
                ?.  check:blockcheck
                    %.n
            %.y
        =/  blockcheck  (check-blocks [tape-blocks letter])
        ?.  check:blockcheck
            %.n
        $(i +(i), letter (snag +(i) tapeword), tape-blocks (oust [num:blockcheck 1] tape-blocks))
::  cycles through blocks, checking for a letter
++  check-blocks
    |=  [tape-blocks=(list tape) letter=@t]
    ^-  [num=@ check=?]
        =/  i  0
        =/  block  (snag i tape-blocks)
        |-
        ?:  =(+(i) (lent tape-blocks))
            ?~  (find [letter]~ block)
                [~ %.n]
            [i %.y]
        ?~  (find [letter]~ block)
            $(i +(i), block (snag +(i) tape-blocks))
        [i %.y]
    --
```

### Solution #3
_By ~dannul-bortux_

```hoon
!:
|=  [inlist=(list [@t @t]) inword=@t]
^-  $?(%.y %.n)
::  If, input list is empty
::
?:  =(0 (lent inlist))
  ::  Then, throw error
  ::
  ~|  'Error - input list cannot be empty'
  !!
=<  (validate-input inlist (cass (trip inword)))
|%
++  validate-input
  |=  [blocks=(list [@t @t]) cword=tape]
  =/  lblocks  (to-lowercase blocks)
  ?:  ?&  (validate-alpha-only cword)
          (validate-complete-alpha lblocks)
          (validate-word lblocks cword)
        ==
    %.y
  %.n
++  validate-alpha-only
  |=  w=tape
  =/  i  0
  :: =/  tword  (trip w)
  |-
  ?:  =(i (lent w))
    %.y
  ?.  ?&  (gte `@ud`(snag i w) 97)
          (lte `@ud`(snag i w) 122)
      ==
    !!
  %=  $
    i  +(i)
  ==
++  validate-complete-alpha
  |=  blocks=(list [@t @t])
  =/  alphabet  "abcdefghijklmnopqrstuvwxyz"
  =/  bltape  (block-taper blocks)
  :: ~&  "bl tape is {<bltape>}"
  :: =/  bltape  "abcdefghijklmnopqrstuvwxyz"
  =/  i  0
  |-
  ?:  =(i (lent alphabet))
  :: ~&  "returning yes"
    %.y
  ?:  =(~ (find (trip (snag i alphabet)) bltape))
      :: ~&  "returning no at letter: {<(snag i alphabet)>}"
    !!
  %=  $
    :: alphabet  (remove-letters alphabet (snag i blocks))
    i  +(i)
  ==
  :: %.n
  :: ++  remove-letters
  ::   |=  [in=tape let=[@t @t]]
  ::   ~&  "removing letters"

  ::   in
++  block-taper
    |=  b=(list [@t @t])
    =/  i  0
    =/  bltape  *tape
    |-
    ?:  =(i (lent b))
      bltape
    :: ~&  +2:(snag i `(list [@t @t])`b)
    %=  $
      bltape  (snoc (snoc bltape +2:(snag i `(list [@t @t])`b)) +3:(snag i `(list [@t @t])`b))
      :: bltape  (snoc bltape 'a')
      i  +(i)
    ==
++  validate-word
    |=  [blocks=(list [@t @t]) cword=tape]
    =/  wordcombos  `(list tape)`(get-combos blocks)
    :: ~&  "validating word"
    :: ~&  wordcombos
    =/  i  0
    |-
    ?:  =(i (lent wordcombos))
      %.n
      :: ~&  (snag i wordcombos)
    ?:  (word-compare (snag i wordcombos) cword)
      %.y
      %=  $
        i  +(i)
      ==
  :: ?:  ?&  (validate-alph-aonly )
  ::         (validate-complete-alpha )
  ::         (validate-word )
  ::       ==
    :: %.y
  :: %.n
++  get-combos
|=  n=(list [@t @t])
=/  i  1
=/  outlist  `(list tape)`(snoc `(list tape)`(snoc *(list tape) (trip +2:(snag 0 `(list [@t @t])`n))) (trip +3:(snag 0 `(list [@t @t])`n)))
:: ~&  outlist
|-
?:  =(i (lent n))
  outlist
:: ?:  =(i  0)
:: %=  $
::   outlist  (snoc `(list tape)`(snoc `(list tape)`outlist (trip +2:(snag 0 `(list [@t @t])`n))) (trip +3:(snag 0 `(list [@t @t])`n)))
::   i  +(i)
:: ==
=/  j  0
=/  temp  *(list tape)
|-
?:  =(j (lent outlist))
  %=  ^$
    outlist  temp
    i  +(i)    
  ==
%=  $
  :: temp  (snoc (snoc `(list tape)`outlist (trip +2:(snag 0 `(list [@t @t])`n))) (trip +3:(snag 0 `(list [@t @t])`n)))
  temp  (snoc `(list tape)`(snoc `(list tape)`temp (snoc (snag j outlist) +2:(snag i `(list [@t @t])`n))) (snoc (snag j outlist) +3:(snag i `(list [@t @t])`n)))
  j  +(j)
==
:: %=  $
::   i  +(i)
::   j  3
:: ==
++  word-compare
|=  [combo=tape cword=tape]
=/  i  0
:: ~&  combo
:: ~&  cword
|-
:: ~&  combo
?:  =(i (lent cword))
  %.y
?:  =(~ (find (trip (snag i cword)) combo))
  %.n
%=  $
  combo  (oust [+3:(find (trip (snag i cword)) combo) 1] combo)
  i  +(i)
==
++  to-lowercase
    |=  blocks=(list [@t @t])
    =/  lcase  *(list [@t @t])
    =/  i  0
    |-
    ?:  =(i (lent blocks))
      :: lcase
      :: ~&  lcase
      lcase
    =/  m  (crip (cass (trip +2:(snag i blocks))))
    =/  n  (crip (cass (trip +3:(snag i blocks))))
    %=  $
      lcase  (snoc `(list [@t @t])`lcase [m n])
      :: lcase  (snoc `(list [@t @t])`lcase ['a' 'b'])
      i  +(i)
    ==
    :: blocks
  :: %.n
--
```


# competitive.md

---

+++
title = "Competitive Programming"
weight = 10
+++

Let's take a quick look at implementations for some common tasks in Hoon.  I assume that you want to use library tools whenever possible, but you can delve into the source code itself if you want to know more.

## Sorting

- Given a `list` of values, sort the values according to a given rule and produce a `list`.

The standard `++sort` gate implements a quicksort.  You need to provide a comparison function as a gate as well.

```hoon
> =/  my-list  `(list @ud)`~[10 9 8 1 2 3 7 6 4 5]
  (sort my-list gth)
~[10 9 8 7 6 5 4 3 2 1]

> =/  my-list  `(list @ud)`~[10 9 8 1 2 3 7 6 4 5]
  (sort my-list lth)
~[1 2 3 4 5 6 7 8 9 10]
```

If you are sorting something more complicated than atoms, you'll need a comparison gate that handles pairwise values and returns truthness.

E.g. given a data structure like `[@ud @tas]`, a cell which we wish to sort on the tail, we could sort like this:

```hoon
> =/  my-list  `(list [@ud @tas])`~[[1 %a] [2 %c] [3 %b] [4 %d]]
  (sort my-list |=([a=[@ud @tas] b=[@ud @tas]] (lth +.a +.b)))
~[[1 %a] [3 %b] [2 %c] [4 %d]]
```

- Given a `set` of values, sort the values according to a given rule and produce a `list`.

If something isn't a `list`, the easiest way to sort it is to convert it to a `list` first and then sort that.

```hoon
> =/  my-set  (silt ~[1 10 10 1 2 3 3 2 4 9 8 5 7 6 8 9])
  =/  my-list  ~(tap in my-set)
  (sort my-list lth)
~[1 2 3 4 5 6 7 8 9 10]
```

## Bitwise Operations

Bitwise operations are necessary when you are closely packing data into binary formats or otherwise dealing with binary data.  Basically there are three scenarios:

1. Using packed binary data, e.g. bit packing or [NaN-boxing](https://anniecherkaev.com/the-secret-life-of-nan).  Urbit supports bitwise operations on arbitrarily-sized atoms.
2. Working with MIME-type data.  Urbit has standard library support for yielding and parsing these, but it's sometimes a bit confusing where they may be located.
3. Directly processing particular kinds of data streams, like audio or video data.  On Urbit, you'll be serving these or interfacing with an external service.  (Remember, Urbit is more like a server than a GPU.)

### Binary Operations

If you are working with packed binary data, you'll typically print the atom data with a `@ux` unsigned hexadecimal aura.

We'll use `'Wild Hearts Can\'t Be Broken'` as our source atom.  As `@ux` the ASCII components are clearly visible.

```hoon
> `@ux`'Wild Hearts Can\'t Be Broken'  
0x6e.656b.6f72.4220.6542.2074.276e.6143.2073.7472.6165.4820.646c.6957  
```

Here are a few ways to slice and dice binary atom data.

[`++rip`](https://urbit.org/docs/hoon/reference/stdlib/2c#rip) disassembles an atom `b` into `2^a`-sized chunks as a `list`.

```hoon
> =/  text  'Wild Hearts Can\'t Be Broken'  
 (rip 3 text)  
~[87 105 108 100 32 72 101 97 114 116 115 32 67 97 110 39 116 32 66 101 32 66 114 111 107 101 110]  

> =/  text  'Wild Hearts Can\'t Be Broken'  
 `(list @ux)`(rip 3 text)  
~[0x57 0x69 0x6c 0x64 0x20 0x48 0x65 0x61 0x72 0x74 0x73 0x20 0x43 0x61 0x6e 0x27 0x74 0x20 0x42 0x65 0x20 0x42 0x72 0x6f 0x6b 0x65 0x6e]

> =/  text  'Wild Hearts Can\'t Be Broken'  
 `(list @ux)`(rip 6 text)  
~[0x6165.4820.646c.6957 0x276e.6143.2073.7472 0x6f72.4220.6542.2074 0x6e.656b]
```

[`++rap`](https://urbit.org/docs/hoon/reference/stdlib/2c#rap) is the opposite operation, producing an atom from a list of atoms `b` with a block size `2^a`.

```hoon
> `(list @ux)`(rip 3 'Mars')
~[0x4d 0x61 0x72 0x73]

> `@t`(rap 3 ~[0x4d 0x61 0x72 0x73])
'Mars'

> `@ux`(rap 3 ~[0x4d 0x61 0x72 0x73])
0x7372.614d

> `@ux`(rap 6 ~[0x4d 0x61 0x72 0x73])
0x73.0000.0000.0000.0072.0000.0000.0000.0061.0000.0000.0000.004d
```

[`++cut`](https://urbit.org/docs/hoon/reference/stdlib/2c#cut) slices `2^a`-sized chunks from `b` to `c` out of atom `d`.

```hoon
> =/  text  'Wild Hearts Can\'t Be Broken'
 `@ux`(cut 3 [0 4] text)
0x646c.6957

> =/  text  'Wild Hearts Can\'t Be Broken'
 `@t`(cut 3 [0 4] text)
'Wild'
```

(There are many more of these types of operations available as well.)

Standard bitwise logical operations are available:

- `OR` is [`++con`](https://urbit.org/docs/hoon/reference/stdlib/2d#con) (conjoint):

    ```hoon
    > `@ub`(con 0b10.0001.0110 0b11.1101.1011)
    0b11.1101.1111
    ```

- `AND` is [`++dis`](https://urbit.org/docs/hoon/reference/stdlib/2d#dis) (disjoint):

    ```hoon
    > `@ub`(dis 0b10.0001.0110 0b11.1101.1011)
    0b10.0001.0010
    ```

- `XOR` is [`++mix`](https://urbit.org/docs/hoon/reference/stdlib/2d#mix):

    ```hoon
    > `@ub`534
    0b10.0001.0110

    > `@ub`987
    0b11.1101.1011

    > `@ub`(mix 534 987)
    0b1.1100.1101
    ```

- `NOT` is [`++not`](https://urbit.org/docs/hoon/reference/stdlib/2d#not); it requires a block size (powers of 2) because leading zeroes are always stripped in Hoon (and thus `NOT` is implicitly based on block size):

    ```hoon
    > `@ub`(not 2 1 0b1011)
    0b100

    > `@ub`(not 3 1 0b1011)
    0b1111.0100
    
    > `@ub`(not 4 1 0b1011)
    0b1111.1111.1111.0100
    ```

### MIME Data Operations

[MIME data types](https://en.wikipedia.org/wiki/MIME) allow HTTP communications to include rich content.  The `++html` core in the standard library provides quite a few operations for encoding and decoding MIME-typed values.

Data transmitted as bytes ([“octets”](https://en.wikipedia.org/wiki/Octet_%28computing%29)) are decoded using `++as-octs:mimes:html`.  This is transparent for ASCII text data:

```hoon
> (as-octs:mimes:html '<html><body>')
[p=12 q=19.334.824.924.412.244.887.090.784.316]

> `[@ @ux]`(as-octs:mimes:html '<html><body>')
[12 0x3e79.646f.623c.3e6c.6d74.683c]

> `[@ @t]`(as-octs:mimes:html '<html><body>')
[12 '<html><body>']
```

Perhaps surprisingly, many text conversion operations live here.  To parse a hexadecimal value as a string, for instance, use `++de:base16:mimes:html`:

```hoon
> (de:base16:mimes:html 'deadbeef')
[~ [p=4 q=3.735.928.559]]

> `(unit [@ @ux])`(de:base16:mimes:html 'deadbeef')
[~ [4 0xdead.beef]]
```

There are operations for JSON, [Base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), and XML/HTML as well.

- [JSON](/language/hoon/guides/json-guide)
- [Sail (HTML)](/language/hoon/guides/sail)

Urbit furthermore has a notion of _jammed noun_, which is essentially a serialization (marshaling, pickling) of a noun into an atom.

## Primes and Factors

To calculate a prime number, the tried-and-true method is the Sieve of Eratosthenes, which is an elimination algorithm.  In other words, we need to be able to calculate factors of a given positive integer.  We're actually going to do an even simpler (and less efficient) method here, and leave the Sieve as an exercise to the reader.

This gate accepts a number and divides it by every number from half the number down to 2.  If the remainder after division is zero, then it is a factor and we add it to the front of the list of factors.

```hoon
|%
++  factors
  |=  n=@ud  ^-  (list @ud)
  =/  ctr  (div n 2)
  =/  fxr  *(list @ud)
  |-  ^-  (list @ud)
  ?:  =(1 ctr)  fxr
  ?:  =(0 +:(dvr n ctr))
    $(ctr (sub ctr 1), fxr [ctr fxr])
  $(ctr (sub ctr 1))
--
```

Now that we can find factors, it should be straightforward to find primes.  In this case, we simply check each value up to `n` and see if it has any factors (other than itself and 1, of course).

```hoon
|%
++  factors
  |=  n=@ud  ^-  (list @ud)
  =/  ctr  (div n 2)
  =/  fxr  *(list @ud)
  |-  ^-  (list @ud)
  ?:  =(1 ctr)  fxr
  ?:  =(0 (mod n ctr))
    $(ctr (sub ctr 1), fxr [ctr fxr])
  $(ctr (sub ctr 1))
++  primes
  |=  n=@ud  ^-  (list @ud)
  =/  ctr  n
  =/  prm  *(list @ud)
  |-  ^-  (list @ud)
  ?:  =(1 ctr)  prm
  ?:  =(~ (factors ctr))
    $(ctr (sub ctr 1), prm [ctr prm])
  $(ctr (sub ctr 1))
--
```

- How would you change this algorithm to the more efficient Sieve of Eratosthenes?

## Pragmatic Input/Output

While Hoon has a sophisticated text parsing library, the primitives are rather low-level and we won't assume that you want to directly implement a parser using them in a rapid-fire competitive environment.

- [Text Processing III](/courses/hoon-school/Q2-parsing) - This module will cover text parsing.
- [Parsing Text](/language/hoon/guides/parsing)

Fortunately, there is a regular expression library you can incorporate into your program which will allow you to match and work with code.

- https://github.com/lynko/re.hoon

## Functional Operators

Hoon is a functional programming language, so naturally it supports the basic collective operations which functional programming languages expect.

### Curry

[_Currying_](https://en.wikipedia.org/wiki/Currying) describes taking a function of multiple arguments and reducing it to a set of functions that each take only one argument. _Binding_, an allied process, is used to set the value of some of those arguments permanently.  Hoon has a left-bind `++cury` and a right-bind `++curr`.

```hoon
> =full |=([x=@ud a=@ud b=@ud c=@ud] (add (add (mul (mul x x) a) (mul x b)) c))

> (full 5 4 3 2)
117

> =one (curr full [4 3 2])

> (one 5)  
117
```

### Map

The Map operation describes applying a function to each item of a set or iterable object, resulting in the same final number of items transformed. In Hoon terms, we would say slamming a gate on each member of a `list` or `set`. The standard library arms that accomplish this include [`++turn`](/language/hoon/reference/stdlib/2b#turn) for a `list`, [`++run:in`](/language/hoon/reference/stdlib/2h#repin) for a `set`, and [`++run:by`](/language/hoon/reference/stdlib/2i#runby) for a `map`.

```hoon
> (turn `(list @ud)`~[1 2 3 4 5] one)
```

### Reduce

The Reduce operation applies a function as a sequence of pairwise operations to each item, resulting in one summary value. The standard library arms that accomplish this are [`++roll`](/language/hoon/reference/stdlib/2b#roll) and [`++reel`](/language/hoon/reference/stdlib/2b#reel) for a `list`, [`++rep:in`](/language/hoon/reference/stdlib/2h#repin) for a `set`, and [`++rep:by`](/language/hoon/reference/stdlib/2i#repby) for a `map`.

```hoon
> =my-set (silt `(list @ud)`~[1 2 3 4 5])

> (~(rep in my-set) mul)
b=120
```

### Filter

The Filter operation applies a true/false function to each member of a collection, resulting in some number of items equal to or fewer than the size of the original set. In Hoon, the library arms that carry this out include [`++skim`](/language/hoon/reference/stdlib/2b#skim), [`++skid`](/language/hoon/reference/stdlib/2b#skid), [`++murn`](/language/hoon/reference/stdlib/2b#murn) for a `list`, and [`++rib:by`](/language/hoon/reference/stdlib/2i#ribby) for a `map`.

```hoon
> `(list @ud)`(skim `(list @ud)`~[1 2 3 4 5] (curr gth 2))
~[3 4 5]
```

An interesting feature of Hoon is that it really prefers functions-that-produce-functions, which feels very functional once you get used to the idiom.  Here you can see that done with `++curr`.

- [Functional Programming](/courses/hoon-school/Q-func) - This module will discuss some gates-that-work-on-gates and other assorted operators that are commonly recognized as functional programming tools.

## Floating-Point Operations

`@ud` unsigned decimal operations are, of course, postive-integer-only.  For floating-point maths, you will need to work with `@rs` for 32-bit single-precision IEEE 754 floating-point atoms.  These are prefixed with a single `.` which is _not_ a decimal point.

```hoon
> .100
.100

> .1e2
.100

> .1e-4
.1e-4

> .0.0001
.1e-4
```

Equivalent mathematical operations for `@rs` values are available in the `++rs` door:

```hoon
> (add:rs .1 .2)
.3

> (mul:rs .5 .0.6)
.0.3

> (div:rs .10 .3)
.3.3333333
```

- [Mathematics](/courses/hoon-school/S-math) - This module introduces how non-`@ud` mathematics are instrumented in Hoon.

(I picked the above set of examples after perusing the excellent book [Antti Laaksonen (2017) _Guide to Competitive Programming:  Learning and Improving Algorithms Through Contests_](https://link.springer.com/book/10.1007/978-3-319-72547-5).)

## Debugging and Troubleshooting

Static typing with compile-time type checking turns out to be a secret strength of Hoon.  Once you've satisfied the typechecker, your code is often surprisingly free of bugs (compared to e.g. Python).

There are three basic things that tend to go wrong:

1. Syntax error, general (just typing things out wrong, for instance in a way Dojo would prevent)
2. Syntax error mismatching rune daughters (due to `ace`/`gap` or miscounting children)
3. Type issues (`need`/`have`, notoriously)

This last case can be handled with a couple of expedients:

- Frequent use of `^-` kethep/`^+` ketlus to make sure that types match at various points in the code.

    This has two benefits:  it verifies your expectations about what values are being passed around, and it means that mismatches raise an error more closely to the source of the error.

    (Since Hoon checks type at build time, this does not incur a computational cost when the program is running.)

- Use of assertions to enforce type constraints.  Assertions are a form of `?` wut rune which check the structure of a value.  Ultimately they all reduce back to `?:` wutcol, but are very useful in this sugar form:

    - [`?>` wutgar](https://urbit.org/docs/hoon/reference/rune/wut#-wutgar) is a positive assertion, that a condition _must_ be true.
    - [`?<` wutgal](https://urbit.org/docs/hoon/reference/rune/wut#-wutgal) is a negative assertion, that a condition _must_ be false.
    - [`?~` wutsig](https://urbit.org/docs/hoon/reference/rune/wut#-wutsig) is a branch on null.

    For instance, some operations require a `lest`, a `list` guaranteed to be non-null (that is, `^-  (list)  ~` is excluded).

    ```hoon
    > =/  list=(list @)  ~[1 2 3]
     i.list
    -find.i.list
    find-fork
    dojo: hoon expression failed
    ```

    `?~` wutsig solves the problem for this case:

    ```hoon
    > =/  list=(list @)  ~[1 2 3]
     ?~  list  !!
     i.list
    1
    ```
    
    In general, if you see an error like `find.fork`, it means that the type system is confused by your use of a too general of a type for a particular case.  Use the assertion runes to correct its assumption.

- [Testing Code](/courses/hoon-school/I-testing) - This module will discuss how we can have confidence that a program does what it claims to do, using unit testing and debugging strategies.
- [Unit Tests](/userspace/apps/guides/unit-tests)


# emirp.md

---

+++
title = "Emirp"
weight = 90
+++
## Challenge: Reversible Primes

A prime number is a number that is only divisible by 1 and itself, for example, `7`. An [emirp](https://en.wikipedia.org/wiki/Emirp) is a prime number that results in a different prime when its decimal digits are reversed. For example, `107` and `701` are a pair of emirps, and `3,049` and `9,403`.

Palindromic numbers are not emirps. `101` is a prime and its reverse is itself -- it is not an emirp.

Your task for this challenge is write a generator that will add up all the first `n` emirps. To be precise, you should write a generator `emirp` which takes a `@ud` number `n` as an input, and returns a `@ud` number which is the sum of the first `n` emirps.

Example usage:
```
> +emirp 10
638
```

The first 10 emirps are `13, 17, 31, 37, 71, 73, 79, 97, 107, 113`, and their sum is `638`.

##  Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2024.3.  They are made available under the MIT License and CC0.  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_By ~nodmel-todsyr. A very fast and efficient solution._

```hoon
::  emirp.hoon
::  Finds a sum of first n emirp numbers
|^
|=  [n=@ud]
=/  i  0
=/  sum  0
=/  number  13
=|  emirps=(set @ud)
|-
?:  =(i n)
  sum
=^  x=@ud  emirps  (find-emirp number emirps)
%=  $
  i  +(i)
  sum  (add sum x)
  :: iterating only over 6k +- 1 numbers
  number  (add ?:(=((mod x 6) 1) 4 2) x)
==
::  Finds a smallest emirp which is greater than or equal to x.
::  Adds flipped emirp to the set of emirps
::  If emirp is in the set, returns it immediately
::
++  find-emirp
  |=  [x=@ud emirps=(set @ud)]
  ^-  [@ud (set @ud)]
  =/  flipped  (flip x)
  ?:  (~(has in emirps) x)
    [x emirps]
  ?:  &(!=(x flipped) (is-prime x) (is-prime flipped))
    [x (~(put in emirps) flipped)]
  $(x (add ?:(=((mod x 6) 1) 4 2) x))
::  Checks if x is a prime. 
::
++  is-prime
  |=  [x=@ud]
  ^-  ?
  ?:  (lte x 3)
    (gth x 1)
  ?:  |(=((mod x 2) 0) =((mod x 3) 0))
    %.n
  =/  limit  p:(sqt x)
  =/  j  5
  |-
  ?:  (gth j limit)
    %.y
  ?:  |(=((mod x j) 0) =((mod x (add 2 j)) 0))
    %.n
  $(j (add j 6))
::  Flips a number.
::
++  flip
  |=  [number=@ud]
  ^-  @ud
  =/  m  0
  =/  rip  (curr div 10)
  =/  last  (curr mod 10)
  |-
  ?:  =(number 0)
    m
  %=  $
    number  (rip number)
    m  (add (mul 10 m) (last number))
  ==
--
```



### Solution #2
_By ~ramteb-tinmut. Well-commented, easy to read, and fast._

```hoon
::  emirp.hoon
:: Return the sum of the first n emirp numbers
::
|=  target=@ud
=/  emirp-candidate  13  :: starting at the first emirp makes sense
=|  emirps=(list @ud)
=<
sieve
|%
++  sieve
  :: When the target is reached, sum the list of emirps
  ::
  ?:  =(target (lent emirps))
    |-
    ?~  emirps
      0
    (add i.emirps $(emirps t.emirps))
  :: Whilst below target, recurse on is-emirp after incrementing
  :: 
  %=  sieve
    emirps  (is-emirp emirp-candidate)
    emirp-candidate  (add emirp-candidate 1)
  ==
++  is-emirp
  |=  candidate=@ud
  =/  reversed  (reverse-ud candidate)
  :: Check if candidate number is a palindrome
  ::
  ?:  !=(reversed candidate)
    :: Is it also a prime?
    ::
    ?:  (is-prime [candidate (sqt candidate)])
      :: Check if the reverse is also a prime:
      ::
      ?:  (is-prime [reversed (sqt reversed)])
        :: Success! - store the emirp
        ::
        (into emirps 1 candidate)
      :: The reverse is not a prime:
      ::
      emirps
    :: Not prime
    ::
    emirps
  :: Palindrome & invalid
  ::  
  emirps
++  is-prime
  =/  divisor  2
  |=  [candidate=@ud root=[@ @]]  
  
  :: Fastest check first - has the divisor reached our input candidate? 
  ::
  ?:  =(candidate divisor)
    %.y
  :: Ensure non-zero modulo
  ::
  ?:  =((mod candidate divisor) 0)
    %.n
  :: If not a prime, then number must have a divisor less than or equal to its square root. There's an edge case if the square root is not a whole number, in which case we need to round up:
  ::
  ?:  &(=(+3.root 0) (gth divisor +2.root))
    %.y
  ?:  (gth divisor (add 1 +2.root))
    %.y
  :: Increment divisor and repeat
  ::
  %=  $
    divisor  (add divisor 1)
  ==

++  reverse-ud
  |=  number=@ud
  ^-  @ud
  =/  reversed  0
  :: Return reversed @ud when number reaches zero
  ::
  |-
    ?:  =(0 number)  
      reversed
    :: Otherwise loop until all digits are swapped:
    ::
    =.  reversed  (add (mul 10 reversed) (mod number 10))
    $(number (div number 10))  
--
```

##  Unit Tests

Following a principle of test-driven development, the unit tests below allow us to check for expected behavior. To run the tests yourself, follow the instructions in the [Unit Tests](/userspace/apps/guides/unit-tests) section.

```hoon
/+  *test
/=  emirp  /gen/emirp
|%
++  test-01
  %+  expect-eq
    !>  `@ud`13
    !>  (emirp 1)
++  test-02
  %+  expect-eq
    !>  `@ud`30
    !>  (emirp 2)
++  test-03
  %+  expect-eq
    !>  `@ud`169
    !>  (emirp 5)
++  test-04
  %+  expect-eq
    !>  `@ud`638
    !>  (emirp 10)
++  test-05
  %+  expect-eq
    !>  `@ud`6.857
    !>  (emirp 25)
++  test-06
  %+  expect-eq
    !>  `@ud`32.090
    !>  (emirp 50)
++  test-07
  %+  expect-eq
    !>  `@ud`115.370
    !>  (emirp 100)
++  test-08
  %+  expect-eq
    !>  `@ud`4.509.726
    !>  (emirp 500)
--
```

# gleichniszahlenreihe.md

---

+++
title = "Gleichniszahlenreihe"
weight = 20
+++

## Challenge: The Look-and-Say Sequence

_Gleichniszahlenreihe_, or the [look-and-say sequence](https://en.wikipedia.org/wiki/Look-and-say_sequence), is constructed from an aural description of a sequence of numbers.

Consider the sequence of numbers that begins with `1, 11, 21, 1211, 111221, 312211, 13112221, ...`.  Each number in the sequence represents what would result if the digits in the preceding value were counted and spoken aloud.  For instance, "1" yields "one 1 → 11"; "11" yields "two 1s → 21"; "21" yields "one 2, one 1 → 1211", and so forth.  The next number in the sequence after "13112221" is thus "one 1, one 3, two 1s, three 2s, one 1 → 1113213211".

This is a fairly complicated program.  You need a few parts:  the ability to take a tape and parse it into components, the ability to count components, and the ability to produce a new tape.  Then a recursing bit to produce a list of these values and (ultimately) return the last one.  Think about the Caesar cipher's structure.

- Compose a `%say` generator which carries out the look-and-say sequence calculation for a given input.  The input should be a number which indicates which value in the sequence is desired (e.g. 1→1, 2→11, 3→21).

## Solutions

_These solutions were submitted by the Urbit community as part of the Hoon School Live ~2022.2 cohort.  They are made available under both the [MIT license](https://mit-license.org/) and the [CC0 license](https://creativecommons.org/share-your-work/public-domain/cc0).  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_This solution was produced by ~midsum-salrux.  This code exhibits good core structure and code encapsulation in arms._

**`/gen/look-and-say.hoon`**

```hoon
:-  %say
|=  [* [n=@ud ~] *]
:-  %noun
=<  (compute-sequence n)
|%
+$  counted-digit  [count=@ud digit=@t]
++  compute-sequence
  |=  n=@ud
  ^-  tape
  =/  sequence  "1"
  |-
  ?:  =(n 1)
    sequence
  $(sequence (progress sequence), n (dec n))
++  progress
  |=  sequence=tape
  ^-  tape
  (speak (count-digits sequence))
++  speak
  |=  cd=(list counted-digit)
  ^-  tape
  (zing (turn cd |=(d=counted-digit ~[(crip ~(rud at count.d)) digit.d])))
++  count-digits
  |=  sequence=tape
  ^-  (list counted-digit)
  (scan sequence several-repeated-digits)
++  several-repeated-digits  (plus (cook unreap many-same-digit))
++  unreap
  |=  a=tape
  ^-  counted-digit
  [(lent a) (snag 0 a)]
++  many-same-digit
  ;~  pose
    (many-particular-digit '1')
    (many-particular-digit '2')
    (many-particular-digit '3')
    (many-particular-digit '4')
    (many-particular-digit '5')
    (many-particular-digit '6')
    (many-particular-digit '7')
    (many-particular-digit '8')
    (many-particular-digit '9')
  ==
++  many-particular-digit  (corl plus just)
--
```


Usage:

```hoon
> +look-and-say 1
"1"

> +look-and-say 2
"11"

> +look-and-say 5
"111221"

> +look-and-say 10
"13211311123113112211"

> +look-and-say 20
"11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211"
```


### Solution #2

_This solution was produced by ~nallux-dozryl.  This code exemplifies parsimonious use of parsing rules and can parse any arbitrary sequence of digits._

**`/gen/look-and-say.hoon`**

```hoon
:-  %say
|=  [* [in=tape ~] ~]
:-  %noun
^-  tape
=|  final=tape
|-
?~  in  final
=+  nums=`tape`(scan in (star nud))
=+  slot=(head nums)
=+  parsed=((star (just slot)) [[1 1] nums])
=+  count=(scow %ud (dec (tail (head (tail (need (tail parsed)))))))
=+  return=:(weld final count (trip slot))
=+  newin=(tail (tail (need (tail parsed))))
$(final return, in newin)
```

Usage:

```hoon
> +look-and-say "12"
"1112"

> +look-and-say "123"
"111213"

> +look-and-say "1234"
"11121314"

> +look-and-say "123455"
"1112131425"
```


# islands.md

---

+++
title = "Islands"
weight = 110
+++
## Challenge: Largest Island

We are given a map of an island archipelago and want to determine the size of the largest island. We begin with a 2-dimensional grid which is represented as a `(list (list @ud))`. Each `@ud` entry is either a `0`, which represents water, or a `1`, which represents land. We consider two land squares to be part of the same island if they are connected horizontally or vertically, **not diagonally**. We assume that the area outside of the map is entirely water.


You will write a generator `islands` that accepts a `(list (list @ud))` and returns a `@ud` representing the size of the largest island. It should also crash if given an invalid input, for example, if every grid row (the inner `(list @ud)`) is not the same length, or if any `@ud` is greater than `1`.

Example usage:

```
> +islands ~[~[0 0 1 0 0 0 0 1 0 0 0 0 0] ~[0 0 0 0 0 0 0 1 1 1 0 0 0] ~[0 1 1 0 1 0 0 0 0 0 0 0 0] ~[0 1 0 0 1 1 0 0 1 0 1 0 0] ~[0 1 0 0 1 1 0 0 1 1 1 0 0] ~[0 0 0 0 0 0 0 0 0 0 1 0 0] ~[0 0 0 0 0 0 0 1 1 1 0 0 0] ~[0 0 0 0 0 0 0 1 1 0 0 0 0]]
6
```
This input returns 6 this map has a largest island of size 6.

```
> islands ~[~[0 1] ~[0 1 0]]
dojo: naked generator failure
```

```
> islands ~[~[0 1] ~[1 2]]
dojo: naked generator failure
```

##  Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2024.3.  They are made available under the MIT License and CC0.  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_An efficient and clear solution by ~dabmul-matdel._

```hoon
::  sizes.hoon
::
::  Given a map with islands find the size of the largest one.
::
|=  input=(list (list @ud))
^-  @ud
::  total number of rows
::
=/  nrows  (lent input)
::  row index
::
=|  i=@ud
::  map from initial island-id to final island-id
::
=|  islands=(map @ud @ud)
::  map from final-island id to island size
::
=|  sizes=(map @ud @ud)
::  map from cell coordinates to initial island-id
::
=|  cells=(map [@ud @ud] @ud)
::  previous row accessed in the loop
::
=|  prev-row=(list @ud)
::  previous number of columns in the previous row
::
=|  prev-ncols=@ud
|^
::  nested loop, outer loop
::
=*  outer  $
::  parsed all rows, exit
::
?:  =(i nrows)
  (max-value sizes)
::  current row
::
=/  row  (snag i input)
::  number of columns in current row
::
=/  ncols=@ud  (lent row)
::  raise error if mismatch in number of columns
::
?>  |(=(prev-ncols 0) =(ncols prev-ncols))
::  columns index
::
=|  j=@ud
::  nested loop, inner loop
::
|-  ^-  @ud
=*  inner  $
::  parsed all columns, next row
::
?:  =(j ncols)
  outer(i +(i), prev-row row, prev-ncols ncols)
::  error if cell value is not 0 or 1
::
?>  (lth (snag j row) 2)
::  if cell value is 1 we are in an island
::
?:  =((snag j row) 1)
  ::  is the cell above an island?
  ::
  ?:  &((gth i 0) =((snag j prev-row) 1))
    =/  island-id=@ud  (get-island i j %up)
    ::  are the islands left and above our current cell connected?
    ::
    ?:  &((gth j 0) =((snag (sub j 1) row) 1))
      =/  left-island-id  (get-island i j %left)
      :: if so just grow the island
      ::
      ?:  =(island-id left-island-id)
        =/  new  (grow-island i j island-id)
        %=  inner
          sizes  sizes.new
          cells  cells.new
          j  +(j)
        ==
      ::  otherwise merge islands left and above, and grow the merged island
      ::
      =/  new  (merge-and-grow-islands i j island-id left-island-id)
      %=  inner
        islands  islands.new
        sizes  sizes.new
        cells  cells.new
        j  +(j)
      ==
    ::  otherwise just grow the island
    ::
    =/  new  (grow-island i j island-id)
    %=  inner
      sizes  sizes.new
      cells  cells.new
      j  +(j)
    ==
  ::  is the cell to our left an island?
  ::
  ?:  &((gth j 0) =((snag (sub j 1) row) 1))
    :: if so just grow the island
    ::
    =/  island-id  (get-island i j %left)
    =/  new  (grow-island i j island-id)
    %=  inner
      sizes  sizes.new
      cells  cells.new
      j  +(j)
    ==
  ::  otherwise create a new island
  ::
  =/  new  (new-island i j)
  %=  inner
    islands  islands.new
    sizes  sizes.new
    cells  cells.new
    j  +(j)
  ==
::  nothing to do
::
inner(j +(j))
++  max-value
  ::    return the maximum value of a map
  ::
  ::  my-map: map with @ud key-value pairs
  ::
  |=  [my-map=(map @ud @ud)]
  ^-  @ud
  (~(rep by my-map) |=([[k=@ud v=@ud] cur=@ud] ?:((gth v cur) v cur)))
++  get-island
  ::    return the island id left or above given coordinates
  ::
  ::  i: row index
  ::  j: column index
  ::  dir: direction
  ::
  |=  [i=@ud j=@ud dir=?(%left %up)]
  ^-  @ud
  =<  +
  %-  ~(get by islands)
  ?-  dir
  %up  +:(~(get by cells) [(sub i 1) j])
  %left  +:(~(get by cells) [i (sub j 1)])
  ==
++  new-island
  ::    create a new island at given coordinates
  ::
  ::  i: row index
  ::  j: column index
  ::
  |=  [i=@ud j=@ud]
  =/  island-id  (add ~(wyt by islands) 1)
  [
  islands=(~(put by islands) island-id island-id)
  sizes=(~(put by sizes) island-id 1)
  cells=(~(put by cells) [i j] island-id)
  ]
++  grow-island
  ::    grow island at given coordinates with given id
  ::
  ::  i: row index
  ::  j: column index
  ::  island-id: island id
  ::
  |=  [i=@ud j=@ud island-id=@ud]
  [
  sizes=(~(put by sizes) island-id +(+:(~(get by sizes) island-id)))
  cells=(~(put by cells) [i j] island-id)
  ]
++  merge-and-grow-islands
  ::    merge two islands at given coordinates with given ids
  ::
  ::  i: row index
  ::  j: column index
  ::  island-id: island id
  ::  other-island-id: island id of other island
  ::
  |=  [i=@ud j=@ud island-id=@ud other-island-id=@ud]
  =/  sizes  (~(put by sizes) island-id (add +:(~(get by sizes) other-island-id) +:(~(get by sizes) island-id)))
  [
    islands=(~(put by islands) other-island-id island-id)
    sizes=(~(put by sizes) island-id +(+:(~(get by sizes) island-id)))
    cells=(~(put by cells) [i j] island-id)
  ]
--
```



### Solution #2
_An excellent solution by ~ramteb-tinmut._

```hoon
::  islands.hoon
::  Just the wind and the sea, and the stars to guide you.
::
|=  archipelago=(list (list @ud))
^-  @ud
=/  greatest-isle  0
=<
=/  stretch  (lent archipelago)
=/  span  (lent (snag 0 archipelago))
:: Validate the incoming dataset - or else wreck
::
?:  !(levy archipelago |=(row=(list @ud) &(=((lent row) span) (levy row |=(cell=@ud (lth cell 2))))))
  !!
:: All hands make-sail, t'gansuls and courses - stand by the braces!
::
(voyage [archipelago stretch span 0 0 0])
|%
++  voyage
  |=  [archipelago=(list (list @ud)) stretch=@ud span=@ud lat=@ud long=@ud greatest-isle=@ud]
  ^-  @ud
  :: Completion - set the royals and stunsails, return to port
  ?:  =(lat (lent archipelago))
    greatest-isle
  :: Edge of the map: great serpents barr our course [~] ... turn south
  ::
  =/  course  (snag lat archipelago)
  ?:  =(long (lent course))
    $(long 0, lat +(lat))
  :: Land ho? (ie cell == 1)
  :: 
  ?:  =((snag long course) 1)
    :: Explore the extents of new land
    ::
    =/  newfound-land  0
    =/  revised-map  `(list (list @ud))`~
    =^  newfound-land  revised-map
      (landing-party [archipelago lat long stretch span 0])
    :: Maybe update the largest found island?
    ::
    ?:  (gth newfound-land greatest-isle)
      $(long +(long), archipelago revised-map, greatest-isle newfound-land)
    $(long +(long), archipelago revised-map)
  :: Just the endless ocean. Sail East
  ::
  $(long +(long), archipelago (snap archipelago lat (snap course long 8)))
++  landing-party
  |=  [archipelago=(list (list @ud)) lat=@ud long=@ud stretch=@ud span=@ud size=@ud]
  ^-  [@ud (list (list @ud))]
  :: Check if current cell is (still) land - and not already visited
  ::
  ?:  =((snag long (snag lat archipelago)) 1)
    ::  Make note of our location, before the rum starts flowing - then explore
    ::
    =/  new-size  +(size)
    =/  revised-map  (snap archipelago lat (snap (snag lat archipelago) long 8))
    :: North
    ::
    =^  new-size  revised-map
      ?:  !=(lat 0)
        $(lat (dec lat), archipelago revised-map, size new-size) 
      [new-size revised-map]
    :: South
    ::
    =^  new-size  revised-map
      ?:  !=(lat (dec stretch))
        $(lat +(lat), archipelago revised-map, size new-size)
      [new-size revised-map]
    :: East
    ::
    =^  new-size  revised-map
      ?:  !=(long (dec span))
        $(long +(long), archipelago revised-map, size new-size)
      [new-size revised-map]
    :: West
    ::
    =^  new-size  revised-map
      ?:  !=(long 0)
        $(long (dec long), archipelago revised-map, size new-size)
      [new-size revised-map]
    [new-size revised-map]
  ::  No more lands - ¡rückkehr zum schiff! 
  ::
  [size archipelago]
--
```

##  Unit Tests

Following a principle of test-driven development, the unit tests below allow us to check for expected behavior. To run the tests yourself, follow the instructions in the [Unit Tests](/userspace/apps/guides/unit-tests) section.

```hoon
/+  *test
/=  islands  /gen/islands
|%
::  tests for success
++  test-01
  %+  expect-eq
    !>  `@ud`1
    !>  %-  islands
        ~[~[1]]
++  test-02
  %+  expect-eq
    !>  `@ud`0
    !>  %-  islands
        ~[~[0]]
++  test-03
  %+  expect-eq
    !>  `@ud`0
    !>  %-  islands
        :~  
        ~[0 0]
        ~[0 0]
        ==
++  test-04
  %+  expect-eq
    !>  `@ud`1
    !>  %-  islands
        :~  
        ~[1 0]
        ~[0 0]
        ==
++  test-05
  %+  expect-eq
    !>  `@ud`1
    !>  %-  islands
        :~  
        ~[0 1]
        ~[0 0]
        ==
++  test-06
  %+  expect-eq
    !>  `@ud`1
    !>  %-  islands
        :~  
        ~[0 0]
        ~[1 0]
        ==
++  test-07
  %+  expect-eq
    !>  `@ud`1
    !>  %-  islands
        :~  
        ~[0 0]
        ~[0 1]
        ==
++  test-08
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[1 1]
        ~[0 0]
        ==
++  test-09
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[1 0]
        ~[1 0]
        ==
++  test-10
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[0 0]
        ~[1 1]
        ==
++  test-11
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[0 1]
        ~[0 1]
        ==
++  test-12
  %+  expect-eq
    !>  `@ud`1
    !>  %-  islands
        :~  
        ~[1 0]
        ~[0 1]
        ==
++  test-13
  %+  expect-eq
    !>  `@ud`1
    !>  %-  islands
        :~  
        ~[0 1]
        ~[1 0]
        ==
++  test-14
  %+  expect-eq
    !>  `@ud`3
    !>  %-  islands
        :~  
        ~[0 1]
        ~[1 1]
        ==
++  test-15
  %+  expect-eq
    !>  `@ud`3
    !>  %-  islands
        :~  
        ~[1 0]
        ~[1 1]
        ==
++  test-16
  %+  expect-eq
    !>  `@ud`3
    !>  %-  islands
        :~  
        ~[1 1]
        ~[0 1]
        ==
++  test-17
  %+  expect-eq
    !>  `@ud`3
    !>  %-  islands
        :~  
        ~[1 1]
        ~[1 0]
        ==
++  test-18
  %+  expect-eq
    !>  `@ud`4
    !>  %-  islands
        :~  
        ~[1 1]
        ~[1 1]
        ==
++  test-19
  %+  expect-eq
    !>  `@ud`4
    !>  %-  islands
        :~  
        ~[1 1 0]
        ~[1 1 0]
        ==        
++  test-20
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[1 0 1]
        ~[1 0 1]
        ==    
++  test-21
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[0 0 1]
        ~[1 0 1]
        ==   
++  test-22
  %+  expect-eq
    !>  `@ud`5
    !>  %-  islands
        :~  
        ~[0 1 1]
        ~[1 1 1]
        ==     
++  test-23
  %+  expect-eq
    !>  `@ud`3
    !>  %-  islands
        :~  
        ~[0 1 1]
        ~[1 0 1]
        ==     
++  test-24
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[0 1 0]
        ~[0 1 0]
        ==  
++  test-25
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[0 1 1]
        ~[1 0 0]
        ==  
++  test-26
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[1 0 1]
        ~[1 0 0]
        ==
++  test-27
  %+  expect-eq
    !>  `@ud`2
    !>  %-  islands
        :~  
        ~[1 1 0]
        ~[0 0 1]
        ==
:: random grids
++  test-28
  %+  expect-eq
    !>  `@ud`5
    !>  %-  islands
        :~  
        ~[0 1 1 1 1]
        ~[0 0 1 0 0]
        ~[0 0 0 0 0]
        ~[0 1 0 0 0]
        ~[0 1 0 0 1]
        ==
++  test-29
  %+  expect-eq
    !>  `@ud`5
    !>  %-  islands
        :~  
        ~[0 0 1 0 1]
        ~[0 1 0 1 0]
        ~[0 1 0 0 1]
        ~[0 1 0 1 1]
        ~[0 0 1 1 0]
        ==
++  test-30
  %+  expect-eq
    !>  `@ud`5
    !>  %-  islands
        :~  
        ~[1 1 0 1 1]
        ~[1 1 0 1 1]
        ~[1 0 1 0 0]
        ~[0 0 0 0 1]
        ~[0 0 0 1 0]
        ==
++  test-31
  %+  expect-eq
    !>  `@ud`20
    !>  %-  islands
        :~  
        ~[0 1 1 0 1 1 0 0 0 1]
        ~[0 1 0 0 1 0 1 0 0 0]
        ~[1 1 0 1 1 1 1 0 1 1]
        ~[0 0 1 0 0 1 1 0 0 1]
        ~[1 0 0 0 0 0 1 1 0 0]
        ~[1 1 0 1 1 1 0 1 1 0]
        ~[1 1 1 1 1 1 0 0 0 1]
        ~[1 1 1 0 0 0 0 1 0 0]
        ~[1 1 1 0 0 1 0 1 1 1]
        ~[1 1 0 1 0 1 1 1 0 0]
        ==
++  test-32
  %+  expect-eq
    !>  `@ud`18
    !>  %-  islands
        :~  
        ~[1 1 1 1 1 1 1 0 1 1]
        ~[1 0 1 0 1 1 1 1 1 0]
        ~[0 1 0 1 0 0 1 1 0 1]
        ~[1 0 1 1 0 1 0 0 0 1]
        ~[0 1 0 1 0 1 0 0 0 1]
        ~[1 1 0 1 1 1 1 0 0 0]
        ~[1 0 1 0 0 0 0 1 0 0]
        ~[1 0 0 1 1 1 0 1 1 1]
        ~[0 1 1 1 0 1 0 1 0 0]
        ~[0 1 0 0 0 0 1 0 1 0]
        ==
++  test-33
  %+  expect-eq
    !>  `@ud`10
    !>  %-  islands
        :~  
        ~[1 0 1 1 1 0 1 1 0 1]
        ~[0 0 1 0 1 1 0 0 1 0]
        ~[1 0 1 0 0 0 1 1 0 1]
        ~[1 0 0 0 1 0 0 1 1 0]
        ~[0 0 1 0 0 1 1 0 0 1]
        ~[0 0 0 1 1 0 0 0 0 0]
        ~[1 0 1 0 1 1 1 1 0 1]
        ~[0 1 0 1 1 1 0 0 0 1]
        ~[0 1 0 1 0 0 0 0 1 1]
        ~[1 0 0 0 0 0 0 0 1 0]
        ==
++  test-34
  %+  expect-eq
    !>  `@ud`1
    !>  %-  islands
        :~  
        ~[0 0 0 0 0 0 0 0 0 0]
        ~[1 0 1 0 0 0 1 0 0 0]
        ~[0 0 0 0 0 0 0 0 0 0]
        ~[0 0 0 0 0 1 0 0 0 0]
        ~[0 1 0 0 0 0 0 0 0 0]
        ~[0 0 1 0 0 0 0 0 0 0]
        ~[0 0 0 0 1 0 0 0 0 0]
        ~[0 0 0 0 0 0 1 0 1 0]
        ~[1 0 0 0 0 0 0 0 0 0]
        ~[0 1 0 0 1 0 0 0 0 0]
        ==
++  test-35
  %+  expect-eq
    !>  `@ud`6
    !>  %-  islands
        :~  
        ~[0 1 0 1 0 0 1 0 0 1]
        ~[0 0 0 1 0 0 0 0 0 0]
        ~[1 0 1 0 1 0 0 0 0 1]
        ~[0 1 0 0 0 0 1 1 0 0]
        ~[1 0 0 0 0 0 1 0 1 0]
        ~[0 0 0 0 1 0 1 0 0 0]
        ~[0 0 0 0 1 0 0 0 1 0]
        ~[0 0 0 0 0 1 1 0 1 0]
        ~[1 0 0 0 0 1 1 1 0 0]
        ~[0 0 0 0 0 1 0 0 0 0]
        ==
++  test-36
  %+  expect-eq
    !>  `@ud`6
    !>  %-  islands
        :~  
        ~[1 0 1 0 0 0 0 0 0 1 0 1 0 1 0]
        ~[0 0 0 0 0 1 0 0 0 0 1 0 0 1 0]
        ~[1 1 0 0 0 0 1 0 1 1 0 0 1 0 1]
        ~[1 0 0 1 0 0 1 0 0 0 1 0 0 0 0]
        ~[0 1 1 1 0 0 0 0 0 0 0 1 0 0 0]
        ~[0 0 0 0 0 1 0 0 0 1 0 0 0 0 0]
        ~[0 0 0 0 0 0 1 0 1 0 0 1 0 0 1]
        ~[0 0 0 0 0 1 0 1 0 0 0 1 1 0 0]
        ~[0 0 0 0 1 0 1 0 0 0 1 1 0 0 0]
        ~[0 0 1 0 0 0 1 1 0 1 0 0 0 0 0]
        ~[0 1 1 0 0 0 1 0 0 0 0 1 0 0 0]
        ~[1 1 0 0 0 1 0 0 0 0 0 0 0 1 0]
        ~[1 0 0 0 0 1 0 0 0 1 0 0 0 1 1]
        ~[0 0 0 1 0 0 1 0 0 1 0 1 0 1 0]
        ~[0 1 0 0 0 0 0 1 0 0 0 1 1 0 1]
        ==
++  test-37
  %+  expect-eq
    !>  `@ud`4
    !>  %-  islands
        :~  
        ~[0 1 0 0 0 1 0 0 0 0 1 0 1 0 0]
        ~[0 1 0 1 1 0 0 1 0 0 0 1 0 0 1]
        ~[0 1 0 0 1 0 1 1 1 0 0 0 0 0 0]
        ~[0 1 0 0 0 0 0 0 0 0 0 0 0 0 0]
        ~[0 0 1 0 0 0 1 0 1 0 0 0 0 1 0]
        ~[0 0 0 1 1 0 1 0 0 1 0 0 0 0 0]
        ~[1 0 0 1 0 1 0 0 0 0 0 0 0 0 0]
        ~[0 0 0 0 1 0 0 0 1 0 0 0 0 1 0]
        ~[0 0 0 0 0 0 0 0 0 0 1 0 0 0 0]
        ~[0 1 0 0 0 1 0 0 0 0 0 0 0 0 0]
        ~[0 1 0 0 0 0 0 1 0 0 1 0 1 0 0]
        ~[0 0 0 1 0 0 0 0 0 0 0 0 0 0 0]
        ~[0 1 0 0 0 1 0 0 0 0 1 1 0 1 0]
        ~[0 0 0 0 0 0 0 0 0 0 1 0 1 0 0]
        ~[0 1 1 0 0 0 0 0 0 0 1 0 0 0 0]
        ==
++  test-38
  %+  expect-eq
    !>  `@ud`21
    !>  %-  islands
        :~  
        ~[1 1 0 0 0 0 1 0 0 0 0 0 1 0 1]
        ~[1 0 0 1 0 0 0 0 0 0 1 1 1 0 1]
        ~[0 0 0 0 0 1 1 0 1 0 1 1 0 1 0]
        ~[1 0 1 0 0 0 0 1 1 0 0 0 0 0 0]
        ~[1 0 0 0 0 1 0 0 1 0 0 0 1 1 0]
        ~[0 0 0 1 0 0 1 0 1 0 0 1 0 1 0]
        ~[1 0 1 0 0 0 0 0 1 1 0 1 0 1 1]
        ~[0 1 1 0 0 0 0 0 1 0 1 0 1 0 0]
        ~[1 0 1 1 0 1 0 0 0 0 0 0 1 1 0]
        ~[0 1 0 1 1 0 0 0 1 1 1 0 0 1 0]
        ~[0 1 0 0 1 1 0 0 0 1 1 0 0 0 0]
        ~[0 0 1 0 0 0 1 1 1 1 1 0 1 0 0]
        ~[0 1 1 1 1 1 1 0 0 0 1 0 0 0 1]
        ~[0 0 0 0 0 1 1 0 0 1 0 0 0 0 0]
        ~[0 0 0 0 0 0 1 0 0 0 1 0 1 0 1]
        ==
++  test-39
  %+  expect-eq
    !>  `@ud`9
    !>  %-  islands
        :~  
        ~[0 0 1 1 0 1 1 0 0 0 0 0 0 0 0]
        ~[0 1 0 0 0 0 1 0 0 1 0 1 0 0 0]
        ~[1 1 1 0 0 0 1 0 0 0 1 0 0 0 0]
        ~[0 0 0 1 0 0 0 0 1 0 0 1 1 0 0]
        ~[1 0 1 0 0 0 0 1 0 1 0 0 1 1 1]
        ~[0 1 1 1 0 0 1 0 0 0 0 0 1 0 1]
        ~[0 0 1 1 0 0 0 1 1 0 1 0 0 0 0]
        ~[0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
        ~[1 1 0 1 1 0 0 1 1 0 1 0 1 0 1]
        ~[0 0 0 0 0 0 1 0 0 1 0 0 0 0 1]
        ~[0 0 0 1 1 0 1 0 0 0 0 0 1 0 1]
        ~[1 1 0 0 0 0 0 0 1 0 0 0 1 0 1]
        ~[0 0 1 1 1 0 1 0 0 0 0 1 0 1 0]
        ~[1 1 0 0 1 1 0 1 0 1 1 0 0 0 0]
        ~[0 0 1 1 1 1 0 0 0 0 1 0 0 1 1]
        ==
:: test for crash
++  test-40
    %-  expect-fail
    |.  %-  islands
        :: digit greater than 1 in matrix
        :~
        ~[0 0 1 1 0 1 1 0 0 0 0 0 0 0 0]
        ~[0 1 0 0 0 0 1 0 0 1 0 1 0 0 0]
        ~[1 1 1 0 0 0 1 0 0 0 1 0 0 0 0]
        ~[0 0 0 1 0 0 0 0 1 0 0 1 1 0 0]
        ~[1 0 1 0 0 0 0 1 0 1 0 0 1 1 1]
        ~[0 1 1 1 0 0 1 0 0 0 2 0 1 0 1]
        ~[0 0 1 1 0 0 0 1 1 0 1 0 0 0 0]
        ~[0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
        ~[1 1 0 1 1 0 0 1 1 0 1 0 1 0 1]
        ~[0 0 0 0 0 0 1 0 0 1 0 0 0 0 1]
        ~[0 0 0 1 1 0 1 0 0 0 0 0 1 0 1]
        ~[1 1 0 0 0 0 0 0 1 0 0 0 1 0 1]
        ~[0 0 1 1 1 0 1 0 0 0 0 1 0 1 0]
        ~[1 1 0 0 1 1 0 1 0 1 1 0 0 0 0]
        ~[0 0 1 1 1 1 0 0 0 0 1 0 0 1 1]
        ==
++  test-41
    %-  expect-fail
    |.  %-  islands
        :: one row too short
        :~  
        ~[1 1 0 0 0 0 1 0 0 0 0 0 1 0 1]
        ~[1 0 0 1 0 0 0 0 0 0 1 1 1 0 1]
        ~[0 0 0 0 0 1 1 0 1 0 1 1 0 1 0]
        ~[1 0 1 0 0 0 0 1 1 0 0 0 0 0 0]
        ~[1 0 0 0 0 1 0 0 1 0 0 0 1 1 0]
        ~[0 0 0 1 0 0 1 0 1 0 0 1 0 1 0]
        ~[1 0 1 0 0 0 0 0 1 1 0 1 0 1 1]
        ~[0 1 1 0 0 0 0 0 1 0 1 0 1 0]
        ~[1 0 1 1 0 1 0 0 0 0 0 0 1 1 0]
        ~[0 1 0 1 1 0 0 0 1 1 1 0 0 1 0]
        ~[0 1 0 0 1 1 0 0 0 1 1 0 0 0 0]
        ~[0 0 1 0 0 0 1 1 1 1 1 0 1 0 0]
        ~[0 1 1 1 1 1 1 0 0 0 1 0 0 0 1]
        ~[0 0 0 0 0 1 1 0 0 1 0 0 0 0 0]
        ~[0 0 0 0 0 0 1 0 0 0 1 0 1 0 1]
        ==
++  test-42
    %-  expect-fail
    |.  %-  islands
        :: one row too long
        :~  
        ~[1 1 0 0 0 0 1 0 0 0 0 0 1 0 1]
        ~[1 0 0 1 0 0 0 0 0 0 1 1 1 0 1]
        ~[0 0 0 0 0 1 1 0 1 0 1 1 0 1 0]
        ~[1 0 1 0 0 0 0 1 1 0 0 0 0 0 0]
        ~[1 0 0 0 0 1 0 0 1 0 0 0 1 1 0]
        ~[0 0 0 1 0 0 1 0 1 0 0 1 0 1 0]
        ~[1 0 1 0 0 0 0 0 1 1 0 1 0 1 1 1]
        ~[0 1 1 0 0 0 0 0 1 0 1 0 1 0 0]
        ~[1 0 1 1 0 1 0 0 0 0 0 0 1 1 0]
        ~[0 1 0 1 1 0 0 0 1 1 1 0 0 1 0]
        ~[0 1 0 0 1 1 0 0 0 1 1 0 0 0 0]
        ~[0 0 1 0 0 0 1 1 1 1 1 0 1 0 0]
        ~[0 1 1 1 1 1 1 0 0 0 1 0 0 0 1]
        ~[0 0 0 0 0 1 1 0 0 1 0 0 0 0 0]
        ~[0 0 0 0 0 0 1 0 0 0 1 0 1 0 1]
        ==
--
```

# luhn-number.md

---

+++
title = "Luhn Number"
weight = 80
+++

## Challenge: Luhn Number

The Luhn test is used by some credit card companies to distinguish valid credit card numbers from what could be a random selection of digits.

A Luhn number is a sequence of digits that passes the following test:

1. Reverse the order of the digits.
2. Take the first, third, and every odd-numbered digit in the reversed digits and sum them to form `s1`
3. Taking the second, fourth, and every even-numbered digit in the reversed digits:
     1. Multiply each by two. Within each doubled digit, sum those digits (if the answer is greater than nine) to form partial sums.
     2. Sum the partial sums of the even digits to form `s2`
4. If `s1 + s2` ends in zero then the original number is in the form of a valid credit card number as verified by the Luhn test.

For example, if the trial number is 49927398716:

```
Reverse the digits:
  61789372994
Sum the odd digits:
  6 + 7 + 9 + 7 + 9 + 4 = 42 = s1
The even digits:
    1,  8,  3,  2,  9
  Two times each even digit:
    2, 16,  6,  4, 18
  Sum the digits of each multiplication:
    2,  7,  6,  4,  9
  Sum the last:
    2 + 7 + 6 + 4 + 9 = 28 = s2

s1 + s2 = 70 ends in zero, which means that 49927398716 passes the Luhn test
```

Your task for this challenge is as follows. First you will write a library file `lib/luhn-number` with a core containing an arm named `++validate`. `validate` will be a gate that takes as input a `tape` which is a sequence of digits, and returns either a `%.y` or `%.n` if the number is a Luhn number or not. 

Example usage:
```
> =ln -build-file %/lib/luhn-number/hoon
> (validate:ln "49927398716")
%.y
> (validate:ln "1234")
%.n
```

Next you will write a generator file `gen/luhn-number` which takes as input a `tape` which consists of digits or the `*` character, such as:
```
"*1*25**574*18403"
"****"
"584"
```

It will return a `(list tape)` which contains all of the Luhn numbers that fit that format. The numbers should be in lexicographic order (smallest to largest by first digit, then second digit, and so on). You may choose to import and use your `++validate` arm, or perhaps use some other strategy.

Example usage:
```
> +luhn-number "**123"
["01123" "15123" "20123" "39123" "44123" "58123" "63123" "77123" "82123" "96123" ~]

> +luhn-number "123"
~

> +luhn-number "49927398716"
[49927398716 ~]
```

Some notes: 
* We take the input as a `tape` rather than a `@ud` because a potential credit card number can have leading zeros.

* Note that in Hoon, we index starting from 0 -- so the first digit will be in the 0th index, second in 1st index, and so on.

* This website may be of use for both checking if a number is Luhn and generating a list from missing digits: https://www.dcode.fr/luhn-algorithm

* Don't worry about numbers with less than 2 digits, or improperly formatted input (with letters and spaces etc.). You can assume that the input tape will have the correct format.

##  Unit Tests

Following a principle of test-driven development, we compose a series of tests which allow us to rigorously check for expected behavior.

```hoon
/+  *test
/+  ln=luhn-number
/=  luhn-number  /gen/luhn-number
|%
::  test valid numbers
::
++  test-01
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "49927398716")
++  test-02
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "1234567812345670")
++  test-03
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "4417123456789105")
++  test-04
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "20210917131347022")
++  test-05
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "1806040794512")
++  test-06
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "9856849794512")
++  test-07
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "5995841300227")
++  test-08
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "00")
++  test-09
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "34")
++  test-10
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "00005991")
++  test-11
  %+  expect-eq
    !>  %.y
    !>  (validate:ln "02310568590238405")
::  test invalid numbers
::
++  test-12
  %+  expect-eq
    !>  %.n
    !>  (validate:ln "1234")
++  test-13
  %+  expect-eq
    !>  %.n
    !>  (validate:ln "92")
++  test-14
  %+  expect-eq
    !>  %.n
    !>  (validate:ln "00001463")
++  test-15
  %+  expect-eq
    !>  %.n
    !>  (validate:ln "754717798")
++  test-16
  %+  expect-eq
    !>  %.n
    !>  (validate:ln "507274573")
++  test-17
  %+  expect-eq
    !>  %.n
    !>  (validate:ln "2342352356198234238")
++  test-18
  %+  expect-eq
    !>  %.n
    !>  (validate:ln "02310568590238406")
++  test-19
  %+  expect-eq
    !>  %.n
    !>  (validate:ln "5019876543217144")
++  test-20
  %+  expect-eq
    !>  %.n
    !>  (validate:ln "220743131719012023")
::  test number generation
::
++  test-21
  %+  expect-eq
    !>  `(list tape)`["01123" "15123" "20123" "39123" "44123" "58123" "63123" "77123" "82123" "96123" ~]
    !>  (luhn-number "**123")
++  test-22
  %+  expect-eq
    !>  `(list tape)`~
    !>  (luhn-number "123")
++  test-23
  %+  expect-eq
    !>  `(list tape)`["12345690" ~]
    !>  (luhn-number "12345690")
++  test-24
  %+  expect-eq
    !>  `(list tape)`["023259872" "123259871" "223259870" "323259879" "423259878" "523259877" "623259876" "723259875" "823259874" "923259873" ~]
    !>  (luhn-number "*2325987*")
++  test-25
  %+  expect-eq
    !>  `(list tape)`["845927593912820" ~]
    !>  (luhn-number "8459275*3912820")
++  test-26
  %+  expect-eq
    !>  `(list tape)`["00" "18" "26" "34" "42" "59" "67" "75" "83" "91" ~]
    !>  (luhn-number "**")
++  test-27
  %+  expect-eq
    !>  `(list tape)`["4002" "4192" "4242" "4382" "4432" "4572" "4622" "4762" "4812" "4952" ~]
    !>  (luhn-number "4**2")
++  test-28
  %+  expect-eq
    !>  `(list tape)`["10017" "10157" "10207" "10397" "10447" "10587" "10637" "10777" "10827" "10967" "11007" "11197" "11247" "11387" "11437" "11577" "11627" "11767" "11817" "11957" "12047" "12187" "12237" "12377" "12427" "12567" "12617" "12757" "12807" "12997" "13037" "13177" "13227" "13367" "13417" "13557" "13607" "13797" "13847" "13987" "14027" "14167" "14217" "14357" "14407" "14597" "14647" "14787" "14837" "14977" "15057" "15107" "15297" "15347" "15487" "15537" "15677" "15727" "15867" "15917" "16097" "16147" "16287" "16337" "16477" "16527" "16667" "16717" "16857" "16907" "17087" "17137" "17277" "17327" "17467" "17517" "17657" "17707" "17897" "17947" "18077" "18127" "18267" "18317" "18457" "18507" "18697" "18747" "18887" "18937" "19067" "19117" "19257" "19307" "19497" "19547" "19687" "19737" "19877" "19927" ~]
    !>  (luhn-number "1***7")
--
```

##  Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2023.6.  They are made available under the MIT License and CC0.  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_By ~dozreg-toplud._

`lib/luhn-number.hoon`
```hoon
::  lib/luhn-number.hoon
::  Library for HSL challenge #3
::
|%
::  ++validate: gate defined in the challenge
::
++  validate
  |=  a=tape
  ^-  ?
  =.  a  (flop a)
  =/  a-digits=(list @)  (turn a (cury slav %ud))
  =/  s1=@  (roll (skim-odd a-digits) add)
  =;  s2=@
    =(0 (mod (add s1 s2) 10))
  %+  roll
    (skim-even a-digits)
  ::  (gate that adds digits of 2*i to the accumulator)
  ::
  |=  [i=@ acc=@]
  =+  i2=(mul i 2)
  :(add acc (div i2 10) (mod i2 10))
::  ++skim-odd: return elements of a list with odd indices (1-indexed)
::
++  skim-odd
  |*  a=(list)
  ^+  a
  ?~  a
    ~
  ?~  t.a
    ~[i.a]
  [i.a $(a t.t.a)]
::  ++skim-even: return elements of a list with even indices (1-indexed)
::
++  skim-even
  |*  a=(list)
  ^+  a
  ?:  |(?=(~ a) ?=(~ t.a))
    ~
  [i.t.a $(a t.t.a)]
::
--
```

`gen/luhn-number.hoon`
```hoon
::  gen/luhn-number.hoon
::  Naked generator for HSL challenge #3
::
/+  *luhn-number
::
|=  a=tape
^-  (list tape)
=*  this-gate  ..$
=/  index-tar=(unit @)  (find "*" a)
::  if no * in `a`,
::
?~  index-tar
  ::  then return empty list if `a` is not a Luhn number, else return list
  ::  with `a`
  ::
  ?.  (validate a)
    ~
  ~[a]
::  else, replace first * with a digit, call this gate for each digit 0-9,
::  weld the results
::
=/  dry-snap  ^~((bake snap ,[tape @ char]))
%-  zing
%+  turn
  "0123456789"
(cork (cury (cury dry-snap a) u.index-tar) this-gate)
```

### Solution #2

_By ~pardun-nollev._

`lib/luhn-number.hoon`
```hoon
|%
++  validate
  |=  input=tape
  =/  input  (flop input)
  =(0 (mod (add (get-s1 input) (get-s2 input)) 10))
++  get-s1
  |=  input=tape
  ^-  @ud
  (roll (odd-digits input) add)
  ++  get-s2
  |=  input=tape
  ^-  @ud
  (roll (multiply-digits (convert-digits-to-text (double-digits input))) add)
:: take a tape
:: convert to @ud and sum
  ++  sum-digits
  |=  input=tape
  ^-  @ud
  (roll (turn input |=(a=@t (rash a dem))) add)
:: take list of tapes
:: convert to digits
:: multiply each list of digits
  ++  multiply-digits
  |=  input=(list tape)
  ^-  (list @ud)
  (turn input |=(a=tape (sum-digits a)))
:: take each number
:: convert to tape
++  convert-digits-to-text
  |=  input=(list @ud)
  ^-  (list tape)
  (turn input |=(a=@ud (scow %ud a)))
:: get even digits and multiply by two
++  double-digits
  |=  input=tape
  ^-  (list @ud)
  (turn (even-digits input) |=(a=@ud (mul a 2)))
++  get-element
  |=  [idx=@ud input=tape]
  ^-  tape
  ?:  (gte (lent input) +(idx))
  `tape`~[(snag idx input)]
  ~
++  odd-digits
  |=  input=tape
  ^-  (list @ud)
  =/  output=tape  ~
  |- 
  ?:  =(input ~)
    (turn output |=(a=@t (rash a dem)))
  %=  $
    output  (weld output (get-element 0 input))
    input  (oust [0 2] input)
  ==
++  even-digits
  |=  input=tape
  ^-  (list @ud)
  =/  output=tape  ~
  |- 
  ?:  =(input ~)
    (turn output |=(a=@t (rash a dem)))
  %=  $
    output  (weld output (get-element 1 input))
    input  (oust [0 2] input)
  ==
--
```

`gen/luhn-number.hoon`

```hoon
/+  luhn-number
|=  input=tape
=<
(skim `(list tape)`(get-permutations input) validate:luhn-number)
|%
++  digits  "0123456789"
++  get-permutations
  |=  input=tape
  =/  output=(list tape)  ~[input]
  =/  idx  0
  |- 
  ?:  =(idx (lent input))
    output
  %=  $
    output  (churn-numbers idx output)
    idx  +(idx)
  ==
++  churn-numbers
  |=  [idx=@ud input=(list tape)]
  ^-  (list tape)
  (zing (turn input |=(a=tape (generate-perms idx a))))
++  generate-perms
  |=  [idx=@ud input=tape]
  ^-  (list tape)
  ?:  =((snag idx input) '*')
  (turn digits |=(a=@t (snap input idx a)))
  ~[input]
--
```

### Solution #3

_By ~motdeg-bintul_

`lib/luhn-number`

```hoon
::  lib/luhn-number.hoon
::  Your code goes here
::
|%
++  validate
|=  a=tape
&(=((checkdits a) 0) (gth (lent a) 0)) 
++  checkdits
|=  a=tape
=/  totalsum  (add (s1 a) (s2 a))
=/  sumtape  (trip `@t`(scot %ud totalsum))
=/  digits  (scan sumtape (star dit))
::  ~&  (odds a)
::  ~&  (doubler a)
::  ~&  `(list @)`(getsums (doubler a))
::  ~&  (s1 a)
::  ~&  (s2 a)
::  ~&  totalsum
?:  (lte totalsum 9)
  +2:digits
(snag (sub (lent +3:digits) 1) `(list @ud)`+3:digits)
++  odds
|=  a=tape
=/  reverse  (flop a)
=/  count  0
|-
^-  (list @ud)
|-
?:  (gte count (lent reverse))
  ~
:-  (scan (trip (snag count reverse)) dit)
$(count (add 2 count))
++  s1
|=  a=tape
(roll `(list @ud)`(odds a) add)
++  evens
|=  a=tape
=/  reverse  (flop a)
=/  count  1
|-
^-  (list @ud)
|-
?:  (gte count (lent reverse))
  ~
:-  (scan (trip (snag count reverse)) dit)
$(count (add 2 count))
++  double
|=  [a=@]
(mul 2 a)
++  doubler
|=  a=tape
(turn `(list @ud)`(evens a) double)
++  adddit
|=  [a=(list @ud) b=@ud]
=/  list1  a
=/  list2  `(list @t)`(turn list1 (cury scot %ud))
=/  count  b
=/  digits  (scan (trip (snag count list2)) (star dit))
=/  d1  (snag 0 digits)
?:  =((lent digits) 1)
  `@ud`d1
?:  (gth (lent digits) 1)
  `@ud`(add d1 (snag 1 digits))
~
++  getsums
|=  a=(list @ud)
=/  nums  a
=/  count  0
|-
?:  (lth count (lent nums))
:-  (adddit nums count)
$(count (add 1 count))
?:  =(count (lent nums))
  ~
$(count (add 1 count))
++  s2
|=  a=tape
=/  nums  (doubler a)
(roll `(list @)`(getsums nums) add)
--
```

`gen/luhn-number`

```hoon
::  gen/luhn-number.hoon
::  Your code goes here
::
/=  ln  /lib/luhn-number
|=  a=tape
=<
(checkmissing a)
|%
  ++  missingnums
  |=  a=tape
  =/  count  0
  |-
  ?:  =(count (lent a))
    ~
  ?:  =((snag count a) '*')
  :-  count
  $(count (add 1 count))
  ?:  =(count (sub (lent a) 1))
    ~
  $(count (add 1 count))
  ++  replaceast
  |=  a=tape
  =/  pos  `(list @)`(missingnums a)
  =/  count  0
  =/  newtape  a
  =/  num  `@t`(scot %ud 0)
  |-
  ?:  =(count (sub (lent pos) 1))
    `(list @t)`(snap newtape (snag count pos) num)
  %=  $
    newtape  (snap newtape (snag count pos) num)
    count  (add count 1)
  ==
  ++  replacedigits
  |=  [a=tape b=@ud]
  =/  count  0
  =/  dits  (trip (crip (replaceast a)))
  =/  newdits  (a-co:co b) 
  =/  flopdits  (flop newdits)
  =/  indexcap  (sub (lent flopdits) 1)
  =/  pos  (flop `(list @ud)`(missingnums a))
  =/  newnum  `tape`dits
  |-
  ?:  =(count (lent newdits))
    newnum
  %=  $
    newnum  `tape`(snap newnum (snag count pos) (snag count flopdits))
    count  (add 1 count)
  ==
  ++  testnewnum
  |=  a=tape
  =/  format  a
  =/  count  0
  =/  countdit  (a-co:co count)
  =/  newnum  `tape`~
  =/  pos  `(list @ud)`(missingnums format)
  =/  dgtlent  (lent pos)
  |-
  ^-  (list tape)
  ?:  &(=((lent (a-co:co count)) (add 1 dgtlent)) =((validate:ln newnum) %.y))
    [newnum ~]
  ?:  =((lent (a-co:co count)) (add 1 dgtlent))
    ~
  ?:  =((validate:ln newnum) %.y)
  :-  newnum
  %=  $
    count  (add 1 count)
    newnum  (replacedigits format count)
    countdit  (a-co:co count)
  ==
  ?:  =((lent countdit) (add 1 dgtlent))
    ~
  %=  $
    count  (add 1 count)
    newnum  (replacedigits format count)
    countdit  (trip `@t`(scot %ud count))
  ==
  ++  checkmissing
  |=  a=tape
  ?:  &(=((missingnums a) ~) =((validate:ln a) %.y))
    `(list tape)`[a ~]
  (testnewnum a)
--
```


# min-path.md

---

+++
title = "Minimum Path Sum"
weight = 120
+++
## Challenge: Minimum Path Sum

You are given a 2D grid of positive whole numbers, represented as a `(list (list @ud))` You start in the top left corner of the grid, and your goal is to walk to the botttom right corner by taking steps either down or to the right. Your goal is to find the path that minimizes the sum of the numbers on the path.

Your task for this challenge is to write a generator that takes a `(list (list @ud))` and returns a `@ud` representing the minimum sum of numbers on a path from top left to bottom right.

Example usage:
```
> +min-path ~[~[1 3 1] ~[1 5 1] ~[4 2 1]]
7
```

Here you can see the above grid represented visually, and the minimum path totaling 7 that goes straight right then straight down.

```
1  3  1
1  5  1
4  2  1
```

##  Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2024.8.  They are made available under the MIT License and CC0.  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_The speed winner, and a very effective and clear solution by ~diblud-ricbet._

```hoon
::  min-path.hoon
::  Find the cheapest way of traversing a grid of costs from the top left
::  to the bottom right, moving only right and down.
::
|=  grid=(list (list @ud))
^-  @ud
::  Input: 2D (n x n) grid of costs to go through a square.
::  Output: Cheapest path from top left to bottom right.
::
=/  num-rows  (lent grid)
=/  num-columns  (lent (snag 0 grid))
::  Number of rows and number of columns in the grid.
::
=/  destination-costs  (reap num-rows (reap num-columns 0))
::  Initially, prepopulate destination-costs with 0s, the same
::  dimesions as grid. The tactic is to replace the 0 in destination-costs
::  at an index with the actual cheapeast cost of going from the top left
::  to that index.
::
::  We do so in a "diagonal" order of indices, since, if we know the cheapest
::  cost of getting to any squares a distance d from the top-left, we can
::  calculate quickly the cheapest cost of getting to any squares a distance
::  d+1 from the top left.
::
=/  row-index  0
=/  column-index  0
::  row-index and column-index keep track of what square we're actually on.
::
|-
=.  destination-costs
::  Change destination-costs to be...
::
%^  snap  destination-costs  row-index
%^  snap  (snag row-index destination-costs)  column-index
::  the current destination-costs but with (row-index, column-index)
::  replaced by the value computed below:
::
?:  &(=(row-index 0) =(column-index 0))
  (snag column-index (snag row-index grid))
  ::  If we're at (0, 0), the cost is going to be just grid[0][0].
  ::
?:  =(row-index 0)
  %+  add
  (snag column-index (snag row-index grid))
  (snag (sub column-index 1) (snag row-index destination-costs))
  ::  Else, if we're at (0, column-index), the cost is going to be
  ::  grid[0][column-index] + destination_costs[0][column-index - 1]
  ::
?:  =(column-index 0)
  %+  add
  (snag column-index (snag row-index grid))
  (snag column-index (snag (sub row-index 1) destination-costs))
  ::  Else, if we're at (row-index, 0), the cost is going to be
  ::  grid[row-index][0] + destination_costs[row-index - 1][0]
  ::
%+  add
(snag column-index (snag row-index grid))
%+  min
(snag (sub column-index 1) (snag row-index destination-costs))
(snag column-index (snag (sub row-index 1) destination-costs))
::  Else, the cost is going to be grid[row-index][column-index] +
::  min(
::    destination-costs[row-index][column-index - 1],
::    destination-costs[row-index - 1][column-index]
::  )
::
?:  &(=(row-index (sub num-rows 1)) =(column-index (sub num-columns 1)))
  (snag column-index (snag row-index destination-costs))
  ::  If we're in the bottom right, produce the answer.
  ::
?:  |(=(column-index 0) =(row-index (sub num-rows 1)))
  ?:  (lth :(add row-index column-index 1) num-columns)
    %=  $
    row-index  0
    column-index  :(add row-index column-index 1)
    ==
  %=  $
  row-index  (sub :(add row-index column-index 2) num-columns)
  column-index  (sub num-columns 1)
  ==
  ::  Else, if we've reached the end of our diagonal, restart again from
  ::  the top right of the next diagonal. Two cases for whether the new
  ::  diagonal starts on the top row or last column.
  ::
%=  $
row-index  +(row-index)
column-index  (sub column-index 1)
==
::  Else, keep moving along the diagonal.
::
```



### Solution #2
_Another good solution by ~norweg-rivlex._

```hoon
::  min-path.hoon
::  barebones a* implementation, using a sorted list
::  because I couldn't find a handy min-heap/priority
::  queue type thing, using basic distance to the goal
::  as the heuristic.
::
|=  grid=(list (list @ud))
^-  @ud
=/  max-y=@ud  (sub (lent grid) 1)
=/  max-x=@ud  (sub (lent (snag 0 grid)) 1)
::
::  the value at a position in the grid
=/  get-xy
  |=  [x=@ud y=@ud]
  ^-  @ud
  (snag x (snag y grid))
::
::  how many items still have to be added from a 
::  position in the grid
=/  dist-to-goal
  |=  [x=@ud y=@ud]
  ^-  @ud
  (add (sub max-x x) (sub max-y y))
::
::  data structure containing the search state at
::  each point in the grid, tot as the sum of the 
::  grid items so far visited, cmp as the heuristic
::  weight, x, y as the grid location
=/  search-pt  ,[tot=@ud cmp=@ud x=@ud y=@ud]
::
::  get the search point one step to the right in the
::  grid from the passed search point, if not at limit
=/  next-right
  |=  p=search-pt
  ^-  (unit search-pt)
  ?:  =(x.p max-x)  ~
  =/  x  +(x.p)
  =/  tot  (add tot.p (get-xy x y.p))
  =/  cmp  (add tot (dist-to-goal x y.p))
  (some [tot cmp x y.p])
::
::  get the search point one step down in the grid
::  from the passed search point, if not at limit
=/  next-down
  |=  p=search-pt
  ^-  (unit search-pt)
  ?:  =(y.p max-y)  ~
  =/  y  +(y.p)
  =/  tot  (add tot.p (get-xy x.p y))
  =/  cmp  (add tot (dist-to-goal x.p y))
  (some [tot cmp x.p y])
::
::  insert a new search point to the correct location
::  in the passed frontier to maintain ordering by cmp
=/  add-frontier-pt
  |=  [f=(list search-pt) pt=search-pt]
  ?~  f  ~[pt]
  ?:  (gth cmp.i.f cmp.pt)  [pt f]
  [i.f $(f t.f)]
::
::  insert a number of new search points to the 
::  correct locations in the passed frontier
=/  add-frontier-pts
  |=  [f=(list search-pt) pts=(list search-pt)]
  ?~  pts  f
  $(f (add-frontier-pt f i.pts), pts t.pts)
::
::  the initial state of the frontier, containing the
::  search point for the top left item in the grid
=/  frontier=(list search-pt)  
  =/  top-left  (get-xy 0 0)
  =/  cmp  (add top-left (dist-to-goal 0 0))
  ~[[top-left cmp 0 0]]
::
::  main loop, getting the lowest cmp search point
::  from the frontier, getting the possible next points,
::  if there are none, we're done - return the tot
::  value; otherwise loop, updating the frontier to
::  remove the current point and insert its neighbours
|-
  ?~  frontier  !!
  =/  p  i.frontier
  =/  r  (next-right p)
  =/  d  (next-down p)
  =/  pts-to-add  (murn ~[r d] |=(a=(unit search-pt) a))
  ?~  pts-to-add  tot.p
  $(frontier (add-frontier-pts t.frontier pts-to-add))
```

##  Unit Tests

Following a principle of test-driven development, the unit tests below allow us to check for expected behavior. To run the tests yourself, follow the instructions in the [Unit Tests](/userspace/apps/guides/unit-tests) section.

```hoon
/+  *test
/=  min-path  /gen/min-path
|%
++  test-01
  %+  expect-eq
    !>  `@ud`1
    !>  %-  min-path
        ~[~[1]]
++  test-02
  %+  expect-eq
    !>  `@ud`0
    !>  %-  min-path
        ~[~[0]]
++  test-03
  %+  expect-eq
    !>  `@ud`12
    !>  %-  min-path
        :~  
       ~[2 3]
       ~[8 7]
        ==
++  test-04
  %+  expect-eq
    !>  `@ud`5
    !>  %-  min-path
        :~  
        ~[0 0 4]
        ~[1 0 5]
        ~[8 4 1]
        ==
++  test-05
  %+  expect-eq
    !>  `@ud`21
    !>  %-  min-path
        :~  
        ~[6 3 1 8 1]
        ~[5 6 0 0 9]
        ~[0 0 4 5 6]
        ==
++  test-06
  %+  expect-eq
    !>  `@ud`27
    !>  %-  min-path
        :~  
        ~[2 3 2]
        ~[6 7 5]
        ~[5 8 6]
        ~[2 1 4]
        ~[1 9 7]
        ==
++  test-07
  %+  expect-eq
    !>  `@ud`28
    !>  %-  min-path
        :~  
        ~[7 4 9 4 2]
        ~[8 7 0 0 5]
        ~[3 3 3 3 3]
        ~[0 4 3 4 0]
        ~[8 6 8 1 4]
        ==
++  test-08
  %+  expect-eq
    !>  `@ud`46
    !>  %-  min-path
        :~  
       ~[5 4 3 6 1 1 9 7 5 8]
       ~[5 6 3 9 3 2 6 7 9 1]
       ~[6 7 8 5 6 1 9 5 9 7]
       ~[3 5 7 7 5 2 8 3 4 2]
       ~[3 8 3 8 8 2 4 1 0 6]
       ~[2 5 4 0 1 0 7 7 6 2]
       ~[1 9 4 5 9 1 0 7 1 9]
       ~[3 4 8 5 1 0 6 8 4 1]
       ~[3 1 8 0 6 0 9 2 7 4]
       ~[9 4 8 6 6 7 1 5 2 3]
        ==
++  test-09
  %+  expect-eq
    !>  `@ud`57
    !>  %-  min-path
        :~  
        ~[8 1 1 3 0 8 7 4 6 0]
        ~[1 9 7 9 8 0 2 2 5 2]
        ~[4 5 1 7 7 4 8 8 1 7]
        ~[0 6 1 1 2 8 8 5 9 8]
        ~[6 1 9 8 8 2 4 9 1 9]
        ~[5 6 4 2 9 4 9 9 3 1]
        ~[6 5 9 0 0 4 5 4 2 5]
        ~[3 0 3 7 7 8 0 3 7 4]
        ~[9 5 0 0 3 3 7 5 7 3]
        ~[0 3 5 6 0 0 6 3 3 8]
        ==
++  test-10
  %+  expect-eq
    !>  `@ud`56
    !>  %-  min-path
        :~  
        ~[0 4 8 0 1 3 4 8 1 8 2 8 7 1 7]
        ~[4 5 9 1 3 2 4 4 3 4 0 2 6 6 3]
        ~[5 4 8 9 3 1 1 6 7 0 8 0 0 4 1] 
        ~[7 5 7 3 7 3 8 2 4 7 7 0 8 4 8]
        ~[7 1 1 1 1 0 8 1 2 5 4 6 5 9 0]
        ~[0 0 3 2 9 4 3 7 8 1 9 6 9 3 0]
        ~[9 4 9 6 4 0 0 3 3 6 4 6 8 8 2]
        ~[0 0 8 0 4 4 2 1 7 9 2 4 8 3 8]
        ~[1 0 7 6 4 2 9 3 5 5 7 1 3 8 3]
        ~[6 0 3 6 1 6 6 7 0 2 6 4 3 3 1]
        ==
++  test-11
  %+  expect-eq
    !>  `@ud`63
    !>  %-  min-path
        :~
        ~[6 5 9 2 5 9 9 6 1 4]
        ~[7 5 3 4 5 9 0 9 3 9]
        ~[2 5 2 7 7 4 4 0 9 9]
        ~[1 2 1 6 3 8 8 7 1 7]
        ~[8 1 2 4 8 0 2 7 4 3]
        ~[8 3 6 8 0 6 6 4 9 6]
        ~[2 3 5 4 4 9 8 2 7 3]
        ~[5 1 6 4 1 4 2 1 3 1]
        ~[2 6 1 6 1 0 2 5 7 4]
        ~[8 2 2 4 6 1 4 4 5 9]
        ~[6 0 5 3 2 8 4 2 6 2]
        ~[5 1 6 3 9 2 8 6 0 8]
        ~[3 0 7 1 3 2 4 6 3 0]
        ~[2 7 5 1 5 1 9 5 9 1]
        ~[3 2 5 5 4 1 9 1 5 4]
        ==
++  test-12
  %+  expect-eq
    !>  `@ud`65
    !>  %-  min-path
        :~
        ~[4 7 6 1 6 8 8 2 1 5 1 2 2 8 3]
        ~[6 8 0 8 6 4 9 7 6 1 7 3 1 9 9]
        ~[4 8 2 6 7 1 5 1 1 7 3 7 3 4 2]
        ~[7 7 5 9 6 0 0 5 0 2 3 9 0 5 3]
        ~[0 2 3 8 1 8 9 7 1 6 9 0 9 7 9]
        ~[1 4 1 5 7 6 6 1 3 8 9 6 9 7 6]
        ~[2 8 4 6 0 2 2 2 5 7 7 9 8 4 7]
        ~[0 4 1 1 5 4 7 3 9 1 4 6 1 3 2]
        ~[6 0 5 2 8 4 5 1 7 6 3 5 1 7 7]
        ~[4 1 7 2 9 0 7 0 1 4 8 1 1 9 1]
        ~[3 6 2 5 2 2 9 9 2 8 3 2 8 2 3]
        ~[1 8 1 7 2 3 0 2 1 3 6 3 1 2 9]
        ~[6 5 8 4 4 2 9 4 3 2 0 6 0 3 2]
        ~[7 1 1 0 8 8 7 2 7 7 3 7 7 3 3]
        ~[9 6 9 4 7 8 2 6 7 2 1 0 2 5 0]
        ==
--
```

# phone-letters.md

---

+++
title = "Phone Letters"
weight = 130
+++
## Challenge: Phone Letters


Previously, people typed words on a phone by pressing combinations of numbers. Each number mapped to a few different possible letters, as shown below.

```
 1    2    3
     ABC  DEF

 4    5    6
GHI  JKL  MNO

 7    8    9
PQRS TUV  WXYZ
    
      0
```

In this task, you will write a generator that accepts a `@ud` number and returns a `(list tape)` containing all the different strings that it could represent.

* Note that `1` and `0` do not map to any letters in the phonepad. Let's crash if the input `@ud` contains any `1` or `0`.
* Let's return the list of strings sorted in alphabetical order, all in lowercase.

Recall that `@ud` numbers need a dot marking every three digit places if the number is higher than `999`, i.e. `234.567.892` is `234,567,892`.
  
Example usage:
```
> +phone-letters 29
<<"aw" "ax" "ay" "az" "bw" "bx" "by" "bz" "cw" "cx" "cy" "cz">>
```

##  Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2024.8.  They are made available under the MIT License and CC0.  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_Our style winner, a clean and well-commented solution by ~norweg-rivlex._

```hoon
::  phone-letters.hoon
::  convert a positive integer into a list of the possible
::  phone number mnemonics
::
|=  n=@ud
^-  (list tape)
::
::  mapping from phone number digits to the letters that
::  may be used for it, which letters are in alphabetic
::  order
=/  digit-letters  %-  my  :~
  ['2' "abc"]
  ['3' "def"]
  ['4' "ghi"]
  ['5' "jkl"]
  ['6' "mno"]
  ['7' "pqrs"]
  ['8' "tuv"]
  ['9' "wxyz"]
==
::
::  get the letters for the passed digit, or die if
::  none such exist
=/  letters-for-digit
  |=  [digit=@t]
  ^-  tape
  (need (~(get by digit-letters) digit))
::
::  for a list of incomplete mnemonics, being constructed
::  from end to start, for a passed digit, result in a
::  new list with the new letters prepended in order
=/  prepend-all-for-digit
  |=  [digit=@t values=(list tape)]
  ^-  (list tape)
  ?:  =(digit '.')  values
  =/  letters  (flop (letters-for-digit digit))
  =|  result=(list tape)
  |-
  ^-  (list tape)
  ?~  letters  result
  %=  $
    letters  t.letters
    result  (weld (turn values |=(item=tape [i.letters item])) result)
  ==
::
::  digits of the passed number in reverse order
=/  digits=tape  (flop "{<n>}")
::
::  building the result
=|  result=(list tape)
::
::  main loop - get each digit in reverse order, and
::  build the list of results by adding the possible
::  letters in turn
|-
  ?~  digits  result
  =/  next
    ?~  result  (turn (letters-for-digit i.digits) |=(d=@t ~[d]))
    (prepend-all-for-digit i.digits result)
  %=  $
    digits  t.digits
    result  next
  ==
```



### Solution #2
_The speed winner by ~diblud-ricbet._

```hoon
::  phone-letters.hoon
::  Convert a @ud entry into an old-school T9 keyboard into a list of possible tapes.
::
|=  n=@ud
^-  (list tape)
?<  =(n 0)
=/  char-map
%-  malt
:~
[2 `(list tape)`~["a" "b" "c"]]
[3 `(list tape)`~["d" "e" "f"]]
[4 `(list tape)`~["g" "h" "i"]]
[5 `(list tape)`~["j" "k" "l"]]
[6 `(list tape)`~["m" "n" "o"]]
[7 `(list tape)`~["p" "q" "r" "s"]]
[8 `(list tape)`~["t" "u" "v"]]
[9 `(list tape)`~["w" "x" "y" "z"]]
==
=/  output  `(list tape)`~
|-
?:  =(n 0)
  (sort output aor)
%=  $
n  (div n 10)
output
?~  output
  (~(got by char-map) (mod n 10))
%-  zing
%+  turn  output
|=  existing=tape
%+  turn  (~(got by char-map) (mod n 10))
|=  letter=tape
%+  weld  letter  existing
==
```

##  Unit Tests

Following a principle of test-driven development, the unit tests below allow us to check for expected behavior. To run the tests yourself, follow the instructions in the [Unit Tests](/userspace/apps/guides/unit-tests) section.

```hoon
/+  *test
/=  phone-letters  /gen/phone-letters
|%
::  tests for success
::
++  test-01
  %+  expect-eq
    !>  `(list tape)`~["a" "b" "c"]
    !>  %-  phone-letters  2
++  test-02
  %+  expect-eq
    !>  `(list tape)`~["d" "e" "f"]
    !>  %-  phone-letters  3
++  test-03
  %+  expect-eq
    !>  `(list tape)`~["g" "h" "i"]
    !>  %-  phone-letters  4
++  test-04
  %+  expect-eq
    !>  `(list tape)`~["j" "k" "l"]
    !>  %-  phone-letters  5
++  test-05
  %+  expect-eq
    !>  `(list tape)`~["m" "n" "o"]
    !>  %-  phone-letters  6
++  test-06
  %+  expect-eq
    !>  `(list tape)`~["p" "q" "r" "s"]
    !>  %-  phone-letters  7
++  test-07
  %+  expect-eq
    !>  `(list tape)`~["t" "u" "v"]
    !>  %-  phone-letters  8
++  test-08
  %+  expect-eq
    !>  `(list tape)`~["w" "x" "y" "z"]
    !>  %-  phone-letters  9
++  test-09
  %+  expect-eq
    !>  `(list tape)`~["aw" "ax" "ay" "az" "bw" "bx" "by" "bz" "cw" "cx" "cy" "cz"]
    !>  %-  phone-letters  29
++  test-10
  %+  expect-eq
    !>  `(list tape)`~["dj" "dk" "dl" "ej" "ek" "el" "fj" "fk" "fl"]
    !>  %-  phone-letters  35
++  test-11
  %+  expect-eq
    !>  `(list tape)`~["pg" "ph" "pi" "qg" "qh" "qi" "rg" "rh" "ri" "sg" "sh" "si"]
    !>  %-  phone-letters  74
++  test-12
  %+  expect-eq
    !>  `(list tape)`~["aga" "agb" "agc" "aha" "ahb" "ahc" "aia" "aib" "aic" "bga" "bgb" "bgc" "bha" "bhb" "bhc" "bia" "bib" "bic" "cga" "cgb" "cgc" "cha" "chb" "chc" "cia" "cib" "cic"]
    !>  %-  phone-letters  242
++  test-13
  %+  expect-eq
    !>  `(list tape)`~["amw" "amx" "amy" "amz" "anw" "anx" "any" "anz" "aow" "aox" "aoy" "aoz" "bmw" "bmx" "bmy" "bmz" "bnw" "bnx" "bny" "bnz" "bow" "box" "boy" "boz" "cmw" "cmx" "cmy" "cmz" "cnw" "cnx" "cny" "cnz" "cow" "cox" "coy" "coz"]
    !>  %-  phone-letters  269
++  test-14
  %+  expect-eq
    !>  `(list tape)`~["tta" "ttb" "ttc" "tua" "tub" "tuc" "tva" "tvb" "tvc" "uta" "utb" "utc" "uua" "uub" "uuc" "uva" "uvb" "uvc" "vta" "vtb" "vtc" "vua" "vub" "vuc" "vva" "vvb" "vvc"]
    !>  %-  phone-letters  882
++  test-15
  %+  expect-eq
    !>  `(list tape)`~["pdm" "pdn" "pdo" "pem" "pen" "peo" "pfm" "pfn" "pfo" "qdm" "qdn" "qdo" "qem" "qen" "qeo" "qfm" "qfn" "qfo" "rdm" "rdn" "rdo" "rem" "ren" "reo" "rfm" "rfn" "rfo" "sdm" "sdn" "sdo" "sem" "sen" "seo" "sfm" "sfn" "sfo"]
    !>  %-  phone-letters  736
++  test-16
  %+  expect-eq
    !>  `(list tape)`~["jtdg" "jtdh" "jtdi" "jteg" "jteh" "jtei" "jtfg" "jtfh" "jtfi" "judg" "judh" "judi" "jueg" "jueh" "juei" "jufg" "jufh" "jufi" "jvdg" "jvdh" "jvdi" "jveg" "jveh" "jvei" "jvfg" "jvfh" "jvfi" "ktdg" "ktdh" "ktdi" "kteg" "kteh" "ktei" "ktfg" "ktfh" "ktfi" "kudg" "kudh" "kudi" "kueg" "kueh" "kuei" "kufg" "kufh" "kufi" "kvdg" "kvdh" "kvdi" "kveg" "kveh" "kvei" "kvfg" "kvfh" "kvfi" "ltdg" "ltdh" "ltdi" "lteg" "lteh" "ltei" "ltfg" "ltfh" "ltfi" "ludg" "ludh" "ludi" "lueg" "lueh" "luei" "lufg" "lufh" "lufi" "lvdg" "lvdh" "lvdi" "lveg" "lveh" "lvei" "lvfg" "lvfh" "lvfi"]
    !>  %-  phone-letters  5.834
++  test-17
  %+  expect-eq
    !>  `(list tape)`~["jjdd" "jjde" "jjdf" "jjed" "jjee" "jjef" "jjfd" "jjfe" "jjff" "jkdd" "jkde" "jkdf" "jked" "jkee" "jkef" "jkfd" "jkfe" "jkff" "jldd" "jlde" "jldf" "jled" "jlee" "jlef" "jlfd" "jlfe" "jlff" "kjdd" "kjde" "kjdf" "kjed" "kjee" "kjef" "kjfd" "kjfe" "kjff" "kkdd" "kkde" "kkdf" "kked" "kkee" "kkef" "kkfd" "kkfe" "kkff" "kldd" "klde" "kldf" "kled" "klee" "klef" "klfd" "klfe" "klff" "ljdd" "ljde" "ljdf" "ljed" "ljee" "ljef" "ljfd" "ljfe" "ljff" "lkdd" "lkde" "lkdf" "lked" "lkee" "lkef" "lkfd" "lkfe" "lkff" "lldd" "llde" "lldf" "lled" "llee" "llef" "llfd" "llfe" "llff"]
    !>  %-  phone-letters  5.533
++  test-18
  %+  expect-eq
    !>  `(list tape)`~["jggp" "jggq" "jggr" "jggs" "jghp" "jghq" "jghr" "jghs" "jgip" "jgiq" "jgir" "jgis" "jhgp" "jhgq" "jhgr" "jhgs" "jhhp" "jhhq" "jhhr" "jhhs" "jhip" "jhiq" "jhir" "jhis" "jigp" "jigq" "jigr" "jigs" "jihp" "jihq" "jihr" "jihs" "jiip" "jiiq" "jiir" "jiis" "kggp" "kggq" "kggr" "kggs" "kghp" "kghq" "kghr" "kghs" "kgip" "kgiq" "kgir" "kgis" "khgp" "khgq" "khgr" "khgs" "khhp" "khhq" "khhr" "khhs" "khip" "khiq" "khir" "khis" "kigp" "kigq" "kigr" "kigs" "kihp" "kihq" "kihr" "kihs" "kiip" "kiiq" "kiir" "kiis" "lggp" "lggq" "lggr" "lggs" "lghp" "lghq" "lghr" "lghs" "lgip" "lgiq" "lgir" "lgis" "lhgp" "lhgq" "lhgr" "lhgs" "lhhp" "lhhq" "lhhr" "lhhs" "lhip" "lhiq" "lhir" "lhis" "ligp" "ligq" "ligr" "ligs" "lihp" "lihq" "lihr" "lihs" "liip" "liiq" "liir" "liis"]
    !>  %-  phone-letters  5.447
++  test-19
  %+  expect-eq
    !>  `(list tape)`~["gwad" "gwae" "gwaf" "gwbd" "gwbe" "gwbf" "gwcd" "gwce" "gwcf" "gxad" "gxae" "gxaf" "gxbd" "gxbe" "gxbf" "gxcd" "gxce" "gxcf" "gyad" "gyae" "gyaf" "gybd" "gybe" "gybf" "gycd" "gyce" "gycf" "gzad" "gzae" "gzaf" "gzbd" "gzbe" "gzbf" "gzcd" "gzce" "gzcf" "hwad" "hwae" "hwaf" "hwbd" "hwbe" "hwbf" "hwcd" "hwce" "hwcf" "hxad" "hxae" "hxaf" "hxbd" "hxbe" "hxbf" "hxcd" "hxce" "hxcf" "hyad" "hyae" "hyaf" "hybd" "hybe" "hybf" "hycd" "hyce" "hycf" "hzad" "hzae" "hzaf" "hzbd" "hzbe" "hzbf" "hzcd" "hzce" "hzcf" "iwad" "iwae" "iwaf" "iwbd" "iwbe" "iwbf" "iwcd" "iwce" "iwcf" "ixad" "ixae" "ixaf" "ixbd" "ixbe" "ixbf" "ixcd" "ixce" "ixcf" "iyad" "iyae" "iyaf" "iybd" "iybe" "iybf" "iycd" "iyce" "iycf" "izad" "izae" "izaf" "izbd" "izbe" "izbf" "izcd" "izce" "izcf"]
    !>  %-  phone-letters  4.923
::  tests for failure
::
++  test-20
    %-  expect-fail
    |.  (phone-letters 0)
++  test-21
    %-  expect-fail
    |.  (phone-letters 1)
++  test-22
    %-  expect-fail
    |.  (phone-letters 12)
++  test-23
    %-  expect-fail
    |.  (phone-letters 13)
++  test-24
    %-  expect-fail
    |.  (phone-letters 14)
++  test-25
    %-  expect-fail
    |.  (phone-letters 15)
++  test-26
    %-  expect-fail
    |.  (phone-letters 16)
++  test-27
    %-  expect-fail
    |.  (phone-letters 17)
++  test-28
    %-  expect-fail
    |.  (phone-letters 18)
++  test-29
    %-  expect-fail
    |.  (phone-letters 19)
++  test-30
    %-  expect-fail
    |.  (phone-letters 20)
++  test-31
    %-  expect-fail
    |.  (phone-letters 21)
++  test-32
    %-  expect-fail
    |.  (phone-letters 5.814)
++  test-33
    %-  expect-fail
    |.  (phone-letters 5.804)
++  test-34
    %-  expect-fail
    |.  (phone-letters 53.204)
++  test-35
    %-  expect-fail
    |.  (phone-letters 12.345)
++  test-36
    %-  expect-fail
    |.  (phone-letters 59.491)
++  test-37
    %-  expect-fail
    |.  (phone-letters 87.650)
++  test-38
    %-  expect-fail
    |.  (phone-letters 87.651)
++  test-39
    %-  expect-fail
    |.  (phone-letters 81.123)
++  test-40
    %-  expect-fail
    |.  (phone-letters 10.000)
--
```

# restore-ip.md

---

+++
title = "Restore IP"
weight = 100
+++
## Challenge: Restore IP Addresses

An IPv4 address consists of exactly four non-negative whole numbers, separated by single dots. Each number is between 0 and 255 (inclusive) and cannot have leading zeros, unless it is 0.

For example, the following are valid IPv4 addresses:
* `1.1.1.1`
* `255.255.255.255`
* `192.168.0.1`
* `23.25.1.194`

While the following are not:
* `01.1.1.01`
* `256.255.255.255`
* `192.168.00.1`
* `a23.b25.1.194`

A database containing IPv4 addresses has gotten out of order up by addresses losing their dots. Your job is to restore it. You'll write a generator `restore-ip` such that it takes a `@t` `cord` containing only numerical digits and returns a `set` of all the `@t` `cord`s with dots inserted into the given digits to create a valid IPv4 address. 

We also want to crash if the input given is clearly invalid. Your generator should crash in the following cases:
* If the input contains any characters other than digits.
* If the input length is greater than 12.


Example usage:
```
> +restore-ip '12345678'
{'1.234.56.78' '123.45.6.78' '12.34.56.78' '123.45.67.8' '123.4.56.78'}
```

```
> +restore-ip '1234567890123456'
dojo: naked generator failure
```

```
> +restore-ip '111a'
dojo: naked generator failure
```

##  Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2024.3.  They are made available under the MIT License and CC0.  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_By ~nodsup-halnux. Clearly written, well-commented, and very Hoonish._

```hoon
::  +restore-ip: An algorithm that takes a cord
::    of digits, and tries to generate valid ips.
::    If digit cord length is <4, returns ~
::    If digit cord length is >12, crashes (!!)
::    If non-numerics present, crashes (!!)
::    Otherwise, return a (set @t) of results.
::
|^
::  Bar-ket (|^) buck arm.
::    $ arm has control flow and tests basic cases
::    before handing off input tape to the main 
::    algorithm for finding IPs.
::    Returns a (set @t).
::
|=  [tcord=@t]
  ^-  (set @t)
  ::  We need a tape for our work. Convert.
  ::
  =/  ttape  (trip tcord)
  :: We use length twice, so pin a variable.
  ::
  =/  lentape  (lent ttape)
  :: Are all of our characters digits?  If not, crash
  ::
  ?.  =((lent (skip ttape is-digit)) 0)  !!
    :: Is our length less than 4? If so, return ~
    ::
    ?.  (gte lentape 4)
      `(set @t)`(silt `(list @t)`~)
      ::  Is our tape greater than 12?  If so, crash.
      ::
      ?.  ?!((gth lentape 12))  !!
        ::  Finally, lets call the algorithm.
        ::
        (first-loop ttape)
::  This is a structure used for generating our IPs
::  in the algorithm below. An IPv4 consists of four
::  octets (8 bits), making a 32 bit address.
::
+$  octets  $:  o1=tape
           o2=tape
         o3=tape
       o4=tape
    ==
::  ++is-digit: Checks to see if an inputed character
::    is a valid digit from 0-9.  Used by the skip
::    gate as a negative filter, to check for 
::    non-numeric characters in cord input.
::    Interestingly, our tapes are made up of @tD's, 
::    but checking equality with an @t works. 
::    Returns a loobean.
::
++  is-digit
|=  [c=@t]
  ^-  ?
  ::  Check if c is any numeric digit. Return true
  ::  If we find a digit.
  ::
  ?|  =(c '0')  =(c '1')  =(c '2')
    =(c '3')  =(c '4')  =(c '5')
    =(c '6')  =(c '7')  
    =(c '8')  =(c '9')
  ==
::  ++range-ok: Small gate for seeing if our octet
::    from the octets structure is between 1 and 255
::    (inclusive).  Note slav crashes if we have a 
::    cord that starts with zero - this is guarded
::    against by the ++check-ip control flow.
::    Returns a loobean.
::
++  range-ok
|=  [q=tape]
  ^-  ?
    =/  testnum  (slav %ud (crip q))
    &((gth testnum 0) (lth testnum 255))
::  ++check-ip:  Given a octet from the  octets struct
::    checks the following:  If first character is a 
::    zero AND length is 1, return %.y. Else, Check if 
::    our characters are < 4 in length, and number they
::    represent is in range.
::    Returns a loobean
::
++  check-ip
|=  [octet=tape]
  ^-  ?
    :: Prove octet not ~, expose i/t faces for use.
    ::
    ?~  octet  !!
      :: Is our first digit zero?
      ::
      ?:  =('0' i.octet)
        :: If it is, only a string of length 1 is valid
        ::
        ?:  =((lent octet) 1)
          %.y
        ::  Otherwise, return false.
        ::
        %.n
        ::If it is not zero, then test length and range
        ::
      ?:  &((lth (lent octet) 4) (range-ok octet))
          %.y
      :: Our length/range test failed, so return false.
      ::
      %.n
::  ++build-ip:  Given the  octets structure, build a
::    valid IP. Assumes we checked our octet and all 
::    tests passed.
::    Returns a cord.
::
++  build-ip
|=  [ip=octets]
  ^-  @t  (crip "{o1.ip}.{o2.ip}.{o3.ip}.{o4.ip}")
::  General comments about loops below:
::    Splitting up the loops into three gates makes it 
::    easier to read, with the drawback that our gate 
::    inputs for loops 2 and 3 get a bit long and our 
::    run-time might go up a bit.  As our input cords 
::    are no longer than 12 characters, computational 
::    efficiency isn't a serious issue.
::
::  ++first-loop:  First of three loops. Variable i is 
::    set, which represents the dot separation between 
::    our first and second octet, conceptually.
::    Calls second-loop, and then union merges the 
::    results into the result1 variable.
::    Returns a (set @t).
::
++  first-loop
|=  [iptape=tape]
  ^-  (set @t)
  ::  Paramters for our trap.
  ::
  =/  i  1
  =/  len  (lent iptape)
  =/  result1  `(set @t)`~
  |-  
    ^-  (set @t)
    ::  Is i less than tape length?
    ::
    ?:  (lth i len)
      ::If so, compute j, and call second-loop. Then 
      :: merge second loop results in to result1.
      ::
      =/  j  (add i 1)
      %=  $
        result1  (~(uni in result1) (second-loop i j iptape))
        i  +(i)
      ==
      ::If i bound is hit, return result1.
      ::
      result1
::  ++second-loop:  Structurally, this is the same
::    as first-loop.  Takes i and j as input,
::    and sets up k for third-loop.
::    Returns a (set @t)
::
++  second-loop
|=  [i=@ud j=@ud iptape=tape]
  ^-  (set @t)
  ::  Paramters for our trap.
  ::
  =/  result2  `(set @t)`~
  =/  len  (lent iptape)
  |-
    ^-  (set @t)
    ::  Is j less than tape length?
    ::
    ?:  (lth j len)
      ::  If so, compute k, and call third-loop. Then 
      ::  merge third loop results in to result2.
      ::  
      =/  k  (add j 1)
      %=  $
        result2  (~(uni in result2) (third-loop i j k iptape))
        j  +(j)
      ==
      ::If j bound is hit, return result1.
      result2
::  ++third-loop:  This is the main body of code for
::    generating IP addresses. It takes ijk and
::    finds octet, which are stored in the octets
::    structure. Validity checks (above) are called,
::    and if they pass, a valid IP is generated and
::    inserted into the results3 variable.
::    Returns a (set @t)
::
++  third-loop
|=  [i=@ud j=@ud k=@ud iptape=tape]
  ^-  (set @t)
  ::  Paramters for our trap.
  ::
  =/  len  (lent iptape)
  =/  result3  `(set @t)`~
  |-
    ^-  (set @t)
    ::  Is j less than tape length?
    ::
    ?:  (lth k len)
      ::  If so...now we do something different!
      ::  Pin gen-ip to sample, and insert each octet
      ::  into the octets structure. Use current ijk
      ::  to figure out our individual octets. 
      ::
      =/  gen-ip  
        ^-  octets  
          :^    o1=(limo (scag i iptape)) 
              o2=(limo (slag i (scag j iptape))) 
            o3=(limo (slag j (scag k iptape))) 
          o4=(limo (slag k iptape))
        ::  Main checks on octet. Do they all pass?
        ::
        ?:  ?&  (check-ip o1.gen-ip) 
                (check-ip o2.gen-ip) 
                (check-ip o3.gen-ip) 
                (check-ip o4.gen-ip)
            ==        
            ::  If they do, build a valid IP.
            ::  Place results in result3. Increase k.
            ::
            %=  $
                result3  (~(put in result3) (build-ip gen-ip))
                k  +(k)
            ==
            ::  If they do not, lets increase k and
            ::  try the next IP.
            ::
            %=  $
              k  +(k)
            ==
      ::  k has hit bound, return result3.
      ::
      result3
--
```



### Solution #2
_By ~ramteb-tinmut. Another great solution, well written and commented._

```hoon
::  restore-ip.hoon
::  A generator to parse valid IPv4 format addresses from an input cord
::
|=  input=@t
:: Ensure output type
::
^-  (set cord)
=<
:: cord to tape
::
=/  input-tape  (trip input)
:: Check for forbidden characters
::
?>  (validate-input input-tape)
:: Return an empty set if the tape is less than minimum required to form a valid IP
::
?:  (lth (lent input-tape) 4)
  `(set cord)`~
:: Otherwise proceed to create a set of possible valid ips
::
(do-tape [input-tape "" 1 0 `(set cord)`~])
|%

:: This is our core logic where the input tape is repeatedly parsed for combinations of IP octets, and the set of possible IPs is assembled
::
++  do-tape
  |=  [input-tape=tape found-ip=tape count=@ud found-octets=@ud ip-set=(set cord)]
  :: 4 found octets mean we may have a vali IP, if the tape is exhausted
  ::
  ?:  =(found-octets 4)
    ?:  =(0 (lent input-tape))
      (~(put in ip-set) (crip found-ip))
    ip-set
  :: If we haven't got a full set of octets, and our remaining tape can't be split, we catch that here
  ::
  ?:  |(=(count 4) (gth count (lent input-tape)))
    ip-set
  :: Divide the tape in to a head & tail, based on current split count
  ::
  =/  head  (scag count input-tape)
  =/  tail  (slag count input-tape)
  :: Check if the head is a valid octet, and weld it to our existing tape
  ::
  ?:  (is-octet head)
    =/  updated-ip  (weld found-ip ?:((lth found-octets 3) (snoc head '.') head))
    :: tisdot was the missing ingredient to get recursion on the remaining tape, and ensure all possible combinations are sought. 
    ::
    :: We're updating the value of the ip-set with the return value of an additional call to this do-tape arm; with the counter is reset, along with our updated-ip tape, which contains the new valid octet, and the current tail as our new input tape
    ::
    =.  ip-set  
      $(input-tape tail, found-ip updated-ip, count 1, found-octets +(found-octets), ip-set ip-set)
    :: This new subject is then fed into another, inner recursive loop, with the count incremented until we either find a new octet or exhaust the string
    ::
    $(count +(count))
  :: If we didn't get a match, this is where we also feed back in on the outer loop with the split counter incremented
  ::
  $(count +(count))

:: Takes a tape, and ensures it fulfils requirement for an IPv4 octet
::
++  is-octet
  |=  input=tape
  :: If candidate is only 1 digit, then it's always valid:
  ::
  ?:  =((lent input) 1)
    %.y
  :: If candidate starts with 0, then it must have length 1
  ::
  ?:  &(=((head input) '0') (gth (lent input) 1))
    %.n
  :: Candidate as a number must be =< 255
  ::
  ?:  (gth (rash (crip input) dem) 255)
    %.n
  %.y
  
:: Checks a input tape for illegal chars and length restrictions
::
++  validate-input
  |=  input=tape
  =/  allowed  "1234567890"
  ?&
    :: Ensure input =< 13
    ::
    (lth (lent input) 13)
    :: Ensure all elements are numbers:
    ::
    (levy input |=(a=@ !=((find `(list @t)`~[a] allowed) ~)))
  ==
--
```

##  Unit Tests

Following a principle of test-driven development, the unit tests below allow us to check for expected behavior. To run the tests yourself, follow the instructions in the [Unit Tests](/userspace/apps/guides/unit-tests) section.

```hoon
/+  *test
/=  restore-ip  /gen/restore-ip
|%
::  test for failures
++  test-01
    %-  expect-fail
    |.  (restore-ip 'a')
++  test-02
    %-  expect-fail
    |.  (restore-ip '1234567890123')
++  test-03
    %-  expect-fail
    |.  (restore-ip '111a1111')
++  test-04
    %-  expect-fail
    |.  (restore-ip '111111@1')
++  test-05
    %-  expect-fail
    |.  (restore-ip '11111111111^')
::  tests for success
++  test-06
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~)
    !>  (restore-ip '1')
++  test-07
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~)
    !>  (restore-ip '11')
++  test-08
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~)
    !>  (restore-ip '111')
++  test-09
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.1.1.1'])
    !>  (restore-ip '1111')
++  test-10
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.1.1.11' '1.1.11.1' '1.11.1.1' '11.1.1.1'])
    !>  (restore-ip '11111')
++  test-11
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.1.1.111' '1.1.11.11' '1.1.111.1' '1.11.1.11' '1.11.11.1' '1.111.1.1' '11.1.1.11' '11.1.11.1' '11.11.1.1' '111.1.1.1'])
    !>  (restore-ip '111111')
++  test-12
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.1.11.111' '1.1.111.11' '1.11.1.111' '1.11.11.11' '1.11.111.1' '1.111.1.11' '1.111.11.1' '11.1.1.111' '11.1.11.11' '11.1.111.1' '11.11.1.11' '11.11.11.1' '11.111.1.1' '111.1.1.11' '111.1.11.1' '111.11.1.1'])
    !>  (restore-ip '1111111')
++  test-13
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.1.111.111' '1.11.11.111' '1.11.111.11' '1.111.1.111' '1.111.11.11' '1.111.111.1' '11.1.11.111' '11.1.111.11' '11.11.1.111' '11.11.11.11' '11.11.111.1' '11.111.1.11' '11.111.11.1' '111.1.1.111' '111.1.11.11' '111.1.111.1' '111.11.1.11' '111.11.11.1' '111.111.1.1'])
    !>  (restore-ip '11111111')
++  test-14
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.11.111.111' '1.111.11.111' '1.111.111.11' '11.1.111.111' '11.11.11.111' '11.11.111.11' '11.111.1.111' '11.111.11.11' '11.111.111.1' '111.1.11.111' '111.1.111.11' '111.11.1.111' '111.11.11.11' '111.11.111.1' '111.111.1.11' '111.111.11.1'])
    !>  (restore-ip '111111111')
++  test-15
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.111.111.111' '11.11.111.111' '11.111.11.111' '11.111.111.11' '111.1.111.111' '111.11.11.111' '111.11.111.11' '111.111.1.111' '111.111.11.11' '111.111.111.1'])
    !>  (restore-ip '1111111111')
++  test-16
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['11.111.111.111' '111.11.111.111' '111.111.11.111' '111.111.111.11'])
    !>  (restore-ip '11111111111')
++  test-17
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['111.111.111.111'])
    !>  (restore-ip '111111111111')
++  test-18
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.9.99.91' '1.99.9.91' '1.99.99.1' '19.9.9.91' '19.9.99.1' '19.99.9.1' '199.9.9.1'])
    !>  (restore-ip '199991')
++  test-19
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.99.99.91' '19.9.99.91' '19.99.9.91' '19.99.99.1' '199.9.9.91' '199.9.99.1' '199.99.9.1'])
    !>  (restore-ip '1999991')
++  test-20
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['19.99.99.91' '199.9.99.91' '199.99.9.91' '199.99.99.1'])
    !>  (restore-ip '19999991')
++  test-21
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['199.99.99.91'])
    !>  (restore-ip '199999991')
++  test-22
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~)
    !>  (restore-ip '1999999991')
++  test-23
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['9.8.7.6'])
    !>  (restore-ip '9876')
++  test-24
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['9.8.7.65' '9.8.76.5' '9.87.6.5' '98.7.6.5'])
    !>  (restore-ip '98765')
++  test-25
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['9.8.76.54' '9.87.6.54' '9.87.65.4' '98.7.6.54' '98.7.65.4' '98.76.5.4'])
    !>  (restore-ip '987654')
++  test-26
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['9.87.65.43' '98.7.65.43' '98.76.5.43' '98.76.54.3'])
    !>  (restore-ip '9876543')
++  test-27
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['98.76.54.32'])
    !>  (restore-ip '98765432')
++  test-28
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~)
    !>  (restore-ip '987654321')
++  test-29
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.1.25.61' '1.12.5.61' '1.12.56.1' '1.125.6.1' '11.2.5.61' '11.2.56.1' '11.25.6.1' '112.5.6.1'])
    !>  (restore-ip '112561')
++  test-30
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.12.56.11' '1.125.6.11' '1.125.61.1' '11.2.56.11' '11.25.6.11' '11.25.61.1' '112.5.6.11' '112.5.61.1' '112.56.1.1'])
    !>  (restore-ip '1125611')
++  test-31
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['1.112.56.111' '11.12.56.111' '11.125.6.111' '11.125.61.11' '111.2.56.111' '111.25.6.111' '111.25.61.11'])
    !>  (restore-ip '111256111')
++  test-32
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~)
    !>  (restore-ip '111256111111')
++  test-33
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['100.0.0.1'])
    !>  (restore-ip '100001')
++  test-34
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['100.0.100.1'])
    !>  (restore-ip '10001001')
++  test-35
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['10.0.100.100' '100.10.0.100' '100.100.10.0'])
    !>  (restore-ip '100100100')
++  test-36
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['10.10.10.101' '10.101.0.101' '101.0.10.101'])
    !>  (restore-ip '101010101')
++  test-37
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~)
    !>  (restore-ip '1010101010')
++  test-38
  %+  expect-eq
    !>  `(set @t)`(silt `(list @t)`~['0.1.1.111' '0.1.11.11' '0.1.111.1' '0.11.1.11' '0.11.11.1' '0.111.1.1'])
    !>  (restore-ip '011111')
--
```

# rhonda.md

---

+++
title = "Rhonda Numbers"
weight = 30
+++

## Challenge: Rhonda Numbers

A Rhonda number is a positive integer _n_ that satisfies the property that, for [a given base _b_](https://en.wikipedia.org/wiki/Radix), the product of the base-_b_ digits of _n_ is equal to _b_ times the sum of _n_'s prime factors.  Only composite bases (non-prime bases) have Rhonda numbers.

For instance, consider 10206₁₀ = 2133132₄, that is, 2×4⁶ + 1×4⁵ + 3×4⁴ + 3×4³ + 1×4² + 3×4¹ + 2×4⁰ = 2×4096₁₀ + 1×1024₁₀ + 3×256₁₀ + 3×64₁₀ + 1×16₁₀ + 3×4₁₀ + 2 = 8192₁₀ + 1024₁₀ + 768₁₀ + 192₁₀ + 16₁₀ + 12₁₀ + 2 = 10206₁₀.  10206₁₀ has the prime factorization (2, 3, 3, 3, 3, 3, 3, 7) because 2×3⁶×7 = 10206₁₀.  This is a base-4 Rhonda number because 2×1×3×3×1×3×2 = 108₁₀ and 4×(2+3+3+3+3+3+3+7) = 4×27₁₀ = 108₁₀.

The [Wolfram MathWorld entry for “Rhonda Number”](https://mathworld.wolfram.com/RhondaNumber.html) provides tables of many Rhonda numbers.  Further information on Rhonda numbers may be found at [Numbers Aplenty](https://www.numbersaplenty.com/set/Rhonda_number/).  You may also find this [base conversion tool](https://www.rapidtables.com/convert/number/base-converter.html) helpful.

- Produce three files to carry out this task:

    - `/lib/rhonda/hoon`

        Your library `/lib/rhonda/hoon` should expose two arms:

        - `++check` accepts a `@ud` unsigned decimal value for the base and a `@ud` unsigned decimal value for the number, and returns `%.y` or `%.n` depending on whether the given number is a Rhonda number in that base or not.
        - `++series` accepts a base as a `@ud` unsigned decimal value and a number of values to return `n`, and either returns `~` if the base is prime or the `n` first Rhonda numbers in that base.

    - `/gen/rhonda-check/hoon`

        You should provide a `%say` generator at `/gen/rhonda-check/hoon` which accepts a `@ud` unsigned decimal value and applies `++check` to verify if that value is a Rhonda number or not.

    - `/gen/rhonda-series/hoon`

        You should provide a `%say` generator at `/gen/rhonda-series/hoon` which accepts a `@ud` unsigned decimal value `b` and a `@ud` unsigned decimal value `n`, where `b` is the base _b_, and returns the first _n_ Rhonda numbers in that base.

##  Unit Tests

Following a principle of test-driven development, we compose a series of tests which allow us to rigorously check for expected behavior.

```hoon
/+  *test, *rhonda
|%
++  test-check-four
  ;:  weld
  %+  expect-eq
    !>  %.n
    !>  (check 4 10.000)
  %+  expect-eq
    !>  %.y
    !>  (check 4 10.206)
  %+  expect-eq
    !>  %.n
    !>  (check 4 10.500)
  %+  expect-eq
    !>  %.y
    !>  (check 4 11.935)
  %+  expect-eq
    !>  %.n
    !>  (check 4 50.000)
  %+  expect-eq
    !>  %.y
    !>  (check 4 94.185)
  ==
++  test-check-six
  ;:  weld
  %+  expect-eq
    !>  %.n
    !>  (check 6 800)
  %+  expect-eq
    !>  %.y
    !>  (check 6 855)
  %+  expect-eq
    !>  %.n
    !>  (check 6 1.000)
  %+  expect-eq
    !>  %.y
    !>  (check 6 1.029)
  %+  expect-eq
    !>  %.n
    !>  (check 6 18.181)
  %+  expect-eq
    !>  %.y
    !>  (check 6 19.136)
  ==
++  test-check-eight
  ;:  weld
  %+  expect-eq
    !>  %.n
    !>  (check 8 1.200)
  %+  expect-eq
    !>  %.y
    !>  (check 8 1.836)
  %+  expect-eq
    !>  %.n
    !>  (check 8 4.800)
  %+  expect-eq
    !>  %.y
    !>  (check 8 6.622)
  %+  expect-eq
    !>  %.n
    !>  (check 8 18.181)
  %+  expect-eq
    !>  %.y
    !>  (check 8 25.398)
  ==
++  test-check-nine
  ;:  weld
  %+  expect-eq
    !>  %.n
    !>  (check 9 15.000)
  %+  expect-eq
    !>  %.y
    !>  (check 9 15.540)
  %+  expect-eq
    !>  %.n
    !>  (check 9 20.000)
  %+  expect-eq
    !>  %.y
    !>  (check 9 21.054)
  %+  expect-eq
    !>  %.n
    !>  (check 9 45.000)
  %+  expect-eq
    !>  %.y
    !>  (check 9 47.652)
  ==
++  test-check-ten
  ;:  weld
  %+  expect-eq
    !>  %.n
    !>  (check 10 1.000)
  %+  expect-eq
    !>  %.y
    !>  (check 10 1.568)
  %+  expect-eq
    !>  %.n
    !>  (check 10 2.000)
  %+  expect-eq
    !>  %.y
    !>  (check 10 2.835)
  %+  expect-eq
    !>  %.n
    !>  (check 10 12.000)
  %+  expect-eq
    !>  %.y
    !>  (check 10 12.985)
  ==
++  test-check-twelve
  ;:  weld
  %+  expect-eq
    !>  %.n
    !>  (check 12 500)
  %+  expect-eq
    !>  %.y
    !>  (check 12 560)
  %+  expect-eq
    !>  %.n
    !>  (check 12 1.000)
  %+  expect-eq
    !>  %.y
    !>  (check 12 3.993)
  %+  expect-eq
    !>  %.n
    !>  (check 12 50.000)
  %+  expect-eq
    !>  %.y
    !>  (check 12 58.504)
  ==
++  test-series-three
  ;:  weld
  %+  expect-eq
    !>  ~
    !>  (series 3 5)
  ==
++  test-series-four
  ;:  weld
  %+  expect-eq
    !>  `(list @ud)`~[10.206]
    !>  (series 4 1)
  %+  expect-eq
    !>  `(list @ud)`~[10.206 11.935 12.150 16.031]
    !>  (series 4 4)
  %+  expect-eq
    !>  `(list @ud)`~[10.206 11.935 12.150 16.031 45.030 94.185]
    !>  (series 4 6)
  ==
++  test-series-six
  ;:  weld
  %+  expect-eq
    !>  `(list @ud)`~[855]
    !>  (series 6 1)
  %+  expect-eq
    !>  `(list @ud)`~[855 1.029 3.813 5.577]
    !>  (series 6 4)
  %+  expect-eq
    !>  `(list @ud)`~[855 1.029 3.813 5.577 7.040 7.304]
    !>  (series 6 6)
  ==
++  test-series-nine
  ;:  weld
  %+  expect-eq
    !>  `(list @ud)`~[15.540]
    !>  (series 9 1)
  %+  expect-eq
    !>  `(list @ud)`~[15.540 21.054 25.331]
    !>  (series 9 3)
  %+  expect-eq
    !>  `(list @ud)`~[15.540 21.054 25.331 44.360 44.660 44.733 47.652]
    !>  (series 9 7)
  ==
++  test-series-ten
  ;:  weld
  %+  expect-eq
    !>  `(list @ud)`~[1.568]
    !>  (series 10 1)
  %+  expect-eq
    !>  `(list @ud)`~[1.568 2.835 4.752 5.265 5.439 5.664 5.824]
    !>  (series 10 7)
  %+  expect-eq
    !>  `(list @ud)`~[1.568 2.835 4.752 5.265 5.439 5.664 5.824 5.832 8.526 12.985]
    !>  (series 10 10)
  ==
++  test-series-sixteen
  ;:  weld
  %+  expect-eq
    !>  `(list @ud)`~[1.000 1.134]
    !>  (series 16 2)
  %+  expect-eq
    !>  `(list @ud)`~[1.000 1.134 6.776 15.912 19.624]
    !>  (series 16 5)
  %+  expect-eq
    !>  `(list @ud)`~[1.000 1.134 6.776 15.912 19.624 20.043 20.355 23.946 26.296]
    !>  (series 16 9)
  ==
--
```

##  Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2022.6.  They are made available under both the [MIT license](https://mit-license.org/) and the [CC0 license](https://creativecommons.org/share-your-work/public-domain/cc0).  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_This solution was produced by ~mocmex-pollen.  This code includes the `~_` sigcab error message rune and demonstrates the use of a helper core in a library and shows `^` ket skipping of `$` buc._

**`/lib/rhonda.hoon`**

```hoon
::
::  A library for producing Rhonda numbers and testing if numbers are Rhonda.
::
::    A number is Rhonda if the product of its digits of in base b equals 
::    the product of the base b and the sum of its prime factors.
::    see also: https://mathworld.wolfram.com/RhondaNumber.html
::
=<
::
|%
::  +check: test whether the number n is Rhonda to base b
::
++  check
  |=  [b=@ud n=@ud]
  ^-  ?
  ~_  leaf+"base b must be >= 2"
  ?>  (gte b 2)
  ~_  leaf+"candidate number n must be >= 2"
  ?>  (gte n 2)
  ::
  .=  (roll (base-digits b n) mul)
  %+  mul
    b
  (roll (prime-factors n) add)
::  +series: produce the first n numbers which are Rhonda in base b
::
::    produce ~ if base b has no Rhonda numbers
::
++  series
  |=  [b=@ud n=@ud]
  ^-  (list @ud)
  ~_  leaf+"base b must be >= 2"
  ?>  (gte b 2)
  ::
  ?:  =((prime-factors b) ~[b])
    ~
  =/  candidate=@ud  2
  =+  rhondas=*(list @ud)
  |-
  ?:  =(n 0)
    (flop rhondas)
  =/  is-rhonda=?  (check b candidate)
  %=  $
    rhondas    ?:(is-rhonda [candidate rhondas] rhondas)
    n          ?:(is-rhonda (dec n) n)
    candidate  +(candidate)
  ==
--
::
|%
::  +base-digits: produce a list of the digits of n represented in base b
::
::    This arm has two behaviors which may be at first surprising, but do not
::    matter for the purposes of the ++check and ++series arms, and allow for
::    some simplifications to its implementation.
::    - crashes on n=0
::    - orders the list of digits with least significant digits first
::
::    ex: (base-digits 4 10.206) produces ~[2 3 1 3 3 1 2]
::
++  base-digits
  |=  [b=@ud n=@ud]
  ^-  (list @ud)
  ?>  (gte b 2)
  ?<  =(n 0)
  ::
  |-
  ?:  =(n 0)
    ~
  :-  (mod n b)
  $(n (div n b))
::  +prime-factors: produce a list of the prime factors of n
::    
::    by trial division
::    n must be >= 2
::    if n is prime, produce ~[n]
::    ex: (prime-factors 10.206) produces ~[7 3 3 3 3 3 3 2]
::
++  prime-factors
  |=  [n=@ud]
  ^-  (list @ud)
  ?>  (gte n 2)
  ::
  =+  factors=*(list @ud)
  =/  wheel  new-wheel
  ::  test candidates as produced by the wheel, not exceeding sqrt(n) 
  ::
  |-
  =^  candidate  wheel  (next:wheel)
  ?.  (lte (mul candidate candidate) n)
    ?:((gth n 1) [n factors] factors)
  |-
  ?:  =((mod n candidate) 0)
    ::  repeat the prime factor as many times as possible
    ::
    $(factors [candidate factors], n (div n candidate))
  ^$
::  +new-wheel: a door for generating numbers that may be prime
::
::    This uses wheel factorization with a basis of {2, 3, 5} to limit the
::    number of composites produced. It produces numbers in increasing order
::    starting from 2.
::
++  new-wheel
  =/  fixed=(list @ud)  ~[2 3 5 7]
  =/  skips=(list @ud)  ~[4 2 4 2 4 6 2 6]
  =/  lent-fixed=@ud  (lent fixed)
  =/  lent-skips=@ud  (lent skips)
  ::
  |_  [current=@ud fixed-i=@ud skips-i=@ud]
  ::  +next: produce the next number and the new wheel state
  ::
  ++  next
    |.
    ::  Exhaust the numbers in fixed. Then calculate successive values by
    ::  cycling through skips and increasing from the previous number by
    ::  the current skip-value.
    ::
    =/  fixed-done=?  =(fixed-i lent-fixed)
    =/  next-fixed-i  ?:(fixed-done fixed-i +(fixed-i))
    =/  next-skips-i  ?:(fixed-done (mod +(skips-i) lent-skips) skips-i)
    =/  next
    ?.  fixed-done
      (snag fixed-i fixed)
    (add current (snag skips-i skips))
    :-  next
    +.$(current next, fixed-i next-fixed-i, skips-i next-skips-i)
  --
--
```

**`/gen/rhonda-check.hoon`**

```hoon
::  %say the product of the check arm of /lib/rhonda/hoon
::
/+  *rhonda
::
:-  %say
|=  [* [b=@ud n=@ud ~] *]
^-  [%noun ?]
[%noun (check b n)]
```

**`/gen/rhonda-series.hoon`**

```hoon
::  %say the product of the series arm of /lib/rhonda/hoon
::
/+  *rhonda
::
:-  %say
|=  [* [b=@ud n=@ud ~] *]
^-  [%noun (list @ud)]
[%noun (series b n)]
```

### Solution #2

_This solution was produced by ~ticlys-monlun.  This code demonstrates using a `++map` data structure and a different square-root solution algorithm._

**`/lib/rhonda.hoon`**

```hoon
|%
++  check
  |=  [n=@ud base=@ud]
  ::  if base is prime, automatic no
  ::
  ?:  =((~(gut by (prime-map +(base))) base 0) 0)
    %.n
  ::  if not multiply the digits and compare to base x sum of factors
  ::
  ?:  =((roll (digits [base n]) mul) (mul base (roll (factor n) add)))
    %.y
  %.n
++  series
  |=  [base=@ud many=@ud]
  =/  rhondas  *(list @ud)
  ?:  =((~(gut by (prime-map +(base))) base 0) 0)
    rhondas
  =/  itr  1
  |-
  ?:  =((lent rhondas) many)
    (flop rhondas)
  ?:  =((check itr base) %.n)
    $(itr +(itr))
  $(rhondas [itr rhondas], itr +(itr))
::  digits: gives the list of digits of a number in a base
::
::    We strip digits least to most significant.
::    The least significant digit (lsd) of n in base b is just n mod b.
::    Subtract the lsd, divide by b, and repeat.
::    To know when to stop, we need to know how many digits there are.
++  digits
  |=  [base=@ud num=@ud]
  ^-  (list @ud)
  |-
  =/  modulus=@ud  (mod num base)
  ?:  =((num-digits base num) 1)
    ~[modulus]
  [modulus $(num (div (sub num modulus) base))]
::  num-digits: gives the number of digits of a number in a base
::
::    Simple idea: k is the number of digits of n in base b if and
::    only if k is the smallest number such that b^k > n.
++  num-digits
  |=  [base=@ud num=@ud]
  ^-  @ud
  =/  digits=@ud  1
  |-
  ?:  (gth (pow base digits) num)
    digits
  $(digits +(digits))
::  factor: produce a list of prime factors
::
::    The idea is to identify "small factors" of n, i.e. prime factors less than
::    the square root. We then divide n by these factors to reduce the
::    magnitude of n. It's easy to argue that after this is done, we obtain 1
::    or the largest prime factor.
::
++  factor
  |=  n=@ud
  ^-  (list @ud)
  ?:  ?|(=(n 0) =(n 1))
    ~[n]
  =/  factorization  *(list @ud)
  ::  produce primes less than or equal to root n
  ::
  =/  root  (sqrt n)
  =/  primes  (prime-map +(root))
  ::  itr = iterate; we want to iterate through the primes less than root n
  ::
  =/  itr  2
  |-
  ?:  =(itr +(root))
  ::  if n is now 1 we're done
  ::
    ?:  =(n 1)
      factorization
    ::  otherwise it's now the original n's largest primes factor
    ::
    [n factorization]
  ::  if itr not prime move on
  ::
  ?:  =((~(gut by primes) itr 0) 1)
    $(itr +(itr))
  ::  if it is prime, divide out by the highest power that divides num
  ::
  ?:  =((mod n itr) 0)
    $(n (div n itr), factorization [itr factorization])
  ::  once done, move to next prime
  ::
  $(itr +(itr))
::  sqrt: gives the integer square root of a number
::
::    Yes, this is a square root algorithm I wrote just because.
::    It's based on an algorithm that predates the Greeks:
::    To find the square root of A, think of A as an area.
::    Guess the side of the square x. Compute the other side y = A/x.
::    If x is an over/underestimate then y is an under/overestimate.
::    So (x+y)/2 is the average of an over and underestimate, thus better than x.
::    Repeatedly doing x --> (x + A/x)/2 converges to sqrt(A).
::
::    This algorithm is the same but with integer valued operations.
::    The algorithm either converges to the integer square root and repeats,
::    or gets trapped in a two-cycle of adjacent integers.
::    In the latter case, the smaller number is the answer.
::
++  sqrt
  |=  n=@ud
  =/  guess=@ud  1
  |-
  =/  new-guess  (div (add guess (div n guess)) 2)
  ::  sequence stabilizes
  ::
  ?:  =(guess new-guess)
    guess
  ::  sequence is trapped in 2-cycle
  ::
  ?:  =(guess +(new-guess))
    new-guess
  ?:  =(new-guess +(guess))
    guess
  $(guess new-guess)
::  prime-map: (effectively) produces primes less than a given input
::
::    This is the sieve of Eratosthenes to produce primes less than n.
::    I used a map because it had much faster performance than a list.
::    Any key in the map is a non-prime. The value 1 indicates "false."
::    I.e. it's not a prime.
++  prime-map
  |=  n=@ud
  ^-  (map @ud @ud)
  =/  prime-map  `(map @ud @ud)`(my ~[[0 1] [1 1]])
  ::  start sieving with 2
  ::
  =/  sieve  2
  |-
  ::  if sieve is too large to be a factor we're done
  ::
  ?:  (gte (mul sieve sieve) n)
    prime-map
  ::  if not too large but not prime, move on
  ::
  ?:  =((~(gut by prime-map) sieve 0) 1)
    $(sieve +(sieve))
  ::  sequence: explanation
  ::
  ::    If s is the sieve number, we start sieving multiples
  ::    of s at s^2 in sequence: s^2, s^2 + s, s^2 + 2s, ...
  ::    We start at s^2 because any number smaller than s^2
  ::    has prime factors less than s and would have been
  ::    eliminated earlier in the sieving process.
  ::
  =/  sequence  (mul sieve sieve)
  |-
  ::  done sieving with s once sequence is past n
  ::
  ?:  (gte sequence n)
    ^$(sieve +(sieve))
  ::  if sequence position is known not prime we move on
  ::
  ?:  =((~(gut by prime-map) sequence 0) 1)
    $(sequence (add sequence sieve))
  ::  otherwise we mark position of sequence as not prime and move on
  ::
  $(prime-map (~(put by prime-map) sequence 1), sequence (add sequence sieve))
--
```

**`/gen/rhonda-check.hoon`**

```hoon
/+  *rhonda
:-  %say
|=  [* [n=@ud base=@ud ~] ~]
:-  %noun
(check n base)
```

**`/gen/rhonda-series.hoon`**

```hoon
/+  *rhonda
:-  %say
|=  [* [base=@ud many=@ud ~] ~]
:-  %noun
(series base many)
```

### Solution #3

_This solution was produced by ~tamlut-modnys.  This code demonstrates a clean prime factorization algorithm and the use of `++roll`._

**`/lib/rhonda.hoon`**

```hoon
|%
::
:: check if a given input is a Rhonda number for a given base
::
++  check
  |=  [base=@ud num=@ud]
  ^-  ?
  ?:  (lte base 1)
    !!
  =((roll (get-base-digits base num) mul) (mul base (roll (prime-factors num) add)))
::
:: returns the first n Rhonda numbers in a base or ~ if the base is prime
::
++  series
  |=  [base=@ud n=@ud]
  ^-  (list @ud)
  ?:  (lte base 1)
    !!
  ::  checking if the base is prime.
  ::
  ?:  =((prime-factors base) ~[base])
    ~
  ::  variable for the output
  ::
  =/  result  *(list @ud)
  ::  iteration variable to check if it's a Rhonda number
  ::
  =/  iter  1
  ::  iteration variable in base digit representation as a list, to save time by preventing repeated conversion
  ::
  =/  iterbase  (limo [1 ~])
  :: length variable to prevent repeated calls of lent on the result
  ::
  =/  length  0
  |-
    ::  output if finished
    ::
    ?:  =(length n)
      (flop result)
    ::  check if the current number is a Rhonda number in the base
    ::
    ?:  =((roll iterbase mul) (mul base (roll (prime-factors iter) add)))
      ::  if so add it to the result and check higher
      ::
      $(result [iter result], length +(length), iter +(iter), iterbase (increment-num-in-base iterbase base))
    ::  otherwise just check higher
    ::
    $(iter +(iter), iterbase (increment-num-in-base iterbase base))
::
::  returns the base decomposition of a number as a list of digits
::
++  get-base-digits
  |=  [base=@ud num=@ud]
  ^-  (list @ud)
  ?:  (lte base 1)
    !!
  ::  define the output
  ::
  =/  result  *(list @ud)
  |-
    ::  loop until there are no more digits
    ::
    ?:  =(num 0)
      (flop result)
    =/  division  (dvr num base)
    ::  divide the number by the base, prepend the remainder to the result and loop
    ::
    $(result [q.division result], num p.division)
::
:: returns the prime factorization of a number as a list
::
++  prime-factors
  |=  num=@ud
  ^-  (list @ud)
  ::  define the output
  ::
  =/  result  *(list @ud)
  ::  used to iterate on possible prime factors starting from 2
  ::
  =/  iter  2
  |-
    ::  if the number is 1, there are no more factors
    ::
    ?:  =(num 1)
      result
    ::  divide the number by the current factor, get result and remainder
    ::
    =/  division  (dvr num iter)
    ::  if it divides cleanly, then add the current factor to the list of prime factors and loop on the result
    ::
    ?:  =(q.division 0)
      $(num p.division, result [iter result])
    ::  if the current factor is greater than the square root of the number, then add the number as a factor and terminate
    ::
    ?:  (gth iter p.division)
      [num result]
    :: in all other cases just increment the factor and keep testing
    ::
    $(iter +(iter))
::
::  increments a base decomposition of a number (a list of digits) by 1.
::  this functionality is implemented to speed up the series function and avoid repeated calls to get-base-digits
::
++  increment-num-in-base
  ::  input is a number as a list of digits and a base
  ::
  |=  [num=(list @ud) base=@ud]
  ^-  (list @ud)
  ::  length variable to avoid repeated calls to lent
  ::
  =/  length  (lent num)
  ::  iterate to potentially carry a digit when adding
  ::
  =/  index  0
  |-
    ::  if we carry a digit to the end (e.g. 999 + 1) then append a 1
    ::
    ?:  =(index length)
      (snoc num 1)
    ::  incrementation
    ::
    =/  num  (snap num index (add (snag index num) 1))
    ::  if we need to carry a digit
    ::
    ?:  (gte (snag index num) base)
      ::  then make the current digit 0 and loop
      ::
      $(index +(index), num (snap num index 0))
    :: otherwise return the incremented number
    ::
    num
--
```

**`/gen/rhonda-check.hoon`**

```hoon
::  say generator that calls the check function to see if a number is a Rhonda number
::
/+  rhonda
:-  %say
|=  [* [base=@ud n=@ud ~] *]
:-  %noun
(check:rhonda [base n])
```

**`/gen/rhonda-series.hoon`**

```hoon
::  say generator that calls the series function to get the first n Rhonda numbers in a base
::
/+  rhonda
:-  %say
|=  [* [base=@ud n=@ud ~] *]
:-  %noun
(series:rhonda [base n])
```

### Solution #4

_This solution was produced by ~sidnym-ladrut.  This code demonstrates using multiple cores in a library._

**`/lib/rhonda.hoon`**

```hoon
::  rhonda number validator/generator
::  https://www.numbersaplenty.com/set/Rhonda_number/
::
|%
  ++  as-base                     :: convert n to base b
    |=  [b=@ud n=@ud]
    ^-  (list @ud)
    =+  p=(log-base b n)
    =|  l=(list @ud)
    |-
    ?:  =(p 0)
      [n l]
    =+  btop=(pow b p)
    =+  next=(div n btop)
    $(p (dec p), n (sub n (mul next btop)), l [next l])
  ++  log-base                    :: b-based unsigned log of value n
    |=  [b=@ud n=@ud]
    ^-  @ud
    =+  p=1
    |-
    ?:  (lth n (pow b p))
      (dec p)
    $(p +(p))
  ++  prime-factors               :: prime number factors of n
    |=  n=@ud
    ^-  (list @ud)
    ~+
    =|  l=(list @ud)
    =/  i=@ud  2
    |-
    ?:  (gth i -:(sqt n))
      ?:  (gth n 2)
        [n l]
      l
    |-
    ?:  !=((mod n i) 0)
      ^$(i +(i))
    $(n (div n i), l [i l])
  ++  is-prime                    :: is given @ud a prime number?
    |=  n=@ud
    ^-  bean
    ~+
    ?:  (lte n 1)  %.n
    ?:  (lte n 3)  %.y
    %+  levy  (gulf 2 -:(sqt n))
    |=(i=@ud !=((mod n i) 0))
--
::
|%
  ++  check                       :: check if n is rhonda in base b
    :: rhonda(b, n) := Π_digits(n_b) == b * Σ_values(prime-factors(n))
    |=  [b=@ud n=@ud]
    ^-  bean
    :: https://mathworld.wolfram.com/RhondaNumber.html
    :: "Rhonda numbers exist only for bases that are composite since
    :: there is no way for the product of integers less than a prime b
    :: to have b as a factor."
    ?:  (is-prime b)
      %.n
    =+  baseb=(as-base b n)
    =+  facts=(prime-factors n)
    .=  (roll baseb mul)
    (mul b (roll facts add))
  ++  series                      :: list first n rhondas of base b
    |=  [b=@ud n=@ud]
    ^-  (list @ud)
    =|  l=(list @ud)
    =/  i=@ud  2
    =/  c=@ud  0
    ?:  (is-prime b)
      l
    |-
    ?:  =(c n)
      (flop l)
    ?.  (check b i)
      $(i +(i))
    $(i +(i), c +(c), l [i l])
```

**`/gen/rhonda-check.hoon`**

```hoon
/+  *rhonda
:-  %say
|=  [* [n=@ud ~] ~]
:-  %noun
^-  bean
:: 4 is the minimum rhonda base (lowest non-prime integer).
:: n is *a* maximum because n != n * (v >= 2), but likely not the best maximum.
?&  (gte n 4)
  %+  lien  (gulf 4 n)
  |=  b=@ud
  ^-  bean
  (check b n)
==
```

**`/gen/rhonda-series.hoon`**

```hoon
/+  *rhonda
:-  %say
|=  [* [b=@ud n=@ud ~] ~]
:-  %noun
^-  (list @ud)
(series b n)
```


# roman.md

---

+++
title = "Roman Numerals"
weight = 40
+++

## Challenge: Printing and Parsing Roman Numerals

Roman numerals constitute a numeral system capable of expressing positive integers by additive values (rather than place-number notation).  Additive series are produced by summing values in a series, as `iii` → 3, while subtractive values are produced by prepending certain smaller values ahead of a larger value, as `ix` → 9.

- Produce a library which converts to and from Roman numeral representations according to the standard values:

    | Character | Value |
    | --------- | ----- |
    | `i` | 1 |
    | `v` | 5 |
    | `x` | 10 |
    | `l` | 50 |
    | `c` | 100 |
    | `d` | 500 |
    | `m` | 1,000 |

    There are many incorrect formulations, as `iix` → 8 or `id` → 499, and the code is not expected to parse these “correctly”.  (It should not produce them!)  However, both `iv` and `iiii` are frequently used to represent 4 (e.g. look at a clock face), so you should support this variation.

    For this task, produce two files:

    - `/lib/roman/hoon`

        Your library `/lib/roman/hoon` should expose two arms:

        - `++parse` accepts a `tape` text string containing a Roman numeral expression in lower or upper case and returns the corresponding `@ud` unsigned decimal value.  On failure to parse, call `!!` zapzap.
        - `++yield` accepts a `@ud` unsigned decimal value and returns the corresponding `tape` text string in lower case.

    - `/gen/roman/hoon`

        Provide a `%say` generator at `/gen/roman/hoon` which accepts a `tape` text string or a `@ud` unsigned decimal value and performs the appropriate conversion on the basis of the sample's type.

        **Note**:  This design pattern is not optimal since analysis over a union of some types can be difficult to carry out, and it would be better to either separate the generators or use a flag.  In this case, the pattern works because we are distinguishing an atom from a cell.

## Unit Tests

Following a principle of test-driven development, we compose a series of tests which allow us to rigorously check for expected behavior.

```hoon
/+  *test, *roman
|%
++  test-output-one
  =/  src  "i"
  =/  trg  1
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-two
  =/  src  "ii"
  =/  trg  2
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-three
  =/  src  "iii"
  =/  trg  3
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-four
  =/  src  "iv"
  =/  trg  4
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-four-var
  =/  src  "iiii"
  =/  trg  4
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-five
  =/  src  "v"
  =/  trg  5
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-six
  =/  src  "vi"
  =/  trg  6
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-seven
  =/  src  "vii"
  =/  trg  7
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-eight
  =/  src  "viii"
  =/  trg  8
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-nine
  =/  src  "ix"
  =/  trg  9
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-ten
  =/  src  "x"
  =/  trg  10
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-eleven
  =/  src  "xi"
  =/  trg  11
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-twelve
  =/  src  "xii"
  =/  trg  12
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-thirteen
  =/  src  "xiii"
  =/  trg  13
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-fourteen
  =/  src  "xiv"
  =/  trg  14
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-fifteen
  =/  src  "xv"
  =/  trg  15
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-sixteen
  =/  src  "xvi"
  =/  trg  16
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-seventeen
  =/  src  "xvii"
  =/  trg  17
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-eighteen
  =/  src  "xviii"
  =/  trg  18
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-nineteen
  =/  src  "xix"
  =/  trg  19
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-twenty
  =/  src  "xx"
  =/  trg  20
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-twenty-three
  =/  src  "xxiii"
  =/  trg  23
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-twenty-five
  =/  src  "xxv"
  =/  trg  25
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-twenty-seven
  =/  src  "xxvii"
  =/  trg  27
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-thirty-one
  =/  src  "xxxi"
  =/  trg  31
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-thirty-nine
  =/  src  "xxxix"
  =/  trg  39
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-forty-two
  =/  src  "xlii"
  =/  trg  42
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-forty-nine
  =/  src  "xlix"
  =/  trg  49
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-fifty
  =/  src  "l"
  =/  trg  50
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-sixty-two
  =/  src  "lxii"
  =/  trg  62
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-seventy-eight
  =/  src  "lxxviii"
  =/  trg  78
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-ninety-four-var
  =/  src  "xciiii"
  =/  trg  94
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-one-hundred
  =/  src  "c"
  =/  trg  100
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-one-hundred-thirty-three
  =/  src  "cxxxiii"
  =/  trg  133
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-four-hundred-ninety-nine
  =/  src  "cdxcix"
  =/  trg  499
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-five-hundred
  =/  src  "d"
  =/  trg  500
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-five-hundred-forty-eight
  =/  src  "dxlviii"
  =/  trg  548
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-six-hundred-sixty-nine
  =/  src  "dclxix"
  =/  trg  669
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-eight-hundred-eighty-eight
  =/  src  "dccclxxxviii"
  =/  trg  888
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-nine-hundred-ninety-nine
  =/  src  "cmxcix"
  =/  trg  999
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-one-thousand
  =/  src  "m"
  =/  trg  1.000
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-one-thousand-nine-hundred-ninety-nine
  =/  src  "mcmxcix"
  =/  trg  1.999
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-two-thousand-twenty-two
  =/  src  "mmxxii"
  =/  trg  2.022
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-output-three-thousand-nine-hundred-ninety-nine
  =/  src  "mmmcmxcix"
  =/  trg  3.999
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (parse src)
  %+  expect-eq
    !>  trg
    !>  (parse (cuss src))
  ==
++  test-input-one
  =/  trg  "i"
  =/  src  1
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-two
  =/  trg  "ii"
  =/  src  2
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-three
  =/  trg  "iii"
  =/  src  3
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-four
  =/  trg  "iv"
  =/  src  4
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-five
  =/  trg  "v"
  =/  src  5
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-six
  =/  trg  "vi"
  =/  src  6
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-seven
  =/  trg  "vii"
  =/  src  7
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-eight
  =/  trg  "viii"
  =/  src  8
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-nine
  =/  trg  "ix"
  =/  src  9
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-ten
  =/  trg  "x"
  =/  src  10
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-eleven
  =/  trg  "xi"
  =/  src  11
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-twelve
  =/  trg  "xii"
  =/  src  12
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-thirteen
  =/  trg  "xiii"
  =/  src  13
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-fourteen
  =/  trg  "xiv"
  =/  src  14
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-fifteen
  =/  trg  "xv"
  =/  src  15
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-sixteen
  =/  trg  "xvi"
  =/  src  16
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-seventeen
  =/  trg  "xvii"
  =/  src  17
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-eighteen
  =/  trg  "xviii"
  =/  src  18
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-nineteen
  =/  trg  "xix"
  =/  src  19
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-twenty
  =/  trg  "xx"
  =/  src  20
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-twenty-three
  =/  trg  "xxiii"
  =/  src  23
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-twenty-five
  =/  trg  "xxv"
  =/  src  25
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-twenty-seven
  =/  trg  "xxvii"
  =/  src  27
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-thirty-one
  =/  trg  "xxxi"
  =/  src  31
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-thirty-nine
  =/  trg  "xxxix"
  =/  src  39
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-forty-two
  =/  trg  "xlii"
  =/  src  42
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-forty-nine
  =/  trg  "xlix"
  =/  src  49
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-fifty
  =/  trg  "l"
  =/  src  50
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-sixty-two
  =/  trg  "lxii"
  =/  src  62
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-seventy-eight
  =/  trg  "lxxviii"
  =/  src  78
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-one-hundred
  =/  trg  "c"
  =/  src  100
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-one-hundred-thirty-three
  =/  trg  "cxxxiii"
  =/  src  133
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-four-hundred-ninety-nine
  =/  trg  "cdxcix"
  =/  src  499
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-five-hundred
  =/  trg  "d"
  =/  src  500
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-five-hundred-forty-eight
  =/  trg  "dxlviii"
  =/  src  548
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-six-hundred-sixty-nine
  =/  trg  "dclxix"
  =/  src  669
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-eight-hundred-eighty-eight
  =/  trg  "dccclxxxviii"
  =/  src  888
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-nine-hundred-ninety-nine
  =/  trg  "cmxcix"
  =/  src  999
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-one-thousand
  =/  trg  "m"
  =/  src  1.000
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-one-thousand-nine-hundred-ninety-nine
  =/  trg  "mcmxcix"
  =/  src  1.999
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-two-thousand-twenty-two
  =/  trg  "mmxxii"
  =/  src  2.022
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
++  test-input-three-thousand-nine-hundred-ninety-nine
  =/  trg  "mmmcmxcix"
  =/  src  3.999
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (yield src)
  ==
--
```

## Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2022.6.  They are made available under both the [MIT license](https://mit-license.org/) and the [CC0 license](https://creativecommons.org/share-your-work/public-domain/cc0).  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_This solution was produced by ~sidnym-ladrut.  This code utilizes the Hoon parser tools like `++cook` and `++scan`, and in particular illustrates a strong ethic of [function encapsulation](https://en.wikipedia.org/wiki/Encapsulation_%28computer_programming%29)._

**`/lib/roman.hoon`**

```hoon
::  roman: roman numeral conversion library
::
=<
::  public core
|%
::  +parse: given a roman numeral, produce the equivalent arabic numeral
::
++  parse
  |=  roman=tape
  ^-  @ud
  ~|  'Input numeral has invalid syntax.'
  ?>  !=((lent roman) 0)
  |^  %+  scan  (cass roman)
      %+  cook  sum-up
      ;~  plug
        (parse-just (pow 10 3) 0 3)
        (parse-base (pow 10 2) 3)
        (parse-base (pow 10 1) 3)
        (parse-base (pow 10 0) 4)
        (easy ~)
      ==
  ::  +sum-up: sum up the contents of a given list
  ::
  ++  sum-up
    |=  l=(list @)
    (roll l add)
  ::  +parse-just: parse just the roman equivalent of given arabic [range] times
  ::
  ++  parse-just
    |=  [value=@ud range=[@ud @ud]]
    %+  cook  sum-up
    %+  stun  range
    %+  cold  value
    (jest (~(got by glyph-map) value))
  ::  +parse-base: parse the roman base of given base-10 arabic [0, reps] times
  ::
  ::    This function parses the *contextualized* roman base equivalent of a
  ::    given base-10 arabic value up to a given number of times. Crucially,
  ::    this applies roman numeral contextual rules, such as numeral ordering
  ::    and subtraction rules (e.g. iv=4, ix=9, id=invalid, etc.), to the given
  ::    base. In concrete terms, this means enforcing the following regex:
  ::
  ::    ```
  ::    R: Reps | N: Next (B*10)
  ::    B: Base | H: Half (B*5)
  ::
  ::    (BN|BH|H?B{0,R})
  ::    ```
  ::
  ++  parse-base
    |=  [base=@ud reps=@ud]
    =+  next=(mul base 10)
    =+  half=(mul base 5)
    ;~  pose
      (parse-just (sub next base) 1 1)
      (parse-just (sub half base) 1 1)
      %+  cook  sum-up
      ;~  plug
        (parse-just half 0 1)
        (parse-just base 0 reps)
        (easy ~)
      ==
      (easy 0)
    ==
  --
::  +yield: given an arabic numeral, produce the equivalent roman numeral
::
++  yield
  |=  arabic=@ud
  ^-  tape
  ~|  'Input value is out of range (valid range: [1, 3.999]).'
  ?>  &((gth arabic 0) (lth arabic 4.000))
  =<  +>
  %^  spin  glyph-list  [arabic ""]
  |=  [n=[@ud @t] a=[@ud tape]]
  ?:  (lth -.a -.n)  [n a]
  $(a [(sub -.a -.n) (weld +.a (trip +.n))])
--
::  private core
|%
::  +glyph-map: map of arabic glyphs to their roman equivalents
::
++  glyph-map
  ^-  (map @ud @t)
  (malt glyph-list)
::  +glyph-list: list of pairs of equivalent [arabic roman] glyphs
::
++  glyph-list
  ^-  (list [@ud @t])
  :~  :-  1.000   'm'
      :-  900    'cm'
      :-  500     'd'
      :-  400    'cd'
      :-  100     'c'
      :-  90     'xc'
      :-  50      'l'
      :-  40     'xl'
      :-  10      'x'
      :-  9      'ix'
      :-  5       'v'
      :-  4      'iv'
      :-  1       'i'
  ==
--
```

**`/gen/roman.hoon`**

```hoon
::  +roman: given arabic or roman numeral, produce the opposite
::
::    +roman @ud
::      given arabic numeral, generate roman equivalent
::    +roman tape
::      given roman numeral, generate arabic equivalent
::
/+  *roman
::
:-  %say
|=  [* [i=?(@ud tape) ~] ~]
:-  %noun
^-  ?(@ud tape)
?-  i
  ~   (parse i)
  @   (yield i)
  ^   (parse i)
==
```

### Solution #2

_This solution was produced by ~mocmex-pollen.  It particularly illustrates the use of `++cook` and `++pose` in constructing a parser-based solution._

**`/lib/roman.hoon`**

```hoon
::
::  A library for parsing and producing Roman numeral expressions.
::
=<
::
|%
::  +parse: produce the value of a Roman numeral expression
::
++  parse
  |=  expression=tape
  ^-  @ud
  %+  scan
    (cass expression)
  %-  full
  ;~  (comp |=([a=@ud b=@ud] (add a b)))
    (cook roman-value-unit (punt (numeral-rule %m)))
    (cook roman-value-unit (punt (numeral-rule %d)))
    (cook roman-value-unit (punt (numeral-rule %c)))
    (cook roman-value-unit (punt (numeral-rule %l)))
    (cook roman-value-unit (punt (numeral-rule %x)))
    (cook roman-value-unit (punt (numeral-rule %v)))
    (cook roman-value-unit (punt (numeral-rule %i)))
  ==
::  +yield: produce the Roman numeral for a given value
::
++  yield
  |=  n=@ud
  ^-  tape
  ?>  (gte n 1)
  ::
  =/  options  numerals-and-subtractives
  =/  final  *tape
  |-
  ?:  =(n 0)
    final
  ?~  options
    !!
  =/  roman=tape  -.i.options
  =/  value=@ud  +.i.options
  =/  expression=tape  (zing (reap (div n value) roman))
  %=  $
    n        (mod n value)
    options  t.options
    final    (weld final expression)
  ==
--
::
|%  
::  +numeral-rule: match valid sequences that begin with the given numeral
::
++  numeral-rule
  |=  numeral=?(%i %v %x %l %c %d %m)
  ?-  numeral
    %i  ;~(pose (jest 'iiii') (jest 'iii') (jest 'ii') (jest 'iv') (jest 'ix') (just 'i'))
    %v  (just 'v')
    %x  ;~(pose (jest 'xxx') (jest 'xx') (jest 'xc') (jest 'xl') (just 'x'))
    %l  (just 'l')
    %c  ;~(pose (jest 'ccc') (jest 'cc') (jest 'cm') (jest 'cd') (just 'c'))
    %d  (just 'd')
    %m  ;~(pose (jest 'mmm') (jest 'mm') (just 'm'))
  ==
::  +roman-value-unit: 0 if the unit is empty otherwise ++roman-value
::
++  roman-value-unit
  |=  roman=(unit @t)
  ^-  @ud
  ?~  roman
    0
  (roman-value (trip u.roman))
::  +roman-value: produce the value of a simple expression
::
::    "Simple" here means a single numeral, an additive series or 
::    a subtractive pair. ex: "i", "ii", "iv" but not "xi"
:: 
::    Caution: this will produce a value for an invalid Roman numeral and
::    a wrong value for "complex" expressions.
::
++  roman-value
  |=  roman=tape
  ^-  @ud
  ?~  roman
    !!
  ::
  =/  value-map  (malt numerals-and-subtractives)
  %+  fall
    ::  roman is a single numeral or a subtractive
    ::
    (~(get by value-map) roman)
  ::  roman is an additive series
  ::
  %+  mul
    (lent roman)
  (~(got by value-map) (trip i.roman))
::  +numerals-and-subtractives: a list of pairs of single numerals 
::  and valid subtractive pairs in descending order of value
::
++  numerals-and-subtractives
  ^-  (list [tape @ud])
  :~  ["m" 1.000]
      ["cm" 900]
      ["d" 500]
      ["cd" 400]
      ["c" 100]
      ["xc" 90]
      ["l" 50]
      ["xl" 40]
      ["x" 10]
      ["ix" 9]
      ["v" 5]
      ["iv" 4]
      ["i" 1]
  ==
--
```

**`/gen/roman.hoon`**

```hoon
::
::  %say the product of the conversion to/from a Roman numeral expression
::
::    The direction of conversion is determined by the type of the input.
::    tape -> Roman numeral expression to a quantity
::    @ud -> quantity to a Roman numeral expression
::
/+  *roman
::
:-  %say
::  caution - the type union in this spec is sensitive to the order of
::  its arguments: ?(tape @ud) results in fish-loop
::
|=  [* [value=?(@ud tape) ~] *]
^-  [%noun ?(@ud tape)]
:-  %noun
?:  ?=(@ud value)
  (yield value)
(parse value)
```

### Solution #3

_This solution was produced by ~mashex-masrex.  Notice how it utilizes a well-structured parser based on `++jest` and `++cold`._

**`/lib/roman.hoon`**

```hoon
::  Convert Roman numerals to Arabic numbers, or vice versa.
::
|%
::  +parse: accept a tape containing a roman numeral and produce the number
::
++  parse
  |=  numeral=tape  ^-  @ud
  ::  (the sum of arabic numbers that are found in the roman numeral)
  ::
  |^  (roll (scan (cuss numeral) (star as-arabic)) add)
  ::  +as-arabic: convert numeral characters into their numeric value
  ::
  ++  as-arabic
    ;~  pose
      (cold 4 (jest 'IV'))
      (cold 9 (jest 'IX'))
      (cold 1 (just 'I'))
      (cold 5 (just 'V'))
      (cold 40 (jest 'XL'))
      (cold 90 (jest 'XC'))
      (cold 10 (just 'X'))
      (cold 50 (just 'L'))
      (cold 400 (jest 'CD'))
      (cold 900 (jest 'CM'))
      (cold 100 (just 'C'))
      (cold 500 (just 'D'))
      (cold 1.000 (just 'M'))
    ==
  --
::  +yield: accept a decimal number and produce the corresponding roman numeral
::
++  yield
  |=  number=@ud  ^-  tape
  :: if, number is zero
  ::
  ?:  =(0 number)
    ::  then, end the list (i.e. conclude the tape)
    ::
    ~
  ::  else, if, number is one-thousand or greater
  ::
  ?:  (gte number 1.000)
    ::  then, append "m", and recurse subtracting one-thousand
    ::
    :-  'm'
    $(number (sub number 1.000))
  ::  else, if, number is nine-hundred or greater
  ::
  ?:  (gte number 900)
    ::  then, append "cm", and recurse subtracting nine-hundred
    ::
    :-  'c'  :-  'm'
    $(number (sub number 900))
  ::  else, if, number is five-hundred or greater
  ::
  ?:  (gte number 500)
    ::  then, append "d", and recurse subtracting five-hundred
    ::
    :-  'd'
    $(number (sub number 500))
  ::  else, if, number is four-hundred or greater
  ::
  ?:  (gte number 400)
    ::  then, append "cd", and recurse subtracting four-hundred
    ::
    :-  'c'  :-  'd'
    $(number (sub number 400))
  ::  else, if, number is one-hundred or greater
  ::
  ?:  (gte number 100)
    ::  then, append "c", and recurse subtracting one-hundred
    ::
    :-  'c'
    $(number (sub number 100))
  ::  else, if, number is ninety or greater
  ::
  ?:  (gte number 90)
    ::  then, append "xc", and recurse subtracting ninety
    ::
    :-  'x'  :-  'c'
    $(number (sub number 90))
  ::  else, if, number is fifty or greater
  ::
  ?:  (gte number 50)
    ::  then, append "l", and recurse subtracting fifty
    ::
    :-  'l'
    $(number (sub number 50))
  ::  else, if, number is forty or greater
  ::
  ?:  (gte number 40)
    ::  then, append "xl", and recurse subtracting forty
    ::
    :-  'x'  :-  'l'
    $(number (sub number 40))
  ::  else, if, number is ten or greater
  ::
  ?:  (gte number 10)
    ::  then, append "x", and recurse subtracting ten
    ::
    :-  'x'
    $(number (sub number 10))
  ::  else, if, number is nine or greater
  ::
  ?:  (gte number 9)
    ::  then, append "ix", and recurse subtracting nine
    ::
    :-  'i'  :-  'x'
    $(number (sub number 9))
  ::  else, if, number is five or greater
  ::
  ?:  (gte number 5)
    ::  then, append "v", and recurse subtracting five
    ::
    :-  'v'
    $(number (sub number 5))
  ::  else, if, number is four or greater
  ::
  ?:  (gte number 4)
    ::  then, append "iv", and recurse subtracting four
    ::
    :-  'i'  :-  'v'
    $(number (sub number 4))
  ::  else, append "i", and recurse subtracting one
  ::
  :-('i' $(number (sub number 1)))
--
```

**`/gen/roman.hoon`**

```hoon
::  roman: Convert Roman numerals to Arabic numbers, or vice versa.
::
/+  *roman
:-  %say
|=  [* [arabic-or-roman=$@(@ud tape) ~] ~]
:-  %noun
::  if, arabic-or-roman is null
::
?~  arabic-or-roman
  ::  then, produce zero
  0
::  else, if, arabic-or-roman is a cell
::
?^  arabic-or-roman
  ::  then, parse the tape of roman numerals
  ::
  (parse arabic-or-roman)
::  else, produce a roman numeral from the arabic number
::
(yield arabic-or-roman)
```

### Solution #4

_This solution was produced by ~fonnyx-nopmer.  It comes sans comments, and particularly demonstrates how to produce legible and idiomatic Hoon code without requiring comments._

**`/lib/roman.hoon`**

```hoon
|%
++  parse
  |=  t=tape  ^-  @ud
  =.  t  (cass t)
  =|  result=@ud
  |-
  ?~  t  result
  ?~  t.t  (add result (from-numeral i.t))
  =+  [a=(from-numeral i.t) b=(from-numeral i.t.t)]
  ?:  (gte a b)  $(result (add result a), t t.t)
  $(result (sub (add result b) a), t t.t.t)
++  yield
  |=  n=@ud  ^-  tape
  =|  result=tape
  =/  values  to-numeral
  |-
  ?~  values  result
  ?:  (gte n -.i.values)
    $(result (weld result +.i.values), n (sub n -.i.values))
  $(values t.values)
++  from-numeral
  |=  c=@t  ^-  @ud
  ?:  =(c 'i')  1
  ?:  =(c 'v')  5
  ?:  =(c 'x')  10
  ?:  =(c 'l')  50
  ?:  =(c 'c')  100
  ?:  =(c 'd')  500
  ?:  =(c 'm')  1.000
  !!
++  to-numeral
  ^-  (list [@ud tape])
  :*
    [1.000 "m"]
    [900 "cm"]
    [500 "d"]
    [400 "cd"]
    [100 "c"]
    [90 "xc"]
    [50 "l"]
    [40 "xl"]
    [10 "x"]
    [9 "ix"]
    [5 "v"]
    [4 "iv"]
    [1 "i"]
    ~
  ==
--
```

**`/gen/roman.hoon`**

```hoon
/+  *roman
:-  %say
|=  [* [x=$%([%from-roman tape] [%to-roman @ud]) ~] ~]
:-  %noun
^-  tape
?-  -.x
  %from-roman  "{<(parse +.x)>}"
  %to-roman  (yield +.x)
==
```


# solitaire.md

---

+++
title = "Solitaire Cipher"
weight = 50
+++

## Challenge: Solitaire Encryption Cipher

The [Solitaire or Pontifex algorithm](https://en.wikipedia.org/wiki/Solitaire_%28cipher%29) is a cryptographic algorithm designed by cryptographer [Bruce Schneier](https://www.schneier.com/academic/solitaire/) based on coordinating two decks of cards so that they can be used to communicate between two field agents.  Given a standard deck of 52 playing cards and two distinguishable jokers, a message may be encrypted as a keystream, or sequence of values combined with the message to encrypt or decrypt it.  The algorithm features prominently in Neal Stephenson's novel _Cryptonomicon_.

Playing cards are conventionally numbered as clubs (1–13); diamonds (14–26); hearts (27–39); and spades (40–52).  The two jokers (53 and 54) are used to track the position of variables in the keystream.

Per Wikipedia:

> To encrypt a message:
>
> 1.  Remove all punctuation and spaces, leaving only the 26 letters A–Z.
> 2.  Convert each letter to its natural numerical value, A = 1, B = 2, ..., Z = 26.
> 3.  Generate one keystream value for each letter in the message using the keystream algorithm below.
> 4.  Add each keystream value to the corresponding plaintext number, subtracting 26 if the resulting value is greater than 26. (In mathematics this is called [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic "Modular arithmetic").)
> 5.  Convert the resulting numbers back to letters. This sequence of letters is the [ciphertext](https://en.wikipedia.org/wiki/Ciphertext "Ciphertext").
>
> To decrypt a ciphertext:
>
> 1.  Convert each letter in the ciphertext to its natural numerical value.
> 2.  Generate one keystream value for each letter in the ciphertext.
> 3.  Subtract each keystream value from the corresponding ciphertext value, adding 26 if the resulting value is less than 1.
> 4.  Convert the resulting numbers back to letters.

The keystream algorithm generates the overall value by moving cards within the deck.  The algorithm is deterministic, which means that the values depend on the initial order of the deck (and thus why two decks are necessary).  The deck is circular (a card moved past the bottom cycles back in at the top and vice versa).

The mesage is converted to ALLUPPERCASE, conventionally in groups of five:  ALLUP PERCA SEXXX.

To generate one character:

> 1.  Locate the A joker (value 27) and move it down the deck by one place. If it is the last card, it becomes the second card. There is no way for it to become the first card.
> 2.  Locate the B joker (value 28) and move it down the deck by two places. Notice that if it is the second to last card, it becomes the second card by wrapping around. If it is the last card, it becomes the third card. There is no way for it to become the first card.
> 3.  Perform a "triple cut": split the deck into three sections. Everything above the top joker (which, after several repetitions, may not necessarily be the A joker) and everything below the bottom joker will be exchanged. The jokers themselves, and the cards between them, are left untouched.
> 4.  Perform a "count cut": observe the value of the card at the bottom of the deck. If the card is either joker take its value to be 27. Remove that number of cards from the top of the deck and insert them just above the last card in the deck.
> 5.  Now, look at the value of the top card. Again, either joker counts as 27. Count this many places below that card and take the value of that card as the next value in the keystream. If the card counted to is either joker, ignore it and repeat the keystream algorithm. In this example the top card is 23, so we count to the 24th card, which is 11; thus the keystream value is 11. (Note that no cards change places in this step, this step simply determines the keystream value).

The foregoing hyperlinks showcase worked examples of Solitaire in action.


## Solutions

_This solution was produced by ~rabsef-bicrym.  It is made available under the [GNU GPL](https://github.com/rabsef-bicrym/urbitasofia/blob/master/LICENSE).  (Note that this is different from the other code snippets on this site, which are made available under the [MIT license](https://mit-license.org/)._

The following Hoon generator can be used to encrypt a message with a default or custom deck.  With the default deck:

```hoon
> +pontifex "hello" %encode  
"eek`z"

> +pontifex "eek`z" %decode  
"hello"
```

A custom deck would look like `~[5 31 4 51 ...]` for all 54 values in a specified or random order.  One could compose a `shuffle` gate to randomize card order within that range:

```hoon {% copy=true %}
|=  [count=@ud eny=@uvJ]
^-  (list @ud)
=/  rng  ~(. og eny)
=/  index  1
=/  deck  (gulf 1 count)
|-  ^-  (list @ud)
?:  =(index count)  deck
=^  other  rng  (rads:rng count)
=/  value  (snag other deck)
%=  $
  index  +(index)
  deck   (snap (snap deck (dec index) value) other (snag (dec index) deck))
==
```

and invoke this as

```hoon {% copy=true %}
+pontifex "hello" %encode, =customdeck (shuffle 52 eny)
```

The generator will print the deck, so you can recover the random deck as needed.

E.g., for a given starting deck:

```hoon
> +pontifex "hello" %encode, =customdeck ~[30 41 7 39 31 23 20 12 48 36 16 24 33 5 4 14 38 43 28 32 6 44 8 10 3 35 50 1 2 18 21 37 42 53 52 27 46 15 13 29 34 26 11 40 49 45 54 19 51 9 25 17 22 47]
"rduqh"

> +pontifex "rduqh" %decode, =customdeck ~[30 41 7 39 31 23 20 12 48 36 16 24 33 5 4 14 38 43 28 32 6 44 8 10 3 35 50 1 2 18 21 37 42 53 52 27 46 15 13 29 34 26 11 40 49 45 54 19 51 9 25 17 22 47]
"hello"
```

**`/gen/pontifex.hoon`**

```hoon {% copy=true mode="collapse" %}
!:
:-  %say
|=  [[now=@da eny=@uvJ bec=beak] [incometape=tape action=@tas ~] [customdeck=(list @ud) ~]]
:-  %noun
|^
=/  tempvaltape=(list @ud)  (convert incometape)
=/  swapdeck=deckform  ?~(customdeck deckbuilder (customdeckbuilder customdeck))
=/  tempvalcard=@ud  `@ud`(keystreamcard (findoperant (triplecut (jokerbfunc (jokerafunc swapdeck)))))
=/  passone=@ud  0
=|  numencodemsg=(list @ud)
^-  tape
|-
?~  tempvaltape
  (alphashift numencodemsg)
%=  $
  tempvalcard  `@ud`(keystreamcard (findoperant (triplecut (jokerbfunc (jokerafunc (findoperant (triplecut (jokerbfunc (jokerafunc swapdeck)))))))))
  numencodemsg  [?:(=(%encode action) (add i.tempvaltape tempvalcard) ?:((gte tempvalcard i.tempvaltape) (sub (add 26 i.tempvaltape) ?:((gth tempvalcard 26) (mod tempvalcard 26) tempvalcard)) (sub i.tempvaltape ?:((gth tempvalcard 26) (mod tempvalcard 26) tempvalcard)))) numencodemsg]
  tempvaltape  t.tempvaltape
  swapdeck  `deckform`(findoperant (triplecut (jokerbfunc (jokerafunc swapdeck))))
==
+$  suits  ?(%heart %spade %club %diamond %joker)
+$  value  ?(%ace %1 %2 %3 %4 %5 %6 %7 %8 %9 %10 %jack %queen %king %a %b)
+$  card  ?([s=suits v=value])
+$  deckform  (list card)
++  suitlist  `(list suits)`~[%club %heart %spade %diamond]
++  suitpoints
  ^-  (map suits @ud)
  %-  my
  :~  :-  %club  0
      :-  %diamond  13
      :-  %heart  26
      :-  %spade  39
  ==
++  valuelist  `(list value)`~[%ace %2 %3 %4 %5 %6 %7 %8 %9 %10 %jack %queen %king]
++  valuepoints
  =/  valuepl=(list value)  valuelist
  =/  counter=@ud  1
  =|  valuemap=(map value @ud)
  |-  ^-  (map value @ud)
  ?~  valuepl
    valuemap
  $(valuemap (~(put by valuemap) i.valuepl counter), valuepl t.valuepl, counter +(counter))
++  deckbuilder
::  This deck's head is the bottom card in the deck, if using a physical deck
::  We recommend doing the manipulations with cards face up, if using a physical deck
::  Assuming the two above, your physical deck's top card (facing you) should be the Ace of Diamonds
::
  =/  deckvalue=(list value)  valuelist
  =/  decksuit=(list suits)  (flop suitlist)
  =|  deck=(list card)
  |-  ^-  deckform
  ?~  decksuit
    (into (into deck 13 `card`[%joker %a]) 27 `card`[%joker %b])
  ?~  deckvalue
    $(decksuit t.decksuit, deckvalue valuelist)
  $(deck [[i.decksuit i.deckvalue] deck], deckvalue t.deckvalue)
++  convert
  |=  msg=tape
  =.  msg  (cass msg)
  ^-  (list @ud)
  %+  turn  msg
  |=  a=@t
  (sub `@ud`a 96)
++  cardtovalue
  |=  crd=card
  ^-  @ud
  =/  suitpt=(map suits @ud)  suitpoints
  =/  valuept=(map value @ud)  valuepoints
  ?:  =(s.crd %joker)
      53
  (add (~(got by suitpt) s.crd) (add 1 (~(got by valuept) v.crd)))
++  jokerafunc
  |=  incomingdeck1=deckform
  ^-  deckform
  =/  startera  (find [%joker %a]~ incomingdeck1)
  =/  posita=@ud  ?~(startera ~|("No Joker A in Deck" !!) ?:(=(0 u.startera) 100 (dec u.startera)))
  ?:  =(posita 100)
    `deckform`(into `deckform`(oust [0 1] incomingdeck1) 51 `card`[%joker %a])
  `deckform`(into `deckform`(oust [+(posita) 1] incomingdeck1) posita `card`[%joker %a])
++  jokerbfunc
  |=  incomingdeck2=deckform
  ^-  deckform
  =/  starterb  (find [%joker %b]~ incomingdeck2)
  =/  positb=@ud  ?~(starterb ~|("No Joker B in Deck" !!) ?:((lth u.starterb 2) ?:(=(0 u.starterb) 100 101) (dec (dec u.starterb))))
  ?:  (gth positb 53)
    ?:  =(positb 100)
      `deckform`(into `deckform`(oust [0 1] incomingdeck2) 50 `card`[%joker %b])
    `deckform`(into `deckform`(oust [1 1] incomingdeck2) 51 `card`[%joker %b])
  `deckform`(into `deckform`(oust [(add positb 2) 1] incomingdeck2) positb `card`[%joker %b])
++  triplecut
  |=  incomingdeck3=deckform
  ^-  deckform
  =/  startera  (find [%joker %a]~ incomingdeck3)
  =/  starterb  (find [%joker %b]~ incomingdeck3)
  =/  posita=@ud  ?~(startera !! u.startera)
  =/  positb=@ud  ?~(starterb !! u.starterb)
  =/  higherjoker=@ud  ?:((gth posita positb) posita positb)
  =/  lowerjoker=@ud  ?:((lth posita positb) posita positb)
  =/  toptobottom=deckform  (slag +(higherjoker) incomingdeck3)
  =/  topcutlength=@ud  (lent toptobottom)
  =/  middle=deckform  (slag lowerjoker (oust [+(higherjoker) topcutlength] incomingdeck3))
  =/  midcutlength=@ud  (lent middle)
  =/  bottomtotop=deckform  (oust [lowerjoker (add midcutlength topcutlength)] incomingdeck3)
  `deckform`(weld (weld toptobottom middle) bottomtotop)
++  findoperant
  |=  incomingdeck4=deckform
  ^-  deckform
  =/  bcardval=@ud  (cardtovalue `card`(snag 0 incomingdeck4))
  =/  tempcutcards=deckform  (slag (sub 54 bcardval) incomingdeck4)
  =/  tempcardcut=deckform  (slag 1 (oust [(sub 54 bcardval) bcardval] incomingdeck4))
  =/  primacard=card  (snag 0 incomingdeck4)
  ?:  =(53 bcardval)
    `deckform`(findoperant (triplecut (jokerbfunc (jokerafunc incomingdeck4))))
  `deckform`(weld (into tempcutcards 0 primacard) tempcardcut)
++  keystreamcard
  |=  incomingdeck5=deckform
  ^-  @ud
  =/  opc=card  `card`(snag 53 incomingdeck5)
  =/  tempval=@ud  (cardtovalue opc)
  =/  keycard=card  (snag (sub 53 tempval) incomingdeck5)
  `@ud`(cardtovalue keycard)
++  alphashift
  |=  inclist=(list @ud)
  =|  outlist=tape
  |-
  ?~  inclist
    outlist
  $(outlist [`@t`(add 96 ?:((gth i.inclist 26) (mod i.inclist 26) i.inclist)) outlist], inclist t.inclist)
++  customdeckbuilder
  |=  decksettings=(list @ud)
  =/  valuefrom=(list value)  valuelist
  =|  outputdeck=deckform
  |-  ^-  deckform
  ?~  decksettings
    (flop outputdeck)
  ?:  &((gth i.decksettings 0) (lte i.decksettings 13))
    $(decksettings t.decksettings, outputdeck [`card`[%club (snag i.decksettings valuefrom)] outputdeck])
  ?:  &((gte i.decksettings 14) (lte i.decksettings 26))
    $(decksettings t.decksettings, outputdeck [`card`[%diamond (snag (sub i.decksettings 13) valuefrom)] outputdeck])
  ?:  &((gte i.decksettings 27) (lte i.decksettings 39))
    $(decksettings t.decksettings, outputdeck [`card`[%heart (snag (sub i.decksettings 26) valuefrom)] outputdeck])
  ?:  &((gte i.decksettings 40) (lte i.decksettings 52))
    $(decksettings t.decksettings, outputdeck [`card`[%spade (snag (sub i.decksettings 39) valuefrom)] outputdeck])
  ?:  =(53 i.decksettings)
    $(decksettings t.decksettings, outputdeck [`card`[%joker %a] outputdeck])
  ?:  =(54 i.decksettings)
    $(decksettings t.decksettings, outputdeck [`card`[%joker %b] outputdeck])
  !!
--
```


# water-towers.md

---

+++
title = "Water Towers"
weight = 60
+++

## Challenge: Water between Towers

In a two-dimensional world, we begin with a bar-chart, or rows of unit-width 'towers' of arbitrary height. Then it rains, completely filling all convex enclosures in the chart with water.

```
9        █       
8        █           
7   █    █          
6   █ █  █           
5 █ █ █ ██      
4 █ █ ████      
3 ███ ████     
2 ████████ █ 
1 ██████████ 
```
```
9        █    
8        █    
7   █≈≈≈≈█    
6   █≈█≈≈█    
5 █≈█≈█≈██    
4 █≈█≈████    
3 ███≈████    
2 ████████≈█
1 ██████████
```

Your task for this challenge is to write a generator `water-towers`. It will take as input a `(list @ud)`, with each number representing the height of a tower from left to right. It will output a `@ud` representing the units of water that can be contained within the structure.

Example usage:
```
> +water-towers [5 3 7 2 6 4 5 9 1 2 ~]
14
```

##  Unit Tests

Following a principle of test-driven development, we compose a series of tests which allow us to rigorously check for expected behavior.

```hoon
/+  *test
/=  water-towers  /gen/water-towers
|%
++  test-01
  %+  expect-eq
    !>  `@ud`2
    !>  (water-towers [1 5 3 7 2 ~])
++  test-02
  %+  expect-eq
    !>  `@ud`14
    !>  (water-towers [5 3 7 2 6 4 5 9 1 2 ~])
++  test-03
  %+  expect-eq
    !>  `@ud`35
    !>  (water-towers [2 6 3 5 2 8 1 4 2 2 5 3 5 7 4 1 ~])
++  test-04
  %+  expect-eq
    !>  `@ud`0
    !>  (water-towers [5 5 5 5 ~])
++  test-05
  %+  expect-eq
    !>  `@ud`0
    !>  (water-towers [5 6 7 8 ~])
++  test-06
  %+  expect-eq
    !>  `@ud`0
    !>  (water-towers [8 7 7 6 5 4 3 2 ~])
++  test-07
  %+  expect-eq
    !>  `@ud`0
    !>  (water-towers [0 1 6 7 10 7 6 1 0 ~])
++  test-08
  %+  expect-eq
    !>  `@ud`0
    !>  (water-towers [100 0 0 0 0 0 0 0 ~])
++  test-09
  %+  expect-eq
    !>  `@ud`7
    !>  (water-towers [100 0 0 0 0 0 0 0 1 ~])
++  test-10
  %+  expect-eq
    !>  `@ud`50
    !>  (water-towers [10 0 0 0 0 0 10 ~])
++  test-11
  %+  expect-eq
    !>  `@ud`4
    !>  (water-towers [8 7 8 7 8 7 8 7 8 ~])
++  test-12
  %+  expect-eq
    !>  `@ud`40
    !>  (water-towers [0 1 2 3 4 5 4 3 2 1 1 2 3 4 5 4 3 2 1 1 2 3 4 5 4 3 2 1 0 ~])
--
```

##  Solutions

_These solutions were submitted by the Urbit community as part of a competition in ~2023.6.  They are made available under the MIT License and CC0.  We ask you to acknowledge authorship should you utilize these elsewhere._

### Solution #1

_By ~dannul-bortux. A model for literate programming in Hoon._

```hoon
::
::  A gate for computing volume of water collected between towers.
::
::    Take a list (of type list @ud), with each value representing the height of
::    a tower from left to right. Outputs a @ud representing the units of water 
::    that can be contained within the structure.
::
::    Our approach involves calculating the total volume of rainfall or water by
::    aggregating the water volume from each tower location. For a specific 
::    tower location. water volume is determined by subtracting the “height” 
::    of the tower with maximum rainfall (“total height with water”) from the 
::    height of the tower alone. Tower heights are given by corresponding values
::    in the input list.
::  
::    The “total height with water” at a location is determined by the height of
::    surrounding boundary towers within our structure. Each tower location will
::    have at most two boundary towers: one boundary tower on either side (left 
::    and right). The left boundary tower is defined as the highest tower to the
::    left of our specified tower location. The right boundary tower is defined 
::    as the highest tower to the right of our specified tower location. The 
::    value of “total height with water” at a location is equal to the lesser of
::    the two boundary tower heights (the minimum of the left boundary tower 
::    height vs. right boundary tower height). When less than two boundary 
::    towers are present, the “total height with water” is equal to the height
::    of the tower itself because no water can be contained without boundaries.
::
|=  inlist=(list @ud)
^-  @ud
::  If, input list is empty
::
?:  =(0 (lent inlist))
  ::  Then, throw error
  ::
  ~|  'Error - input list cannot be empty'
  !!
=<  (compute-totalvol inlist)
|%
::
::  +compute-totalvol: Gets total volume of water by summing water at each 
::  individual location.
::
::    Moves left to right iterating over each location (index in list). 
::    Determines waterfall at each location and aggregates all waterfall to 
::    find and return total volume.
::
++  compute-totalvol
  |=  [n=(list @ud)]
  ^-  @ud
  ::  i is face for iterating over all index/locations
  ::
  =/  i  0
  ::  tot is face for aggregating volume of water
  ::
  =/  tot  0
  |-
  ::  If, we're at end of input list
  ::
  ?:  =(i (lent n))
    ::  then, return total
    ::
    tot
  ::  else, compute water volume at current index, add to total, and increment i
  ::
  %=  $
      tot  (add tot (compute-indvol i n))
      i  +(i)
  ==
::
::  +compute-indvol: Computes volume at an individual location.
::   
::    Computes volume at an individual location (index in input list) by 
::    subtracting tower height from “total height with water”. “Total height 
::    with water” will be determined at a particular location by the height of 
::    “boundary towers” for that location. 
::
++  compute-indvol
  |=  [loc=@ud n=(list @ud)]
  ^-  @ud
  (sub (compute-waterheight loc n) (snag loc `(list @ud)`n))
::
::  +compute-waterheight: Measures the “total height with water” at a specified 
::  index/location.
::
::    “Total height with water” at a particular location is measured using the 
::    heights (value) at the left and right boundary towers. The lesser of these
::    two values (left height vs right height) is equal to the “total height 
::    with water” at our input location. 
::  
::    Right boundary tower is the tallest tower to the right of the location--
::    i.e. highest value (height) with higher index. The left boundary tower is
::    the tallest tower to the left of the location i.e. highest value (height) 
::    with lower index. 
::
::    The “find-boundaryheight” arm iterates left to right and works for 
::    measuring height of the right boundary tower. For the left boundary tower 
::    we can use a mirror approach. We reverse the input list and adjust the 
::    input index accordinglyto move right-to-left. 
::
::    In the case where no right or left boundary tower exists, our 
::    “find-boundaryheight” arm will return the tower height at our current 
::    index (indicating no water present) and we correctly compute 0 water 
::    volume in our compute-indvol arm.
::
++  compute-waterheight
  |=  [loc=@ud n=(list @ud)]
  ^-  @ud
  ::  rbth is a face for our "right boundary tower height" computed using our 
  ::  "find-boundaryheight" arm moving left to right
  ::
  =/  rbth  (find-boundaryheight loc n)
  ::  lbth is a face for our "right boundary tower height" computed using our 
  ::  "find-boundaryheight" arm moving (mirrored) right to left
  ::
  =/  lbth  (find-boundaryheight (sub (lent n) +(loc)) (flop n))
  ::  If, right boundary tower height is less than left boundary tower height, 
  ::
  ?:  (lth rbth lbth)
  ::  then, return right boundary tower height
  ::
    rbth
  ::  else, return left boundary tower height
  ::
  lbth
::
::  +find-boundaryheight: Computes the height of the highest tower to the right 
::  of the input location
::
::    Moves left to right starting at input location until the end of input 
::    list. Tracks height of each tower location with a height greater than 
::    height at corresponding input location.
::
++  find-boundaryheight
  |=  [loc=@ud n=(list @ud)]
  ^-  @ud
  ::  i is face used to iterate over input list starting one past input index
  ::
  =/  i  +(loc)
  ::  bheight is face used to measure boundary tower heights--i.e. any tower
  ::  heights greater than height at input location. At start, bheight is set to
  ::  input location height. If no greater heights are found, input location
  ::  height is returned (indicating no higher boundary towers found).
  ::
  =/  bheight  (snag loc n)
  |-
  ::  If, we are at the end of our input
  ::
  ?:  (gte i (lent n))
    ::  then, return boundary tower height
    ::
    bheight
  ::  else, if current tower height is greater than currently stored boundary 
  ::  tower height, replace boundary tower height. Incr iteration idx.
  ::
  %=  $
      bheight  ?:  (gth (snag i n) bheight)
                 (snag i n) 
               bheight
      i        +(i)
  ==
--
```



### Solution #2
_By ~racfer-hattes. A short and elegant solution._

```hoon
=>
|%
++  go 
  |=  [current=@ud previous=(list @ud) next=(list @ud)]
  =/  left-peak  (roll previous max)
  =/  right-peak  (roll next max)
  =/  min-peak  (min left-peak right-peak)
  =/  water-level  
    ?:  (lth min-peak current)  0  
    (sub min-peak current)
  ?~  next  water-level
  (add water-level $(current i.next, next t.next, previous [current previous]))
--
|=  xs=(list @ud)
?~  xs  0
%-  go  [i.xs ~ t.xs]
```

### Solution #3
_By ~dozreg-toplud. Another very literate and clean solution._


```hoon
::  +water-towers: a solution to the HSL challenge #1
::
::    https://github.com/tamlut-modnys/template-hsl-water-towers
::    Takes a (list @ud) of tower heights, returns the number of the units of
::    water that can be held in the given structure.
::
|=  towers=(list @ud)
^-  @ud
=<
::  x, y are horizontal and vertical axes
::
=|  water-counter=@ud
=/  x-last-tower=@ud  (dec (lent towers))
=/  y-highest-tower=@ud  (roll towers max)
::  iterate along y axis from y=0
::
=/  y=@ud  0
|-
^-  @ud
::  if, y > max(towers)
::
?:  (gth y y-highest-tower)
  ::  then, return water-counter
  ::
  water-counter
::  else, iterate along x axis from x=1
::
=/  x=@ud  1
|-
^-  @ud
::  if, x = x(last tower)
::
?:  =(x x-last-tower)
  ::  then, go to the next y
  ::
  ^$(y +(y))
::  else, increment water-counter if the point [x y] is not occupied by a tower
::  and has towers to the left and right on the same y, after go to the next x
::
=?  water-counter  ?&  (not-tower x y)
                       (has-tower-left x y)
                       (has-tower-right x y)
                   ==
  +(water-counter)
$(x +(x))
::
::  Core with helping functions
::
|%
::  ++not-tower: returns %.y if the coordinate [x y] is free from a tower,
::  %.n if occupied.
::
++  not-tower
  |=  [x=@ud y=@ud]
  ^-  ?
  (gth y (snag x towers))
::  ++has-tower-left: returns %.y if there is a tower with height >= y to
::  the left from x, %.n otherwise. Enabled computation caching to only test
::  each point once.
::
++  has-tower-left
  |=  [x=@ud y=@ud]
  ~+
  ^-  ?
  ::  no towers to the left from the 0th tower
  ::
  ?:  =(x 0)
    %.n
  ::  check recursively to the left
  ::
  ?|  (gte (snag (dec x) towers) y)
      $(x (dec x))
  ==
::  ++has-tower-right: returns %.y if there is a tower with height >= y to
::  the right from x, %.n otherwise. Enabled computation caching to only test
::  each point once.
::
++  has-tower-right
  |=  [x=@ud y=@ud]
  ~+
  ^-  ?
  ::  no towers to the right from the last tower
  ::
  ?:  =(x (dec (lent towers)))
    %.n
  ::  check recursively to the right
  ::
  ?|  (gte (snag +(x) towers) y)
      $(x +(x))
  ==
::
--
```
