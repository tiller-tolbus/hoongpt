# Hoon School Complete Documentation

---

##  Pronouncing Hoon

Hoon uses {% tooltip label="runes" href="/glossary/rune" /%}, or
two-character ASCII symbols, to describe its structure.  (These are
analogous to keywords in other programming languages.)  Because there
has not really been a standard way of pronouncing, say, `#` (hash,
pound, number, sharp, hatch) or `!` (exclamation point, bang, shriek,
pling), the authors of Urbit decided to adopt a one-syllable mnemonic to
uniquely refer to each.

{% table %}
- Name
- Character
- Name
- Character
- Name
- Character
---
- `ace`
- `␣`
- `gap`
- `␣␣`, `\n` 
- `pat` 
- `@`
---
- `bar`
- `|`
- `gar`
- `>`
- `sel`
- `[`
---
- `bas`
- `\`
- `hax`
- `#`
- `ser`
- `]`
---
- `buc`
- `$`
- `hep`
- `-`
- `sig`
- `~`
---
- `cab`
- `_`
- `kel`
- `{`
- `soq`
- `'`
---
- `cen`
- `%`
- `ker`
- `}`
- `tar`
- `*`
---
- `col`
- `:`
- `ket`
- `^`
- `tic`
- `` ` ``
---
- `com`
- `,`
- `lus`
- `+`
- `tis`
- `=`
---
- `doq`
- `"`
- `mic`
- `;`
- `wut`
- `?`
---
- `dot`
- `.`
- `pal`
- `(`
- `zap`
- `!`
---
- `fas`
- `/`
- `pam`
- `&`
- `gal`
- `<`
---
- `par`
- `)`
{% /table %}

Note that the list includes two separate whitespace forms: `ace` for a
single space `␣`; `gap` is either two or more spaces `␣␣` or a line
break `\n`.  In Hoon, the only whitespace significance is the
distinction between `ace` and `gap`—i.e., the distinction between one
space and more than one.


# B-syntax.md

---

+++
title = "1. Hoon Syntax"
objectives = ["Distinguish nouns, cells, and atoms.", "Apply auras to transform an atom.", "Identify common Hoon molds, such as cells, lists, and tapes.", "Pin a face to the subject.", "Make a decision at a branch point.", "Distinguish loobean from boolean operations.", "Slam a gate (call a function)."]
+++

_This module will discuss the fundamental data concepts of Hoon and how
programs handle control flow._

##  Hoon Elements

An
[**expression**](https://en.wikipedia.org/wiki/Expression_%28computer_science%29)
is a combination of characters that a language interprets and evaluates
to produce a value.  All Hoon programs are built of expressions, rather
like mathematical equations.  Hoon expressions are built along a
backbone of {% tooltip label="runes" href="/glossary/rune" /%}, which
are two-character symbols that act like keywords in other programming
languages to define the syntax, or grammar, of the expression.

Runes are the building blocks of all Hoon code, represented as a pair of
non-alphanumeric ASCII characters.  Runes form expressions; runes are
used how keywords are used in other languages.  In other words, all
computations in Hoon ultimately require runes.  Runes and other Hoon
expressions are all separated from one another by either two spaces or a
line break.

All runes take a fixed number of “children” or “daughters”.  Children
can themselves be runes with children, and Hoon programs work by
chaining through these until a value—not another rune—is arrived at.
For this reason, we very rarely need to close expressions.  Keep this
scheme in mind when examining Hoon code.

Hoon expressions can be either basic or complex.  Basic expressions of
Hoon are fundamental, meaning that they can’t be broken down into
smaller expressions.  Complex expressions are made up of smaller
expressions (which are called **subexpressions**).

The Urbit operating system hews to a conceptual model wherein each
expression takes place in a certain context (the {% tooltip
label="subject" href="/glossary/subject" /%}).  While sharing a lot of
practicality with other programming paradigms and platforms, Urbit's
model is mathematically well-defined and unambiguously specified.  Every
expression of Hoon is evaluated relative to its subject, a piece of data
that represents the environment, or the context, of an expression.

At its root, Urbit is completely specified by {% tooltip label="Nock"
href="/glossary/nock" /%}, sort of a machine language for the Urbit
virtual machine layer and event log.  However, Nock code is basically
unreadable (and unwriteable) for a human.  [One worked
example](/language/nock/examples/decrement) yields, for decrementing a
value by one, the Nock formula:

```hoon
[8 [1 0] 8 [1 6 [5 [0 7] 4 0 6] [0 6] 9 2 [0 2] [4 0 6] 0 7] 9 2 0 1]
```

This is like reading binary machine code:  we mortals need a clearer vernacular.

Hoon serves as Urbit's practical programming language.  Everything in
Urbit OS is written in Hoon, and many of the ancillary tools as well.  

Any operation in Urbit ultimately results in a value.  Much like machine
language designates any value as a command, an address, or a number, a
Hoon value is interpreted per the Nock rules and results in a basic data
value at the end.  So what are our data values in Hoon, and how do they
relate to each other?


##  Nouns

Think about a child persistently asking you what a thing is made of.  At
first, you may respond, “plastic”, or “metal”.  Eventually, the child
may wear you down to a more fundamental level:  atoms and molecules
(bonded atoms).

In a very similar sense, everything in a Hoon program is an atom or a
bond.  Metaphorically, a Hoon program is a complex molecule, a digital
chemistry that describes one mathematical representation of data.

The most general data category in Hoon is a {% tooltip label="noun"
href="/glossary/noun" /%}.  This is just about as broad as saying
“thing”, so let's be more specific:

> A noun is an atom or a cell.

Progress?  We can say, in plain English, that

- An {% tooltip label="atom" href="/glossary/atom" /%} is a non-negative
  integer number (0 to +∞), e.g. `42`.
- A {% tooltip label="cell" href="/glossary/cell" /%} is a pair of two
  nouns, written in square brackets, e.g. `[0
  1]`.

_Everything_ in Hoon (and Nock, and Urbit) is a noun.  The Urbit OS
itself is a noun.  So given any noun, the Urbit VM simply applies the
Nock rules to change the noun in well-defined mechanical ways.

### Atoms

If an atom is a non-negative number, how do we represent anything else?
Hoon provides each atom an {% tooltip label="aura" href="/glossary/aura"
/%} , a tag which lets you treat a number as text, time, date, Urbit
address, IP address, and much more.

An aura always begins with `@` pat, which denotes an atom (as opposed to
a cell, `^` ket, or the general noun, `*` tar).  The next letter or
letters tells you what kind of representation you want the value to
have.

For instance, to change the representation of a regular decimal number
like `32` to a binary representation (i.e. for 2⁵), use `@ub`:

```hoon
> `@ub`32
0b10.0000
```

(The tic marks are a shorthand which we'll explain later.)

Aura values are all designed to be
[URL-safe](https://developers.google.com/maps/url-encoding), so the
European-style thousands separator `.` dot is used instead of the
English `,` com.  `1.000` is one thousand, not `1.0` one with a
fractional part of zero.

While there are dozens of auras for specialized applications, here are
the most important ones for you to know:

| Aura | Meaning | Example | Comment |
| ---- | ------- | ------- | ------- |
| `@`  | Empty aura | `100` | (displays as `@ud`) |
| `@da` | Date (absolute) | ~2022.2.8..16.48.20..b53a | Epoch calculated from 292 billion B.C. |
| `@p` | Ship name | `~zod` |  |
| `@rs` | Number with fractional part | `.3.1415` | Note the preceding `.` dot. |
| `@t` | Text (“cord”) | `'hello'` | One of Urbit's several text types; only UTF-8 values are valid. |
| `@ub` | Binary value | `0b1100.0101` |  |
| `@ud` | Decimal value | `100.000` | Note that German-style thousands separator is used, `.` dot. |
| `@ux` | Hexadecimal value | `0x1f.3c4b` |  |

Hearkening back to our discussion of interchangeable representations in
Lesson -1, you can see that these are all different-but-equivalent ways
of representing the same underlying data values.

There's a special value that recurs in many contexts in Hoon:  `~` sig
is the null or zero value.

The `^-` {% tooltip label="kethep"
href="/language/hoon/reference/rune/ket#--kethep" /%} rune is useful for
ensuring that everything in the second child matches the type (aura) of
the first, e.g.

```hoon
^-  @ux  0x1ab4
```

We will use `^-` kethep extensively to enforce type constraints, a very
useful tool in Hoon code.

### Cells

A {% tooltip label="cell" href="/glossary/cell" /%} is a pair of nouns.
Cells are traditionally written using square brackets:  `[]`.  For now,
just recall the square brackets and that cells are always _pairs_ of
values.

```hoon
[1 2]
[@p @t]
[[1 2] [3 4]]
```

This is actually a shorthand for a rune as well, `:-` {% tooltip
label="colhep" href="/language/hoon/reference/rune/col#--colhep" /%}

```hoon
:-  1  2
```

produces a cell `[1 2]`.  You can chain these together:

```hoon
:-  1  :-  2  3
```

to produce `[1 [2 3]]` or `[1 2 3]`.

We deal with cells in more detail below.

{% callout %}

**Hoon as Noun**
 
We mentioned earlier that everything in Urbit is a noun, including the
program itself.  This is true, but getting from the rune expression in
Hoon to the numeric expression requires a few more tools than we
currently are prepared to introduce.

For now, you can preview the structure of the Urbit OS as a noun by
typing `.` dot at the Dojo prompt.  This displays a summary of the
structure of the operating function itself as a noun.

##  Verbs (Runes)

The backbone of any Hoon expression is a scaffolding of {% tooltip
label="runes" href="/glossary/rune" /%} , which are essentially
mathematical relationships between daughter components.  If nouns are
nouns, then runes are verbs:  they describe how nouns relate.  Runes
provide the structural and logical relationship between noun values.

A rune is just a pair of ASCII characters (a digraph).  We usually {%
tooltip label="pronounce runes" href="/glossary/aural-ascii" /%} by
combining their characters’ names, e.g.: {% tooltip label="\"kethep\""
href="/language/hoon/reference/rune/ket#--kethep" /%} for `^-`, {%
tooltip label="\"bartis\""
href="/language/hoon/reference/rune/bar#-bartis" /%} for `|=`, and {%
tooltip label="\"barcen\""
href="/language/hoon/reference/rune/bar#-barcen" /%} for `|%`.

For instance, when we called a function earlier (in Hoon parlance, we
_slammed a gate_), we needed to provide the `%-` {% tooltip
label="cenhep" href="/language/hoon/reference/rune/cen#-cenhep" /%} rune
with two bits of information, a function name and the values to
associate with it:

```hoon {% copy=true %}
%-
add  
[1 2]
```

The operation you just completed is straightforward enough:  `1 + 2`, in
many languages, or `(+ 1 2)` in a [Lisp
dialect](https://en.wikipedia.org/wiki/Lisp_%28programming_language%29)
like [Clojure](https://en.wikipedia.org/wiki/Clojure).  Literally, we
can interpret `%-  add  [1 2]` as “evaluate the `add` core on the input
values `[1 2]`”.

The {% tooltip label="++add"
href="/language/hoon/reference/stdlib/1a#add" /%} function expects
precisely two values (or _arguments_), which are provided by {% tooltip
label="%-" href="/language/hoon/reference/rune/cen#-cenhep" /%} in the
neighboring child expression as a cell.  There's really no limit to the
complexity of Hoon expressions:  they can track deep and wide.  They
also don't care much about layout, which leaves you a lot of latitude.
The only hard-and-fast rule is that there are single spaces (`ace`s) and
everything else (`gap`s).

```hoon {% copy=true %}
%-
add
[%-(add [1 2]) 3]
```

(Notice that inside of the `[]` cell notation we are using a slightly
different form of the `%-` rune call.  In general, there are several
ways to use many runes, and we will introduce these gradually.  We'll
see more expressive ways to write Hoon code after you're comfortable
using runes.)

For instance, here are some of the standard library functions which have
a similar architecture in common:

- [`++add`](/language/hoon/reference/stdlib/1a#add) (addition)
- [`++sub`](/language/hoon/reference/stdlib/1a#sub) (subtraction, positive results only—what happens if you subtract past zero?)
- [`++mul`](/language/hoon/reference/stdlib/1a#mul) (multiplication)
- [`++div`](/language/hoon/reference/stdlib/1a#div) (integer division, no remainder)
- [`++pow`](/language/hoon/reference/stdlib/2g#pow) (power or exponentiation)
- [`++mod`](/language/hoon/reference/stdlib/1a#mod) (modulus, remainder after integer division)
- [`++dvr`](/language/hoon/reference/stdlib/1a#dvr) (integer division with remainder)
- [`++max`](/language/hoon/reference/stdlib/1a#max) (maximum of two numbers)
- [`++min`](/language/hoon/reference/stdlib/1a#min) (minimum of two numbers)

### Rune Expressions

Any Hoon program is architected around runes.  If you have used another
programming language, you can see these as analogous to keywords,
although they also make explicit what most language syntax parsers leave
implicit.  Hoon aims at a parsimony of representation while leaving
latitude for aesthetics.  In other words, Hoon strives to give you a
unique characteristic way of writing a correct expression, but it leaves
you flexibility in how you lay out the components to maximize
readability.

We are only going to introduce a handful of runes in this lesson, but by
the time we're done with Hoon School, you'll know the twenty-five or so
runes that yield 80% of the capability.

Most runes are used at the beginning of a complex expression, but there
are exceptions. For example, the runes `--` {% tooltip label="hephep"
href="/language/hoon/reference/rune/terminators#---hephep" /%} and
`==` {% tooltip label="tistis"
href="/language/hoon/reference/rune/terminators#-tistis" /%} are used at
the end of certain expressions.

#### Aside:  Writing Incorrect Code

At the Dojo, you can attempt to operate using the wrong values; for
instance, `++add` doesn't know how to add three numbers at the same
time.

```hoon
> %-  add  [1 2 3]
-need.@
-have.[@ud @ud]
nest-fail
dojo: hoon expression failed
```

So this statement above is _syntactically_ correct (for the `%-` rune)
but in practice fails because the expected input arguments don't match.
Any time you see a `need`/`have` pair, this is what it means.

### Rune Families

Runes are classified by family (with the exceptions of `--` hephep and
`==` tistis). The first of the two symbols indicates the family—e.g.,
the `^-` kethep rune is in the `^` {% tooltip label="ket"
href="/language/hoon/reference/rune/ket" /%} family of runes, and the
`|=` bartis and `|%` barcen runes are in the `|` {% tooltip label="bar"
href="/language/hoon/reference/rune/bar" /%} family.  The runes of
particular family usually have related meanings.  Two simple examples:
the runes in the `|` bar family are all used to create cores, and the
runes in the `:` {% tooltip label="col"
href="/language/hoon/reference/rune/col" /%} family are all used to
create cells.

Rune expressions are usually complex, which means they usually have one
or more subexpressions.  The appropriate syntax varies from rune to
rune; after all, they’re used for different purposes.  To see the syntax
rules for a particular rune, consult the rune reference.  Nevertheless,
there are some general principles that hold of all rune expressions.

Runes generally have a fixed number of expected children, and thus do
not need to be closed.  In other languages you’ll see an abundance of
terminators, such as opening and closing parentheses, and this way of
doing this is largely absent from Urbit.  That’s because all runes take
a fixed number of children.  Children of runes can themselves be runes
(with more children), and Hoon programs work by chaining through these
series of children until a value—not another rune—is arrived at. This
makes Hoon code nice and neat to look at.

### Tall and Wide Forms

We call rune expressions separated by `gap`s **tall form** and those
using parentheses **wide form**.  Tall form is usually used for
multi-line expressions, and wide form is used for one-line expressions.
Most runes can be used in either tall or wide form.  Tall form
expressions may contain wide form subexpressions, but wide form
expressions may not contain tall form.

The spacing rules differ in the two forms.  In tall form, each rune and
subexpression must be separated from the others by a `gap`:  two or more
spaces, or a line break.  In wide form the rune is immediately followed
by parentheses `( )`, and the various subexpressions inside the
parentheses must be separated from the others by an `ace`:  a single
space.

Seeing an example will help you understand the difference.  The `:-`
colhep rune is used to produce a cell.  Accordingly, it is followed by
two subexpressions: the first defines the head of the cell, and the
second defines the tail.  Here are three different ways to write a `:-`
colhep expression in tall form:

```hoon
> :-  11  22
[11 22]

> :-  11
  22
[11 22]

> :-
  11
  22
[11 22]
```

All of these expressions do the same thing.  The first example shows
that, if you want to, you can write tall form code on a single line.
Notice that there are two spaces between the `:-` colhep rune and `11`,
and also between `11` and `22`.  This is the minimum spacing necessary
between the various parts of a tall form expression—any fewer will
result in a syntax error.

Usually one or more line breaks are used to break up a tall form
expression. This is especially useful when the subexpressions are
themselves long stretches of code. The same `:-` colhep expression in
wide form is:

```hoon
> :-(11 22)
[11 22]
```

This is the preferred way to write an expression on a single line. The
rune itself is followed by a set of parentheses, and the subexpressions
inside are separated by a single space. Any more spacing than that
results in a syntax error.

Nearly all rune expressions can be written in either form, but there are
exceptions.  `|%` {% tooltip label="barcen"
href="/language/hoon/reference/rune/bar#-barcen" /%} and `|_` {%
tooltip label="barcab" href="/language/hoon/reference/rune/bar#_-barcab"
/%} expressions, for example, can only be written in tall form.  (Those
are a bit too complicated to fit comfortably on one line anyway.)

### Nesting Runes

Since runes take a fixed number of children, one can visualize how Hoon
expressions are built by thinking of each rune being followed by a
series of boxes to be filled—one for each of its children.  Let us
illustrate this with the `:-` {% tooltip label="colhep"
href="/language/hoon/reference/rune/col#--colhep" /%} rune.

![Colhep rune with two empty boxes for children.](https://media.urbit.org/docs/hoon-syntax/cell1.png)

Here we have drawn the `:-` colhep rune followed by a box for each of
its two children.  We can fill these boxes with either a value or an
additional rune. The following figure corresponds to the Hoon expression
`:-  2  3`.

![Colhep rune with two boxes for children containing 2 and 3.](https://media.urbit.org/docs/hoon-syntax/cell2.png)

This, of course, evaluates to the cell `[2 3]`.

The next figure corresponds to the Hoon expression `:-  :-  2  3  4`.

![Colhep rune with two boxes for children, one containing a colhep rune with two boxes for children containing 2 and 3, and 4.](https://media.urbit.org/docs/hoon-syntax/cell3.png)

This evaluates to `[[2 3] 4]`, and we can think of the second `:-`
colhep as being “nested” inside of the first `:-` colhep.

What Hoon expression does the following figure correspond to, and what
does it evaluate to?

![Colhep rune with two boxes for children containing 2 and  a colhep rune with two boxes for children containing 3 and 4.](https://media.urbit.org/docs/hoon-syntax/cell4.png)

This represents the Hoon expression `:-  2  :-  3  4`, and evaluates to
`[2 [3 4]]`.  (If you input this into dojo it will print as `[2 3 4]`,
which we'll consider later.)

Thinking in terms of such “LEGO brick” diagrams can be a helpful
learning and debugging tactic.

##  Preserving Values with Faces

A Hoon expression is evaluated against a particular subject, which
includes Hoon definitions and the standard library, as well as any
user-specified values which have been made available.  Unlike many
procedural programming languages, a Hoon expression only knows what it
has been told explicitly.  This means that as soon as we calculate a
value, it returns and falls back into the ether.

```hoon
%-  sub  [5 1]
```

Right now, we don't have a way of preserving values for subsequent use
in a more complicated Hoon expression.

We are going to store the value as a variable, or in Hoon, “pin a face
to the subject”.  Hoon faces aren't exactly like variables in other
programming languages, but for now we can treat them that way, with the
caveat that they are only accessible to daughter or sister expressions.

When we used {% tooltip label="++add"
href="/language/hoon/reference/stdlib/1a#add" /%} or {% tooltip
label="++sub" href="/language/hoon/reference/stdlib/1a#sub" /%}
previously, we wanted an immediate answer.  There's not much more to say
than `5 + 1`.  In contrast, pinning a face accepts three daughter
expressions:  a name (or face), a value, and the rest of the expression.

```hoon {% copy=true %}
=/  perfect-number  28
%-  add  [perfect-number 10]
```

This yields `38`, but if you attempt to refer to `perfect-number` again
on the next line, the Dojo fails to locate the value.

```hoon
> =/  perfect-number  28
  %-  add  [perfect-number 10]
38

> perfect-number
-find.perfect-number
dojo: hoon expression failed
```

This syntax is a little bit strange in the Dojo because subsequent
expressions, although it works quite well in long-form code.  The Dojo
offers a workaround to retain named values:

```hoon
> =perfect-number 28
> %-  add  [perfect-number 10]
38

> perfect-number
28
```

The difference is that the Dojo “pin” is permanent until deleted:

```hoon {% copy=true %}
=perfect-number
```

rather than only effective for the daughter expressions of a `=/` tisfas
rune.  (We also won't be able to use this Dojo-style pin in a regular
Hoon program.)


##  Containers & Basic Data Structures

Atoms are well and fine for relatively simple data, but we already know
about cells as pairs of nouns.  How else can we think of collections of
data?

### Cells

A cell is formally a pair of two objects, but as long as the second
(right-hand) object is a cell, these can be written stacked together:

```hoon
> [1 [2 3]]
[1 2 3]

> [1 [2 [3 4]]]
[1 2 3 4]
```

This convention keeps the notation from getting too cluttered.  For now,
let's call this a “running cell” because it consists of several cells
run together.

Since almost all cells branch rightwards, the pretty-printer (the
printing routine that the Dojo uses) prefers to omit `[]` brackets
marking the rightmost cells in a running cell.  These read to the
right—that is, `[1 2 3]` is the same as `[1 [2 3]]`.

### Lists

A running cell which terminates in a `~` sig (null) atom is a list.

- What is `~`'s value?  Try casting it to another aura.

  `~` is the null value, and here acts as a list terminator.
  
Lists are ubiquitous in Hoon, and many specialized tools exist to work
with them.  (For instance, to apply a gate to each value in a list, or
to sum up the values in a list, etc.)  We'll see more of them in a
future lesson.

### Exercise:  Making a List from a Null-Terminated Cell

You can apply an aura to explicitly designate a null-terminated running
cell as a list containing particular types of data.  Sometimes you have
to clear the aura using a more general aura (like `@`) before the
conversion can work.

```hoon
> `(list @ud)`[1 2 3 ~]
~[1 2 3]

> `(list @ux)`[1 2 3 ~]
mint-nice
-need.?(%~ [i=@ux t=it(@ux)])
-have.[@ud @ud @ud %~]
nest-fail
dojo: hoon expression failed

> `(list @)`[1 2 3 ~]
~[1 2 3]

> `(list @ux)``(list @)`[1 2 3 ~]
~[0x1 0x2 0x3]
```

### Text

There are two ways to represent text in Urbit:  cords (`@t` {% tooltip
label="aura" href="/glossary/aura" /%} atoms) and {% tooltip
label="tapes" href="/glossary/tape" /%} (lists of individual
characters).  Both of these are commonly called
[“strings”](https://en.wikipedia.org/wiki/String_%28computer_science%29).

Why represent text?  What does that mean?  We have to have a way of
distinguishing words that mean something to Hoon (like `list`) from
words that mean something to a human or a process (like `'hello
world'`).

Right now, all you need to know is that there are (at least) two valid
ways to write text:

- `'with single quotes'` as a cord.
- `"with double quotes"` as text.

We will use these incidentally for now and explain their characteristics
in a later lesson.  Cords and text both use
[UTF-8](https://en.wikipedia.org/wiki/UTF-8) representation, but all
actual code is [ASCII](https://en.wikipedia.org/wiki/ASCII).

```hoon
> "You can put ½ in quotes, but not elsewhere!"
"You can put ½ in quotes, but not elsewhere!"

> 'You can put ½ in single quotes, too.'
'You can put ½ in single quotes, too.'

> "Some UTF-8: ἄλφα"
"Some UTF-8: ἄλφα"
```

### Exercise:  ASCII Values in Text

A {% tooltip label="cord" href="/glossary/cord" /%} (`@t`) represents
text as a sequence of characters.  If you know the
[ASCII](https://en.wikipedia.org/wiki/ASCII) value for a particular
character, you can identify how the text is structured as a number.
(This is most easily done using the hexadecimal `@ux` representation due
to bit alignment.)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/1024px-ASCII-Table-wide.svg.png)

If you produce a text string as a cord, you can see the internal
structure easily in Hoon:

```hoon
> `@ux`'Mars'
0x7372.614d
```

that is, the character codes `0x73` = `'s'`, `0x72` = `'r'`, `0x61` =
`'a'`, and `0x4d` = `'M'`.  Thus a cord has its first letter as the
smallest (least significant, in computer-science parlance) byte.

##  Making a Decision

The final rune we introduce in this lesson will allow us to select
between two different Hoon expressions, like picking a fork in a road.
Any computational process requires the ability to distinguish options.
For this, we first require a basis for discrimination:  truthness.

Essentially, we have to be able to decide whether or not some value or expression evaluates as `%.y` _true_ (in which case we will do one thing) or `%.n` _false_ (in which case we do another).  At this point, our basic expressions are always mathematical; later on we will check for existence, for equality of two values, etc.

- [`++gth`](/language/hoon/reference/stdlib/1a#gth) (greater than `>`)
- [`++lth`](/language/hoon/reference/stdlib/1a#lth) (less than `<`)
- [`++gte`](/language/hoon/reference/stdlib/1a#gte) (greater than or equal to `≥`)
- [`++lte`](/language/hoon/reference/stdlib/1a#lte) (less than or equal to `≤`)

If we supply these with a pair of numbers to a `%-` cenhep call, we can
see if the expression is considered `%.y` true or `%.n` false.

```hoon
> %-  gth  [5 6]
%.n
> %-  lth  [7 6]
%.n
> %-  gte  [7 6]
%.y
> %-  lte  [7 7]
%.y
```

Given a test expression like those above, we can use the `?:` wutcol
rune to decide between the two possible alternatives.  `?:` wutcol
accepts three children:  a true/false statement, an expression for the
`%.y` true case, and an expression for the `%.n` false case.

[Piecewise mathematical
functions](https://en.wikipedia.org/wiki/Piecewise) require precisely
this functionality.  For instance, the Heaviside function is a piecewise
mathematical function which is equal to zero for inputs less than zero
and one for inputs greater than or equal to zero.

{% math block=true %}
H(x)
=
\begin{cases} 1, & x > 0 \\\ 0, & x \le 0 \end{cases}
{% /math %}

_However_, we don't yet know how to represent a negative value!  All of
the decimal values we have used thus far are unsigned (non-negative)
values, `@ud`.  For now, the easiest solution is to just translate the
Heaviside function so it activates at a different value:

{% math block=true %}
H_{10}(x)
=
\begin{cases} 1, & x > 10 \\\ 0, & x \le 10 \end{cases}
{% /math %}

Thus equipped, we can evaluate the Heaviside function for particular
values of `x`:

```hoon {% copy=true %}
=/  x  10
?:  %-  gte  [x 10]
  1
0
```

We don't know yet how to store this capability for future use on
as-yet-unknown values of `x`, but we'll see how to do so in a future
lesson.

Carefully map how the runes in that statement relate to each other, and
notice how the taller structure makes it relatively easier to read and
understand what's going on.

# C-azimuth.md

---

+++
title = "2. Azimuth (Urbit ID)"
objectives = ["Understand the role of the public-key infrastructure in Urbit.", "Describe the high-level architecture of the Urbit ID address space and distinguish types of points.", "Interpret and apply the Azimuth point naming scheme.", "Identify point features such as activity.", "List at least two services/roles provided by a galaxy for the network.", "List at least two services provided by a star for its planets.", "Use Hoon to map the Azimuth address space domains and boundaries.", "Identify points, sponsors, neighbors, etc. from `@p` identifiers and simple operations."]
+++

_This module introduces how Urbit ID is structured and provides practice
in converting and working with `@p` identity points.  It may be
considered optional and skipped if you are speedrunning Hoon School._


##  A Public-Key Infrastructure

What is the purpose of a [public-key
infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure)?
Essentially a PKI defines a protocol for asymmetrically revealing a
public key (which anyone can use to check that a message came from where
it says it came) and retaining a private key, used by the owner as a
cryptographically secure tool for signing electronic transactions. {%
tooltip label="Azimuth" href="/glossary/azimuth" /%} functions as a PKI
so that Urbit ID points can be uniquely controlled, transferred, and
used to work with instances of Urbit OS (ships).

Urbit ID (=Azimuth) provides persistent and stable futureproof identity
to its users through a hierarchical address space.  Any particular Urbit
ID plays a particular role in the overall Urbit system which is
determined by its point number and classified into ranks.

### The Urbit Address Space

Each Urbit ID point is a 128-bit address.  Urbit is structured with a
hierarchy of addressable points, and bands of smaller values (preceded
by many zeroes) have more “weight” in the system and broker access for
higher-addressed points.

- **Galaxies** represent the “governing council” of Urbit, primarily
  concerned with peer discovery and packet routing as well as network
  protocol governance. Galaxies allocate star address space.
- **Stars** provide peer discovery services, handle distribution of
  software updates, and allocate planet address space.
- **Planets** are the primary single-user identities.
- **Moons** are intended to represent devices and associated accounts
  for the owning planet, but are currently only rarely used. Each planet
  has 2³² moons available to it.
- **Comets** are zero-reputation instances, in principle spammers or
  bots.  Comets require a star sponsor to access the network, but once
  online they are persistent.  They are also free to spin up.

In total there are 2¹²⁸ addressable points, of which the vast majority
are available as unclaimed “comet space.”

#### Naming

Urbit uses a system of mnemonic syllables to uniquely identify each
address point.  These mnemonic names, called “`patp`s” after their Hoon
representation `@p`, occur in a set of 256 suffixes (such as “zod”) and
256 prefixes (such as “lit”).  They were selected to be memorable and
pronounceable but not meaningful.

| Number | Prefix | Suffix |
| -----: | :----: | :----: |
| 0    | doz | zod |
| 1    | mar | nec |
| 2    | bin | bud |
| 3    | wan | wes |
| 4    | sam | sev |
| …    | …   | …   |
| 254  | mip | nev |
| 255  | fip | fes | 

Many points may be determined from the prefix and suffix alone, but
planet names are obfuscated, meaning that they are scrambled so that the
sponsor is not readily apparent to a peer.

#### Galaxy

The {% tooltip label="Galaxies" href="/glossary/galaxy" /%} span the
first 2⁸ addresses of Azimuth.  There are 255 (`0xff` - 1) associated
stars; counting the galaxy yields 256 points (not counting moons).
Galaxy names are suffix-only.

|              | First Address | Last Address |
| ------------ | ------------- | ------------ |
|  Decimal     | `0`           | `255`        |
|  Hexadecimal | `0x0`         | `0xff`       |
|  `@p`        | ~zod          | ~fes         |

As galaxies have no sponsors, they instead have an IP address determined
by `gal.urbit.org` at port `13337`+galaxy number.

At the current time, galaxies play the role of network peer discovery,
but at some future time this will fall to the stars instead.

#### Star

Peer discovery, the primary role of stars besides planet allocation, is
an important step in responsibly controlling network traffic. “The basic
idea is, you need someone to sponsor your membership on the network. An
address that can’t find a sponsor is probably a bot or a spammer”
([docs](https://urbit.org/understanding-urbit/)).

The {% tooltip label="Stars" href="/glossary/star" /%} span the
remaining addresses to 2¹⁶. There are thus 65,536 - 256 = 65,280 stars.
Star names have prefix and suffix. They share the suffix with their
sponsoring galaxy.

|              | First Address | Last Address |
| ------------ | ------------- | ------------ |
|  Decimal     | `256`         | `65.535`     |
|  Hexadecimal | `0x100`       | `0xffff`     |
|  `@p`        | ~marzod       | ~fipfes      |

A star's sponsor can be calculated as modulo 2⁸. The first star of ~zod
is `0x100` ~marzod.  The last star of ~zod is `0xffff` - `0xff` =
`0xff00` ~fipzod.  The last star (of ~fes) is `0xffff` ~fipfes.

#### Planet

The {% tooltip label="Planets" href="/glossary/planet" /%} span the
remaining addresses to 2³².  There are thus 4,294,967,296 - 65,536 =
4,294,901,760 planets.  Planet names occur in pairs separated by a
single hyphen.  A planet's name is obfuscated so it is not immediately
apparent who its sponsor is.

|              | First Address | Last Address |
| ------------ | ------------- | ------------ |
|  Decimal     | `65.536`      | `4.294.967.295` |
|  Hexadecimal | `0x1.0000`    | `0xffff.ffff` |
|  `@p`        | ~dapnep-ropmyl | ~dostec-risfen |

A planet's sponsor can be calculated as modulo 2¹⁶.

Galaxy planets occupy points beginning with `0x1.0000` ~dapnep-ronmyl
(for ~zod); ~zod's last galaxy planet is `0xffff.ffff` - `0xffff` =
`0xffff.0000` ~lodnyt-ranrud.  The last galaxy planet (of ~fes) is
`0xffff.ffff` - `0xffff` + `0x00ff` = `0xffff.00ff` ~hidwyt-mogbud.

Star planets span the remaining space.  The first star planet (of
~marzod) is `0x1.000` + `0x100` = `0x1.0100` ~wicdev-wisryt.  The last
star planet (of ~fipfes) is `0xffff.ffff` ~dostec-risfen.  Remember that
star planet recur module 2¹⁶.

#### Moon

The {% tooltip label="Moons" href="/glossary/moon" /%} occupy the block
to 2⁶⁴, with 2³² moons for each planet.  Moon names have more than two
blocks (three or four) separated by single hyphens.

|              | First Address | Last Address |
| ------------ | ------------- | ------------ |
|  Decimal     | `4.294.967.296` | `18.446.744.073.709.551.615` |
|  Hexadecimal | `0x1.0000.0000` | `0xffff.ffff.ffff.ffff` |
|  `@p`        | ~doznec-dozzod-dozzod | ~fipfes-fipfes-dostec-risfen |

Moons recur modulo 2³² from their sponsor.  Thus dividing a moon's
address by 2³² and taking the remainder yields the address of the
sponsor.

Any moon that begins with the prefix ~dopzod-dozzod-doz___ is a
galaxy moon, but not every galaxy moon begins with that prefix. The
first galaxy moon of ~zod is 0x1.0000.0000 ~doznec-dozzod-dozzod; the
last is `0xffff.ffff.ffff.ffff` - `0xffff.ffff` = `0xffff.ffff.0000.0000` ~fipfes-fipfes-dozzod-dozzod.

Any moon that begins with the prefix ~dopzod-dozzod-______ is a
star moon (other than galaxy moons), but not every star moon begins with
that prefix. The first star moon of ~marzod is `0x1.0000.0000.0100`
~doznec-dozzod-dozzod-marzod; the last is `0xffff.ffff.ffff.ffff` -
`0xffff.ffff` + `0x100` = `0xffff.ffff.0000.0100`
~fipfes-fipfes-dozzod-marzod.

Any moon from ~dopzod-______-______ onwards is a planet
moon.

#### Comet

The {% tooltip label="Comets" href="/glossary/comet" /%} occupy the
upper portion of the Urbit address space.  There are approximately
3.4×10³⁸ comets, a fantastically large number.  Comet names occur in
blocks of five to eight syllable pairs, separated by a double hyphen at
the fourth.

|              | First Address | Last Address |
| ------------ | ------------- | ------------ |
| Decimal      | `18.446.744.073.709.551.616` | `340.282.366.920.938.463.463.374.607.431.768.211.456` |
| Hexadecimal  | `0x1.0000.0000.0000.0000` | `0xffff.ffff.ffff.ffff.ffff.ffff.ffff.ffff` |
| @p           | ~doznec--dozzod-dozzod-dozzod-dozzod | ~fipfes-fipfes-fipfes-fipfes--fipfes-fipfes-fipfes-fipfes |

A comet is sponsored by a star.  Currently star sponsors are determined
randomly from a list supplied to `u3_dawn_come` in
`pkg/urbit/vere/dawn.c` from a [jamfile](/language/hoon/reference/stdlib/2p#jam) provided by urbit.org at
`https://bootstrap.urbit.org/comet-stars.jam`.

Comets cannot be breached or rekeyed:  possession of the comet is *ipso
facto* attestation of ownership.

##  Calculating with Addresses

### Sponsors

Each point other than a galaxy has a sponsor.  To determine the sponsor
of any point, use `++sein:title`:

```hoon {% copy=true %}
%-(sein:title [our now ~marzod])
```

where ~marzod is the point in question; or more succinctly:

```hoon {% copy=true %}
(sein:title our now ~marzod)
```

(This previews the irregular syntax of `%-` cenhep; it is equivalent to
`%-  sein:title  [our now ~marzod]`.)

# D-gates.md

---

+++
title = "3. Gates (Functions)"
objectives = ["Use the `+ls` generator to show a directory's contents.", "`|mount` and `|commit` a desk.", "Identify current known irregular syntax.", "Convert between regular and irregular forms of runes to date.", "Employ a gate to defer a computation.", "Produce a gate as a generator.", "Annotate Hoon code with comments.", "Produce a generator to convert a value between auras."]
+++

_This module will teach you how to produce deferred computations for
later use, like functions in other languages._

##  A Spoonful of Sugar

Until this point in Hoon School, we have rigorously adhered to the
regular syntax of runes so that you could get used to using them.  In
fact, the only two irregular forms we used were these:

- Cell definition `[a b]` which represents the `:-` {% tooltip
  label="colhep" href="/language/hoon/reference/rune/col#--colhep" /%}
  rune, `:-  a  b`.

    That is, these expressions are all the same for Hoon:

    ```hoon
    > [1 2]
    [1 2]

    > :-  1  2
    [1 2]

    > :-
    1
    2
    [1 2]
    ```

- Aura application `` `@ux`500 `` which represents a double `^-` {%
  tooltip label="kethep"
  href="/language/hoon/reference/rune/ket#--kethep" /%}, like `^-  @ux  ^-  @  500`.

    These are equivalent in Hoon:

    ```hoon
    > ^-  @p  ^-  @  255
    ~fes

    > `@p`255
    ~fes
    ```

    (Why two `^-`s?  We have to clear the type information in general to
    be able to apply new type information.)

Hoon developers often employ irregular forms, sometimes called “sugar
syntax”.  Besides the `:-` colhep and `^-` kethep forms, we will
commonly use a new form for `%-` {% tooltip label="cenhep"
href="/language/hoon/reference/rune/cen#-cenhep" /%} “function calls”:

```hoon
> %-  add  [1 2]
3

> (add 1 2)
3
```

You should get used to reading and interpreting these forms.  We will
start to use them actively during this lesson.  You can find other
irregular forms in the [irregular forms
reference](/language/hoon/reference/irregular).


##  Deferring Computations

So far, every time we have calculated something, we have had to build it
from scratch in Dojo.  This is completely untenable for nontrivial
calculations, and clearly the Urbit OS itself is built on persistent
code structures defining the behavior.

```hoon {% copy=true %}
::  Confirm whether a value is greater than one.
=/  a  5
?:  (gth a 1)
  'yes'
'no'
```

This has no flexibility:  if we want to change `a` we have to rewrite
the whole thing every time!

(Note also our introduction of the `::` {% tooltip label="colcol"
href="/language/hoon/reference/rune/col#-colcol" /%} digraph in the
above code block.  This marks anything following it as a _comment_,
meaning that it is meant for the developer and reader, and ignored by
the computer.)

Hoon uses {% tooltip label="gates" href="/glossary/gate" /%} as deferred
computations.  What this means is that we can build a Hoon expression
now and use it at need later on, perhaps many times.  More than that, we
can also use it on different data values.  A gate is the Hoon analogue
of a [function or subroutine](https://en.wikipedia.org/wiki/Subroutine)
in other programming languages.

The word "function" is used in various ways, but let's start by talking
about them in the [mathematical
sense](https://en.wikipedia.org/wiki/Function_%28mathematics%29).
Roughly put, a function takes one or more arguments (i.e., input values)
and returns a value.  The return value depends solely on the
argument(s), and nothing else. For example, we can understand
multiplication as a function:  it takes two numbers and returns another
number.  It doesn't matter where you ask, when you ask, or what kind of
hat you're wearing when you ask.  If you pass the same two numbers
(e.g., `3` and `4`), you get the same answer returned every time (`12`).

That output value depends solely upon input value(s) is an important
property of functions. This property is called [referential
transparency](https://en.wikipedia.org/wiki/Referential_transparency),
and it's one of the key ingredients to building a secure Urbit stack.

Functions are implemented in Hoon with a special kind of {% tooltip
label="core" href="/glossary/core" /%} called a _gate_.  In this lesson
you'll learn what a gate is and how a gate represents a function.  (We
_won't_ talk about what a core is quite yet.)  Along the way you'll
build some example gates of your own.

### Building a Gate

Syntactically, a gate is a `|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%} rune with two
children:  a {% tooltip label="spec"
href="/language/hoon/reference/stdlib/4o#spec" /%} (specification of
input) and a {% tooltip label="hoon"
href="/language/hoon/reference/stdlib/4o#hoon" /%} (body). Think of just
replacing the `=/` {% tooltip label="tisfas"
href="/language/hoon/reference/rune/tis#-tisfas" /%} with the `|=`
bartis:

```hoon {% copy=true %}
::  Confirm whether a value is greater than one.
|=  a=@ud
?:  (gth a 1)
  'yes'
'no'
```

Compare this to other programming languages, if you know any:
- Does it have a name?
- Does it have a return value?

Beyond those, what is the purpose of each line?

The `spec` gives the type as a mold and attaches a face to it for use in
the gate.

The `hoon` body expression evaluates and yields a result, ultimately
sent back to the call site.  Frequently it is wise to explicitly require
a particular type for the return value using the `^-` {% tooltip
label="kethep" href="/language/hoon/reference/rune/ket#--kethep" /%}
rune:

```hoon {% copy=true %}
::  Confirm whether a value is greater than one.
|=  a=@ud
^-  @t
?:  (gth a 1)
  'yes'
'no'
```

The input value, what is included in the `spec`, is sometimes called the
argument or parameter in mathematics and other programming languages.
It's basically the input value.  Hoon prefers to call it the `sample`
for reasons that will become apparent later on, but you won't confuse
other developers if you call it the argument or input.

Note as well that the backbone of the program runs straight down the
left-hand margin.  This makes it easier to read the essential mainline
logic of the program.

Gates enforce the type of incoming and outgoing values.  In other words,
a `spec` is a kind of type which is fixing the possible noun inputs.
(The lesson on types which follows this one will go into greater
detail.)

Gates can take multiple arguments as a cell:

```hoon {% copy=true %}
::  Return which of two numbers is larger.
|=  [a=@ud b=@ud]
?:  (gth a b)
  a
b
```

You can also call them different ways with raw `%` {% tooltip
label="cen" href="/language/hoon/reference/rune/cen" /%} runes:

```hoon {% copy=true %}
%-  max  [100 200]
%+  max  100  200
```

### Creating Your Own Gate

You can type the above Hoon code snippets directly into Dojo, but
there's no way to actually use them yet!  The Dojo recognizes the
expression as valid Hoon code, but can't actually apply it to an input
`sample` yet.

```hoon
> |=  [a=@ud b=@ud]
  ?:  (gth a b)
    a
  b
< 1.tfm
  [ [a=@ud b=@ud]
    [our=@p now=@da eny=@uvJ]
    <15.eah 40.ihi 14.tdo 54.xjm 77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
  ]
```

We need to attach a _name_ or a {% tooltip label="face"
href="/glossary/face" /%} to the expression.  Then we'll be able to use
it directly.  Somewhat confusingly, there are three common ways to do
this:

1. Attach the face (name) directly in Dojo.  (This is a good quick
   solution, and we'll use it when teaching and testing code, but it
   doesn't work inside of code files.)
2. Save the gate as a {% tooltip label="generator"
   href="/glossary/generator" /%} file and call it using the name of the
   file.  (We'll do this in the next section of this lesson.)
3. Attach the face (name) as an {% tooltip label="arm"
   "href"="/glossary/arm" /%} in a {% tooltip label="core"
   href="/glossary/core" /%}.  (We don't know what those are yet, so
   we'll set them aside for a couple of lessons.)

To name a gate in Dojo (or any expression resulting in a value, which is
_every_ expression), you can use the Dojo-specific syntax `=name value`:

```hoon
> =inc |=  [a=@]
       (add 1 a)

> (inc 1)
2

> (inc 12)
13

> (inc 5)
6
```

Notice that there is _one_ space (`ace`) after the `=name` term and then
regular `gap`s thereafter.  We could also do this in one line using wide
form:

```hoon
> =inc |=(a=@ (add 1 a))

> (inc 123)
124
```

To reiterate:  we typically use the `|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%} rune to create a
gate. In the expression above the `|=` is immediately followed by a set
of parentheses containing two subexpressions: `a=@` and `(add 1 a)`. The
first defines the gate's {% tooltip label="sample"
href="/glossary/sample" /%} (input value type), and the second defines
the gate's product (output value).

In the example gate above, `inc`, the sample is defined by `a=@`.  This
means that the sample is defined as an atom `@` meaning that the gate
will take as input anything of that type (so, not a cell).  The `sample`
is given the face `a`.  With a face it's easier to refer to the `sample`
value in later code.

The second subexpression after the `|=` bartis rune is used to build the
gate's body, where all the computations go.  In `inc`, the product is
defined by `(add 1 a)`.  There's not much to it—it returns the value of
`a+1`!

### Exercise:  Double a Value

- Produce a gate which accepts any `@` unsigned integer value and
  doubles it.  Call it `double`.

    ```hoon
    > =double |=(a=@ (mul a 2))

    > (double 5)
    10
    ```

### Exercise:  Convert Between Auras

- Produce a gate which accepts any `@` unsigned integer value and
  converts it to the `@p` equivalent.  Call it `myship`.

- Produce a gate which accepts any `@` unsigned integer value and
  calculates the next neighbor (the `@p` of the number plus one).  Call
  it `myneighbor`.

- Produce a gate which accepts a `@p` ship name and produces the `@ux`
  unsigned hexadecimal integer value of the ship.  Call it `mynumber`.

### Output Values

How can we control what kind of value a gate returns?  Many programming
languages (such as C and Java) are _extremely_ concerned about this
specification.  Others, like Python and MATLAB, are _laissez-faire_.
Hoon tends to be strict, but leaves some discretion over _how_ strict to
you, the developer.

Remember `^-` {% tooltip label="kethep"
href="/language/hoon/reference/rune/ket#--kethep" /%}?  We will use `^-`
as a _fence_, a way of making sure only data matching the appropriate
structure get passed on.

```hoon {% copy=true %}
::  Confirm whether a value is greater than one by return 1 (if no) or 0 (if yes).
|=  a=@ud
^-  @ud
?:  (gth a 1)
  1
0
```

**This is the correct way to define a gate.**  Frequent annotation of
type with `^-` kethep fences is _essential_ to producing good Hoon code.
From this point forward in Hoon School, we will hew to this standard.

In technical language, we describe Hoon as a _statically typed_
language.  This means that it enforces type constraints on all values
very aggressively.  If you are used to a dynamic language like Python or
Ruby, this will seem very restrictive at first.  The flip side is that
once your code compiles correctly, you will often find that it is very
much along the way towards being a working correct product.

A generator is a simple program which can be called from the Dojo.  It
is a gate, so it takes some input as sample and produces some result.
Naked generators are the simplest generators possible, having access
only to information passed to them directly in their {% tooltip
label="sample" href="/glossary/sample" /%}.

In this section, we will compose our first generator.

### The Gate

```hoon
::  Square a number.
|=  a=@ud
^-  @ud
%+  mul
  a
a
```

### Hoon Source and Special Characters

Hoon source files are composed almost entirely of the printable ASCII
characters.  Hoon does not accept any other characters in source files
except for [UTF-8](https://en.wikipedia.org/wiki/UTF-8) in quoted
strings.  Hard tab characters are illegal; use two spaces instead.

```hoon
> "You can put ½ in quotes, but not elsewhere!"
"You can put ½ in quotes, but not elsewhere!"

> 'You can put ½ in single quotes, too.'
'You can put ½ in single quotes, too.'

> "Some UTF-8: ἄλφα"
"Some UTF-8: ἄλφα"
```

### Coding Piecemeal

If you need to test code without completing it, you can stub out
as-yet-undefined arms with the `!!` {% tolltip label="zapzap"
href="/language/hoon/reference/rune/zap#-zapzap" /%} crash rune.  `!!`
is the only rune which has no children, and it's helpful when you need
something to satisfy Hoon syntax but aren't ready to flesh out the
program yet.

# E-types.md

---

+++
title = "4. Molds (Types)"
objectives = ["Identify a mold in the hierarchy of Urbit types (nouns, molds, marks).", "Understand how type inference and type checking takes place.", "Bunt a mold.", "Produce a type union.", "Produce a named tuple.", "Identify type using `!>`."]
+++

_This module will introduce the Hoon type system and illustrate how type
checking and type inference work._

##  The Hoon Type System

Programming languages use data types to distinguish different kinds of
data and associated rules.  For instance, what does it mean to add 3 to
the letter A?  Depending on your programming language, you could see
`A3`, `D`, or an error.

Like most modern high-level programming languages, Hoon has a type
system.  Because Hoon is a functional programming language, its type
system differs somewhat from those of non-functional languages.  In this
lesson we'll introduce Hoon's type system and point out some of its
distinctive features.  Certain advanced topics (e.g. type polymorphism)
won't be addressed until a later chapter.

A type is ordinarily understood to be a set of values. Examples: the set
of all atoms is a type, the set of all cells is a type, and so on.

Type systems provide type safety, in part by making sure functions
produce values of the correct type. When you write a function whose
product is intended to be an atom, it would be nice to know that the
function is guaranteed to produce an atom. Hoon's type system provides
such guarantees with _type checking_ and _type inference_.

A _type_ is really a rule for interpretation.  But for our Hoonish
purposes, it's rather too broad a notion and we need to clarify some
different kinds of things we could refer to as “type”.  It is
instructive for learners to distinguish three kinds of types in Hoon:

1. Atoms:  values with auras.
2. {% tooltip label="Molds" href="/glossary/mold" /%}:  structures.
   Think of cells, lists, and sets.
3. {% tooltip label="Marks" href="/glossary/mark" /%}:  file types.
   Compare to conventional files distinguished by extension and definite
   internal structure.

To employ a chemical metaphor, an atom is an atom; a cell is a molecule;
a mold is an molecule definition, a template or structural
representation; a mark is like a protein, a more complex transformation
rule.  **All of these are molds, or Hoon types.  We are simply
separating them by complexity as you learn.**

You have seen and worked with the trivial atoms and cells.  We will
leave marks until a later discussion of {% tooltip label="Gall"
href="/glossary/gall" /%} {% tooltip label="agents"
href="/glossary/agent" /%} or the {% tooltip label="Clay"
href="/glossary/clay" /%} filesystem, which use marks to type file data.
For now, we focus on {% tooltip label="molds" href="/glossary/mold" /%}.

This lesson will talk about atoms, cells, then molds in a general sense.
We allude to several topics which will be explored in Data Structures.


##  Atoms and Auras

In the most straightforward sense, atoms simply are unsigned integers.
But they can also be interpreted as representing signed integers, ASCII
symbols, floating-point values, dates, binary numbers, hexadecimal
numbers, and more.  Every atom is, in and of itself, just an unsigned
integer; but Hoon keeps track of type information about each atom, and
this bit of metadata tells Hoon how to interpret the atom in question.

The piece of type information that determines how Hoon interprets an
atom is called an {% tooltip label="aura" href="/glossary/aura" /%}.
The set of all atoms is indicated with the symbol `@`.  An aura is
indicated with `@` followed by some letters, e.g., `@ud` for unsigned
decimal.  Accordingly, the Hoon type system does more than track sets of
values.  It also tracks certain other relevant metadata about how those
values are to be interpreted.

How is aura information generated so that it can be tracked?  One way
involves **type inference**.  In certain cases Hoon's type system can
infer the type of an expression using syntactic clues.  The most
straightforward case of type inference is for a
[literal](https://en.wikipedia.org/wiki/Literal_%28computer_programming%29)
expression of data, such as `0x1000` for `@ux`.  Hoon recognizes the
aura literal syntax and infers that the data in question is an atom with
the aura associated with that syntax.

To see the inferred type of a literal expression in the Dojo, use the
`?` operator.  (This operator isn't part of the Hoon programming
language; it's a Dojo-only tool.)

The `?` Dojo operator shows both the product and the inferred type of an
expression.  Let's try `?` on `15`:

```hoon
> 15
15

> ? 15
  @ud
15
```

`@ud` is the inferred type of `15` (and of course `15` is the product).
The `@` is for “atom” and the `ud` is for “unsigned decimal”.  The
letters after the `@` indicate the “aura” of the atom.

One important role played by the type system is to make sure that the
output of an expression is of the intended data type.  If the output is
of the wrong type then the programmer did something wrong.  How does
Hoon know what the intended data type is?  The programmer must specify
this explicitly by using a _cast_.  To cast for an unsigned decimal
atom, you can use the `^-` kethep rune along with the `@ud` from above.

What exactly does the `^-` {% tooltip label="kethep"
href="/language/hoon/reference/rune/ket#--kethep" /%} rune do?  It
compares the inferred type of some expression with the desired cast
type.  If the expression's inferred type _nests_ under the desired type,
then the product of the expression is returned.

Let's try one in the Dojo.

```hoon
> ^-(@ud 15)
15
```

Because `@ud` is the inferred type of `15`, the cast succeeds.  Notice
that the `^-` kethep expression never does anything to modify the
underlying {% tooltip label="noun" href="/glossary/noun" /%} of the
second subexpression.  It's used simply to mandate a type-check on that
expression.  This check occurs at compile-time (when the expression is
compiled to {% tooltip label="Nock" href="/glossary/nock" /%}).

What if the inferred type doesn't fit under the cast type?  You will see
a `nest-fail` crash at compile-time:

```hoon
> ^-(@ud [13 14])
nest-fail
[crash message]
```

Why `nest-fail`?  The inferred type of `[13 14]` doesn't nest under the
cast type `@ud`.  It's a cell, not an atom.  But if we use the symbol
for nouns, `*`, then the cast succeeds:

```hoon
> ^-(* [13 14])
[13 14]
```

A cell of atoms is a noun, so the inferred type of `[13 14]` nests under
`*`.  Every product of a Hoon expression nests under `*` because every
product is a noun.

### What Auras are There?

Hoon has a wide (but not extensible) variety of atom literal syntaxes.
Each literal syntax indicates to the Hoon type checker which predefined
aura is intended.  Hoon can also pretty-print any aura literal it can
parse.  Because atoms make great path nodes and paths make great URLs,
all regular atom literal syntaxes use only URL-safe characters.  The
pretty-printer is convenient when you are used to it, but may surprise
you occasionally as a learner.

Here's a non-exhaustive list of auras, along with examples of
corresponding literal syntax:

| Aura   | Meaning                      | Example Literal Syntax |
|:-------|:-----------------------------|:-----------------------|
| `@d`   | date                         | no literal |
| `@da`  | absolute date                | `~2018.5.14..22.31.46..1435` |
| `@dr`  | relative date (ie, timespan) | `~h5.m30.s12` |
| `@p`   | phonemic base (ship name)    | `~sorreg-namtyv` |
| `@r`   | [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754) floating-point |  |
| `@rd`  | double precision  (64 bits)  | `.~6.02214085774e23` |
| `@rh`  | half precision (16 bits)     | `.~~3.14` |
| `@rq`  | quad precision (128 bits)    | `.~~~6.02214085774e23` |
| `@rs`  | single precision (32 bits)   | `.6.022141e23` |
| `@s`   | signed integer, sign bit low | no literal |
| `@sb`  | signed binary                | `--0b11.1000` |
| `@sd`  | signed decimal               | `--1.000.056` |
| `@sv`  | signed base32                | `-0v1df64.49beg` |
| `@sw`  | signed base64                | `--0wbnC.8haTg` |
| `@sx`  | signed hexadecimal           | `-0x5f5.e138` |
| `@t`   | UTF-8 text (`cord`)          | `'howdy'` |
| `@ta`  | ASCII text (subset) (`knot`)          | `~.howdy` |
| `@tas` | ASCII text symbol (subset) (`term`)   | `%howdy` |
| `@u`   | unsigned integer             | no literal |
| `@ub`  | unsigned binary              | `0b11.1000` |
| `@ud`  | unsigned decimal             | `1.000.056` |
| `@uv`  | unsigned base32              | `0v1df64.49beg` |
| `@uw`  | unsigned base64              | `0wbnC.8haTg` |
| `@ux`  | unsigned hexadecimal         | `0x5f5.e138` |

Some of these auras nest under others.  For example, `@u` is for all
unsigned auras.  But there are other, more specific auras; `@ub` for
unsigned binary numbers, `@ux` for unsigned hexadecimal numbers, etc.
(For a more complete list of auras, see
[Auras](/language/hoon/reference/auras).)

`knot` and `term` values each use a URL-safe subset of ASCII, omitting
characters like spaces.

### Aura Inference in Hoon

Let's work a few more examples in the Dojo using the `?` operator.
We'll focus on just the unsigned auras for now:

```hoon
> 15
15

> ? 15
  @ud
15

> 0x15
0x15

> ? 0x15
  @ux
0x15
```

When you enter just `15`, the Hoon type checker infers from the syntax
that its aura is `@ud` because you typed an unsigned integer in decimal
notation. Hence, when you use `?` to check the aura, you get `@ud`.

And when you enter `0x15` the type checker infers that its aura is
`@ux`, because you used `0x` before the number to indicate the unsigned
hexadecimal literal syntax. In both cases, Hoon pretty-prints the
appropriate literal syntax by using inferred type information from the
input expression; the Dojo isn't (just) echoing what you enter.

More generally: for each atom expression in Hoon, you can use the
literal syntax of an aura to force Hoon to interpret the atom as having
that aura type. For example, when you type `~sorreg-namtyv` Hoon will
interpret it as an atom with aura `@p` and treat it accordingly.

Here's another example of type inference at work:

```hoon
> (add 15 15)
30

> ? (add 15 15)
  @
30

> (add 0x15 15)
36

> ? (add 0x15 15)
  @
36
```

The {% tooltip label="add" href="/language/hoon/reference/stdlib/1a#add"
/%} function in the Hoon standard library operates on all atoms,
regardless of aura, and returns atoms with no aura specified. Hoon isn't
able to infer anything more specific than `@` for the product of `add`.
This is by design, however. Notice that when you `add` a decimal and a
hexadecimal above, the correct answer is returned (pretty-printed as a
decimal). This works for all of the unsigned auras:

```hoon
> (add 100 0b101)
105

> (add 100 0xf)
115

> (add 0b1101 0x11)
30
```

The reason these add up correctly is that unsigned auras all map
directly to the 'correct' atom underneath. For example, `16`,
`0b1.0000`, and `0x10` are all the exact same atom, just with different
literal syntax. (This doesn't hold for signed versions of the auras!)


##  Cells

Let's move on to consider cells.  For now we'll limit ourselves to
simple cell types made up of various atom types.

### Generic Cells

The `^` ket symbol is used to indicate the type for cells (i.e., the set
of all cells).  We can use it for casting as we did with atom auras,
like `@ux` and `@t`:

```hoon
> ^-(^ [12 13])
[12 13]

> ^-(^ [[12 13] 14])
[[12 13] 14]

> ^-(^ [[12 13] [14 15 16]])
[[12 13] [14 15 16]]

> ^-(^ 123)
nest-fail

> ^-(^ 0x10)
nest-fail
```

If the expression to be evaluated produces a cell, the cast succeeds; if
the expression evaluates produces an atom, the cast fails with a
nest-fail crash.

The downside of using `^` ket for casts is that Hoon will infer only
that the product of the expression is a cell; it won't know what kind of
cell is produced.

```hoon
> ? ^-(^ [12 13])
  [* *]
[12 13]

> ? ^-(^ [[12 13] 14])
  [* *]
[[12 13] 14]

> ? ^-(^ [[12 13] [14 15 16]])
  [* *]
[[12 13] [14 15 16]]
```

When we use the `?` operator to see the type inferred by Hoon for the
expression, in all three of the above cases the same thing is returned:
`[* *]`.  The `*` symbol indicates the type for any noun, and the square
brackets `[ ]` indicate a cell.  Every cell in Hoon is a cell of nouns;
remember that cells are defined as pairs of nouns.

Yet the cell `[[12 13] [14 15 16]]` is a bit more complex than the cell
`[12 13]`.  Can we use the type system to distinguish them?  Yes.

### Getting More Specific

What if you want to cast for a particular kind of cell?  You can use
square brackets when casting for a specific cell type.  For example, if
you want to cast for a cell in which the head and the tail must each be
an atom, then simply cast using `[@ @]`:

```hoon
> ^-([@ @] [12 13])
[12 13]

> ? ^-([@ @] [12 13])
  [@ @]
[12 13]

> ^-([@ @] 12)
nest-fail

> ^-([@ @] [[12 13] 14])
nest-fail
```

The `[@ @]` cast accepts any expression that evaluates to a cell with
exactly two atoms, and crashes with a {% tooltip label="nest-fail"
href="/language/hoon/reference/hoon-errors#nest-fail" /%} for any
expression that evaluates to something different.  The expression `12`
doesn't evaluate to a cell; and while the expression `[[12 13] 14]` does
evaluate to a cell, the left-hand side isn't an atom, but is instead
another cell.

You can get even more specific about the kind of cell you want by using
atom auras:

```hoon
> ^-([@ud @ux] [12 0x10])
[12 0x10]

> ^-([@ub @ux] [0b11 0x10])
[0b11 0x10]

> ? ^-([@ub @ux] [0b11 0x10])
  [@ub @ux]
[0b11 0x10]

> ^-([@ub @ux] [12 13])
nest-fail
```

You are also free to embed more square brackets `[ ]` to indicate cells
within cells:

```hoon
> ^-([[@ud @sb] @ux] [[12 --0b1101] 0xdead.beef])
[[12 --0b1101] 0xdead.beef]

> ? ^-([[@ud @sb] @ux] [[12 --0b1101] 0xdead.beef])
  [[@ud @sb] @ux]
[[12 --0b1101] 0xdead.beef]

> ^-([[@ @] @] [12 13])
nest-fail
```

You can also be highly specific with certain parts of the type
structure, leaving other parts more general. Keep in mind that when you
do this, Hoon's type system will infer a general type from the general
part of the cast. Type information may be thrown away:

```hoon
> ^-([^ @ux] [[12 --0b1101] 0xdead.beef])
[[12 26] 0xdead.beef]

> ? ^-([^ @ux] [[12 --0b1101] 0xdead.beef])
  [[* *] @ux]
[[12 26] 0xdead.beef]

> ^-(* [[12 --0b1101] 0xdead.beef])
[[12 26] 3.735.928.559]

> ? ^-(* [[12 --0b1101] 0xdead.beef])
  *
[[12 26] 3.735.928.559]
```

Because every piece of Hoon data is a noun, everything nests under `*`.
When you cast to `*` you can see the raw noun with cells as brackets and
atoms as unsigned integers.


##  Molds

A {% tooltip label="mold" href="/glossary/mold" /%} is a template or
rule for identifying actual type structures. They are actually gates,
meaning that they operate on a value to coerce it to a particular
structure.  Technically, a mold is a function from a noun to a noun.
What this means is that we can use a mold to map any noun to a typed
value—if this fails, then the mold crashes.

```hoon
> (^ [1 2])
[1 2]

> (@ [1 2])
dojo: hoon expression failed

> `@`[1 2]
mint-nice
-need.@
-have.[@ud @ud]
nest-fail
dojo: hoon expression failed
```

We commonly need to do one of two things with a mold:

1.  Validate the shape of a noun (_clam_).
    
    ```hoon
    > (@ux 0x1000)
    0x1000

    > (@ux [1 2])
    dojo: hoon expression failed
    ```

2.  Produce an example value ({% tooltip label="bunt"
    href="/glossary/bunt" /%}).

We often use bunts to clam; for example `@ud` implicitly uses the `@ud`
default value (`0`) as the type specimen which the computation must
match.

To _actually_ get the bunt value, use the `^*` {% tooltip label="kettar"
href="/language/hoon/reference/rune/ket#-kettar" /%} rune, almost always
used in its irregular form `*` tar:

```hoon
> ^*  @ud
0

> ^*  @da
~2000.1.1

> *@da
~2000.1.1

> *[@ud @ux @ub]
[0 0x0 0b0]
```

One more way to validate against type is to use an example instead of
the extracted mold.  This uses the `^+` {% tooltip label="ketlus"
href="/language/hoon/reference/rune/ket#-ketlus" /%} rune similarly to
how we used `^-` {% tooltip label="kethep"
href="/language/hoon/reference/rune/ket#--kethep" /%} previously:

```hoon {% copy=true %}
^+(1.000 100)
```

(This is what `^-` is actually doing:  `^-(p q)` reduces to `^+(^*(p)
q)`.  Many runes we use actually reduce to other rune forms, and have
been introduced for ease of use.)

We can use more complex structures for molds though, including built-in
types like {% tooltip label="lists" href="/glossary/list" /%} and {%
tooltip label="tapes" href="/glossary/tape" /%}.  (A `tape` represents
text.)

```hoon {% copy=true %}
`(list @)`[104 101 108 108 111 32 77 97 114 115 33 ~]
`tape``(list @)`[104 101 108 108 111 32 77 97 114 115 33 ~]

`(list @)`[144 57 195 46 200 165 186 88 118 99 ~]
`(list @p)``(list @)`[144 57 195 46 200 165 186 88 118 99 ~]
```

(Sometimes you see a `%bad-text` when using `tape`s, which means that
you've tried to convert a number into text which isn't text.  More on
`tape`s in Trees.)

-   Why does this mold conversion fail?

     ```hoon {% copy=true %}
     `(list @ux)`[1 2 3 ~]
     ```

    What do we need to do in order to make it succeed?

We can have more complex molds as well:

```hoon {% copy=true %}
::  [[from-ship to-ship] points]
[[@p @p] @ud]
```

Most of the time, we will define such complex types using specific runes
and “mold builder” tools.  Thus a `list` needs an associated type `(list
@)` to correctly denote the data type.

### Identifying Molds

Besides `?` (which is a Dojo-specific tool), the programmatic way to
figure out which mold the Hoon compiler thinks something is to use the
`!>` {% tooltip label="zapgar"
href="/language/hoon/reference/rune/zap#-zapgar" /%} rune.

```hoon
> !>(0xace2.bead)
[#t/@ux q=2.900.541.101]
```

For reasons which will be elaborated in Trees, this is often employed as
the so-called “type spear” `-:!>`:

```hoon
> -:!>(0xace2.bead)
#t/@ux
```

### Type Unions

`$?` {% tooltip label="bucwut"
href="/language/hoon/reference/rune/buc#-bucwut" /%} forms a type union.
Most commonly these are used with types having different structures,
such as an atom and a cell.

For instance, if you wanted a gate to accept an atom of an unsigned aura
type, but no other type, you could define a type union thus:

```hoon {% copy=true %}
$?  [@ud @ux @ub ~]
```

and use it in a gate:

```hoon {% copy=true %}
|=  [n=$?(@ud @ux @ub)]
(add n 1)
```

```hoon
> (foo 4)  
5  
> (foo 0x5)  
6  
> (foo 0b110)  
7  
> (foo ~zod)  
-need.?(@ub @ud @ux)  
-have.@p  
nest-fail  
dojo: hoon expression failed
```

Unfortunately, type unions of atoms are not helpful in filtering over
produced values (with `^-` kethep), as they default to the type of the
last value in the union.  So the type union `$?(@ (list @))`
distinguishes an atom and a list, but `(list $?(@ud @sd))` does not
successfully produce a list distinguishing both types.

The irregular form of `$?` bucwut looks like this:

```hoon {% copy=true %}
?(@ud @ux @ub)
```

Type unions are mainly helpful when you need to match something that can
have multiple options.  We will use them extensively with `@tas` terms,
such as `?(%red %green %blue)` which would only admit one of those three
tags.


# F-cores.md

---

+++
title = "5. Cores"
objectives = ["Employ a trap to produce a reentrant block of code.", "Produce a recursive gate.", "Distinguish head and tail recursion.", "Consider Hoon structures as cores.", "Identify the special role of the `$` buc arm in many cores.", "Order neighboring cores within the subject for addressibility.", "Produce a type arm."]
+++

_This module will introduce the key Hoon data structure known as the
**core**, as well as ramifications._

The Hoon subject is a noun.  One way to look at this noun is to denote
each fragment of is as either a computation or data.  By strictly
separating these two kinds of things, we derive the data structure known
within Hoon as a {% tooltip label="core" href="/glossary/core" /%}.

Cores are the most important data structure in Hoon.  They allow you to
solve many coding problems by identifying a pattern and supplying a
proper data structure apt to the challenge.  You have already started
using cores with `|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%} {% tooltip
label="gate" href="/glossary/gate" /%} construction and use.

This lesson will introduce another {% tooltip label="core"
href="/glossary/core" /%} to solve a specific use case, then continue
with a general discussion of cores.  Getting cores straight will be key
to understanding why Hoon has the structure and internal logic it does.


##  Repeating Yourself Using a Trap

Computers were built and designed to carry out tasks which were too
dainty and temperamental for humans to repeat consistently, or too
prodigiously numerous for humans to ever complete.  At this point, you
know how to build code that can make a decision between two branches,
two different Hoon expressions.  Computers can decide between
alternatives, but they also need to carry out a task until some
condition is met.  (We can think of it as a recipe step, like “crack
five eggs into a bowl”.  Until that process is complete, we as humans
continue to carry out the equivalent action again and again until the
process has been completed.)

In programming, we call this behavior a “loop”.  A loop describes the
situation in which we set up some condition, and repeat a process over
and over until something we do meets that condition.  _Most_ of the
time, this means counting once for each item in a collection, like a
list.

Hoon effects the concept of a loop using recursion, return to a
particular point in an expression (presumably with some different
values).  One way to do this is using the `|-` {% tooltip label="barhep"
href="/language/hoon/reference/rune/bar#--barhep" /%} rune, which
creates a structure called a {% tooltip label="trap"
href="/glossary/trap" /%}.  (Think of the “trap” in the bottom of your
sink.)  It means a point to which you can return again, perhaps with
some key values (like a counter) changed.  Then you can repeat the
calculation inside the trap again.  This continues until some single
value, some noun, results, thereby handing a value back out of the
expression.  (Remember that every Hoon expression results in a value.)

This program adds 1+2+3+4+5 and returns the sum:

```hoon {% copy=true %}
=/  counter  1
=/  sum  0
|-
?:  (gth counter 5)
  sum
%=  $
  counter  (add counter 1)
  sum      (add sum counter)
==
```

(The last two lines happen simultaneously, so make sure to refer to the
_current_ version of any variables.)

Let's unroll it:

0.  `counter = 1`
    `sum = 0`

1.  `(gth counter 5) = %.n`
    `counter ← (add counter 1) = 2`
    `sum ← (add sum counter) = 0 + 1 = 1`

2.  `(gth counter 5) = %.n`
    `counter ← (add counter 1) = 3`
    `sum ← (add sum counter) = 1 + 2 = 3`

3.  `(gth counter 5) = %.n`
    `counter ← (add counter 1) = 4`
    `sum ← (add sum counter) = 3 + 3 = 6`

4.  `(gth counter 5) = %.n`
    `counter ← (add counter 1) = 5`
    `sum ← (add sum counter) = 6 + 4 = 10`

5.  `(gth counter 5) = %.n`
    `counter ← (add counter 1) = 6`
    `sum ← (add sum counter) = 10 + 5 = 15`

6.  `(gth counter 5) = %.y`

And thus `sum` yields the final value of `15`.

It is frequently helpful, when constructing these, to be able to output
the values at each step of the process.  Use the `~&` {% tooltip
label="sigpam" href="/language/hoon/reference/rune/sig#-sigpam" /%} rune
to create output without changing any values:

```hoon {% copy=true %}
=/  counter  1
=/  sum  0
|-
~&  "counter:"
~&  counter
~&  "sum:"
~&  sum
?:  (gth counter 5)
  sum
%=  $
  counter  (add counter 1)
  sum      (add sum counter)
==
```

You can do even better using _interpolation_:

```hoon {% copy=true %}
=/  counter  1
=/  sum  0
|-
~&  "counter: {<counter>}"
~&  "sum: {<sum>}"
?:  (gth counter 5)
  sum
%=  $
  counter  (add counter 1)
  sum      (add sum counter)
==
```

### Exercise:  Calculate a Factorial

- Let's calculate a
  [factorial](https://mathworld.wolfram.com/Factorial.html).  The
  factorial of a number {% math %}n{% /math %} is {% math %}n \times
  (n-1) \times \ldots \times 2 \times 1{% /math %}.  We will introduce a
  couple of new bits of syntax and a new gate ({% tooltip label="++dec"
  href="/language/hoon/reference/stdlib/1a#dec" /%}).  Make this into a
  generator `factorial.hoon`:

    ```hoon {% copy=true %}
    |=  n=@ud
    |-
    ~&  n
    ?:  =(n 1)
      1
    %+  mul
      n
    %=  $
      n  (dec n)
    ==
    ```

    - We are using the `=` irregular syntax for the `.=` {% tooltip
      label="dottis" href="/language/hoon/reference/rune/dot#-dottis"
      /%} rune, which tests for the equality of two expressions.

    ```hoon
    > +factorial 5
    120
    ```

    Let's visualize the operation of this gate using pseudocode (fake
    code that's explanatory but may not be operational).  Here's
    basically what's happening when `factorial` receives the value `5`:

    ```hoon
    (factorial 5)
    (mul 5 (factorial 4))
    (mul 5 (mul 4 (factorial 3)))
    (mul 5 (mul 4 (mul 3 (factorial 2))))
    (mul 5 (mul 4 (mul 3 (mul 2 (factorial 1)))))
    (mul 5 (mul 4 (mul 3 (mul 2 1))))
    (mul 5 (mul 4 (mul 3 2)))
    (mul 5 (mul 4 6))
    (mul 5 24)
    120
    ```

    We're “floating” gate calls until we reach the final iteration of
    such calls that only produces a value.  The `mul n` component of the
    gate leaves `mul 5` waiting for the final series of terms to be
    operated upon.  The `%=($ n (dec n)))` component expands the
    expression outwards, as illustrated by `(factorial 4)`.  This
    continues until the expression is not expanded further, at which
    point the operations work backwards, successively feeding values
    into the `mul` functions behind them.

    The pyramid-shaped illustration approximates what's happening on the
    _call stack_, a memory structure that tracks the instructions of the
    program.  In this code, every time a parent gate calls another gate,
    the gate being called is "pushed" to the top of the stack in the
    form of a frame.  This process continues until a value is produced
    instead of a function, completing the stack.

    - Why do we return the result (`product` in Hoon parlance) at 1
      instead of 0?

### Exercise:  Tracking Expression Structure

As we write more complicated programs, it is helpful to learn to read
the {% tooltip label="runes" href="/glossary/rune" /%} by identifying
which daughter expressions attach to which runes, e.g.:

```hoon
=/
  n
  15
  |-
    ~&
      n
      ?:
        =(n 1)      :: .=  n  1
        1
      %+
        mul
        n
        %=
          $
          n
          (dec n)   :: %-  dec  n
        ==
```

Recall that the `::` digraph tells the compiler to ignore the rest of
the text on the line.  Such text is referred to as a "comment" because,
instead of performing a computation, it exists to explain things to
human readers of the source code.  Here, we have also explicitly marked
the expansion of the irregular forms.

We will revert to the irregular form more and more.  If you would like
to see exactly how an expression is structured, you can use the `!,` {%
tooltip label="zapcom" href="/language/hoon/reference/rune/zap#-zapcom"
/%} rune.  `!,` zapcom produces an annotated _abstract syntax tree_
(AST) which labels every value and expands any irregular syntax into the
regular runic form.

```hoon
> !,  *hoon  (add 5 6)
[%cncl p=[%wing p=~[%add]] q=[i=[%sand p=%ud q=5] t=[i=[%sand p=%ud q=6] t=~]]]
```

```hoon
> !,  *hoon
 |=  n=@ud
 |-  
 ~&  n  
 ?:  =(n 1)  
   1
 %+  mul  
   n
 %=  $  
   n  (dec n)  
 ==  
[ %brts
  p=[%bcts p=term=%n q=[%base p=[%atom p=~.ud]]]
    q
  [ %brhp
      p
    [ %sgpm
      p=0
      q=[%wing p=~[%n]]
        r
      [ %wtcl
        p=[%dtts p=[%wing p=~[%n]] q=[%sand p=%ud q=1]]
        q=[%sand p=%ud q=1]
          r
        [ %cnls
          p=[%wing p=~[%mul]]
          q=[%wing p=~[%n]]
          r=[%cnts p=~[%$] q=[i=[p=~[%n] q=[%cncl p=[%wing p=~[%dec]] q=[i=[%wing p=~[%n]] t=~]]] t=~]]
        ]
      ]
    ]
  ]
]
```

(_There's a lot going on in there._  Focus on the four-letter runic
identifiers:  `%sgpm` for `~&` {% tooltip label="sigpam"
href="/language/hoon/reference/rune/sig#-sigpam" /%}, for instance.)

##  Cores

So far we have introduced and worked with a few key structures:

1. Nouns
2. Molds (types)
3. Gates
4. Traps

Some of them are _data_, like raw values:  `0x1234.5678.abcd` and `[5 6
7]`.  Others are _code_, programs that do something.  What unifies all
of these under the hood?

A {% tooltip label="core" href="/glossary/core" /%} is a cell pairing
operations to data.  Formally, we'll say a core is a cell `[battery
payload]`, where {% tooltip label="battery" href="/glossary/battery" /%}
describes the things that can be done (the operations) and {% tooltip
label="payload" href="/glossary/payload" /%} describes the data on which
those operations rely.  (For many English speakers, the word “battery”
evokes a [voltaic pile](https://en.wikipedia.org/wiki/Voltaic_pile) more
than a bank of guns, but the artillery metaphor is a better mnemonic for
`[battery payload]`.)

**Cores are the most important structural concept for you to grasp in
Hoon.**  Everything nontrivial is a core.  Some of the runes you have
used already produce cores, like the gate.  That is, a gate marries a
`battery` (the operating code) to the `payload` (the input values AND
the {% tooltip label="subject" href="/glossary/subject" /%} or
operating context).

Urbit adopts an innovative programming paradigm called {% tooltip
label="subject-oriented programming"
href="/glossary/subject-oriented-programming" /%}.  By and large, Hoon
(and {% tooltip label="Nock" href="/glossary/nock" /%}) is a functional
programming language in that running a piece of code twice will always
yield the same result, and because runs cause a program to explicitly
compose various subexpressions in a somewhat mathematical way.

Hoon (and Nock) very carefully bounds the known context of any part of
the program as the {% tooltip label="subject" href="/glossary/subject"
/%}.  Basically, the subject is the noun against which any arbitrary
Hoon code is evaluated.

For instance, when we first composed generators, we made what are called
“naked generators”:  that is, they do not have access to any information
outside of the base subject (Arvo, Hoon, and `%zuse`) and their {%
tooltip label="sample" href="/glossary/sample" /%} (arguments).  Other {%
tooltip label="generators" href="/glossary/generator" /%} (such as
`%say` generators, described below) can have more contextual
information, including random number generators and optional arguments,
passed to them to form part of their subject.

Cores have two kinds of values attached:  {% tooltip label="arms"
href="/glossary/arm" /%} and _legs_, both called limbs.  Arms describe
known labeled addresses (with `++` luslus or `+$` lusbuc) which carry
out computations.  Legs are limbs which store data (with e.g. `=/`
tisfas).

### Arms

So legs are for data and arms are for computations.  But what
_specifically_ is an arm, and how is it used for computation?  Let's
begin with a preliminary explanation that we'll refine later.

An {% tooltip label="arm" href="/glossary/arm" /%} is some expression
of Hoon encoded as a noun.  (By 'encoded as a noun' we literally mean:
'compiled to a Nock formula'.  But you don't need to know anything about
{% tooltip label="Nock" href="/glossary/nock" /%} to understand Hoon.)
You virtually never need to treat an arm as raw data, even though
technically you can—it's just a noun like any other.  You almost always
want to think of an arm simply as a way of running some Hoon code.

Every expression of Hoon is evaluated relative to a subject.  An {%
tooltip label="arm" href="/glossary/arm" /%} is a Hoon expression to be
evaluated against the {% tooltip label="core" href="/glossary/core" /%}
subject (i.e. its parent core is its subject).

#### Arms for Gates

Within a core, we label arms as Hoon expressions (frequently `|=` bartis
gates) using the `++` {% tooltip label="luslus"
href="/language/hoon/reference/rune/lus#-luslus" /%} digraph.  (`++`
isn't formally a rune because it doesn't actually change the structure
of a Hoon expression, it simply marks a name for an expression or value.
The `--` {% tooltip label="hephep"
href="/language/hoon/reference/rune/terminators#---hephep" /%} limiter
digraph is used because `|%` {% tooltip label="barcen"
href="/language/hoon/reference/rune/bar#-barcen" /%} can have any number
of arms attached.  Like `++`, it is not formally a rune.)

```hoon {% copy=true %}
|%
++  add-one
  |=  a=@ud
  ^-  @ud
  (add a 1)
++  sub-one
  |=  a=@ud
  ^-  @ud
  (sub a 1)
--
```

Give the name `adder` to the above, and use it thus:

```hoon
> (add-one:adder 5)
6

> (sub-one:adder 5)
4
```

Notice here that we read the arm resolution from right-to-left.  This
isn't the only way to address an arm, but it's the most common one.

#### Arms for Types

We can define custom types for a core using `+$` {% tooltip
label="lusbuc" href="/language/hoon/reference/rune/lus#-lusbuc" /%}
digraphs.  We won't do much with these yet but they will come in handy
for custom types later on.

This core defines a set of types intended to work with playing cards:

```hoon {% copy=true %}
|%
+$  suit  ?(%hearts %spades %clubs %diamonds)
+$  rank  ?(1 2 3 4 5 6 7 8 9 10 11 12 13)
+$  card  [sut=suit val=rank]
+$  deck  (list card)
--
```

#### Cores in Generators

When we write generators, we can include helpful tools as arms either
before the main code (with `=>` {% tooltip label="tisgar"
href="/language/hoon/reference/rune/tis#-tisgar" /%}) or after the main
code (with `=<` {% tooltip label="tisgal"
href="/language/hoon/reference/rune/tis#-tisgal" /%}):

```hoon {% copy=true %}
|=  n=@ud
=<
(add-one n)
|%
++  add-one
  |=  a=@ud
  ^-  @ud
  (add a 1)
--
```

A library (a file in `/lib`) is typically structured as a `|%` {%
tooltip label="barcen" href="/language/hoon/reference/rune/bar#-barcen"
/%} core.

### Legs

A _leg_ is a data value.  They tend to be trivial but useful ways to pin
constants.  `=/` tisfas values are legs, for instance.

```hoon
> =/  a  1
  (add a 1)
2
```

Under the hood, legs and arms are distinguished by the Nock instructions
used in each case.  A leg is evaluated by Nock 0, while an arm is
evaluated by Nock 9.

### Recalculating a Limb

Arms and legs are both _limbs_.  Either one can be replaced in a given
subject.  This turns out to be very powerful, and permits Hoon to
implement gates (functions) in a mathematically rigorous way, among
other applications.

Often a leg of the subject is produced with its value unchanged. But
there is a way to produce a modified version of the leg as well. To do
so, we use the `%=` {% tooltip label="centis"
href="/language/hoon/reference/rune/cen#-centis" /%} rune:

```hoon {% copy=true %}
%=  subject-limb
  leg-1  new-leg-1
  leg-2  new-leg-2
  ...
==
```

`%=` centis is frequently used in its irregular form, particularly if
the expression within it fits on a single line.  The irregular form
prepends the arm (often `$`) to parentheses `()`.  In its irregular
form, the above would be:

```hoon {% copy=true %}
subject-limb(leg-1 new-leg-1, leg-2 new-leg-2, ...)
```

In the first example, we saw the expression

```hoon {% copy=true %}
%=  $
  counter  (add counter 1)
  sum      (add sum counter)
==
```

which can equivalently be expressed as

```hoon {% copy=true %}
$(counter (add counter 1), sum (add sum counter))
```

This statement means that we recalculate the `$` buc arm of the current
subject with the indicated changes.  But what is `$` buc?  `$` buc is
the _default arm_ for many core structures, including `|=` {% tooltip
label="bartis" href="/language/hoon/reference/rune/bar#-bartis" /%} gate
cores and `|-` {% tooltip label="barhep"
href="/language/hoon/reference/rune/bar#--barhep" /%} trap cores.

### What is a Gate?

A core is a cell:  `[battery payload]`.

A gate is a core with two distinctive properties:

1.  The {% tooltip label="battery" href="/glossary/battery" /%} of a
    gate contains an arm which has the special name `$` buc.  The `$`
    buc arm contains the instructions for the function in question.
2.  The {% tooltip label="payload" href="/glossary/payload" /%} of a
    gate consists of a cell of `[sample context]`.
    1.  The {% tooltip label="sample" href="/glossary/sample" /%} is the
        part of the payload that stores the "argument" (i.e., input
        value) of the function call.
    2.  The **context** contains all other data that is needed for
        computing the `$` buc arm of the gate correctly.
As a tree, a gate looks like the following:

```
[$ [sample context]]

       gate
      /    \
     $      .
           / \
     sample   context
```

Like all arms, `$` buc is computed with its parent core as the subject.
When `$` buc is computed, the resulting value is called the “product” of
the gate.  No other data is used to calculate the product other than the
data in the gate itself.

We will always call the values supplied to the gate the “sample” since
we will later discover that this technical meaning (`[battery [sample
context]]`) holds throughout more advanced cores.

### Exercise:  Another Way to Calculate a Factorial

Let's revisit our factorial code from above:

```hoon {% copy=true %}
|=  n=@ud
|-
?:  =(n 1)
  1
%+  mul
  n
%=  $
  n  (dec n)
==
```

We can write this code in several ways using the `%=` {% tooltip
label="centis" href="/language/hoon/reference/rune/cen#-centis" /%} plus
`$` buc structure.

For instance, we can eliminate the trap by recursing straight back to
the gate:

```hoon {% copy=true %}
|=  n=@ud
?:  =(n 1)
  1
%+  mul
  n
%=  $
  n  (dec n)
==
```

This can be collapsed into a shorter equivalent form by employing the
irregular form of `%=` centis:

```hoon {% copy=true %}
|=  n=@ud
?:  =(n 1)
  1
(mul n $(n (dec n)))
```

(Sugar syntax like `$()` does not affect code efficiency, merely visual
layout.)

#### The `$` Buc Arm

The (only) {% tooltip label="arm" href="/glossary/arm" /%} of a {%
tooltip label="gate" href="/glossary/gate" /%} encodes the instructions
for the Hoon function in question.

```hoon
> =inc |=(a=@ (add 1 a))

> (inc 5)
6
```

The pretty printer represents the `$` buc arm of `inc` as `1.yop`.  To
see the actual noun of the `$` buc arm, enter `+2:inc` into the Dojo:

```hoon
> +2:inc
[8 [9 36 0 4.095] 9 2 10 [6 [7 [0 3] 1 1] 0 14] 0 2]
```

This is un-computed Nock. You don't need to understand any of this,
except that code and data are homoiconic—they are in a sense the same
for Urbit programs.

It's worth pointing out that the arm named `$` buc can be used like any
other name.  We can compute `$` buc directly with `$:inc` in the Dojo:

```hoon
> $:inc
1
```

This result may seem a bit strange.  We didn't call `inc` or in any
other way pass it a number.  Yet using `$` buc to evaluate `inc`'s arm
seems to work—sort of, anyway.  Why is it giving us `1` as the return
value?  We can answer this question after we understand gate samples a
little better.

#### The Sample

The {% tooltip label="sample" href="/glossary/sample" /%} of a gate is
the address reserved for storing the argument(s) to the Hoon function.
Although we don't know about addressing yet, you saw above that `+2`
referred to the battery.  The sample is always at the head of the gate's
tail, `+6`.  (We'll look at addressing in more depth in [the next
module](/courses/hoon-school/G-trees).)

Let's look at the gate for inc again, paying particular attention to its
sample:

```hoon
> inc
< 1.mgz
  [ a=@
    [our=@p now=@da eny=@uvJ]
    <15.eah 40.lcv 14.tdo 54.dnu 77.mau 236.dqo 51.njr 139.hzy 33.uof 1.pnw %138>
  ]
>
```

We see `a=@`.  This may not be totally clear, but at least the `@`
should make a little sense.  This is the pretty-printer's way of
indicating an atom with the face `a`.  Let's take a closer look:

```hoon
> +6:inc
a=0
```

We see now that the sample of `inc` is the value `0`, and has `a` as a
{% tooltip label="face" href="/glossary/face" /%}.  This is a
placeholder value for the function argument.  If you evaluate the `$`
buc arm of `inc` without passing it an argument the placeholder value is
used for the computation, and the return value will thus be `0+1`:

```hoon
> $:inc
1
```

The placeholder value, as you saw in the previous module, is sometimes
called the {% tooltip label="bunt" href="/glossary/bunt" /%} value.  The
bunt value is determined by the input type; for `@` atoms the bunt value
is typically `0`.

The face value of `a` comes from the way we defined the gate above:
`|=(a=@ (add 1 a))`.  This was so we can use `a` to refer to the sample
to generate the product with `(add 1 a)`.

#### The Context

The context of a gate contains other data that may be necessary for the
`$` buc arm to evaluate correctly.  The context is always located at the
tail of the tail of the gate, i.e., `+7` of the gate.  There is no
requirement for the context to have any particular arrangement, though
often it does.

Let's look at the context of inc:

```hoon
> +7:inc
[ [ our=~nec
    now=~2024.5.8..17.14.52..ef1e
      eny
    0v304.vhjvs.406g0.bn6ph.ggd02.buadd.2lot0.va6q0.fiqb1.a96gj.9jmb2.6kk07.5d75s.thpbg.9idrt.vmg9j.e748l.fea0l.7ckcf.ieesj.7q6lr
  ]
  <15.eah 40.ihi 14.tdo 54.xjm 77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
]
```

This is the default Dojo subject from before we put `inc` into the
subject. The `|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%} expression defines
the context as whatever the subject is.  This guarantees that the
context has all the information it needs to have for the `$` buc arm to
work correctly.

#### Gates Define Functions of the Sample

The value of a function's output depends solely upon the input value.
This is one of the features that make functions desirable in many
programming contexts.  It's worth going over how Hoon function calls
implement this feature.

In Hoon, one can use `(gate arg)` syntax to make a function call. For
example:

```hoon
> (inc 234)
235
```

The name of the gate is `inc`.  How is the `$` buc arm of inc evaluated?
When a function call occurs, a copy of the `inc` gate is created, but
with one modification:  the sample is replaced with the function
argument.  Then the `$` buc arm is computed against this modified
version of the `inc` gate.

Remember that the default or “bunt” value of the sample of inc is `0`.
In the function call above, a copy of the `inc` gate is made but with a
sample value of `234`.  When `$` buc is computed against this modified
core, the product is `235`.

Notice that neither the arm nor the context is modified before the arm
is evaluated.  That means that the only part of the gate that changes
before the arm evaluation is the {% tooltip label="sample"
href="/glossary/sample" /%}.  Hence, we may understand each gate as
defining a function whose argument is the sample.  If you call a gate
with the same sample, you'll get the same value returned to you every
time.

Let's unbind inc to keep the subject tidy:

```hoon
> =inc

> inc
-find.inc
```

#### Modifying the Context of a Gate

It is possible to modify the context of a gate when you make a function
call; or, to be more precise, it's possible to call a _mutant copy_ of
the gate in which the context is modified.  To illustrate this let's use
another example gate.  Let's write a gate which uses a value from the
context to generate the product.  Bind `b` to the value 10:

```hoon
> =b 10

> b
10
```

Now let's write a gate called `ten` that adds `b` to the input value:

```hoon
> =ten |=(a=@ (add a b))

> (ten 10)
20

> (ten 20)
30

> (ten 25)
35
```

We can unbind `b` from the Dojo subject, and `ten` works just as well
because it's using a copy of `b` stored its context:

```hoon
> =b

> (ten 15)
25

> (ten 35)
45

> b.+14.ten
10
```

We can use `ten(b 25)` to produce a variant of `ten`.  Calling this
mutant version of ten causes a different value to be returned than we'd
get with a normal `ten` call:

```hoon
> (ten(b 25) 10)
35

> (ten(b 1) 25)
26

> (ten(b 75) 100)
175
```

Before finishing the lesson let's unbind ten:

```hoon
> =ten
```

### Recursion

_Recursion_ refers to a return to the same logical point in a program
again and again.  It's a common pattern for solving certain problems in
most programming languages, and Hoon is no exception.

In the following code, the `|-` {% tooltip label="barhep"
href="/language/hoon/reference/rune/bar#--barhep" /%} {% tooltip
label="trap" href="/glossary/trap" /%} serves as the point of recursion,
and the return to that point (with changes) is indicated by the `%=`
centis.  All this code does is count to the given number, then return
that number.

```hoon {% copy=true %}
|=  n=@ud
=/  index  0
|-
?:  =(index n)
  index
%=($ index +(index))
```

We are using the `+` irregular syntax for the `.+` {% tooltip
label="dotlus" href="/language/hoon/reference/rune/dot#-dotlus" /%}
rune, which increments a value (adds one).

In a formal sense, we have to make sure that there is always a base
case, a way of actually ending the recursion—if there isn't, we end up
with an [infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)!

You need to make sure when you compose a {% tooltip label="trap"
href="/glossary/trap" /%} that it has a base case which returns a noun.
The following trap results in an infinite loop:

```hoon {% copy=true %}
=/  index  1
|-
?:  (lth index 1)  ~
$(index +(index))
```

Recursion can be set up different ways.  A full treatment requires
thinking about [algorithmic complexity and
efficiency](https://en.wikipedia.org/wiki/Big_O_notation), but we can
highlight some good rules of thumb here.

#### Tutorial:  The Fibonacci Sequence

For instance, let's talk about calculating the [Fibonacci
sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence), which is a
sequence of numbers wherein each is formed by adding the two previous
numbers together.  Thus 1, 1, 1+1→2, 1+2→3, 2+3→5, and so forth.  We may
write the {% math %}n^\text{th}{% /math %} Fibonacci number in a generic
way as:

{% math block=true %}
F_n = F_{n-1} + F_{n-2}
{% /math %}

and verify that our program correctly produces the sequence of numbers
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ….

- Compose a Fibonacci sequence program which produces a {% tooltip
  label="list" href="/glossary/list" /%} of the appropriate values.

    We can elide some details of working with `list`s until the next
    lesson; simply recall that they are a way of storing multiple values
    in a cell of cells of cells….

    The most naïve version of this calculation simply calculates all
    previous numbers in the sequence every time they are needed.

    ```hoon {% copy=true %}
    |=  n=@ud
    ^-  @ud
    ?:  =(n 1)  1
    ?:  =(n 2)  1
    (add $(n (dec n)) $(n (dec (dec n))))
    ```

    We can use _two_ recursion points for `%=` {% tooltip label="centis"
    href="/language/hoon/reference/rune/cen#-centis" /%}.  The first
    calculate {% math %}F{% /math %} for {% math %}n-1{% /math %}; the
    second calculate {% math %}F{% /math %} for {% math %}n-2{% /math
    %}.  These are then added together.  If we diagram what's happening,
    we can see that each additional number costs as much as the previous
    numbers:

    ```hoon
    (fibonacci 5)
    (add (fibonacci 4) (fibonacci 3))
    (add (add (fibonacci 3) (fibonacci 2)) (add (fibonacci 2) (fibonacci 1)))
    (add (add (add (fibonacci 2) (fibonacci 1)) (fibonacci 2)) (add (fibonacci 2) (fibonacci 1)))
    (add (add (add 1 1) 1) (add 1 1))
    5
    ```

    ```hoon
    (fibonacci 6)
    (add (fibonacci 5) (fibonacci 4))
    ...
    (add (add (add (add (fibonacci 2) (fibonacci 1)) (fibonacci 2)) (add (fibonacci 2) (fibonacci 1))) (add (add (fibonacci 2) (fibonacci 1)) (fibonacci 2)))
    (add (add (add (add 1 1) 1) (add 1 1)) (add (add 1 1) 1))
    8
    ```

    This fully recursive version of the Fibonacci calculation is very
    wasteful because it keeps no intermediate results.

    An improved version stores each value in the sequence as an element
    in a list so that it can be used rather than re-calculated.  We use
    the {% tooltip label="++snoc"
    href="/language/hoon/reference/stdlib/2b#snoc" /%} gate to append a
    noun to a `list`.

    ```hoon {% copy=true %}
    |=  n=@ud
    =/  index  0
    =/  p  0
    =/  q  1
    =/  r  *(list @ud)
    |-  ^-  (list @ud)
    ?:  =(index n)  r
    ~&  >  [index p q r]
    %=  $
      index  +(index)
      p      q
      q      (add p q)
      r      (snoc r q)
    ==
    ```

    (As in an earlier code example, `(add index 1)` can be replaced by
    the Nock increment rune, `.+` {% tooltip label="dotlus"
    href="/language/hoon/reference/rune/dot#-dotlus" /%}.)

    This version is a little more complicated to compare using a diagram
    because of the {% trap, but yields something like this:

    ```hoon
    (fibonacci 5)
    ~[1]
    ~[1 1]
    ~[1 1 2]
    ~[1 1 2 3]
    ~[1 1 2 3 5]
    ```

    The program can be improved somewhat again by appending to the head
    of the cell (rather than using `++snoc`).  This builds a list in a
    backwards order, so we apply the {% tooltip label="++flop"
    href="/language/hoon/reference/stdlib/2b#flop" /%} gate to flip the
    order of the list before we return it.

    ```hoon {% copy=true %}
    |=  n=@ud
    %-  flop
    =/  index  0
    =/  p  0
    =/  q  1
    =/  r  *(list @ud)
    |-  ^-  (list @ud)
    ?:  =(index n)  r
    %=  $
      index  +(index)
      p      q
      q      (add p q)
      r      [q r]
    ==
    ```

    Why are we building the list backwards instead of just producing the
    list in the order we want it in the first place?  Because with
    lists, adding an element to the end is a computationally expensive
    operation that gets more expensive the longer the list is, due to
    the fact that you need to traverse to the end of the tree.  Adding
    an element to the front, however, is cheap.  In Big-O notation,
    adding to the end of a list is _O_(_n_) while adding to the front is
    _O_(1).

    Here's our diagram:

    ```hoon
    (fibonacci 5)
    ~[1]
    ~[1 1]
    ~[2 1 1]
    ~[3 2 1 1]
    ~[5 3 2 1 1]
    ~[1 1 2 3 5]
    ```

    Finally (and then we'll move along) here's a very efficient
    implementation, which starts with a `0` but builds the list entirely
    from cells, then appends the `~` `0` at the end:

    ```hoon {% copy=true %}
    |=  n=@ud
    ^-  (list @ud)
    =/  f0  *@ud
    =/  f1=@ud  1
    :-  0
    |-  ^-  (list @ud)
    ?:  =(n 0)
      ~
    [f1 $(f0 f1, f1 (add f0 f1), n (dec n))]
    ```

    - Produce a diagram of how this last implementation yields a
      Fibonacci sequence for *F*₅, `(fibonacci 5)`.

#### Tutorial:  Tail-Call Optimization of the Factorial Gate

The last factorial gate we produced looked like this:

```hoon {% copy=true %}
|=  n=@ud
?:  =(n 1)
  1
(mul n $(n (dec n)))
```

This example isn't a very efficient use of computing resources.  The
pyramid-shaped illustration from up above approximates what's happening
on the _call stack_, a memory structure that tracks the instructions of
the program.  In our example code, every time a parent gate calls
another gate, the gate being called is "pushed" to the top of the stack
in the form of a frame.  This process continues until a value is
produced instead of a function, completing the stack.

```
                  Push order      Pop order
(fifth frame)         ^               |
(fourth frame)        |               |
(third frame)         |               |
(second frame)        |               |
(first frame)         |               V
```

Once this stack of frames is completed, frames "pop" off the stack
starting at the top.  When a frame is popped, it executes the contained
gate and passes produced data to the frame below it.  This process
continues until the stack is empty, giving us the gate's output.

When a program's final expression uses the stack in this way, it's
considered to be **not tail-recursive**.  This usually happens when the
last line of executable code calls more than one gate, our example
code's `(mul n $(n (dec n)))` being such a case.  That's because such an
expression needs to hold each iteration of `$(n (dec n)` in memory so
that it can know what to run against the `mul` function every time.

To reiterate:  if you have to manipulate the result of a recursion as
the last expression of your gate, as we did in our example, the function
is not tail-recursive, and therefore not very efficient with memory.  A
problem arises when we try to recurse more times than we have space on
the stack.  This will result in our computation failing and producing a
stack overflow.  If we tried to find the factorial of `5.000.000`, for
example, we would almost certainly run out of stack space.

But the Hoon compiler, like most compilers, is smart enough to notice
when the last statement of a parent can reuse the same frame instead of
needing to add new ones onto the stack.  If we write our code properly,
we can use a single frame that simply has its values replaced with each
recursion.

- Change the order of the aspects of the call in such a way that the
  compiler can produce a more
  [tail-recursive](https://en.wikipedia.org/wiki/Tail_call) program.

    With a bit of refactoring, we can write a version of our factorial
    gate that is tail-recursive and can take advantage of this feature:

    ```hoon {% copy=true %}
    |=  n=@ud
    =/  t=@ud  1
    |-
    ^-  @ud
    ?:  =(n 1)  t
    $(n (dec n), t (mul t n))
    ```

    The above code should look familiar.  We are still building a gate
    that takes one argument a `@ud` unsigned decimal integer `n`.  The
    `|-` here is used to create a new gate with one {% tooltip
    label="arm" href="/glossary/arm" /%} `$` and immediately call it.
    As before, think of `|-` as the recursion point.

    We then evaluate `n` to see if it is 1. If it is, we return the
    value of `t`. In case that `n` is anything other than 1, we perform
    our recursion:

    ```hoon {% copy=true %}
    $(n (dec n), t (mul t n))
    ```

    All we are doing here is recursing our new gate and modifying the
    values of `n` and `t`. `t` is used as an accumulator variable that
    we use to keep a running total for the factorial computation.

    Let's use more of our pseudo-Hoon to illustrate how the stack is
    working in this example for the factorial of 5.

    ```
    (factorial 5)
    (|- 5 1)
    (|- 4 5)
    (|- 3 20)
    (|- 2 60)
    (|- 1 120)
    120
    ```

    We simply multiply `t` and `n` to produce the new value of `t`, and
    then decrement `n` before repeating. Since this `$` call is the
    final and solitary thing that is run in the default case and since
    we are doing all computation before the call, this version is
    properly tail-recursive. We don't need to do anything to the result
    of the recursion except recurse it again. That means that each
    iteration can be replaced instead of held in memory.

#### Tutorial:  The Ackermann Function

The [Ackermann
function](https://en.wikipedia.org/wiki/Ackermann_function) is one of
the earliest examples of a function that is both totally
computable—meaning that it can be solved—and not primitively
recursive—meaning it can not be rewritten in an iterative fashion.

{% math block=true %}
\begin{array}{lcl}
\operatorname{A}(0, n) & = & n + 1 \\\\
\operatorname{A}(m+1, 0) & = & \operatorname{A}(m, 1) \\\\
\operatorname{A}(m+1, n+1) & = & \operatorname{A}(m, \operatorname{A}(m+1, n))
\end{array}
{% /math %}

- Compose a gate that computes the Ackermann function.

    ```hoon {% copy=true %}
    |=  [m=@ n=@]
    ^-  @
    ?:  =(m 0)  +(n)
    ?:  =(n 0)  $(m (dec m), n 1)
    $(m (dec m), n $(n (dec n)))
    ```

    This gate accepts two arguments of `@` atom type and yields an atom.

    There are three cases to consider:

    1.  If `m` is zero, return the increment of `n`.
    2.  If `n` is zero, decrement `m`, set `n` to 1 and recurse.
    3.  Else, decrement `m` and set `n` to be the value of the Ackermann
        function with `n` and the decrement of `n` as arguments.

The Ackermann function is not terribly useful in and of itself, but it
has an interesting history in mathematics.  When running this function
the value grows rapidly even for very small input.  The value of
computing this where `m` is `4` and `n` is `2` is an integer with 19,729
digits.

- Calculate some of the {% math %}m{% /math %}/{% math %}n{% /math %}
  pairs given in [the
  table](https://en.wikipedia.org/wiki/Ackermann_function#Table_of_values).

# G-trees.md

---

+++
title = "6. Trees and Addressing"
objectives = ["Address nodes in a tree using numeric notation.", "Address nodes in a tree using lark notation.", "Address data in a tree using faces.", "Distinguish `.` and `:` notation.", "Diagram Hoon structures such as gates into the corresponding abstract syntax tree.", "Use lists to organize data.", "Convert between kinds of lists (e.g. tapes).", "Diagram lists as binary trees.", "Operate on list elements using `snag`, `find`, `weld`, etc.", "Explain how Hoon manages the subject and wing search paths.", "Explain how to skip to particular matches in a wing search path through the subject.", "Identify common Hoon patterns: batteries, and doors, arms, wings, and legs."]
+++

_Every noun in Urbit is an atom or a cell.  This module will elaborate
how we can use this fact to locate data and evaluate code in a given
expression.  It will also discuss the important `list` mold builder and
a number of standard library operations._

##  Trees

Every {% tooltip label="noun" href="/glossary/noun" /%} in Urbit is a
either an {% tooltip label="atom" href="/glossary/atom" /%} or a {%
tooltip label="cell" href="/glossary/cell" /%}.  Since a cell has only
two elements, a head and a tail, we can derive that everything is
representable as a [_binary
tree_](https://en.wikipedia.org/wiki/Binary_tree).  We can draw this
layout naturally:

![Binary tree with labeled nodes](https://media.urbit.org/docs/userspace/hoon-school/binary-tree.png)

A binary tree has a single base node, and each node of the tree may have
up to two child nodes (but it need not have any).  A node without
children is a “leaf”.  You can think of a noun as a binary tree whose
leaves are atoms, i.e., unsigned integers.  All non-leaf nodes are
cells.  An atom is a trivial tree of just one node; e.g., `17`.

For instance, if we produce a cell in the {% tooltip label="Dojo"
href="/glossary/dojo" /%}

```hoon
> =a [[[8 9] [10 11]] [[12 13] [14 15]]]
```

it can be represented as a tree with the contents

![Binary tree with bottom row only populated](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-bottom-row.png)

We will use the convention in these graphics that
black-text-on-white-circle represents an address, and that
green-text-on-black-circle represents the content at that address.  So
another way to represent the same data would be this:

![Binary tree with bottom row only populated](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-bottom-row-full.png)

When we input the above cell representation into the Dojo, the
pretty-printer hides the rightwards-branching `[]` sel/ser brackets.

```hoon
> [[[8 9] [10 11]] [[12 13] [14 15]]]
[[[8 9] 10 11] [12 13] 14 15]
```

We can refer to any data stored anywhere in this tree.  The numbers in
the labeled diagram above are the _numerical addresses_ of the tree, and
may be extended indefinitely downwards into ever-deeper tree
representations.

Most of any possible tree will be unoccupied for any actual data
structure.  For instance, {% tooltip label="lists" href="/glossary/list"
/%} (and thus {% tooltip label="tapes" href="/glossary/tape" /%}) are
collections of values which occupy the tails of cells, leading to a
rightwards-branching tree representation. (Although this may seem
extravagant, it has effectively no bearing on efficiency in and of
itself—that's a function of the algorithms working with the data.)

### Exercise:  Produce a List of Numbers

- Produce a {% tooltip label="generator" href="/glossary/generator" /%}
  called `list.hoon` which accepts a single `@ud` number `n` as input
  and produces a list of numbers from `1` up to (but not including) `n`.
  For example, if the user provides the number `5`, the program will
  produce: `~[1 2 3 4]`.

    ```hoon {% copy=true %}
    |=  end=@
    =/  count=@  1
    |-
    ^-  (list @)
    ?:  =(end count)
      ~
    :-  count
    $(count (add 1 count))
    ```

    In the Dojo:

    ```hoon
    > +list 5
    ~[1 2 3 4]

    > +list 10
    ~[1 2 3 4 5 6 7 8 9]

    > +list 1
    ~
    ```

    OK, we've seen these runes before.  This time we want to focus on
    the list, the thing that's being built here.

    This program works by having each iteration of the list create a
    cell.  In each of these cells, the head—the cell's first position—is
    filled with the current-iteration value of `count`.  The tail of the
    cell, its second position, is filled with _the product of a new
    iteration of our code_ that starts at `|-`.  This iteration will
    itself create another cell, the head of which will be filled by the
    incremented value of `count`, and the tail of which will start
    another iteration.  This process continues until `?:` branches to
    `~` (`null`).  When that happens, it terminates the list and the
    expression ends.  A built-out list of nested cells can be visualized
    like this:

    ```
      [1 [2 [3 [4 ~]]]]

             .
            / \
           1   .
              / \
             2   .
                / \
               3   .
                  / \
                 4   ~
    ```

### Tuples as Trees

What we've been calling a running cell would more conventionally be
named a _tuple_, so we'll switch to that syntax now that the idea is
more familiar.  Basically it's a cell series which doesn't necessarily
end in `~`.

Given the cell `[1 2 3 4 ~]` (or equivalently `~[1 2 3 4]`, an irregular
form for a null-terminated tuple or list), what tree address does each
value occupy?

![A binary tree of the cell [1 2 3 4 ~].](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-1234.png)

At this point, you should start to be able to work this out in your
head, at least for the first few rows.  The `+` lus operator can be used
to return the limb of the subject at a given numeric address.  If there
is no such limb, the result is a crash.

```hoon
> =data ~[1 2 3 4]

> +1:data
[1 2 3 4 ~]

> +2:data
1

> +3:data
[2 3 4 ~]

> +4:data
dojo: hoon expression failed

> +6:data
2

> +7:data
[3 4 ~]

> +14:data
3

> +15:data
[4 ~]

> +30:data
4

> +31:data
~
```

### Lists as Trees

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS140 - Lists.mp4" /%}

We have used lists incidentally.  A {% tooltip label="list"
href="/glossary/list" /%} is an ordered arrangement of elements ending
in a `~` (null).  Most lists have the same kind of content in every
element (for instance, a `(list @rs)`, a list of numbers with a
fractional part), but some lists have many kinds of things within them.
Some lists are even empty.

```hoon
> `(list @)`['a' %b 100 ~]
~[97 98 100]
```

(Notice that all values are converted to the specified {% tooltip
label="aura" href="/glossary/aura" /%}, in this case the empty aura.)

A `list` is built with the `list` mold.  A `list` is actually a _mold
builder_, a {% tooltip label="gate" href="/glossary/gate" /%} that
produces a gate.  This is a common design pattern in Hoon.  (Remember
that a {% tooltip label="mold" href="/glossary/mold" /%} is a type and
can be used as an enforcer:  it attempts to convert any data it receives
into the given structure, and crashes if it fails to do so.)
Lists are commonly written with a shorthand `~[]`:

```hoon
> `(list)`~['a' %b 100]
~[97 98 100]
```

```hoon
> `(list (list @ud))`~[~[1 2 3] ~[4 5 6]]
~[~[1 2 3] ~[4 5 6]]
```

True `list`s have `i` and `t` faces which allow the head and tail of the
data to be quickly and conveniently accessed; the _head_ is the first
element while the _tail_ is everything else.  If something has the same
_structure_ as a `list` but hasn't been explicitly labeled as such, then
Hoon won't always recognize it as a `list`.  In such cases, you'll need
to explicitly mark it as such:

```hoon
> [3 4 5 ~]
[3 4 5 ~]

> `(list @ud)`[3 4 5 ~]
~[3 4 5]

> -:!>([3 4 5 ~])
#t/[@ud @ud @ud %~]

> -:!>(`(list @ud)`[3 4 5 ~])
#t/it(@ud)
```
A null-terminated tuple is almost the same thing as a list.  (That is,
to Hoon all lists are null-terminated tuples, but not all
null-terminated tuples are lists.  This gets rather involved in
subtleties, but you should cast a value as `(list @)` or another type as
appropriate whenever you need a `list`.  See also {% tooltip
label="++limo" href="/language/hoon/reference/stdlib/2b#limo" /%} which
explicitly marks a null-terminated tuple as a `list`.)

##  Addressing Limbs

Everything in Urbit is a binary tree.  And all code in Urbit is also
represented as data.  One corollary of these facts is that we can access
any arbitrary part of an expression, gate, {% tooltip label="core"
href="/glossary/core" /%}, whatever, via addressing (assuming proper
permissions, of course).  (In fact, we can even hot-swap parts of cores,
which is how [wet gates](/courses/hoon-school/R-metals#wet-gates) work.)

There are three different ways to access values:

1. [Numeric addressing](/courses/hoon-school/G-trees#numeric-addressing)
   is useful when you know the address, rather like knowing a house's
   street address directly.
2. [Positional
   addressing](/courses/hoon-school/G-trees#positional-addressing-(lark-notation))
   is helpful when you don't want to figure out the room number, but you
   know how to navigate to the value.  This is like knowing the
   directions somewhere even if you don't know the house number.
3. [Wing addressing](/courses/hoon-school/G-trees#wings) is a way of
   attaching a name to the address so that you can access it directly.

### Numeric Addressing

We have already seen numeric addressing used to refer to parts of a
binary tree.

![Binary tree with labeled nodes](https://media.urbit.org/docs/userspace/hoon-school/binary-tree.png)

Since a node is _either_ an atom (value) _or_ a cell (fork), you never
have to decide if the contents of a node is a direct value or a tree:
it just happens.

### Positional Addressing (Lark Notation)

Much like relative directions, one can also state “left, left, right,
left” or similar to locate a particular node in the tree.  These are
written using `-` (left) and `+` (right) alternating with `<` (left) and
`>` (right).

![](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-lark.png)

Lark notation can locate a position in a tree of any size.  However, it
is most commonly used to grab the head or tail of a cell, e.g. in the
_type spear_ (on which [more later](/courses/hoon-school/M-typecheck)):

```hoon {% copy=true %}
-:!>('hello Mars')
```

Lark notation is not preferred in modern Hoon for more than one or two
elements deep, but it can be helpful when working interactively with a
complicated data structure like a JSON data object.

When lark expressions resolve to the part of the subject containing an
{% tooltip label="arm" href="/glossary/arm" /%}, they don't evaluate the
arm.  They simply return the indicated noun fragment of the subject, as
if it were a leg.

## Wings

One can also identify a resource by a label, called a {% tooltip
label="wing" href="/glossary/wing" /%}.  A wing represents a depth-first
search into the current {% tooltip label="subject"
href="/glossary/subject" /%} (context).  A wing is a limb resolution
path into the subject. A wing expression indicates the path as a series
of limb expressions separated by the `.` character. E.g.,

```hoon {% copy=true %}
inner-limb.outer-limb.limb
```

You can read this as `inner-limb` in `outer-limb` in `limb`, etc.
Notice that these read left-to-right!

A wing is a resolution path pointing to a limb.  It's a search path,
like an index to a particular labeled part of the subject.

Here are some examples:

```hoon
> c.b:[[4 a=5] b=[c=14 15]]
14

> b.b:[b=[a=1 b=2 c=3] a=11]
2

> a.b:[b=[a=1 b=2 c=3] a=11]
1

> c.b:[b=[a=1 b=2 c=3] a=11]
3

> a:[b=[a=1 b=2 c=3] a=11]
11

> b.a:[b=[a=1 b=2 c=3] a=11]
-find.b.a

> g.s:[s=[c=[d=12 e='hello'] g=[h=0xff i=0b11]] r='howdy']
[h=0xff i=0b11]

> c.s:[s=[c=[d=12 e='hello'] g=[h=0xff i=0b11]] r='howdy']
[d=12 e='hello']

> e.c.s:[s=[c=[d=12 e='hello'] g=[h=0xff i=0b11]] r='howdy']
'hello'

> +3:[s=[c=[d=12 e='hello'] g=[h=0xff i=0b11]] r='howdy']
r='howdy'

> r.+3:[s=[c=[d=12 e='hello'] g=[h=0xff i=0b11]] r='howdy']
'howdy'
```

To locate a value in a named tuple data structure:

```hoon
> =data [a=[aa=[aaa=[1 2] bbb=[3 4]] bb=[5 6]] b=[7 8]]

> -:aaa.aa.a.data
1
```

A wing is a limb resolution path into the subject.  This definition
includes as a trivial case a path of just one limb.  Thus, all limbs are
wings, and all limb expressions are wing expressions.

We mention this because it is convenient to refer to all limbs and
non-trivial wings as simply “wings”.

### Names and Faces

A name can resolve either an arm or a leg of the subject.  Recall that
arms are for computations and legs are for data.  When a name resolves
to an arm, the relevant computation is run and the product of the
computation is produced.  When a limb name resolves to a leg, the value
of that leg is produced.

Hoon doesn't have variables like other programming languages do; it has
{% tooltip label="faces" href="/glossary/face" /%}.  Faces are like
variables in certain respects, but not in others.  Faces play various
roles in Hoon, but most frequently faces are used simply as labels for
legs.

A face is a limb expression that consists of a series of alphanumeric
characters.  A face has a combination of lowercase letters, numbers, and
the `-` character. Some example faces: `b`, `c3`, `var`,
`this-is-kebab-case123`. Faces must begin with a letter.

There are various ways to affix a face to a limb of the subject, but for
now we'll use the simplest method: `face=value`.  An expression of this
form is equivalent in value to simply `value`.  Hoon registers the given
`face` as metadata about where the value is stored in the subject, so
that when that face is invoked later its data is produced.

Now we have several ways to access values:

```hoon
> b=5
b=5

> [b=5 cat=6]
[b=5 cat=6]

> -:[b=5 cat=6]
b=5

> b:[b=5 cat=6]
5

> b2:[[4 b2=5] [cat=6 d=[14 15]]]
5

> d:[[4 b2=5] [cat=6 d=[14 15]]]
[14 15]
```

To be clear, `b=5` is equivalent in value to `5`, and `[[4 b2=5] [cat=6
d=[14 15]]]` is equivalent in value to `[[4 5] 6 14 15]`. The faces are
not part of the underlying noun; they're stored as metadata about
address values in the subject.

```hoon
> (add b=5 1)
6
```

If you use a face that isn't in the subject you'll get a `find.[face]`
crash:

```hoon
> a:[b=12 c=14]
-find.a
[crash message]
```

You can even give faces to faces:

```hoon
> b:[b=c=123 d=456]
c=123
```

### Duplicate Faces

There is no restriction against using the same face name for multiple
limbs of the subject. This is one way in which faces aren't like
ordinary variables:

```hoon
> [[4 b=5] [b=6 b=[14 15]]]
[[4 b=5] b=6 b=[14 15]]

> b:[[4 b=5] [b=6 b=[14 15]]]
5
```

Why does this return `5` rather than `6` or `[14 15]`?  When a face is
evaluated on a subject, a head-first binary tree search occurs starting
at address `1` of the subject.  If there is no matching face for address
`n` of the subject, first the head of `n` is searched and then `n`'s
tail.  The complete search path for `[[4 b=5] [b=6 b=[14 15]]]` is:

1.  `[[4 b=5] [b=6 b=[14 15]]]`
2.  `[4 b=5]`
3.  `4`
4.  `b=5`
5.  `[b=6 b=[14 15]]`
6.  `b=6`
7.  `b=[14 15]`

There are matches at steps 4, 6, and 7 of the total search path, but the
search ends when the first match is found at step 4.

The children of legs bearing names aren't included in the search path.
For example, the search path of `[[4 a=5] b=[c=14 15]]` is:

1.  `[[4 a=5] b=[c=14 15]]`
2.  `[4 a=5]`
3.  `4`
4.  `a=5`
5.  `b=[c=14 15]`

Neither of the legs `c=14` or `15` is checked. Accordingly, a search for
`c` of `[[4 a=5] b=[c=14 15]]` fails:

```hoon
> c:[[4 b=5] [b=6 b=[c=14 15]]]
-find.c [crash message]
```

In any programming paradigm, good names are valuable and collisions
(repetitions, e.g. a list named `list`) are likely.  There is no
restriction against using the same face name for multiple limbs of the
subject.  This is one way in which faces aren't like ordinary variables.
If multiple values match a particular face, we need a way to distinguish
them.  In other words, there are cases when you don't want the limb of
the first matching face.  You can ‘skip’ the first match by prepending
`^` to the face.  Upon discovery of the first match at address `n`, the
search skips `n` (as well as its children) and continues the search
elsewhere:

```hoon
> ^b:[[4 b=5] [b=6 b=[14 15]]]
6
```

Recall that the search path for this noun is:

1.  `[[4 b=5] [b=6 b=[14 15]]]`
2.  `[4 b=5]`
3.  `4`
4.  `b=5`
5.  `[b=6 b=[14 15]]`
6.  `b=6`
7.  `b=[14 15]`

The second match in the search path is step 6, `b=6`, so the value at
that leg is produced. You can stack `^` characters to skip more than one
matching face:

```hoon
> a:[[[a=1 a=2] a=3] a=4]
1

> ^a:[[[a=1 a=2] a=3] a=4]
2

> ^^a:[[[a=1 a=2] a=3] a=4]
3

> ^^^a:[[[a=1 a=2] a=3] a=4]
4
```

When a face is skipped at some address `n`, neither the head nor the
tail of `n` is searched:

```hoon
> b:[b=[a=1 b=2 c=3] a=11]
[a=1 b=2 c=3]

> ^b:[b=[a=1 b=2 c=3] a=11]
-find.^b
```

The first `b`, `b=[a=1 b=2 c=3]`, is skipped; so the entire head of the
subject is skipped. The tail has no `b`; so `^b` doesn't resolve to a
limb when the subject is `[b=[a=1 b=2 c=3] a=11]`.

How do you get to that `b=2`?  And how do you get to the `c` in `[[4
a=5] b=[c=14 15]]`? In each case you should use a wing.

We say that the inner face has been _shadowed_ when an outer name
obscures it.

If you run into `^$`, don't go look for a `^$` ketbuc rune:  it's
matching the outer `$` buc arm.  `^$` is one way of setting up a `%=` {%
tooltip label="centis" href="/language/hoon/reference/rune/cen#-centis"
/%} loop/recursion of multiple cores with a `|-` {% tooltip
label="barhep" href="/language/hoon/reference/rune/bar#--barhep" /%} {%
tooltip label="trap" href="/glossary/trap" /%} nested inside of a
`|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%} gate, for instance.

### Limb Resolution Operators

There are two symbols we use to search for a face or limb:

- `.` dot resolves the wing path into the current subject.
- `:` col resolves the wing path with the right-hand-side as the
  subject.

Logically, `a:b` is two operations, while `a.b` is one operation.  The
compiler is smart about `:` col wing resolutions and reduces it to a
regular lookup, though.

### What `%=` Does

Now we're equipped to go back and examine the syntax of the `%=` {%
tooltip label="centis" href="/language/hoon/reference/rune/cen#-centis"
/%} rune we have been using for recursion:  it _resolves a wing with
changes_, which in this particular case means that it takes the `$`
(default) arm of the {% tooltip label="trap" href="/glossary/trap" /%}
core, applies certain changes, and re-evaluates the expression.

```hoon {% copy=true %}
|=  n=@ud
|-
~&  n
?:  =(n 1)
  n
%+  mul
  n
$(n (dec n))
```

The `$()` syntax is the commonly-used irregular form of the `%=` {%
tooltip label="centis" href="/language/hoon/reference/rune/cen#-centis"
/%} rune.

Now, we noted that `$` buc is the default arm for the trap.  It turns
out that `$` is also the default arm for some other structures, like the
gate!  That means we can cut out the trap, in the factorial example, and
write something more compact like this:

```hoon {% copy=true %}
|=  n=@ud
?:  =(n 1)
  1
(mul n $(n (dec n)))
```

It's far more common to just use a trap, but you will see `$` buc used
to manipulate a {% tooltip label="core" href="/glossary/core" /%} in
many in-depth code instances.

### Expanding the Runes
 
`|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%} produces a gate.
It actually expands to

```hoon {% copy=true %}
=|  a=spec
|%  ++  $  b=hoon
--
``` 

where `=|` {% tooltip label="tisbar"
href="/language/hoon/reference/rune/tis#-tisbar" /%} means to add its
sample to the current subject with the given {% tooltip label="face"
href="/glossary/face" /%}.

Similarly, `|-` {% tooltip label="barhep"
href="/language/hoon/reference/rune/bar#--barhep" /%} produces a {%
tooltip label="core" href="/glossary/core" /%} with one arm `$`.  How
could you write that in terms of `|%` and `++`?

### Example:  Number to Digits

- Compose a generator which accepts a number as `@ud` unsigned decimal
  and returns a {% tooltip label="list" href="/glossary/list" /%} of its
  digits.

One verbose Hoon program 

```hoon {% copy=true %}
!:
|=  [n=@ud]
=/  values  *(list @ud)
|-  ^-  (list @ud)
?:  (lte n 0)  values
%=  $
  n       (div n 10)
  values  (weld ~[(mod n 10)] values)
==
```

Save this as a file `/gen/num2dig.hoon`, `|commit %base`, and run it:

```hoon
> +num2dig 1.000
~[1 0 0 0]

> +num2dig 123.456.789
~[1 2 3 4 5 6 7 8 9]
```

A more idiomatic solution would use the `^` ket infix to compose a cell
and build the list from the head first.  (This saves a call to {%
tooltip label="++weld" href="/language/hoon/reference/stdlib/2b#weld"
/%}.)

```hoon {% copy=true %}
!:
|=  [n=@ud]
=/  values  *(list @ud)
|-  ^-  (list @ud)
?:  (lte n 0)  values
%=  $
  n       (div n 10)
  values  (mod n 10)^values
==
```

A further tweak maps to `@t` ASCII characters instead of the digits.

```hoon {% copy=true %}
!:
|=  [n=@ud]
=/  values  *(list @t)
|-  ^-  (list @t)
?:  (lte n 0)  values
%=  $
  n       (div n 10)
  values  (@t (add 48 (mod n 10)))^values
==
```

(Notice that we apply `@t` as a {% tooltip label="mold"
href="/glossary/mold" /%} gate rather than using the tic notation.  This
is because `^` ket is a rare case where the order of evaluation of
operators would cause the intuitive writing to fail.)

- Extend the above {% tooltip label="generator"
  href="/glossary/generator" /%} so that it accepts a cell of type and
  value (a `vase` as produced by the `!>` {% tooltip label="zapgar"
  href="/language/hoon/reference/rune/zap#-zapgar" /%} rune).  Use the
  type to determine which number base the digit string should be
  constructed from; e.g. `+num2dig !>(0xdead.beef)` should yield `~['d'
  'e' 'a' 'd' 'b' 'e' 'e' 'f']`.

## List operations

Once you have your data in the form of a `list`, there are a lot of
tools available to manipulate and analyze the data:

- The {% tooltip label="++flop"
  href="/language/hoon/reference/stdlib/2b#flop" /%} function reverses
  the order of the elements (exclusive of the `~`):
  
    ```hoon
    > (flop ~[1 2 3 4 5])
    ~[5 4 3 2 1]
    ```

- The {% tooltip label="++sort"
  href="/language/hoon/reference/stdlib/2b#sort" /%} function uses a
  `list` and a comparison function (like {% tooltip label="++lth"
  href="/language/hoon/reference/stdlib/1a#lth" /%}) to order things:

    ```hoon
    > (sort ~[1 3 5 2 4] lth)
    ~[1 2 3 4 5]
    ```

- The {% tooltip label="++snag"
  href="/language/hoon/reference/stdlib/2b#snag" /%} function takes an
  index and a `list` to grab out a particular element (note that it
  starts counting at zero):

    ```hoon
    > (snag 0 `(list @)`~[11 22 33 44])
    11

    > (snag 1 `(list @)`~[11 22 33 44])
    22
    
    > (snag 3 `(list @)`~[11 22 33 44])
    44
    
    > (snag 3 "Hello!")
    'l'
    
    > (snag 1 "Hello!")
    'e'
    
    > (snag 5 "Hello!")
    '!'
    ```

- The {% tooltip label="++weld"
  href="/language/hoon/reference/stdlib/2b#weld" /%} function takes two
  lists of the same type and concatenates them:

    ```hoon
    > (weld ~[1 2 3] ~[4 5 6])
    ~[1 2 3 4 5 6]

    > (weld "Happy " "Birthday!")
    "Happy Birthday!"
    ```

There are a couple of sometimes-useful `list` builders:

- The {% tooltip label="++gulf"
  href="/language/hoon/reference/stdlib/2b#gulf" /%} function spans
  between two numeric values (inclusive of both):

    ```hoon
    > (gulf 5 10)  
    ~[5 6 7 8 9 10]
    ```

- The {% tooltip label="++reap"
  href="/language/hoon/reference/stdlib/2b#reap" /%} function repeats a
  value many times in a `list`:

    ```hoon
    > (reap 5 0x0)
    ~[0x0 0x0 0x0 0x0 0x0]

    > (reap 8 'a')
    <|a a a a a a a a|>

    > `tape`(reap 8 'a')
    "aaaaaaaa"

    > (reap 5 (gulf 5 10))
    ~[~[5 6 7 8 9 10] ~[5 6 7 8 9 10] ~[5 6 7 8 9 10] ~[5 6 7 8 9 10] ~[5 6 7 8 9 10]]
    ```

- The {% tooltip label="++roll"
  href="/language/hoon/reference/stdlib/2b#roll" /%} function takes a
  list and a {% tooltip label="gate" href="/glossary/gate" /%}, and
  accumulates a value of the list items using that gate. For example, if
  you want to add or multiply all the items in a list of atoms, you
  would use roll:

    ```hoon
    > (roll `(list @)`~[11 22 33 44 55] add)
    165

    > (roll `(list @)`~[11 22 33 44 55] mul)
    19.326.120
    ```

Once you have a `list` (including a {% tooltip label="tape"
href="/glossary/tape" /%}), there are a lot of manipulation tools you
can use to extract data from it or modify it:

- The {% tooltip label="++lent"
  href="/language/hoon/reference/stdlib/2b#lent" /%} function takes
  `[a=(list)]` and gets the number of elements (length) of the list
- The {% tooltip label="++find"
  href="/language/hoon/reference/stdlib/2b#find" /%} function takes
  `[nedl=(list) hstk=(list)]` and locates a sublist (`nedl`, needle) in
  the list (`hstk`, haystack)
- The {% tooltip label="++snap"
  href="/language/hoon/reference/stdlib/2b#snap" /%} function takes
  `[a=(list) b=@ c=*]` and replaces the element at an index in the list
  (zero-indexed) with something else
- The {% tooltip label="++scag"
  href="/language/hoon/reference/stdlib/2b#scag" /%} function takes
  `[a=@ b=(list)]` and produces the first _a_ elements from the front of
  the list
- The {% tooltip label="++slag"
  href="/language/hoon/reference/stdlib/2b#slag" /%} function takes
  `[a=@ b=(list)]` and produces all elements of the list including and
  after the element at index _a_

There are a few more that you should pick up eventually, but these are
enough to get you started.

Using what we know to date, most operations that we would do on a
collection of data require a trap.

- Roll-Your-Own-`++weld`:

    ```hoon {% copy=true %}
    ::  /gen/weld.hoon
    ::
    |=  [a=(list @) b=(list @)]
    |-  ^-  (list @)
    ?~  a  b
    [i.a $(a t.a)]
    ```

- `++lent` expressions

    Running each one in the Dojo:

    ```hoon
    > (lent ~[1 2 3 4 5])
    5

    > (lent ~[~[1 2] ~[1 2 3] ~[2 3 4]])
    3

    > (lent ~[1 2 (weld ~[1 2 3] ~[4 5 6])])
    3
    ```

- Palindrome

    ```hoon
    ::  palindrome.hoon
    ::
    |=  a=(list)
    =(a (flop a))
    ```

# H-libraries.md

---

+++
title = "9. Text Processing I"
objectives = ["Review Unicode text structure.", "Distinguish cords and tapes and their characteristics.", "Transform and manipulate text using text conversion arms.", "Interpolate text.", "Employ sigpam logging levels.", "Create a `%say` generator.", "Identify how Dojo sees and interprets a generator as a cell with a head tag.", "Identify the elements of a `sample` for a `%say` generator.", "Produce a `%say` generator with optional arguments."]
+++

_This module will discuss how text is represented in Hoon, discuss tools
for producing and manipulating text, and introduce the `%say` generator,
a new generator type.  We don't deal with formatted text (`tank`s) or
parsers here, deferring that discussion.  Formatted text and text
parsing are covered [in a later
module](/courses/hoon-school/P-stdlib-io)._

##  Text in Hoon

We've incidentally used `'messages written as cords'` and `"as tapes"`,
but aside from taking a brief look at how {% tooltip label="lists"
href="/glossary/list" /%} (and thus {% tooltip label="tapes"
href="/glossary/tape" /%}) work with tree addressing, we haven't
discussed why these differ or how text works more broadly.

There are four basic ways to represent text in Urbit:

- `@t`, a {% tooltip label="cord" href="/glossary/cord" /%}, which is an
  {% tooltip label="atom" href="/glossary/atom" /%} (single value)
- `@ta`, a `knot` used for URL-safe path elements, which is an atom
  (single value)
- `@tas`, a `term` used primarily for constants, which is an atom
  (single value)
- `tape`, which is a `(list @t)`

This is more ways than many languages support:  most languages simply
store text directly as a character array, or list of characters in
memory.  Colloquially, we would only call cords and tapes
[_strings_](https://en.wikipedia.org/wiki/String_%28computer_science%29),
however.

What are the applications of each?

### `@t` `cord`

One way to handle text is to assign a code value to each letter, then
represent these as subsequent values in memory.  (Think, for instance,
of [Morse code](https://en.wikipedia.org/wiki/Morse_code).)  On all
modern computers, the numeric values used for each letter are given by
the [ASCII](https://en.wikipedia.org/wiki/ASCII) standard, which defines
128 unique characters (2⁷ = 128).

```
65  83  67  73  73
A   S   C   I   I
```

A {% tooltip label="cord" href="/glossary/cord" /%} simply shunts these
values together in one-byte-wide slots and represents them as an
integer.

```hoon
> 'this is a cord'
'this is a cord'

> `@`'this is a cord'
2.037.307.443.564.446.887.986.503.990.470.772
```

It's very helpful to use the `@ux` {% tooltip label="aura"
href="/glossary/aura" /%} if you are trying to see the internal
structure of a `cord`.  Since the ASCII values align at the 8-bit wide
characters, you can see each character delineated by a hexadecimal pair.

```hoon
> `@ux`'HELLO'
0x4f.4c4c.4548

> `@ub`'HELLO'
0b100.1111.0100.1100.0100.1100.0100.0101.0100.1000
```

You can think of this a couple of different ways.  One way is to simple
think of them as chained together, with the first letter in the
rightmost position.  Another is to think of them as values multipled by
a “place value”:

| Letter | ASCII | Place | “Place Value” |
| ------ | ----- | ----- | ------------- |
| `H`    | 0x48  | 0     | 2⁰ = 1 → 0x48 |
| `E`    | 0x45  | 1     | 2⁸ = 256 = 0x100 → 0x4500 |
| `L`    | 0x4c  | 2     | 2¹⁶ = 65.536 = 0x1.0000 → 0x4c.0000 |
| `L`    | 0x4c  | 3     | 2²⁴ = 16.777.216 = 0x100.0000 → 0x4c00.0000 |
| `O`    | 0x4f  | 4     | 2³² = 4.294.967.296 = 0x1.0000.0000 → 0x4f.0000.0000 |

This way, each value slots in after the preceding value.

Special characters (non-ASCII, beyond the standard keyboard, basically)
are represented using a more complex numbering convention.
[Unicode](https://en.wikipedia.org/wiki/Unicode) defines a standard
specification for _code points_ or numbers assigned to characters, and a
few specific bitwise _encodings_ (such as the ubiquitous UTF-8).  Urbit
uses UTF-8 for `@t` values (thus both `cord` and `tape`).

### `(list @t)` `tape`

There are some tools to work with atom `cord`s of text, but most of the
time it is more convenient to unpack the atom into a {% tooltip
label="tape" href="/glossary/tape" /%}.  A `tape` splits out the
individual characters from a `cord` into a `list` of character values.

![](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-tape.png)

We've hinted a bit at the structure of `list`s before; for now the main
thing you need to know is that they are cells which end in a `~` sig.
So rather than have all of the text values stored sequentially in a
single atom, they are stored sequentially in a rightwards-branching
binary tree of cells.

A tape is a list of `@tD` atoms (i.e., characters).  (The upper-case
character at the end of the {% tooltip label="aura"
href="/glossary/aura" /%} hints that the `@t` values are D→3 so 2³=8
bits wide.)

```hoon
> "this is a tape"
"this is a tape"

> `(list @)`"this is a tape"
~[116 104 105 115 32 105 115 32 97 32 116 97 112 101]
```

Since a {% tooltip label="tape" href="/glossary/tape" /%} is a `(list
@tD)`, all of the `list` tools we have seen before work on them.

### `@ta` `knot`

If we restrict the character set to certain ASCII characters instead of
UTF-8, we can use this restricted representation for system labels as
well (such as URLs, file system paths, permissions).  `@ta` `knot`s and
`@tas` `term`s both fill this role for Hoon.

```hoon
> `@ta`'hello'
~.hello
```

Every valid `@ta` is a valid `@t`, but `@ta` does not permit spaces or a
number of other characters.  (See `++sane`, discussed below.)

### `@tas` `term`

A further tweak of the ASCII-only concept, the `@tas` `term` permits
only “text constants”, values that are first and foremost only
_themselves_.

> [`@tas` permits only] a restricted text atom for Hoon constants. The
> only characters permitted are lowercase ASCII letters, `-`, and `0-9`,
> the latter two of which cannot be the first character. The syntax for
> `@tas` is the text itself, always preceded by `%`. The empty `@tas` has
> a special syntax, `$`.

`term`s are rarely used for message-like text, but they are used all the
time for internal labels in code.  They differ from regular text in a
couple of key ways that can confuse you until you're used to them.

For instance, a `@tas` value is also a mold, and the value will _only_
match its own mold, so they are commonly used with [type
unions](/courses/hoon-school/N-logic) to filter for acceptable values.

```hoon
> ^-  @tas  %5
mint-nice
-need.@tas
-have.%5
nest-fail
dojo: hoon expression failed

> ^-  ?(%5)  %5
%5

> (?(%5) %5)
%5
```

For instance, imagine creating a function to ensure that only a certain
[classical element](https://en.wikipedia.org/wiki/Classical_element) can
pass through a gate.  (This gate is superfluous given how molds work,
but it shows off a point.)

```hoon {% copy=true %}
|=  input=@t
=<
(validate-element input)
|%
+$  element  ?(%earth %air %fire %water)
++  validate-element
  |=  incoming=@t
  %-  element  incoming
--
```

(See how that `=<` {% tooltip label="tisgal"
href="/language/hoon/reference/rune/tis#-tisgal" /%} works with the
helper {% tooltip label="core?" href="/glossary/core" /%})


##  Text Operations

Text-based data commonly needs to be _produced_, _manipulated_, or
_analyzed_ (including parsing).

### Producing Text

String interpolation puts the result of an expression directly into a
`tape`:

```hoon
> "{<(add 5 6)>} is the answer."
"11 is the answer."
```

The {% tooltip label="++weld"
href="/language/hoon/reference/stdlib/2b#weld" /%} function can be used
to glue two `tape`s together:

```hoon
> (weld "Hello" "Mars!")
"HelloMars!"
```

```hoon {% copy=true %}
|=  [t1=tape t2=tape]
^-  tape
(weld t1 t2)
```

### Manipulating Text

If you have text but you need to change part of it or alter its form,
you can use standard library `list` operators like {% tooltip
label="++flop" href="/language/hoon/reference/stdlib/2b#flop" /%} as
well as `tape`-specific arms.

Applicable `list` operations—some of which you've seen before—include:

- The {% tooltip label="++flop"
  href="/language/hoon/reference/stdlib/2b#flop" /%} function takes a
  list and returns it in reverse order:

    ```hoon
    > (flop "Hello!")
    "!olleH"

    > (flop (flop "Hello!"))
    "Hello!"
    ```

- The {% tooltip label="++sort"
  href="/language/hoon/reference/stdlib/2b#sort" /%} function uses the
  [quicksort algorithm](https://en.wikipedia.org/wiki/Quicksort) to sort
  a list.  It takes a `list` to sort and a gate that serves as a
  comparator.  For example, if you want to sort the list `~[37 62 49 921
  123]` from least to greatest, you would pass that list along with
  the {% tooltip label="++lth" href="/language/hoon/reference/stdlib/1a#lth"
  /%} gate (for “less than”):

    ```hoon
    > (sort ~[37 62 49 921 123] lth)
    ~[37 49 62 123 921]
    ```

    To sort the list from greatest to least, use the gth gate ("greater than") as the basis of comparison instead:

    ```hoon
    > (sort ~[37 62 49 921 123] gth)
    ~[921 123 62 49 37]
    ```

    You can sort letters this way as well:

    ```hoon
    > (sort ~['a' 'f' 'e' 'k' 'j'] lth)
    <|a e f j k|>
    ```

    The function passed to sort must produce a flag, i.e., `?`.

- The {% tooltip label="++weld"
  href="/language/hoon/reference/stdlib/2b#weld" /%} function takes two
  lists of the same type and concatenates them:

    ```hoon
    > (weld "Happy " "Birthday!")
    "Happy Birthday!"
    ```

    It does not inject a separator character like a space.

- The {% tooltip label="++snag"
  href="/language/hoon/reference/stdlib/2b#snag" /%} function takes an
  atom `n` and a list, and returns the `n`th item of the list, where 0
  is the first item:

    ```hoon
    > (snag 3 "Hello!")
    'l'

    > (snag 1 "Hello!")
    'e'

    > (snag 5 "Hello!")
    '!'
    ```

- The {% tooltip label="++oust"
  href="/language/hoon/reference/stdlib/2b#oust" /%} function takes a
  pair of atoms `[a=@ b=@]` and a list, and returns the list with b
  items removed, starting at item a:

    ```hoon
    > (oust [0 1] `(list @)`~[11 22 33 44])
    ~[22 33 44]

    > (oust [0 2] `(list @)`~[11 22 33 44])
    ~[33 44]

    > (oust [1 2] `(list @)`~[11 22 33 44])
    ~[11 44]

    > (oust [2 2] "Hello!")
    "Heo!"
    ```

- The {% tooltip label="++lent"
  href="/language/hoon/reference/stdlib/2b#lent" /%} function takes a
  list and returns the number of items in it:

    ```hoon
    > (lent ~[11 22 33 44])
    4

    > (lent "Hello!")
    6
    ```

The foregoing are {% tooltip label="list" href="/glossary/list" /%}
operations.  The following, in contrast, are {% tooltip label="tape"
href="/glossary/tape" /%}-specific operations:

- The {% tooltip label="++crip"
  href="/language/hoon/reference/stdlib/4b#crip" /%} function converts a
  `tape` to a `cord` (`tape`→`cord`).

    ```hoon
    > (crip "Mars")
    'Mars'
    ```

- The {% tooltip label="++trip"
  href="/language/hoon/reference/stdlib/4b#trip" /%} function converts a
  `cord` to a `tape` (`cord`→`tape`).

    ```hoon
    > (trip 'Earth')
    "Earth"
    ```

- The {% tooltip label="++cass"
  href="/language/hoon/reference/stdlib/4b#cass" /%} function: convert
  upper-case text to lower-case (`tape`→`tape`)

    ```hoon
    > (cass "Hello Mars")
    "hello mars"
    ```

- The {% tooltip label="++cuss"
  href="/language/hoon/reference/stdlib/4b#cuss" /%} function: convert
  lower-case text to upper-case (`tape`→`tape`)

    ```hoon
    > (cuss "Hello Mars")
    "HELLO MARS"
    ```

### Analyzing Text

Given a string of text, what can you do with it?

1. Search
2. Tokenize
3. Convert into data

#### Search

- The {% tooltip label="++find"
  href="/language/hoon/reference/stdlib/2b#find" /%} function takes
  `[nedl=(list) hstk=(list)]` and locates a sublist (`nedl`, needle) in
  the list (`hstk`, haystack).  (`++find` starts counting from zero.)

    ```hoon
    > (find "brillig" "'Twas brillig and the slithy toves")
    [~ 6]
    ```

    `++find` returns a `unit`, which right now means that we need to
    distinguish between nothing found (`~` null) and zero `[~ 0]`.
    `unit`s are discussed in more detail in [a later
    lesson](/courses/hoon-school/L-struct).

#### Tokenize/Parse

To _tokenize_ text is to break it into pieces according to some rule.
For instance, to count words one needs to break at some delimiter.

```
"the sky above the port was the color of television tuned to a dead channel"
 1   2   3     4   5    6   7   8     9  10         11    12 13 14  15
```

##  Exercise: Break Text at a Space

Hoon has a very powerful text parsing engine, built to compile Hoon
itself.  However, it tends to be quite obscure to new learners.  We can
build a simple one using `list` tools.

- Compose a {% tooltip label="gate" href="/glossary/gate" /%} which
  parses a long `tape` into smaller `tape`s by splitting the text at
  single spaces.  For example, given a `tape`
 
    ```hoon {% copy=true %}
    "the sky above the port was the color of television tuned to a dead channel"
    ```
    
    the gate should yield
    
    ```hoon
    ~["the" "sky" "above" "the" ...]
    ```
    
    To complete this, you'll need {% tooltip label="++scag"
    href="/language/hoon/reference/stdlib/2b#scag" /%} and {% tooltip
    label="++slag" href="/language/hoon/reference/stdlib/2b#slag" /%}
    (who sound like villainous henchmen from a children's cartoon).

    ```hoon {% copy=true %}
    |=  ex=tape
    =/  index  0  
    =/  result  *(list tape)  
    |-  ^-  (list tape)  
    ?:  =(index (lent ex))  
      (weld result ~[`tape`(scag index ex)])
    ?:  =((snag index ex) ' ')  
      $(index 0, ex `tape`(slag +(index) ex), result (weld result ~[`tape`(scag index ex)]))    
    $(index +(index))
    ```

#### Convert

If you have a Hoon value and you want to convert it into text as such,
use {% tooltip label="++scot"
href="/language/hoon/reference/stdlib/4m#scot" /%} and {% tooltip
label="++scow" href="/language/hoon/reference/stdlib/4m#scow" /%}.
These call for a value of type `+$dime`, which means the `@tas`
equivalent of a regular aura.  These are labeled as returning `cord`s
(`@t`s) but in practice seem to return `knot`s (`@ta`s).

- The {% tooltip label="++scot"
  href="/language/hoon/reference/stdlib/4m#scot" /%} function renders a
  `dime` as a `cord` (`dime`→`cord`); the user must include any
  necessary aura transformation.

    ```hoon
    > `@t`(scot %ud 54.321)
    '54.321'

    > `@t`(scot %ux 54.000)  
    '0xd2f0'
    ```

    ```hoon
    > (scot %p ~sampel-palnet)
    ~.~sampel-palnet

    > `@t`(scot %p ~sampel-palnet)
    '~sampel-palnet'
    ```

- The {% tooltip label="++scow"
  href="/language/hoon/reference/stdlib/4m#scow" /%} function renders a
  `dime` as a `tape` (`dime`→`tape`); it is otherwise identical to {%
  tooltip label="++scot" href="/language/hoon/reference/stdlib/4m#scot"
  /%}.

- The {% tooltip label="++sane"
  href="/language/hoon/reference/stdlib/4b#sane" /%} function checks the
  validity of a possible text string as a `knot` or `term`.  The usage
  of `++sane` will feel a bit strange to you:  it doesn't apply directly
  to the text you want to check, but it produces a gate that checks for
  the aura (as `%ta` or `%tas`).  (The gate-builder is a fairly common
  pattern in Hoon that we've started to hint at by using molds.)
  `++sane` is also not infallible yet.

    ```hoon
    > ((sane %ta) 'ångstrom')
    %.n

    > ((sane %ta) 'angstrom')
    %.y

    > ((sane %tas) 'ångstrom')
    %.n

    > ((sane %tas) 'angstrom')
    %.y
    ```

    Why is this sort of check necessary?  Two reasons:

    1.  `@ta` `knot`s and `@tas` `term`s have strict rules, such as
        being ASCII-only.
    2.  Not every sequence of bits has a conversion to a text
        representation.  That is, ASCII and Unicode have structural
        rules that limit the possible conversions which can be made.  If
        things don't work, you'll get a `%bad-text` response.

        ```hoon
        > 0x1234.5678.90ab.cdef
        0x1234.5678.90ab.cdef
        > `@t`0x1234.5678.90ab.cdef
        [%bad-text "[39 239 205 171 144 120 86 52 92 49 50 39 0]"]
        ```

    There's a minor bug in Hoon that will let you produce an erroneous
    `term` (`@tas`):

    ```hoon
    > `@tas`'hello mars'
    %hello mars
    ```

    Since a `@tas` cannot include a space, this is formally incorrect,
    as `++sane` reveals:

    ```hoon
    > ((sane %tas) 'hello')  
    %.y
    
    > ((sane %tas) 'hello mars')
    %.n
    ```

##  Logging

The most time-honored method of debugging is to simply output relevant
values at key points throughout a program in order to make sure they are
doing what you think they are doing.  To this end, we introduced `~&` {%
tooltip label="sigpam" href="/language/hoon/reference/rune/sig#-sigpam"
/%} in the last lesson.

The `~&` {% tooltip label="sigpam"
href="/language/hoon/reference/rune/sig#-sigpam" /%} rune offers some
finer-grained output options than just printing a simple value to the
screen.  For instance, you can use it with string interpolation to
produce detailed error messages.

There are also `>` modifiers which can be included to mark “debugging
levels”, really just color-coding the output:

1.  No `>`:  regular
2.  `>`:  information
3.  `>>`:  warning
4.  `>>>`:  error

(Since all `~&` sigpam output is a side effect of the compiler, it
doesn't map to the Unix [`stdout`/`stderr`
streams](https://en.wikipedia.org/wiki/Standard_streams) separately;
it's all `stdout`.)

You can use these to differentiate messages when debugging or otherwise
auditing the behavior of a generator or library.  Try these in your own
Dojo:

```hoon
> ~&  'Hello Mars!'  ~  
'Hello Mars!'
~  

> ~&  >  'Hello Mars!'  ~  
>   'Hello Mars!'  
~  

> ~&  >>  'Hello Mars!'  ~  
>>  'Hello Mars!'  
~  

> ~&  >>>  'Hello Mars!'  ~  
>>> 'Hello Mars!'  
~
```

# K-doors.md

---

+++
title = "10. Cores and Doors"
weight = 20
nodes = [150, 155]
objectives = ["Identify the structure of a door and relate it to a core.", "Pull an arm in a door.", "Build cores for later use and with custom samples.", "Identify the `$` buc arm in several structures and its role."]
+++

_Hoon is statically typed, which means (among other things) that {%
tooltip label="auras" href="/glossary/aura" /%} are subject to strict
nesting rules, {% tooltip label="molds" href="/glossary/mold" /%} are
crash-only, and the whole thing is rather cantankerous about matching
types.  However, since gate-building arms are possible, Hoon developers
frequently employ them as templates to build type-appropriate {% tooltip
label="cores" href="/glossary/core" /%}, including {% tooltip
label="gates" href="/glossary/gate" /%}.  This module will start by
introducing the concept of gate-building gates; then it will expand our
notion of cores to include {% tooltip label="doors"
href="/glossary/door" /%}; finally it will introduce a common door,
the {% tooltip label="++map" href="/language/hoon/reference/stdlib/2o#map"
/%}, to illustrate how doors work._

##  Gate-Building Gates

### Calling Gates

There are two ways of making a function call in Hoon. First, you can
call a gate in the {% tooltip label="subject" href="/glossary/subject"
/%} by name.  For instance, we can produce a gate `inc` which adds `1`
to an input:

```hoon
> =inc |=(a=@ (add 1 a))

> (inc 10)
11

> =inc
```

The second way of making a function call involves an expression that
_produces_ a gate on demand:

```hoon
> (|=(a=@ (add 1 a)) 123)
124

> (|=(a=@ (mul 2 a)) 123)
246
```

The difference is subtle:  the first case has an already-created gate in
the subject when we called it, while the latter involves producing a
gate that doesn't exist anywhere in the subject, and then calling it.

Are calls to {% tooltip label="++add"
href="/language/hoon/reference/stdlib/1a#add" /%} and {% tooltip
label="++mul" href="/language/hoon/reference/stdlib/1a#mul" /%} of the
Hoon standard library of the first kind, or the second?

```hoon
> (add 12 23)
35

> (mul 12 23)
276
```

They're of the second kind.  Neither `++add` nor `++mul` resolves to a
gate directly; they're each {% tooltip label="arms" href="/glossary/arm"
/%} that _produce_ gates.

Often the difference doesn't matter much. Either way you can do a
function call using the `(gate arg)` syntax.

It's important to learn the difference, however, because for certain use
cases you'll want the extra flexibility that comes with having an
already produced {% tooltip label="core" href="/glossary/core" /%} in
the subject.

### Building Gates

Let's make a core with arms that build {% tooltip label="gates"
href="/glossary/gate" /%} of various kinds.  As we did in a previous
lesson, we'll use the `|%` {% tooltip label="barcen"
href="/language/hoon/reference/rune/bar#-barcen" /%} rune.  Copy and
paste the following into the {% tooltip label="Dojo"
href="/glossary/dojo" /%}:

```hoon {% copy=true %}
=c |%
++  inc      |=(a=@ (add 1 a))
++  add-two  |=(a=@ (inc (inc a)))
++  double   |=(a=@ (mul 2 a))
++  triple   |=(a=@ (mul 3 a))
--
```

Let's try out these arms, using them for function calls:

```hoon
> (inc:c 10)
11

> (add-two:c 10)
12

> (double:c 10)
20

> (triple:c 10)
30
```

Notice that each {% tooltip label="arm" href="/glossary/arm" /%} in core
`c` is able to call the other arms of `c`—`++add-two` uses the `++inc`
arm to increment a number twice.  As a reminder, each arm is evaluated
with its parent core as the {% tooltip label="subject"
href="/glossary/subject" /%}.  In the case of `++add-two` the parent
core is `c`, which has `++inc` in it.

#### Mutating a Gate

Let's say you want to modify the default {% tooltip label="sample"
href="/glossary/sample" /%} of the gate for `double`. We can infer the
default sample by calling `double` with no argument:

```hoon
> (double:c)
0
```

Given that `a x 2 = 0`, `a` must be `0`. (Remember that `a` is the face
for the `double` sample, as defined in the core we bound to `c` above.)

Let's say we want to mutate the `++double` gate so that the default
sample is `25`. There is only one problem:  `++double` isn't a gate!

```hoon
> double.c(a 25)
-tack.a
-find.a
dojo: hoon expression failed
```

It's an arm that produces a gate, and `a` cannot be found in `++double`
until the gate is created.  Furthermore, every time the gate is created,
it has the default sample, `0`.  If you want to mutate the gate produced
by `++double`, you'll first have to put a copy of that gate into the
subject:

```hoon
> =double-copy double:c

> (double-copy 123)
246
```

Now let's mutate the sample to `25`, and check that it worked with `+6`.
(The sample lives at `+6` in a given {% tooltip label="core"
href="/glossary/core" /%} tree.)

```hoon
> +6:double-copy(a 25)
a=25
```

Good. Let's call it with no argument and see if it returns double the
value of the modified {% tooltip label="sample" href="/glossary/sample"
/%}.

```hoon
> (double-copy(a 25))
50
```

It does indeed. Unbind `c` and `double-copy`:

```hoon
> =c

> =double-copy
```

Contrast this with the behavior of {% tooltip label="++add"
href="/language/hoon/reference/stdlib/1a#add" /%}. We can look at the
sample of the gate for `add` with `+6:add`:

```hoon
> +6:add
[a=0 b=0]
```

If you try to mutate the default sample of `++add`, it won't work:

```hoon
> add(a 3)
-tack.a
-find.a
dojo: hoon expression failed
```

As before with `++double`, Hoon can't find an `a` to modify in a {%
tooltip label="gate" href="/glossary/gate" /%} that doesn't exist yet.

### Slamming a Gate

If you check the docs on our now-familiar `%-` {% tooltip label="cenhep"
href="/language/hoon/reference/rune/cen#-cenhep" /%}, you'll find that
it is actually sugar syntax for another {% tooltip label="rune"
href="/glossary/rune" /%}:

> This rune is for evaluating the `$` arm of a gate, i.e., calling a
> gate as a function. `a` is the gate, and `b` is the desired sample value
> (i.e., input value) for the gate.
>
> ```hoon {% copy=true %}
> %~($ a b)
> ```

So all gate calls actually pass back through `%~` {% tooltip
label="censig" href="/language/hoon/reference/rune/cen#-censig" /%}.
What's the difference?

The `%~` {% tooltip label="censig"
href="/language/hoon/reference/rune/cen#-censig" /%} rune accepts three
children, a wing which resolves to an arm in a {% tooltip label="door"
href="/glossary/door" /%}; the aforesaid door; and a `sample` for the
door.

Basically, whenever you use `%-` {% tooltip label="cenhep"
href="/language/hoon/reference/rune/cen#-cenhep" /%}, it actually looks
up a wing in a door using `%~` {% tooltip label="censig"
href="/language/hoon/reference/rune/cen#-censig" /%}, which is a more
general type of core than a gate.  Whatever that wing resolves to is
then provided a {% tooltip label="sample" href="/glossary/sample" /%}.
The resulting Hoon expression is evaluated and the value is returned.


##  Doors

{% tooltip label="Doors" href="/glossary/door" /%} are another kind of
{% tooltip label="core" href="/glossary/core" /%} whose {% tooltip
label="arms" href="/glossary/arm" /%} evaluate to make {% tooltip
label="gates" href="/glossary/gate" /%}, as we just discovered.  The
difference is that a door also has its own {% tooltip label="sample"
href="/glossary/sample" /%}. A door is the most general case of a
function in Hoon.  (You could say a "gate-building core" or a
"function-building function" to clarify what the intent of most of these
are.)

A core is a {% tooltip label="cell" href="/glossary/cell" /%} of code
and data, called `[battery payload]`.  The {% tooltip label="battery"
href="/glossary/battery" /%} contains a series of arms, and the {%
tooltip label="payload" href="/glossary/payload" /%} contains all the
data necessary to run those arms correctly.

A _door_ is a core with a sample.  That is, a door is a core whose
payload is a cell of {% tooltip label="sample" href="/glossary/sample"
/%} and context:  `[sample context]`.  A door's overall sample can
affect how its gate-building arms work.

```
        door
       /    \
battery      .
            / \
      sample   context
```

It follows from this definition that a gate is a special case of a door.
A gate is a door with exactly one arm, named `$` buc.

Doors are created with the `|_` {% tooltip label="barcab"
href="/language/hoon/reference/rune/bar#_-barcab" /%} rune.  Doors get
used for a few different purposes in the standard library:

- instrumenting and storing persistent data structures like `map`s (this module and the next)
- implementing state machines (the [subject-oriented programming module](/courses/hoon-school/O-subject))

One BIG pitfall for thinking about doors is thinking of them as
“containing” gates, as if they were more like “objects”.  Instead, think
of them the same way as you think of gates, just that they can be
altered at a higher level.

#### Example:  The Quadratic Equation

First, a mathematical example.  If we wanted to calculate a quadratic
polynomial, _y = a x² + b x + c_, then we need to know two kinds of
things:  the unknown or variable _x_, AND the parameters _a_, _b_, and
_c_.  These aren't really the same kind of thing.  When we calculate a
particular curve _y_(_x_), we assume that the parameters _a_, _b_, and
_c_ stay constant across evaluations of _x_, and it's inconvenient for
us to specify them every single time.

If we were to build this as a gate, we would need to pass in four parameters:

```hoon
> =poly-gate |=  [x=@ud a=@ud b=@ud c=@ud]
(add (add (mul a (mul x x)) (mul b x)) c)
```

Any time we call the gate, we have to provide all four values:  one
unknown, three parameters.  But there's a sense in which we want to
separate the three parameters and only call the gate with one _x_ value.
One way to accomplish this is to wrap the gate inside of another:

```hoon
> =wrapped-gate |=  [x=@ud]
=/  a  5
=/  b  4
=/  c  3
(poly-gate x a b c)
```

If we built this as a door instead, we could push the parameters out to
a different layer of the structure.  In this case, the parameters are
the {% tooltip label="sample" href="/glossary/sample" /%} of the door,
while the arm `++quad` builds a gate that corresponds to those
parameters and only accepts one unknown variable `x`.  To make a door we
use the `|_` {% tooltip label="barcab"
href="/language/hoon/reference/rune/bar#_-barcab" /%} rune, which we'll
discuss later:

```hoon
> =poly |_  [a=@ud b=@ud c=@ud]
++  quad
  |=  x=@ud
  (add (add (mul a (mul x x)) (mul b x)) c)
--
```

This will be used in two steps:  a gate-building step then a gate usage
step.

We produce a gate from a door's arm using the `%~` {% tooltip
label="censig" href="/language/hoon/reference/rune/cen#-censig" /%}
rune, almost always used in its irregular form, `~()`.  Here we prime
the door with `[5 4 3]`, which yields a gate:

```hoon {% copy=true %}
~(quad poly [5 4 3])
```

By itself, not so much to say.  We could pin it into the {% tooltip
label="Dojo" href="/glossary/dojo" /%}, for instance, to use later.  Our
ultimate goal is to use the built gate on particular data, however:

```hoon
> (~(quad poly [5 4 3]) 2)
31
```

By hand:  5×2² + 4×2 + 3 = 31, so that's correct.

Doors will enable us to build some very powerful data storage tools by
letting us defer parts of a gate calculation to other stages of building
and calculating the gate.

#### Example:  A Calculator

Let's unpack what's going on more with this next {% tooltip label="door"
href="/glossary/door" /%}.  Each of the {% tooltip label="arms"
href="/glossary/arm" /%} in this example door will define a simple gate.
Let's bind the door to `c`.  To make a door we use the `|_` {% tooltip
label="barcab" href="/language/hoon/reference/rune/bar#_-barcab" /%}
rune:

```hoon {% copy=true %}
=c |_  b=@
++  plus  |=(a=@ (add a b))
++  times  |=(a=@ (mul a b))
++  greater  |=(a=@ (gth a b))
--
```

If you type this into the dojo manually, make sure you attend carefully
to the spacing. Feel free to cut and paste the code, if desired.

Before getting into what these arms do, let's digress into how the
`|_` {% tooltip label="barcab"
href="/language/hoon/reference/rune/bar#_-barcab" /%} rune works in
general.

`|_` {% tooltip label="barcab"
href="/language/hoon/reference/rune/bar#_-barcab" /%} works exactly like
the `|%` {% tooltip label="barcen"
href="/language/hoon/reference/rune/bar#-barcen" /%} rune for making a
core, except that it takes one additional daughter expression, the
door's {% tooltip label="sample" href="/glossary/sample" /%}.  Following
that are a series of `++` {% tooltip label="luslus"
href="/language/hoon/reference/rune/lus#-luslus" /%} runes, each of
which defines an arm of the door. Finally, the expression is terminated
with a `--` {% tooltip label="hephep"
href="/language/hoon/reference/rune/terminators#---hephep" /%} rune.

A door really is, at the bedrock level, the same thing as a {% tooltip
label="core" href="/glossary/core" /%} with a {% tooltip label="sample"
href="/glossary/sample" /%}.  Let's ask Dojo to pretty print a simple
door.

```hoon
> =a =>  ~  |_  b=@  ++  foo  b  --

> a
<1.zgd [b=@ %~]>
```

Dojo tells us that `a` is a core with one arm and a {% tooltip
label="payload" href="/glossary/payload" /%} of `[b=@ %~]`.  Since a
door's payload is `[sample context]`, this means that `b` is the sample
and the context is null.  (The `=> ~` set the context.  We did this to
avoid including the standard library that is included in the context by
default in Dojo, which would have made the pretty-printed core much more
verbose.  Try it without `=>  ~` as well.)

For the {% tooltip label="door" href="/glossary/door" /%} defined above,
`c`, the sample is defined as an `@` {% tooltip label="atom"
href="/glossary/atom" /%} and given the face `b`.  The `++plus` arm
defines a {% tooltip label="gate" href="/glossary/gate" /%} that takes a
single atom as its argument `a` and returns the sum of `a` and `b`.  The
`++times` arm defines a gate that takes a single atom `a` and returns
the product of `a` and `b`. The `++greater` arm defines a gate that
takes a single atom `a`, and returns `%.y` if `a` is greater than `b`;
otherwise it returns `%.n`.

Let's try out the arms of `c` with ordinary function calls:

```hoon
> (plus:c 10)
10

> (times:c 10)
0

> (greater:c 10)
%.y
```

This works, but the results are not exciting.  Passing `10` to the
`plus` gate returns `10`, so it must be that the value of `b` is `0`
(the bunt value of `@`).  The products of the other function calls
reinforce that assessment.  Let's look directly at `+6` of `c` to see
the sample:

```hoon
> +6:c
b=0
```

Having confirmed that `b` is `0`, let's mutate the `c` sample and then
call its arms:

```hoon
> (plus:c(b 7) 10)
17

> (times:c(b 7) 10)
70

> (greater:c(b 7) 10)
%.y

> (greater:c(b 17) 10)
%.n
```

Doing the same mutation repeatedly can be tedious, so let's bind `c` to
the modified version of the door, where `b` is `7`:

```hoon
> =c c(b 7)

> (plus:c 10)
17

> (times:c 10)
70

> (greater:c 10)
%.y
```

There's a more direct way of passing arguments for both the door sample
and the gate sample simultaneously. We may use the `~(arm door arg)`
syntax. This generates the `arm` product after modifying the `door`'s
sample to be `arg`.

```hoon
> (~(plus c 7) 10)
17

> (~(times c 7) 10)
70

> (~(greater c 7) 10)
%.y

> (~(greater c 17) 10)
%.n
```

Readers with some mathematical background may notice that `~( )`
expressions allow us to [curry](https://en.wikipedia.org/wiki/Currying).
For each of the arms above, the `~( )` expression is used to create
different versions of the same gate:

```hoon
> ~(plus c 7)
< 1.xpd
  [ a=@
    < 3.bnz
      [ b=@
        [our=@p now=@da eny=@uvJ]
        <15.eah 40.ihi 14.tdo 54.xjm 77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
      ]
    >
  ]
>

> b:~(plus c 7)
7

> b:~(plus c 17)
17
```

Thus, you may think of the `c` door as a function for making functions.
Use the `~(arm c arg)` syntax—`arm` defines which kind of gate is
produced (i.e., which arm of the door is used to create the gate), and
`arg` defines the value of `b` in that gate, which in turn affects the
product value of the gate produced.

The standard library provides [currying
functionality](/courses/hoon-school/Q-func) outside of the context of
doors.

#### Creating Doors with a Modified Sample

In the above example we created a {% tooltip label="door"
href="/glossary/door" /%} `c` with {% tooltip label="sample"
href="/glossary/sample" /%} `b=@` and found that the initial value of
`b` was `0`, the bunt value of `@`. We then created new door from `c` by
modifying the value of `b`. But what if we wish to define a door with a
chosen sample value directly? We make use of the `$_` {% tooltip
label="buccab" href="/language/hoon/reference/rune/buc#_-buccab" /%}
rune, whose irregular form is simply `_`. To create the door `c` with
the sample `b=@` set to have the value `7` in the dojo, we would write

```hoon {% copy=true %}
=c |_  b=_7
++  plus  |=(a=@ (add a b))
++  times  |=(a=@ (mul a b))
++  greater  |=(a=@ (gth a b))
--
```

Here the type of `b` is inferred to be `@` based on the example value `7`, similar to how we've seen casting done by example.  You will learn more about how types are inferred in the [next module](/courses/hoon-school/L-struct).

##  Key-Value Pairs:  `map` as Door

In general terms, a {% tooltip label="map"
href="/language/hoon/reference/stdlib/2o#map" /%} is a pattern from a
key to a value.  You can think of a dictionary, or an index, or a data
table.  Essentially it scans for a particular key, then returns the data
associated with that key (which may be any {% tooltip label="noun"
href="/glossary/noun" /%}).

| Key         | Value      |
| ----------- | ---------- |
| 'Mazda'     | 'RX-8'     |
| 'Dodge'     | 'Viper'    |
| 'Ford'      | 'Mustang'  |
| 'Chevrolet' | 'Chevelle' |
| 'Porsche'   | 'Boxster'  |
| 'Bugatti'   | 'Type 22'  |

While `map` is the {%tooltip label="mold" href="/glossary/mold" /%} or
type of the value, the {% tooltip label="door" href="/glossary/door" /%}
which affords `map`-related functionality is named {% tooltip
label="++by" href="/language/hoon/reference/stdlib/2i#by" /%}.  (This
felicitously affords us a way to read `map` operations in an
English-friendly phrasing.)

In Urbit, all values are static and never change.  (This is why we
“overwrite” or replace the values in a limb to change it with `%=` {%
tooltip label="centis" href="/language/hoon/reference/rune/cen#-centis"
/%}.)  This means that when we build a `map`, we often rather awkwardly
replace it with its modified value explicitly.

We'll build a color `map`, from a `@tas` of a [color's
name](https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors) to
its HTML hexadecimal representation as a `@ux` hex value.

We can produce a `map` from a {% tooltip label="list"
href="/glossary/list" /%} of key-value cells using the {% tooltip
label="++malt" href="/language/hoon/reference/stdlib/2l#malt" /%}
function.  Using `@tas` terms as keys (which is common) requires us to
explicitly mark the list as `(list (pair @tas @ux))`:

```hoon {% copy=true %}
=colors (malt `(list (pair @tas @ux))`~[[%red 0xed.0a3f] [%yellow 0xfb.e870] [%green 0x1.a638] [%blue 0x66ff]])
```

To insert one key-value pair at a time, we use {% tooltip label="put"
href="/language/hoon/reference/stdlib/2i#putby" /%}.  In Dojo, we need
to either pin it into the subject or modify a copy of the map for the
rest of the expression using `=/` {% tooltip label="tisfas"
href="/language/hoon/reference/rune/tis#-tisfas" /%}.

```hoon {% copy=true %}
=colors (~(put by colors) [%orange 0xff.8833])
=colors (~(put by colors) [%violet 0x83.59a3])
=colors (~(put by colors) [%black 0x0])
```

Note the pattern here:  there is a {% tooltip label="++put"
href="/language/hoon/reference/stdlib/2i#putby" /%} arm of {% tooltip
label="++by" href="/language/hoon/reference/stdlib/2i#by" /%} which
builds a gate to modify `colors` by inserting a value.

What happens if we try to add something that doesn't match the type?

```hoon {% copy=true %}
=colors (~(put by colors) [%cerulean '#02A4D3'])
```

We'll see a `mull-grow`, a `mull-nice`, and a {% tooltip
label="nest-fail" href="/language/hoon/reference/hoon-errors#nest-fail"
/%}.  Essentially these are all flavors of mold-matching errors.

(As an aside, `++put:by` is also how you'd replace a key's value.)

The point of a `map` is to make it easy to retrieve data values given
their appropriate key.  Use {% tooltip label="++get:by"
href="/language/hoon/reference/stdlib/2i#getby" /%}:

```hoon
> (~(get by colors) %orange)
[~ 0xff.8833]
```

What is that {% tooltip label="cell" href="/glossary/cell" /%}?  Wasn't
the value stored as `0xff.8833`?  Well, one fundamental problem that
a {% tooltip label="map" href="/language/hoon/reference/stdlib/2o#map" /%}
needs to solve is to allow us to distinguish an _empty_ result (or
failure to locate a value) from a _zero_ result (or an answer that's
actually zero).  To this end, the {% tooltip label="unit"
href="/language/hoon/reference/stdlib/1c#unit" /%} was introduced, a
type union of a `~` (for no result) and `[~ item]` (for when a result
exists).

- What does `[~ ~]` mean when returned from a `map`?

`unit`s are common enough that they have their own syntax and set of
operational functions.  We'll look at them more in [the next
module](/courses/hoon-school/L-struct).

```hoon
> (~(get by colors) %brown)
~
```

({% tooltip label="++got:by"
href="/language/hoon/reference/stdlib/2i#gotby" /%} returns the value
without the `unit` wrapper, but crashes on failure to locate.  I
recommend just using `++get` and extracting the tail of the resulting
cell after confirming it isn't null with `?~` {% tooltip label="wutsig"
href="/language/hoon/reference/rune/wut#-wutsig" /%}.  See also {%
tooltip label="++gut:by" href="/language/hoon/reference/stdlib/2i#gutby"
/%} which allows a default in case of failure to locate.)

You can check whether a key is present using {% tooltip label="++has:by"
href="/language/hoon/reference/stdlib/2i#hasby" /%}:

```hoon
> (~(has by colors) %teal)
%.n

> (~(has by colors) %green)
%.y
```

You can get a list of all keys with {% tooltip label="++key:by"
href="/language/hoon/reference/stdlib/2i#keyby" /%}:

```hoon
> ~(key by colors)
{%black %red %blue %violet %green %yellow %orange}
```

You can apply a gate to each value using {% tooltip label="++run:by"
href="/language/hoon/reference/stdlib/2i#runby" /%}.  For instance,
these gates will break the color hexadecimal value into red, green, and
blue components:

```hoon
> =red |=(a=@ux ^-(@ux (cut 2 [4 2] a)))

> =green |=(a=@ux ^-(@ux (cut 2 [2 2] a)))

> =blue |=(a=@ux ^-(@ux (cut 2 [0 2] a)))

> (~(run by colors) blue)
{ [p=%black q=0x0]  
 [p=%red q=0x3f]  
 [p=%blue q=0xff]  
 [p=%violet q=0xa3]  
 [p=%green q=0x38]  
 [p=%yellow q=0x70]  
 [p=%orange q=0x33]  
}
```

#### Tutorial:  Caesar Cipher

The Caesar cipher is a shift cipher ([that was indeed used
anciently](https://en.wikipedia.org/wiki/Caesar_cipher)) wherein each
letter in a message is encrypted by replacing it with one shifted some
number of positions down the alphabet.  For example, with a
“right-shift” of `1`, `a` would become `b`, `j` would become `k`, and
`z` would wrap around back to `a`.

Consider the message below, and the cipher that results when we
Caesar-shift the message to the right by 1.

```
Plaintext message:    "do not give way to anger"
Right-shifted cipher: "ep opu hjwf xbz up bohfs"
```

Below is a generator that performs a Caesar cipher on a {% tooltip
label="tape" href="/glossary/tape" /%}.  This example isn't the most
compact implementation of such a cipher in Hoon, but it demonstrates
important principles that more laconic code would not.  Save it as
`/gen/caesar.hoon` on your `%base` {% tooltip label="desk"
href="/glossary/desk" /%}.

**/gen/caesar.hoon**

```hoon {% copy=true mode="collapse" %}
!:
|=  [msg=tape steps=@ud]
=<
=.  msg  (cass msg)
:-  (shift msg steps)
    (unshift msg steps)
::
|%
++  alpha  "abcdefghijklmnopqrstuvwxyz"
::  Shift a message to the right.
::
++  shift
  |=  [message=tape steps=@ud]
  ^-  tape
  (operate message (encoder steps))
::  Shift a message to the left.
::
++  unshift
  |=  [message=tape steps=@ud]
  ^-  tape
  (operate message (decoder steps))
::  Rotate forwards into encryption.
::
++  encoder
  |=  [steps=@ud]
  ^-  (map @t @t)
  =/  value-tape=tape  (rotation alpha steps)
  (space-adder alpha value-tape)
::  Rotate backwards out of encryption.
::
++  decoder
  |=  [steps=@ud]
  ^-  (map @t @t)
  =/  value-tape=tape  (rotation alpha steps)
  (space-adder value-tape alpha)
::  Apply the map of decrypted->encrypted letters to the message.
::
++  operate
  |=  [message=tape shift-map=(map @t @t)]
  ^-  tape
  %+  turn  message
  |=  a=@t
  (~(got by shift-map) a)
::  Handle spaces in the message.
::
++  space-adder
  |=  [key-position=tape value-result=tape]
  ^-  (map @t @t)
  (~(put by (map-maker key-position value-result)) ' ' ' ')
::  Produce a map from each letter to its encrypted value.
::
++  map-maker
  |=  [key-position=tape value-result=tape]
  ^-  (map @t @t)
  =|  chart=(map @t @t)
  ?.  =((lent key-position) (lent value-result))
    ~|  %uneven-lengths  !!
  |-
  ?:  |(?=(~ key-position) ?=(~ value-result))
    chart
  $(chart (~(put by chart) i.key-position i.value-result), key-position t.key-position, value-result t.value-result)
::  Cycle an alphabet around, e.g. from
::  'ABCDEFGHIJKLMNOPQRSTUVWXYZ' to 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
::
++  rotation
  |=  [my-alphabet=tape my-steps=@ud]
  =/  length=@ud  (lent my-alphabet)
  =+  (trim (mod my-steps length) my-alphabet)
  (weld q p)
--
```

This generator takes two arguments:  a {% tooltip label="tape"
href="/glossary/tape" /%}, which is your plaintext message, and an
unsigned integer, which is the shift-value of the cipher.  It produces a
cell of two `tape`s:  one that has been shifted right by the value, and
another that has been shifted left.  It also converts any uppercase
input into lowercase.

Try it out in the Dojo:

```hoon
> +caesar ["abcdef" 1]
["bcdefg" "zabcde"]

> +caesar ["test" 2]
["vguv" "rcqr"]

> +caesar ["test" 26]
["test" "test"]

> +caesar ["test" 28]
["vguv" "rcqr"]

> +caesar ["test" 104]
["test" "test"]

> +caesar ["tESt" 2]
["vguv" "rcqr"]

> +caesar ["test!" 2]
nest-fail
```

##### Examining the Code

Let's examine our caesar.hoon code piece by piece. We won't necessarily
go in written order; instead, we'll cover code in the intuitive order of
the program.  For each chunk that we cover, try to read and understand
the code itself before reading the explanation.

There are a few {% tooltip label="runes" href="/glossary/rune" /%} in
this which we haven't seen yet; we will deal with them incidentally in
the commentary.

```hoon {% copy=true %}
!:
|=  [msg=tape steps=@ud]
=<
```

The `!:` {% tooltip label="zapcol"
href="/language/hoon/reference/rune/zap#-zapcol" /%} in the first line
of the above code enables a full stack trace in the event of an error.

`|= [msg=tape steps=@ud]` creates a {% tooltip label="gate"
href="/glossary/gate" /%} that takes a {% tooltip label="cell"
href="/glossary/cell" /%}. The head of this cell is a `tape`, which is a
string type that's a list of `cord`s. Tapes are represented as text
surrounded by double-quotes, such as this: `"a tape"`. We give this
input tape the face `msg`. The tail of our cell is a `@ud` -- an
unsigned decimal {% tooltip label="atom" href="/glossary/atom" /%} --
that we give the {% tooltip label="face" href="/glossary/face" /%}
`steps`.

`=<` {% tooltip label="zapgal"
href="/language/hoon/reference/rune/tis#-tisgal" /%} is the rune that
evaluates its first child expression with respect to its second child
expression as the {% tooltip label="subject" href="/glossary/subject"
/%}. In this case, we evaluate the expressions in the code chunk below
against the {% tooltip label="core" href="/glossary/core" /%} declared
later, which allows us reference the core's contained {% tooltip
label="arms" href="/glossary/arm" /%} before they are defined. Without
`=<`, we would need to put the code chunk below at the bottom of our
program. In Hoon, as previously stated, we always want to keep the
longer code towards the bottom of our programs - `=<` helps us do that.

```hoon {% copy=true %}
=.  msg  (cass msg)
:-  (shift msg steps)
    (unshift msg steps)
```

`=. msg (cass msg)` changes the input string `msg` to lowercases.
`=.` {% tooltip label="tisdot"
href="/language/hoon/reference/rune/tis#-tisdot" /%} changes the leg of
the subject to something else. In our case, the leg to be changed is
`msg`, and the thing to replace it is `(cass msg)`. `cass` is a
standard-library gate that converts uppercase letters to lowercase.

`:- (shift msg steps)` and `(unshift msg steps)` simply composes a {%
tooltip label="cell" href="/glossary/cell" /%} of a right-shifted cipher
and a left-shifted cipher of our original message. We will see how this
is done using the {% tooltip label="core" href="/glossary/core" /%}
described below, but this is the final output of our {% tooltip
label="generator" href="/glossary/generator" /%}. We have indented the
lower line, which is not strictly good Hoon style but makes the intent
clearer.

```hoon {% copy=true %}
|%
```

`|%` {% tooltip label="barcen"
href="/language/hoon/reference/rune/bar#-barcen" /%} creates a {%
tooltip label="core" href="/glossary/core" /%}, the second child of
`=<` {% tooltip label="tisgal"
href="/language/hoon/reference/rune/tis#-tisgal" /%}. Everything after
`|%` is part of that second child `core`, and will be used as the
subject of the first child of `=<`, described above. The various parts,
or {% tooltip label="arms" href="/glossary/arm" /%}, of the `core` are
denoted by `++` {% tooltip label="luslus"
href="/language/hoon/reference/rune/lus#-luslus" /%} beneath it, for
instance:

```hoon {% copy=true %}
++  rotation
  |=  [my-alphabet=tape my-steps=@ud]
  =/  length=@ud  (lent my-alphabet)
  =+  (trim (mod my-steps length) my-alphabet)
  (weld q p)
```

The `++rotation` arm takes takes a specified number of characters off of
a {% tooltip label="tape" href="/glossary/tape" /%} and puts them on the
end of the tape. We're going to use this to create our shifted alphabet,
based on the number of `steps` given as an argument to our gate.

`|= [my-alphabet=tape my-steps=@ud]` creates a gate that takes two
arguments: `my-alphabet`, a `tape`, and `my-steps`, a `@ud`.

`=/ length=@ud (lent my-alphabet)` stores the length of `my-alphabet` to
make the following code a little clearer.

The {% tooltip label="++trim"
href="/language/hoon/reference/stdlib/4b#trim" /%} gate from the
standard library splits a tape into two parts at a specified position.
So `=+ (trim (mod my-steps length) my-alphabet)` splits the tape
`my-alphabet` into two parts, `p` and `q`, which are now directly
available in the {% tooltip label="subject" href="/glossary/subject"
/%}. We call the modulus operation `mod` to make sure that the point at
which we split our `tape` is a valid point inside of `my-alphabet` even
if `my-steps` is greater than `length`, the length of `my-alphabet`. Try
trim in the dojo:

```hoon
> (trim 2 "abcdefg")
[p="ab" q="cdefg"]

> (trim 4 "yourbeard")
[p="your" q="beard"]
```

`(weld q p)` uses {% tooltip label="++weld"
href="/language/hoon/reference/stdlib/2b#weld" /%}, which combines two
strings into one. Remember that `trim` has given us a split version of
`my-alphabet` with `p` being the front half that was split off of
`my-alphabet` and `q` being the back half. Here we are welding the two
parts back together, but in reverse order: the second part `q` is welded
to the front, and the first part `p` is welded to the back.

```hoon {% copy=true %}
++  map-maker
  |=  [key-position=tape value-result=tape]
  ^-  (map @t @t)
  =|  chart=(map @t @t)
  ?.  =((lent key-position) (lent value-result))
    ~|  %uneven-lengths  !!
  |-
  ?:  |(?=(~ key-position) ?=(~ value-result))
    chart
  $(chart (~(put by chart) i.key-position i.value-result), key-position t.key-position, value-result t.value-result)
```

The `++map-maker` arm, as the name implies, takes two tapes and creates
a {% tooltip label="map" href="/language/hoon/reference/stdlib/2o#map"
/%} out of them. A `map` is a type equivalent to a dictionary in other
languages: it's a data structure that associates a key with a value. If,
for example, we wanted to have an association between `a` and 1 and `b`
and 2, we could use a `map`.

`|= [a=tape b=tape]` builds a gate that takes two tapes, `a` and `b`, as
its sample.

`^- (map @t @t)` casts the gate to a `map` with a `cord` (or `@t`) key
and a `cord` value.

You might wonder, if our gate in this arm takes `tape`s, why then are we
producing a map of `cord` keys and values?

As we discussed earlier, a {% tooltip label="tape" href="/glossary/tape"
/%} is a list of `cord`s. In this case what we are going to do is map a
single element of a `tape` (either our alphabet or shifted-alphabet) to
an element of a different `tape` (either our shifted-alphabet or our
alphabet). This pair will therefore be a pair of `cord`s. When we go to
use this `map` to convert our incoming `msg`, we will take each element
(`cord`) of our `msg` `tape`, use it as a `key` when accessing our `map`
and get the corresponding `value` from that position in the `map`. This
is how we're going to encode or decode our `msg` `tape`.

`=| chart=(map @t @t)` adds a {% tooltip label="noun"
href="/glossary/noun" /%} to the subject with the default value of the
`(map @t @t)` type, and gives that noun the face `chart`.

`?. =((lent key-position) (lent value-result))` checks if the two
`tape`s are the same length. If not, the program crashes with an error
message of `%uneven-lengths`, using `~| %uneven-lengths !!`.

If the two `tape`s are of the same length, we continue on to create a
trap. `|-` {% tooltip label="barhep"
href="/language/hoon/reference/rune/bar#--barhep" /%} creates a {%
tooltip label="trap" href="/glossary/trap" /%}, a gate with no arguments
that is called immediately.

`?: |(?=(~ key-position) ?=(~ value-result))` checks if either `tape` is
empty. If this is true, the `map-maker` arm is finished and can return
`chart`, the {% tooltip label="map"
href="/language/hoon/reference/stdlib/2o#map" /%} that we have been
creating.

If the above test finds that the `tape`s are not empty, we trigger a
recursion that constructs our `map`: `$(chart (~(put by chart) i.a i.b),
a t.a, b t.b)`. This code recursively adds an entry in our `map` where
the head of the `tape` `a` maps to the value of the head of `tape` `b`
with `~(put by chart)`, our calling of the {% tooltip label="put"
href="/language/hoon/reference/stdlib/2i#putby" /%} arm of the {%
tooltip label="by" href="/language/hoon/reference/stdlib/2i#by" /%}
map-engine {% tooltip label="core" href="/glossary/core" /%} (note that
`~(<wing> <door> <sample>`) is a shorthand for `%~ <wing> <door>
<sample>` (see the `%~` {% tooltip label="censig"
href="/language/hoon/reference/rune/cen#-censig" /%} documentation for
more information). The recursion also "consumes" those heads with every
iteration by changing `a` and `b` to their tails using `a t.a, b t.b`.

We have three related arms to look at next, `++decoder`, `++encoder`,
and `++space-adder`. `++space-adder` is required for the other two, so
we'll look at it first.

```hoon {% copy=true %}
++  space-adder
  |=  [key-position=tape value-result=tape]
  ^-  (map @t @t)
  (~(put by (map-maker key-position value-result)) ' ' ' ')
```

`|= [key-position=tape value-result=tape]` creates a gate that takes two
`tapes`.

We use the {% tooltip label="put"
href="/language/hoon/reference/stdlib/2i#putby" /%} arm of the {%
tooltip label="by" href="/language/hoon/reference/stdlib/2i#by" /%} core
on the next line, giving it a {% tooltip label="map"
href="/language/hoon/reference/stdlib/2o#map" /%} produced by the
`map-maker` arm that we created before as its {% tooltip label="sample"
href="/glossary/sample" /%}. This adds an entry to the map where the
space character (called `ace`) simply maps to itself. This is done to
simplify the handling of spaces in {% tooltip label="tapes"
href="/glossary/tape" /%} we want to encode, since we don't want to
shift them.

```hoon {% copy=true %}
++  encoder
  |=  [steps=@ud]
  ^-  (map @t @t)
  =/  value-tape=tape  (rotation alpha steps)
  (space-adder alpha value-tape)
++  decoder
  |=  [steps=@ud]
  ^-  (map @t @t)
  =/  key-tape=tape  (rotation alpha steps)
  (space-adder key-tape alpha)
```

`++encoder` and `++decoder` utilize the `rotation` and `space-adder`
arms. These {% tooltip label="gates" href="/glossary/gate" /%} are
essentially identical, with the arguments passed to `space-adder`
reversed. They simplify the two common transactions you want to do in
this program: producing `maps` that we can use to encode and decode
messages.

In both cases, we create a gate that accepts a `@ud` named `steps`.

In `encoder`: `=/ value-tape=tape (rotation alpha steps)` creates a
`value-tape` {% tooltip label="noun" href="/glossary/noun" /%} by
calling `rotation` on `alpha`. `alpha` is our arm which contains a
`tape` of the entire alphabet. The `value-tape` will be the list of
`value`s in our {% tooltip label="map"
href="/language/hoon/reference/stdlib/2o#map" /%}.

In `decoder`: `=/ key-tape (rotation alpha steps)` does the same work,
but when passed to `space-adder` it will be the list of `key`s in our
`map`.

`(space-adder alpha value-tape)`, for `encoder`, and `(space-adder
key-tape alpha)`, for `decoder`, produce a `map` that has the first
argument as the keys and the second as the values.

If our two inputs to `space-adder` were `"abcdefghijklmnopqrstuvwxyz"`
and `"bcdefghijklmnopqrstuvwxyza"`, we would get a `map` where `'a'`
maps to `'b'`, `'b'` to `'c'` and so on. By doing this we can produce a
`map` that gives us a translation between the alphabet and our shifted
alphabet, or vice versa.

Still with us? Good. We are finally about to use all the stuff that
we've walked through.

```hoon {% copy=true %}
++  shift
  |=  [message=tape shift-steps=@ud]
  ^-  tape
  (operate message (encoder shift-steps))
++  unshift
  |=  [message=tape shift-steps=@ud]
  ^-  tape
  (operate message (decoder shift-steps))
```

Both `++shift` and `++unshift` take two arguments: our `message`, the
`tape` that we want to manipulate; and our `shift-steps`, the number of
positions of the alphabet by which we want to shift our message.

`++shift` is for encoding, and `++unshift` is for decoding. Thus,
`++shift` calls the `operate` arm with `(operate message (encoder
shift-steps))`, and `++unshift` makes that call with `(operate message
(decoder shift-steps))`. These both produce the final output of the
core, to be called in the form of `(shift msg steps)` and `(unshift msg
steps)` in the {% tooltip label="cell" href="/glossary/cell" /%} being
created at the beginning of our code.

```hoon {% copy=true %}
++  operate
  |=  [message=tape shift-map=(map @t @t)]
  ^-  tape
  %+  turn  message
  |=  a=@t
  (~(got by shift-map) a)
```

`++operate` produces a `tape`. The `%+` {% tooltip label="cenlus"
href="/language/hoon/reference/rune/cen#-cenlus" /%} rune allows us to
pull an arm with a pair sample. The arm we are going to pull is {%
tooltip label="turn" href="/language/hoon/reference/stdlib/2b#turn" /%}.
This arm takes two arguments, a {% tooltip label="list"
href="/glossary/list" /%} and a {% tooltip label="gate"
href="/glossary/gate" /%} to apply to each element of the `list`.

In this case, the `gate` we are applying to our `message` uses the {%
tooltip label="got" href="/language/hoon/reference/stdlib/2i#gotby" /%}
arm of the {% tooltip label="by"
href="/language/hoon/reference/stdlib/2i#by" /%} door with our
`shift-map` as the {% tooltip label="sample" href="/glossary/sample" /%}
(which is either the standard alphabet for keys, and the shifted
alphabet for values, or the other way, depending on whether we are
encoding or decoding) to look up each `cord` in our `message`, one by
one and replace it with the `value` from our `map` (either the encoded
or decoded version).

Let's give our arm Caesar's famous statement (translated into English!)
and get our left-cipher and right-cipher.

```hoon
> +caesar ["i came i saw i conquered" 4]
["m geqi m wea m gsruyivih" "e ywia e ows e ykjmqanaz"]
```

Now, to decode, we can put either of our ciphers in with the appropriate
key and look for the legible result.

```hoon
> +caesar ["m geqi m wea m gsruyivih" 4]
["q kium q aie q kwvycmzml" "i came i saw i conquered"]

> +caesar ["e ywia e ows e ykjmqanaz" 4]
["i came i saw i conquered" "a usew a kso a ugfimwjwv"]
```

##  A Bit More on Cores

The `|^` {% tooltip label="barket"
href="/language/hoon/reference/rune/bar#-barket" /%} rune is an example
of what we can call a _convenience rune_, similar to the idea of sugar
syntax (irregular syntax to make writing certain things out in a more
expressive manner).  `|^` {% tooltip label="barket"
href="/language/hoon/reference/rune/bar#-barket" /%} produces a core
with _at least_ a `$` buc arm and computes it immediately, called a
_cork_.  (So a cork is like a trap in the regard of computing
immediately, but it has more arms than just `$` buc.)

This code calculates the volume of a cylinder, _A=πr²h_.

```hoon {% copy=true %}
=volume-of-cylinder |^
(mul:rs (area-of-circle .2.0) height)
++  area-of-circle
  |=  r=@rs
  (mul:rs pi r)
++  pi  .3.1415926
++  height  .10.0
--
```

Since all of the values either have to be pinned ahead of time or made
available as arms, a `|^` {% tooltip label="barket"
href="/language/hoon/reference/rune/bar#-barket" /%} would probably be
used inside of a gate.  Of course, since it is a {% tooltip label="core"
href="/glossary/core" /%} with a `$` buc arm, one could also use it
recursively to calculate values like the factorial.

If you read the docs, you'll find that a `|-` {% tooltip label="barhep"
href="/language/hoon/reference/rune/bar#--barhep" /%} rune “produces a
{% tooltip label="trap" href="/glossary/trap" /%} (a core with one arm
`$`) and evaluates it.”  So a trap actually evaluates to a `|%` {%
tooltip label="barcen" href="/language/hoon/reference/rune/bar#-barcen"
/%} core with an arm `$`:

```hoon {% copy=true %}
:: count to five
=/  index  1
|-
?:  =(index 5)  index
$(index +(index))
```

actually translates to

```hoon {% copy=true %}
:: count to five
=/  index  1
=<  $
|%
++  $
  ?:  =(index 5)  index
  %=  $
    index  +(index)
  ==
--
```

You can also create a trap for later use with the `|.` {% tooltip
label="bardot" href="/language/hoon/reference/rune/bar#-bardot" /%}
rune.  It's quite similar, but without the `=<($...` part then it
doesn't get evaluated immediately.

```hoon
> =forty-two |.(42)
> $:forty-two
42
> (forty-two)
42
```

What is a {% tooltip label="gate" href="/glossary/gate" /%}?  It is a {%
tooltip label="door" href="/glossary/door" /%} with only one arm `$`
buc, and whenever you invoke it then that default arm's expression is
referred to and evaluated.

A _gate_ and a _trap_ are actually very similar:  a gate simply has a {%
tooltip label="sample" href="/glossary/sample" /%} (and can actively
change when evaluated or via a `%=` {% tooltip label="centis"
href="/language/hoon/reference/rune/cen#-centis" /%}), whereas a trap
does not (and can _only_ be passively changed via something like `%=`
centis).

# L-struct.md

---

+++
title = "11. Data Structures"
weight = 21
nodes = [183]
objectives = ["Identify units, sets, maps, and compound structures like jars and jugs.", "Explain why units and vases are necessary.", "Use helper arms and syntax:  `` ` ``, `biff`, `some`, etc."]
+++

_This module will introduce you to several useful data structures built
on the {% tooltip label="door" href="/glossary/door" /%}, then discuss
how the compiler handles types and the {% tooltip label="sample"
href="/glossary/sample" /%}._


##  Key Data Structures and Molds

{% tooltip label="++maps" href="/language/hoon/reference/stdlib/2o#map" /%} are
a versatile way to store and access data, but they are far from
the only useful pattern.  `++map`s were documented in [the previous
module](/courses/hoon-school/K-doors).

### `tree`

We use {% tooltip label="tree"
href="/language/hoon/reference/stdlib/1c#tree" /%} to make a binary tree
data structure in Hoon, e.g., `(tree @)` for a binary tree of atoms.

There are two kinds of `tree` in Hoon:

1. The null tree `~`.
2. A non-null tree which is a cell with three parts.
    1. The node value.
    2. The left child of the node.
    3. The right child of the node.
    
    Each child is itself a tree.  The node value has the {% tooltip
    label="face" href="/glossary/face" /%} `n`, the left child has the
    face `l`, and the right child has the face `r`. The following
    diagram provides an illustration of a `(tree @)` (without the
    faces):

```
          12
        /    \
      8       14
    /   \    /   \
   4     ~  ~     16
 /  \            /  \
~    ~          ~    ~
```

Hoon supports trees of any type that can be constructed in Hoon, e.g.:
`(tree @)`, `(tree ^)`, `(tree [@ ?])`, etc.  Let's construct the tree
in the diagram above in the dojo, casting it accordingly:

```hoon
> `(tree @)`[12 [8 [4 ~ ~] ~] [14 ~ [16 ~ ~]]]
{4 8 12 14 16}
```

Notice that we don't have to insert the faces manually; by casting the
{% tooltip label="noun" href="/glossary/noun" /%} above to a `(tree @)`
Hoon inserts the faces for us.  Let's put this noun in the dojo {%
tooltip label="subject" href="/glossary/subject" /%} with the face `b`
and pull out the tree at the left child of the `12` node:

```hoon
> =b `(tree @)`[12 [8 [4 ~ ~] ~] [14 ~ [16 ~ ~]]]

> b
{4 8 12 14 16}

> l.b
-find.l.b
find-fork
```

This didn't work because we haven't first proved to Hoon that `b` is a
non-null tree.  A null tree has no `l` in it, after all.  Let's try
again, using `?~` {% tooltip label="wutsig"
href="/language/hoon/reference/rune/wut#-wutsig" /%} to prove that `b`
isn't null.  We can also look at `r` and `n`:

```hoon
> ?~(b ~ l.b)
{4 8}

> ?~(b ~ r.b)
{14 16}

> ?~(b ~ n.b)
12
```

#### Find and Replace

Here's a program that finds and replaces certain atoms in a `(tree @)`.

```hoon {% copy=true %}
|=  [nedl=@ hay=(tree @) new=@]
^-  (tree @)
?~  hay  ~
:+  ?:  =(n.hay nedl)
      new
    n.hay
  $(hay l.hay)
$(hay r.hay)
```

`nedl` is the atom to be replaced, `hay` is the tree, and `new` is the
new atom with which to replace `nedl`.  Save this as
`findreplacetree.hoon` and run in the dojo:

```hoon
> b
{4 8 12 14 16}

> +findreplacetree [8 b 94]
{4 94 12 14 16}

> +findreplacetree [14 b 94]
{4 8 12 94 16}
```

### `set`

A {% tooltip label="set" href="/language/hoon/reference/stdlib/2o#set"
/%} is rather like a {% tooltip label="list" href="/glossary/list" /%}
except that each entry can only be represented once.  As with a {%
tooltip label="map" href="/language/hoon/reference/stdlib/2o#map" /%}, a
`set` is typically associated with a particular type, such as `(set
@ud)` for a collection of decimal values.  (`set`s also don't have an
order, so they're basically a bag of unique values.)

`set` operations are provided by {% tooltip label="++in"
href="/language/hoon/reference/stdlib/2h#in" /%}.  Most names are
similar to `map`/{% tooltip label="++by"
href="/language/hoon/reference/stdlib/2i#by" /%} operations when
applicable.

{% tooltip label="++silt" href="/language/hoon/reference/stdlib/2l#silt" /%} produces
a `set` from a `list`:

```hoon {% copy=true %}
=primes (silt ~[2 3 5 7 11 13])
```

{% tooltip label="++put:in" href="/language/hoon/reference/stdlib/2h#putin" /%} adds
a value to a `set` (and null-ops when the value is already present):

```hoon {% copy=true %}
=primes (~(put in primes) 17)
=primes (~(put in primes) 13)
```

{% tooltip label="++del:in" href="/language/hoon/reference/stdlib/2h#delin" /%} removes
a value from a `set`:

```hoon {% copy=true %}
=primes (~(put in primes) 18)
=primes (~(del in primes) 18)
```

{% tooltip label="++has:in" href="/language/hoon/reference/stdlib/2h#hasin" /%} checks
for existence:

```hoon
> (~(has in primes) 15)
%.n

> (~(has in primes) 17)
%.y
```

{% tooltip label="++tap:in" href="/language/hoon/reference/stdlib/2h#tapin" /%} yields
a `list` of the values:

```hoon
> ~(tap in primes)
~[3 2 7 5 11 13 17]

> (sort ~(tap in primes) lth)
~[2 3 5 7 11 13 17]
```

{% tooltip label="++run:in" href="/language/hoon/reference/stdlib/2h#runin" /%} applies
a function across all values:

```hoon
> (~(run in primes) dec)
{10 6 12 1 2 16 4}
```

#### Example:  Cartesian Product

Here's a program that takes two {% tooltip label="sets"
href="/language/hoon/reference/stdlib/2o#set" /%} of atoms and returns
the [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product)
of those sets.  A Cartesian product of two sets `a` and `b` is a set of
all the cells whose head is a member of `a` and whose tail is a member
of `b`.

```hoon {% copy=true %}
|=  [a=(set @) b=(set @)]
=/  c=(list @)  ~(tap in a)
=/  d=(list @)  ~(tap in b)
=|  acc=(set [@ @])
|-  ^-  (set [@ @])
?~  c  acc
%=  $
  c  t.c
  acc  |-  ?~  d  acc
       %=  $
         d  t.d
         acc  (~(put in acc) [i.c i.d])
       ==
==
```

Save this as `cartesian.hoon` in your urbit's {% tooltip label="pier"
href="/glossary/pier" /%} and run in the dojo:

```hoon
> =c `(set @)`(sy ~[1 2 3])

> c
{1 2 3}

> =d `(set @)`(sy ~[4 5 6])

> d
{5 6 4}

> +cartesian [c d]
{[2 6] [1 6] [3 6] [1 4] [1 5] [2 4] [3 5] [3 4] [2 5]}
```

### `unit` Redux (and `vase`)

We encountered the {% tooltip label="unit"
href="/language/hoon/reference/stdlib/1c#unit" /%} briefly as a tool for
distinguishing null results from actual zeroes:  using a `unit` allows
you to specify something that may not be there.  For this reason,
`unit`s are commonly used for operations that sometimes fail, such as
search functions, database lookups, remote data requests, etc.

You can build a `unit` using the tic special notation or {% tooltip
label="++some" href="/language/hoon/reference/stdlib/2a#some" /%}:

```hoon
> `%mars
[~ %mars]

> (some %mars)
[~ u=%mars]
```

While {% tooltip label="++got:by"
href="/language/hoon/reference/stdlib/2i#gotby" /%} is one way to get a
value back without wrapping it in a `unit`, it's better practice to use
the [`unit` logic](/language/hoon/reference/stdlib/2a) gates to
manipulate gates to work correctly with `unit`s.

For example, use {% tooltip label="++need"
href="/language/hoon/reference/stdlib/2a#need" /%} to unwrap a `unit`,
or crash if the `unit` is `~` null.

```hoon
> =colors (malt `(list (pair @tas @ux))`~[[%red 0xed.0a3f] [%yellow 0xfb.e870] [%green 0x1.a638] [%blue 0x66ff]])

> (~(get by colors) %yellow)
[~ q=0xfb.e870]

> (need (~(get by colors) %yellow))
0xfb.e870

> (~(get by colors) %teal)
~

> (need (~(get by colors) %teal))
dojo: hoon expression failed
```

Rather than unwrap a {% tooltip label="unit"
href="/language/hoon/reference/stdlib/1c#unit" /%}, one can modify gates
to work with `unit`s directly even if they're not natively set up that
way.  For instance, one cannot decrement a `unit` because {% tooltip
label="++dec" href="/language/hoon/reference/stdlib/1a#dec" /%} doesn't
accept a `unit`. {% tooltip label="++bind"
href="/language/hoon/reference/stdlib/2a#bind" /%} can bind a non-`unit`
function—another gate-building gate!.

```hoon
> (bind ((unit @ud) [~ 2]) dec)  
[~ 1]

> (bind (~(get by colors) %orange) red)  
[~ 0xff]
```

(There are several others tools listed [on that
page](/language/hoon/reference/stdlib/2a) which may be potentially
useful to you.)

A {% tooltip label="vase" href="/glossary/vase" /%} is a pair of type
and value, such as that returned by `!>` {% tooltip label="zapgar"
href="/language/hoon/reference/rune/zap#-zapgar" /%}.  A `vase` is
useful when transmitting data in a way that may lose its type
information.

### Containers of Containers

{% tooltip label="maps" href="/language/hoon/reference/stdlib/2o#map" /%} and
{% tooltip label="sets" href="/language/hoon/reference/stdlib/2o#set" /%} are
frequently used in the standard library and in the extended ecosystem.
There are other common patterns which recur often enough that
they have their own names:

- {% tooltip label="++jar" href="/language/hoon/reference/stdlib/2o#jar" /%} is
  a mold for a `map` of `list`s.  `++jar` uses the {% tooltip
  label="++ja" href="/language/hoon/reference/stdlib/2j#ja" /%} core.
  (Mnemonic: jars hold solid ordered things, like a {% tooltip
  label="list" href="/glossary/list" /%}.)

- {% tooltip label="++jug" href="/language/hoon/reference/stdlib/2o#jug" /%} is
  a {% tooltip label="mold" href="/glossary/mold" /%} for a `map`
  of `set`s.  `++jug` uses the {% tooltip label="++ju"
  href="/language/hoon/reference/stdlib/2j#ju" /%} core.  (Mnemonic:
  jugs hold liquids, evoking the unordered nature of a {% tooltip
  label="set" href="/language/hoon/reference/stdlib/2o#set" /%}.)

- {% tooltip label="++mip" href="/language/hoon/reference/mip#mip" /%} is
  a mold for a map of maps.  `++mip` lives in the `%landscape` desk in
  `/lib/mip.hoon`.  Affordances are still few but a short example
  follows:

    ```hoon
    > =mip -build-file /=landscape=/lib/mip/hoon
    
    > =my-map-warm (malt `(list (pair @tas @ux))`~[[%red 0xed.0a3f] [%yellow 0xfb.e870]])
    
    > =my-map-cool (malt `(list (pair @tas @ux))`~[[%green 0x1.a638] [%blue 0x66ff]])
    
    > =my-mip *(mip:mip @tas (map @tas @ux))
    
    > =my-mip (~(put bi:mip my-mip) %cool %blue 0x66ff)
    
    > =my-mip (~(put bi:mip my-mip) %cool %green 0x1.a638)
    
    > =my-mip (~(put bi:mip my-mip) %warm %red 0xed.0a3f)
    
    > =my-mip (~(put bi:mip my-mip) %warm %yellow 0xfb.e870)
    
    > my-mip
    [ n=[p=%warm q=[n=[p=%yellow q=0xfb.e870] l=[n=[p=%red q=0xed.0a3f] l=~ r=~] r=~]]
      l=[n=[p=%cool q=[n=[p=%green q=0x1.a638] l=[n=[p=%blue q=0x66ff] l=~ r=~] r=~]] l=~ r=~]
      r=~
    ]

    > (~(got bi:mip my-mip) %cool %green)
    0x1.a638

    > ~(tap bi:mip my-mip)
    ~[
      [x=%warm y=%yellow v=0xfb.e870]
      [x=%warm y=%red v=0xed.0a3f]
      [x=%cool y=%green v=0x1.a638]
      [x=%cool y=%blue v=0x66ff]
    ]
    ```

    `mip`s are unjetted and quite slow but serve as a proof of concept.

- {% tooltip label="++mop" href="/language/hoon/reference/zuse/2m#mop" /%} ordered
  maps are discussed in [the App School guides](/courses/app-school).


##  Molds and Samples

### Modifying Gate Behavior

Sometimes you need to modify parts of a {% tooltip label="core"
href="/glossary/core" /%} (like a {% tooltip label="gate"
href="/glossary/gate" /%}) on-the-fly to get the desired behavior.  For
instance, if you are using {% tooltip label="++roll"
href="/language/hoon/reference/stdlib/2b#roll" /%} to calculate the
multiplicative product of the elements of a list, this “just works”:

```hoon
> (roll `(list @ud)`~[10 12 14 16 18] mul)  
483.840
```

In contrast, if you do the same thing to a list of numbers with a
fractional part (`@rs` floating-point values), the naïve operation will
fail:

```hoon
> (roll `(list @rs)`~[.10 .12 .14 .16 .18] mul:rs)  
.0
```

Why is this?  Let's peek inside the gates and see.  Since we know a core
is a cell of `[battery payload]`, let's take a look at the {% tooltip
label="payload" href="/glossary/payload" /%}:

```hoon
> +:mul
[[a=1 b=1] <33.uof 1.pnw %138>]

> +:mul:rs
[[a=.0 b=.0] <21.ezj [r=?(%d %n %u %z) <51.njr 139.oyl 33.uof 1.pnw %138>]>]
```

The correct behavior for {% tooltip label="++mul:rs"
href="/language/hoon/reference/stdlib/3b#mulrs" /%} is really to
multiply starting from one, not zero, so that {% tooltip label="++roll"
href="/language/hoon/reference/stdlib/2b#roll" /%} doesn't wipe out
the entire product.

### Custom Samples

In an earlier exercise we created a {% tooltip label="door"
href="/glossary/door" /%} with {% tooltip label="sample"
href="/glossary/sample" /%} `[a=@ud b=@ud c=@ud]`.  If we investigated,
we would find that the initial value of each is `0`, the bunt value of
`@ud`.

```hoon
> +6:poly
[a=0 b=0 c=0]
```

What if we wish to define a door with a chosen sample value directly? We
can make use of the `$_` {% tooltip label="buccab"
href="/language/hoon/reference/rune/buc#_-buccab" /%} rune, whose
irregular form is simply `_`. To create the door `poly` with the sample
set to have certain values in the {% tooltip label="Dojo"
href="/glossary/dojo" /%}, we would write

```hoon
> =poly |_  [a=_5 b=_4 c=_3]
++  quad
  |=  x=@ud
  (add (add (mul a (mul x x)) (mul b x)) c)
--

> (quad:poly 2)  
31
```

For our earlier example with {% tooltip label="++roll"
href="/language/hoon/reference/stdlib/2b#roll" /%}, if we wanted to set
the default sample to have a different value than the {% tooltip
label="bunt" href="/glossary/bunt" /%} of the type, we could use `_`
cab:

```hoon
> =mmul |=([a=_.1 b=_.1] (mul:rs a b))

> (roll `(list @rs)`~[.10 .12 .14 .16 .18] mmul)
.483840
```

### Named Tuples

A named tuple is a structured collection of values with {% tooltip
label="faces" href="/glossary/face" /%}.  The `$:` {% tooltip
label="buccol" href="/language/hoon/reference/rune/buc#-buccol" /%} rune
forms a named tuple.  We use these implicitly in an irregular form when
we specify the sample of a gate, as `|=([a=@ b=@] (add a b))` expands to
a `$:` {% tooltip label="buccol"
href="/language/hoon/reference/rune/buc#-buccol" /%} expression for
`[a=@ b=@]`.  Otherwise, we only need these if we are building a special
type like a vector (e.g. with two components like an _x_ and a _y_).

### Structure Mode

Most Hoon expressions evaluate normally (that's what “normal” means),
what we'll call _noun mode_ (or _normal mode_).  However, sample
definitions and `+$` {% tooltip label="lusbuc"
href="/language/hoon/reference/rune/lus#-lusbuc" /%} mold specification
arms evaluate in what is called _structure mode_.  (You may occasionally
see this the older term “spec mode”.)  Structure mode expressions use a
similar syntax to regular Hoon expressions but create structure
definitions instead.

For instance, in eval mode if you use the irregular form `p=1` this is
an irregular form of the `^=` {% tooltip label="kettis"
href="/language/hoon/reference/rune/ket#-kettis" /%} rune.  This is one
way to define a variable using a `=+` {% tooltip label="tislus"
href="/language/hoon/reference/rune/tis#-tislus" /%}; these are
equivalent statements:

```hoon
> =+(hello=1 hello)
1

> =+(^=(hello 1) hello)
1
```

(Normally we have preferred `=/` {% tooltip label="tisfas"
href="/language/hoon/reference/rune/tis#-tisfas" /%} in the Hoon School
docs, but that is just for consistency.)

In a {% tooltip label="sample" href="/glossary/sample" /%} definition,
such as in a {% tooltip label="gate" href="/glossary/gate" /%}, the
statement is evaluated in structure mode; these are equivalent
statements:

```hoon {% copy=true %}
|=(hello=@ hello)

|=($=(hello @) hello)
```

There are several other subtle cases where normal mode and structure
mode diverge, but most of the time structure mode is invisible to you.
The [`$` buc runes](/language/hoon/reference/rune/buc) are typically
invoked in structure mode.


# N-logic.md

---

+++
title = "13. Conditional Logic"
objectives = ["Produce loobean expressions.", "Reorder conditional arms.", "Switch against a union with or without default."]
+++

_Although you've been using various of the `?` {% tooltip label="wut"
href="/language/hoon/reference/rune/wut" /%} runes for a while now,
let's wrap up some loose ends.  This module will cover the nature of
loobean logic and the rest of the `?` wut runes._


##  Loobean Logic

Throughout Hoon School, you have been using `%.y` and `%.n`, often
implicitly, every time you have asked a question like `?:  =(5 4)`.  The
`=()` expression returns a loobean, a member of the type union `?(%.y
%.n)`.  (There is a proper aura `@f` but unfortunately it can't be used
outside of the compiler.)  These can also be written as `&` (`%.y`,
true) and `|` (`%.n`, false), which is common in older code but should
be avoided for clarity in your own compositions.

What are the actual values of these, _sans_ formatting?

```hoon
> `@`%.y
0

> `@`%.n
1
```

Pretty much all conditional operators rely on loobeans, although it is
very uncommon for you to need to unpack them.


##  Noun Equality

The most fundamental comparison in Hoon is provided by `.=` {% tooltip
label="dottis" href="/language/hoon/reference/rune/dot#-dottis" /%}, a
test for equality of two {% tooltip label="nouns" href="/glossary/noun"
/%} using Nock 5.  This is almost always used in its irregular form of
`=` tis.

```hoon
> =(0 0)
%.y

> =('a' 'b')
%.n
```

Since {% tooltip label="Nock" href="/glossary/nock" /%} is unaware of
the Hoon metadata type system, only bare {% tooltip label="atoms"
href="/glossary/atom" /%} in the nouns are compared.  If you need to
compare include type information, create vases with `!>` {% tooltip
label="zapgar" href="/language/hoon/reference/rune/zap#-zapgar" /%}.

```hoon
> =('a' 97)
%.y

> =(!>('a') !>(97))
%.n
```


##  Making Choices

You are familiar in everyday life with making choices on the basis of a
decision expression.  For instance, you can compare two prices for
similar products and select the cheaper one for purchase.

Essentially, we have to be able to decide whether or not some value or
expression evaluates as `%.y` true (in which case we will do one thing)
or `%.n` false (in which case we do another).  Some basic expressions
are mathematical, but we also check for existence, for equality of two
values, etc.

- {% tooltip label="++gth" href="/language/hoon/reference/stdlib/1a#gth" /%} (greater than `>`)
- {% tooltip label="++lth" href="/language/hoon/reference/stdlib/1a#lth" /%} (less than `<`)  
- {% tooltip label="++gte" href="/language/hoon/reference/stdlib/1a#gte" /%} (greater than or equal to `≥`)
- {% tooltip label="++lte" href="/language/hoon/reference/stdlib/1a#lte" /%} (less than or equal to `≤`)
- `.=` {% tooltip label="dottis" href="/language/hoon/reference/rune/dot#-dottis" /%}, irregularly `=()` (check for equality)

The key conditional decision-making rune is `?:` {% tooltip
label="wutcol" href="/language/hoon/reference/rune/wut#-wutcol" /%},
which lets you branch between an `expression-if-true` and an
`expression-if-false`. `?.` {% tooltip label="wutdot"
href="/language/hoon/reference/rune/wut#-wutdot" /%} inverts the order
of `?:`.  Good Hoon style prescribes that the heavier branch of a
logical expression should be lower in the file.

There are also two long-form decision-making runes, which we will call
[_switch statements_](https://en.wikipedia.org/wiki/Switch_statement) by
analogy with languages like C.

- `?-` {% tooltip label="wuthep"
  href="/language/hoon/reference/rune/wut#--wuthep" /%} lets you choose
  between several possibilities, as with a type union.  Every case must
  be handled and no case can be unreachable.

    Since `@tas` terms are constants first, and not `@tas` unless marked
    as such, `?-` {% tooltip label="wuthep"
    href="/language/hoon/reference/rune/wut#--wuthep" /%} switches over
    term unions can make it look like the expression is branching on the
    value.  It's actually branching on the _type_.  These are almost
    exclusively used with term type unions.

    ```hoon {% copy=true %}
    |=  p=?(%1 %2 %3)
    ?-  p
      %1  1
      %2  2
      %3  3
    ==
    ```

- `?+` {% tooltip label="wutlus"
  href="/language/hoon/reference/rune/wut#-wutlus" /%} is similar to
  `?-` but allows a default value in case no branch is taken.  Otherwise
  these are similar to `?-` {% tooltip label="wuthep"
  href="/language/hoon/reference/rune/wut#--wuthep"/%} switch
  statements.

    ```hoon {% copy=true %}
    |=  p=?(%0 %1 %2 %3 %4)
    ?+  p  0
      %1  1
      %2  2
      %3  3
    ==
    ```

##  Logical Operators

Mathematical logic allows the collocation of propositions to determine
other propositions.  In computer science, we use this functionality to
determine which part of an expression is evaluated.  We can combine
logical statements pairwise:

- `?&` {% tooltip label="wutpam"
  href="/language/hoon/reference/rune/wut#-wutpam" /%}, irregularly
  `&()`, is a logical `AND` (i.e. _p_ ∧ _q_) over loobean values, e.g.
  both terms must be true.

    |             `AND`            | `%.y` | `%.n` |
    |------------------------------|-------|-------|
    | `%.y`{% class="font-bold" %} | `%.y` | `%.n` |
    | `%.n`{% class="font-bold" %} | `%.n` | `%.n` |

    <br>

    ```hoon
    > =/  a  5
      &((gth a 4) (lth a 7))
    %.y
    ```

- `?|` {% tooltip label="wutbar"
  href="/language/hoon/reference/rune/wut#-wutbar" /%}, irregularly
  `|()`, is a logical `OR` (i.e. _p_ ∨ _q_)  over loobean values, e.g.
  either term may be true.

    |             `OR`             | `%.y` | `%.n` |
    |------------------------------|-------|-------|
    | `%.y`{% class="font-bold" %} | `%.y` | `%.y` |
    | `%.n`{% class="font-bold" %} | `%.y` | `%.n` |

    <br>

    ```hoon
    > =/  a  5
      |((gth a 4) (lth a 7))
    %.y
    ```

- `?!` {% tooltip label="wutzap"
  href="/language/hoon/reference/rune/wut#-wutzap" /%}, irregularly `!`,
  is a logical `NOT` (i.e. ¬*p*).  Sometimes it can be difficult to
  parse code including `!` because it operates without parentheses.

    |                              | `NOT` |
    |------------------------------|-------|
    | `%.y`{% class="font-bold" %} | `%.n` |
    | `%.n`{% class="font-bold" %} | `%.y` |

    <br>

    ```hoon
    > !%.y
    %.n

    > !%.n
    %.y
    ```

From these primitive operators, you can build other logical statements
at need.

### Exercise:  Design an `XOR` Function

The logical operation `XOR` (i.e. *p*⊕*q* ; exclusive disjunction)
yields true if one but not both operands are true.  `XOR` can be
calculated by (_p_ ∧ ¬*q*) ∨ (¬*p* ∧ _q_).

|             `XOR`            | `%.y` | `%.n` |
|------------------------------|-------|-------|
| `%.y`{% class="font-bold" %} | `%.n` | `%.y` |
| `%.n`{% class="font-bold" %} | `%.y` | `%.n` |

- Implement `XOR` as a {% tooltip label="gate" href="/glossary/gate" /%}
  in Hoon.

    ```hoon {% copy=true %}
    |=  [p=?(%.y %.n) q=?(%.y %.n)]
    ^-  ?(%.y %.n)
    |(&(p !q) &(!p q))
    ```

---

# S-math.md

---

+++
title = "19. Mathematics"
objectives = ["Review floating-point mathematics including IEEE-754.", "Examine `@r` atomic representation of floating-point values.", "Manipulate and convert floating-point values using the `@r` operations.", "Examine `@s` atomic representation of signed integer values.", "Use `+si` to manipulate `@s` signed integer values.", "Define entropy and its source.", "Utilize `eny` in a random number generator (`og`).", "Distinguish insecure hashing (`mug`) from secure hashing (`shax` and friends)."]
+++

_This module introduces how non-`@ud` mathematics are instrumented in
Hoon.  It may be considered optional and skipped if you are speedrunning
Hoon School._

All of the math we've done until this point relied on unsigned integers:
there was no negative value possible, and there were no numbers with a
fractional part.  How can we work with mathematics that require more
than just bare unsigned integers?

`@u` unsigned integers (whether `@ud` decimal, `@ux` hexadecimal, etc.)
simply count upwards by binary place value from zero.  However, if we
apply a different interpretive rule to the resulting value, we can treat
the integer (in memory) _as if_ it corresponded to a different real
value, such as a [negative
number](https://en.wikipedia.org/wiki/Integer) or a [number with a
fractional part](https://en.wikipedia.org/wiki/Rational_number).  Auras
make this straightforward to explore:

```hoon
> `@ud`1.000.000
1.000.000

> `@ux`1.000.000
0xf.4240

> `@ub`1.000.000
0b1111.0100.0010.0100.0000

> `@sd`1.000.000
--500.000

> `@rs`1.000.000
.1.401298e-39

> `@rh`1.000.000
.~~3.125

> `@t`1.000.000
'@B\0f'
```

How can we actually treat other modes of interpreting numbers as
mathematical quantities correctly?  That's the subject of this lesson.

(Ultimately, we are using a concept called [Gödel
numbering](https://en.wikipedia.org/wiki/G%C3%B6del_numbering) to
justify mapping some data to a particular representation as a unique
integer.)


##  Floating-Point Mathematics

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS234 - Floating-Point Maths.mp4" /%}

A number with a fractional part is called a “floating-point number” in
computer science.  This derives from its solution to the problem of
representing the part less than one.

Consider for a moment how you would represent a regular decimal fraction
if you only had integers available.  You would probably adopt one of
three strategies:

1. [**Rational numbers**](https://en.wikipedia.org/wiki/Fraction).
   Track whole-number ratios like fractions.  Thus {% math %}1.25 =
   \frac{5}{4}{% /math %}, thence the pair `(5, 4)`.  Two numbers have
   to be tracked:  the numerator and the denominator.
2. [**Fixed-point**](https://en.wikipedia.org/wiki/Fixed-point_arithmetic).
   Track the value in smaller fixed units (such as thousandths).  By
   defining the base unit to be {% math %}\frac{1}{1000}{% /math %} , {%
   math %}1.25{% /math %} may be written {% math %}1250{% /math %}.  One
   number needs to be tracked:  the value in terms of the scale.  (This is
   equivalent to rational numbers with only a fixed denominator allowed.)
3. [**Floating-point**](https://en.wikipedia.org/wiki/Floating-point_arithmetic).
   Track the value at adjustable scale.  In this case, one needs to
   represent {% math %}1.25{% /math %} as something like {% math %}125
   \times 10^{-2}{% /math %}.  Two numbers have to be tracked:  the
   significand ({% math %}125{% /math %}) and the exponent ({% math %}-2{%
   /math %}).

Most systems use floating-point mathematics to solve this problem.  For
instance, single-precision floating-point mathematics designate one bit
for the sign, eight bits for the exponent (which has 127 subtracted from
it), and twenty-three bits for the significand.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Float_example.svg/640px-Float_example.svg.png)

This number, `0b11.1110.0010.0000.0000.0000.0000.0000`, is converted to
decimal as {% math %}(-1)^0 \times 2^{(124 - 127)} \times 1.25 = 2^{-3}
\times 1.25 = 0.15625{% /math %}.

(If you want to explore the bitwise representation of values, [this
tool](https://evanw.github.io/float-toy/) allows you to tweak values
directly and see the results.)

### Hoon Operations

Hoon utilizes the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)
implementation of floating-point math for four bitwidth representations.

| Aura | Meaning | Example |
| ---- | ------- | ------- |
| `@r` | Floating-point value |  |
| `@rh` | Half-precision 16-bit mathematics | `.~~4.5` |
| `@rs` | Single-precision 32-bit mathematics | `.4.5` |
| `@rd` | Double-precision 64-bit mathematics | `.~4.5` |
| `@rq` | Quadruple-precision 128-bit mathematics | `.~~~4.5` |

There are also a few {% tooltip label="molds" href="/glossary/mold" /%}
which can represent the separate values of the FP representation.  These
are used internally but mostly don't appear in userspace code.

As the {% tooltip label="arms" href="/glossary/arm" /%} for the four
`@r` auras are identical within their appropriate core, we will use
[`@rs` single-precision floating-point
mathematics](/language/hoon/reference/stdlib/3b#rs) to demonstrate all
operations.

#### Conversion to and from other auras

Any `@ud` unsigned decimal integer can be directly cast as an `@rs`.

```hoon
> `@ud`.1
1.065.353.216
```

However, as you can see here, the conversion is not “correct” for the
perceived values.  Examining the `@ux` hexadecimal and `@ub` binary
representation shows why:

```hoon
> `@ux`.1
0x3f80.0000

> `@ub`.1
0b11.1111.1000.0000.0000.0000.0000.0000
```

If you refer back to the 32-bit floating-point example above, you'll see
why:  to represent one exactly, we have to use {% math %}1.0 = (-1)^0
\times 2^{{127 - 127}} \times 1{% /math %} and thus
`0b11.1111.1000.0000.0000.0000.0000.0000`.

So to carry out this conversion from `@ud` to `@rs` correctly, we should
use the {% tooltip label="++sun:rs"
href="/language/hoon/reference/stdlib/3b#sunrs" /%} arm.

```hoon
> (sun:rs 1)
.1
```

To go the other way requires us to use an algorithm for converting an
arbitrary number with a fractional part back into `@ud` unsigned
integers.  The {% tooltip label="++fl"
href="/language/hoon/reference/stdlib/3b#fl" /%} named tuple
representation serves this purpose, and uses the [Dragon4
algorithm](https://dl.acm.org/doi/10.1145/93548.93559) to accomplish the
conversion:

```hoon
> (drg:rs .1)
[%d s=%.y e=--0 a=1]

> (drg:rs .3.1415926535)
[%d s=%.y e=-7 a=31.415.927]

> (drg:rs .1000)
[%d s=%.y e=--3 a=1]
```

It's up to you to decide how to handle this result, however!  Perhaps a
better option for many cases is to round the answer to an `@s` integer
with {% tooltip label="++toi:rs"
href="/language/hoon/reference/stdlib/3b#toirs" /%}:

```hoon
> (toi:rs .3.1415926535)
[~ --3]
```

(`@s` signed integer math is discussed below.)

### Floating-point specific operations

As with {% tooltip label="aura" href="/glossary/aura" /%} conversion,
the standard mathematical operators don't work for `@rs`:

```hoon
> (add .1 1)
1.065.353.217

> `@rs`(add .1 1)
.1.0000001
```

The {% tooltip label="++rs" href="/language/hoon/reference/stdlib/3b#rs"
/%} core defines a set of `@rs`-affiliated operations which should be
used instead:

```hoon
> (add:rs .1 .1)
.2
```

This includes:

- {% tooltip label="++add:rs" href="/language/hoon/reference/stdlib/3b#addrs" /%}, addition
- {% tooltip label="++sub:rs" href="/language/hoon/reference/stdlib/3b#subrs" /%}, subtraction
- {% tooltip label="++mul:rs" href="/language/hoon/reference/stdlib/3b#mulrs" /%}, multiplication
- {% tooltip label="++div:rs" href="/language/hoon/reference/stdlib/3b#divrs" /%}, division
- {% tooltip label="++gth:rs" href="/language/hoon/reference/stdlib/3b#gthrs" /%}, greater than
- {% tooltip label="++gte:rs" href="/language/hoon/reference/stdlib/3b#gters" /%}, greater than or equal to
- {% tooltip label="++lth:rs" href="/language/hoon/reference/stdlib/3b#lthrs" /%}, less than
- {% tooltip label="++lte:rs" href="/language/hoon/reference/stdlib/3b#lters" /%}, less than or equal to
- {% tooltip label="++equ:rs" href="/language/hoon/reference/stdlib/3b#equrs" /%}, check equality (but not nearness!)
- {% tooltip label="++sqt:rs" href="/language/hoon/reference/stdlib/3b#sqtrs" /%}, square root

##  Signed Integer Mathematics

`@u`-{% tooltip label="aura" href="/glossary/aura" /%} atoms are
_unsigned_ values, but there is a complete set of _signed_ auras in the
`@s` series.  ZigZag was chosen for Hoon's signed integer representation
because it represents negative values with small absolute magnitude as
short binary terms.

| Aura | Meaning | Example |
| ---- | ------- | ------- |
| `@s` | signed integer|  |
| `@sb` | signed binary | `--0b11.1000` (positive) |
|       |               | `-0b11.1000` (negative) |
| `@sd` | signed decimal | `--1.000.056` (positive) |
|       |                | `-1.000.056` (negative) |
| `@sx` | signed hexadecimal | `--0x5f5.e138` (positive) |
|       |                    | `-0x5f5.e138` (negative) |

The {% tooltip label="++si" href="/language/hoon/reference/stdlib/3a#si"
/%} core supports signed-integer operations correctly.  However, unlike
the `@r` operations, `@s` operations have different names (likely to
avoid accidental mental overloading).

To produce a signed integer from an unsigned value, use {% tooltip
label="++new:si" href="/language/hoon/reference/stdlib/3a#newsi" /%}
with a sign flag, or simply use {% tooltip label="++sun:si"
href="/language/hoon/reference/stdlib/3a#sunsi" /%}

```hoon
> (new:si & 2)
--2

> (new:si | 2)
-2

> `@sd`(sun:si 5)
--5
```

To recover an unsigned integer from a signed integer, use {% tooltip
label="++old:si" href="/language/hoon/reference/stdlib/3a#oldsi" /%},
which returns the magnitude and the sign.

```hoon
> (old:si --5)
[%.y 5]

> (old:si -5)
[%.n 5]
```

To convert a floating-point value from number (atom) to text, use {%
tooltip label="++scow" href="/language/hoon/reference/stdlib/4m#scow"
/%} or {% tooltip label="++r-co:co"
href="/language/hoon/reference/stdlib/4k#r-coco" /%} with {% tooltip
label="++rlys" href="/language/hoon/reference/stdlib/3b#rlys" /%} (and
friends):

```hoon
> (scow %rs .3.14159)
".3.14159"

> `tape`(r-co:co (rlys .3.14159))
"3.14159"
```

### Beyond Arithmetic

The Hoon standard library at the current time omits many [transcendental
functions](https://en.wikipedia.org/wiki/Transcendental_function), such
as the trigonometric functions.  It is useful to implement pure-Hoon
versions of these, although they are not as efficient as {% tooltip
label="jetted" href="/glossary/jet" /%} mathematical code would be.

- Produce a version of `++factorial` which can operate on `@rs` inputs
  correctly.

- Produce an exponentiation function `++pow-n` which operates on integer
  `@rs` only.

    ```hoon {% copy=true %}
    ++  pow-n
      ::  restricted power, based on integers only
      |=  [x=@rs n=@rs]
      ^-  @rs
      ?:  =(n .0)  .1
      =/  p  x
      |-  ^-  @rs
      ?:  (lth:rs n .2)  p
      $(n (sub:rs n .1), p (mul:rs p x))
    ```

- Using both of the above, produce the `++sine` function, defined by

    {% math block=true %}
    \sin(x)
    = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} x^{2n+1}
    = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots
    {% /math %}

    <!--
    \sin(x) = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!}x^{2n+1}= x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots
    -->

    ```hoon {% copy=true %}
    ++  sine
      ::  sin x = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! - ...
      |=  x=@rs
      ^-  @rs
      =/  rtol  .1e-5
      =/  p   .0
      =/  po  .-1
      =/  i   .0
      |-  ^-  @rs
      ?:  (lth:rs (absolute (sub:rs po p)) rtol)  p
      =/  ii  (add:rs (mul:rs .2 i) .1)
      =/  term  (mul:rs (pow-n .-1 i) (div:rs (pow-n x ii) (factorial ii)))
      $(i (add:rs i .1), p (add:rs p term), po p)
    ```

### Hoon Operations

A timestamp can be separated into the time portion, which is the
relative offset within a given day, and the date portion, which
represents the absolute day.

There are two {% tooltip label="molds" href="/glossary/mold" /%} to
represent time in Hoon:  the `@d` {% tooltip label="aura"
href="/glossary/aura" /%}, with `@da` for a full timestamp and `@dr` for
an offset; and the {% tooltip label="+$date"
href="/language/hoon/reference/stdlib/2q#date" /%}/{% tooltip
label="+$tarp" href="/language/hoon/reference/stdlib/2q#tarp" /%}
structure:

| Aura | Meaning | Example |
| ---- | ------- | ------- |
| `@da` | Absolute date | `~2022.1.1` |
|       |               | `~2022.1.1..1.1.1..0000` |
| `@dr` | Relative date (difference) | `~h5.m30.s12` |
|       |                            | `~d1000.h5.m30.s12..beef` |

```hoon
+$  date  [[a=? y=@ud] m=@ud t=tarp]
+$  tarp  [d=@ud h=@ud m=@ud s=@ud f=(list @ux)]
```

`now` returns the `@da` of the current timestamp (in UTC).

To go from a `@da` to a `+$tarp`, use {% tooltip label="++yell"
href="/language/hoon/reference/stdlib/3c#yell" /%}:

```hoon
> *tarp
[d=0 h=0 m=0 s=0 f=~]

> (yell now)
[d=106.751.991.821.625 h=22 m=58 s=10 f=~[0x44ff]]

> `tarp`(yell ~2014.6.6..21.09.15..0a16)
[d=106.751.991.820.172 h=21 m=9 s=15 f=~[0xa16]]

> (yell ~d20)
[d=20 h=0 m=0 s=0 f=~]
```

To go from a `@da` to a `+$date`, use {% tooltip label="++yore"
href="/language/hoon/reference/stdlib/3c#yore" /%}:

```hoon
> (yore ~2014.6.6..21.09.15..0a16)
[[a=%.y y=2.014] m=6 t=[d=6 h=21 m=9 s=15 f=~[0xa16]]]

> (yore now)
[[a=%.y y=2.022] m=5 t=[d=24 h=16 m=20 s=57 f=~[0xbaec]]]
```

To go from a `+$date` to a `@da`, use {% tooltip label="++year"
href="/language/hoon/reference/stdlib/3c#year" /%}:

```hoon
> (year [[a=%.y y=2.014] m=8 t=[d=4 h=20 m=4 s=57 f=~[0xd940]]])
~2014.8.4..20.04.57..d940

> (year (yore now))
~2022.5.24..16.24.16..d184
```

To go from a `+$tarp` to a `@da`, use {% tooltip label="++yule"
href="/language/hoon/reference/stdlib/3c#yule" /%}:

```hoon
> (yule (yell now))
0x8000000d312b148891f0000000000000

> `@da`(yule (yell now))
~2022.5.24..16.25.48..c915

> `@da`(yule [d=106.751.991.823.081 h=16 m=26 s=14 f=~[0xf727]])
~2022.5.24..16.26.14..f727
```

The Urbit date system correctly compensates for the lack of Year Zero:

```hoon
> ~0.1.1
~1-.1.1

> ~1-.1.1
~1-.1.1
```

The {% tooltip label="++yo" href="/language/hoon/reference/stdlib/3c#yo"
/%} core contains constants useful for calculating time, but in general
you should not hand-roll time or timezone calculations.

##  Unusual Bases

### Phonetic Base

The `@q` aura is similar to `@p` except for two details:  it doesn't
obfuscate names (as planets do) and it can be used for any size of atom
without adjust its width to fill the same size.  Prefixes and suffixes
are in the same order as `@p`, however.  Thus:

```hoon
> `@q`0
.~zod

> `@q`256
.~marzod

> `@q`65.536
.~nec-dozzod

> `@q`4.294.967.296
.~nec-dozzod-dozzod

> `@q`(pow 2 128)
.~nec-dozzod-dozzod-dozzod-dozzod-dozzod-dozzod-dozzod-dozzod
```

`@q` {% tooltip label="auras" href="/glossary/aura" /%} can be used as
sequential mnemonic markers for values.

The {% tooltip label="++po" href="/language/hoon/reference/stdlib/4a#po"
/%} core contains tools for directly parsing `@q` atoms.

### Base-32 and Base-64

The base-32 representation uses the characters
`0123456789abcdefghijklmnopqrstuv` to represent values.  The digits are
separated into collections of five characters separated by `.` dot.

```hoon
> `@uv`0
0v0

> `@uv`100
0v34

> `@uv`1.000.000
0vugi0

> `@uv`1.000.000.000.000
0vt3a.aa400
```

The base-64 representation uses the characters
`0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-~` to
represent values.  The digits are separated into collections of five
characters separated by `.` dot.

```hoon
> `@uw`0
0w0

> `@uw`100
0w1A

> `@uw`1.000.000
0w3Q90

> `@uw`1.000.000.000
0wXCIE0

> `@uw`1.000.000.000.000
0wez.kFh00
```


##  Randomness

### Random Numbers

Given a source of entropy to seed a random number generator, one can
then use the {% tooltip label="++og"
href="/language/hoon/reference/stdlib/3d#og" /%} door to produce various
kinds of random numbers.  The basic operations of `++og` are described
in [the lesson on subject-oriented
programming](/courses/hoon-school/O-subject).

### Exercise:  Produce uniformly-distributed random numbers

- Using entropy as the source, produce uniform random numbers:  that is,
  numbers in the range [0, 1] with equal likelihood to machine
  precision.

We use the LCG defined above, then chop out 23-bit slices using {%
tooltip label="++rip" href="/language/hoon/reference/stdlib/2c#rip" /%}
to produce each number, manually compositing the result into a valid
floating-point number in the range [0, 1].  (We avoid producing special
sequences like [`NaN`](https://en.wikipedia.org/wiki/NaN).)

**`/gen/uniform.hoon`**

```hoon {% copy=true mode="collapse" %}
!:
=<
|=  n=@ud  :: n is the number of values to return
^-  (list @rs)
=/  values  (rip 5 (~(lcg gen 20.220.524) n))
=/  mask-clear           0b111.1111.1111.1111.1111.1111
=/  mask-fill   0b11.1111.0000.0000.0000.0000.0000.0000
=/  clears  (turn values |=(a=@rs (dis mask-clear a)))
(turn clears |=(a=@ (sub:rs (mul:rs .2 (con mask-fill a)) .1.0)))
|%
++  gen
  |_  [z=@ud]
  ++  lcg
    |=  n=@ud                 :: n is the number of bits to return
    =/  a  742.938.285        :: a is the multiplier
    =/  e  31                 :: e is the exponent
    =/  m  (sub (pow 2 e) 1)  :: modulus
    =/  index  0
    =/  accum  *@ub
    |-  ^-  @ub
    ?:  =(index n)  accum
    %=  $
      index  +(index)
      z      (mod (mul a z) m)
      accum  (cat 5 z accum)
    ==
  --
--
```

### Exercise:  Produce normally-distributed random numbers

- Produce a normally-distributed random number generator using the
  uniform RNG described above.

The normal distribution, or bell curve, describes the randomness of
measurement.  The mean, or average value, is at zero, while points fall
farther and farther away with increasingly less likelihood.

![A normal distribution curve with standard deviations marked](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/640px-Standard_deviation_diagram.svg.png)

One way to get from a uniform random number to a normal random number is
[to use the uniform random number as the _cumulative distribution
function_
(CDF)](https://www.omscs-notes.com/simulation/generating-uniform-random-numbers/),
an index into “how far” the value is along the normal curve.

![A cumulative distribution function for three normal distributions](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Normal_Distribution_CDF.svg/640px-Normal_Distribution_CDF.svg.png)

This is an approximation which is accurate to one decimal place:

{% math block=true %}
Z = \frac{U^{0.135} - (1-U)^{0.135}}{0.1975}
{% /math %}

where

- sgn is the signum or sign function.

<!--
$$
Z = \frac{U^{0.135}-(1-U)^{0.135}}{0.1975}
$$
-->

To calculate an arbitrary power of a floating-point number, we require a
few transcendental functions, in particular the natural logarithm and
exponentiation of base {% math %}e{% /math %}.  The following helper
core contains relatively inefficient but clear implementations of
standard numerical methods.

**`/gen/normal.hoon`**

```hoon {% copy=true mode="collapse" %}
!:
=<
|=  n=@ud  :: n is the number of values to return
^-  (list @rs)
=/  values  (rip 5 (~(lcg gen 20.220.524) n))
=/  mask-clear           0b111.1111.1111.1111.1111.1111
=/  mask-fill   0b11.1111.0000.0000.0000.0000.0000.0000
=/  clears    (turn values |=(a=@rs (dis mask-clear a)))
=/  uniforms  (turn clears |=(a=@ (sub:rs (mul:rs .2 (con mask-fill a)) .1.0)))
(turn uniforms normal)
|%
++  factorial
  :: integer factorial, not gamma function
  |=  x=@rs
  ^-  @rs
  =/  t=@rs  .1
  |-  ^-  @rs
  ?:  |(=(x .1) (lth x .1))  t
  $(x (sub:rs x .1), t (mul:rs t x))
++  absrs
  |=  x=@rs  ^-  @rs
  ?:  (gth:rs x .0)
    x
  (sub:rs .0 x)
++  exp
  |=  x=@rs
  ^-  @rs
  =/  rtol  .1e-5
  =/  p   .1
  =/  po  .-1
  =/  i   .1
  |-  ^-  @rs
  ?:  (lth:rs (absrs (sub:rs po p)) rtol)  p
  $(i (add:rs i .1), p (add:rs p (div:rs (pow-n x i) (factorial i))), po p)
++  pow-n
  ::  restricted power, based on integers only
  |=  [x=@rs n=@rs]
  ^-  @rs
  ?:  =(n .0)  .1
  =/  p  x
  |-  ^-  @rs
  ?:  (lth:rs n .2)  p
  $(n (sub:rs n .1), p (mul:rs p x))
++  ln
  ::  natural logarithm, z > 0
  |=  z=@rs
  ^-  @rs
  =/  rtol  .1e-5
  =/  p   .0
  =/  po  .-1
  =/  i   .0
  |-  ^-  @rs
  ?:  (lth:rs (absrs (sub:rs po p)) rtol)
    (mul:rs (div:rs (mul:rs .2 (sub:rs z .1)) (add:rs z .1)) p)
  =/  term1  (div:rs .1 (add:rs .1 (mul:rs .2 i)))
  =/  term2  (mul:rs (sub:rs z .1) (sub:rs z .1))
  =/  term3  (mul:rs (add:rs z .1) (add:rs z .1))
  =/  term  (mul:rs term1 (pow-n (div:rs term2 term3) i))
  $(i (add:rs i .1), p (add:rs p term), po p)
++  powrs
  ::  general power, based on logarithms
  ::  x^n = exp(n ln x)
  |=  [x=@rs n=@rs]
  (exp (mul:rs n (ln x)))
++  normal
  |=  u=@rs
  (div:rs (sub:rs (powrs u .0.135) (powrs (sub:rs .1 u) .0.135)) .0.1975)
++  gen
  |_  [z=@ud]
  ++  lcg
    |=  n=@ud                 :: n is the number of bits to return
    =/  a  742.938.285        :: a is the multiplier
    =/  e  31                 :: e is the exponent
    =/  m  (sub (pow 2 e) 1)  :: modulus
    =/  index  0
    =/  accum  *@ub
    |-  ^-  @ub
    ?:  =(index n)  accum
    %=  $
      index  +(index)
      z      (mod (mul a z) m)
      accum  (cat 5 z accum)
    ==
  --
--
```

### Exercise:  Upgrade the normal RNG

A more complicated formula uses several constants to improve the
accuracy significantly:

{% math block=true %}
Z = \text{sgn}\left(U-\frac{1}{2}\right) \left( t - \frac{c_{0}+c_{1} t+c_{2} t^{2}}{1+d_{1} t+d_{2} t^{2} + d_{3} t^{3}} \right)
{% /math %}

where

- sgn is the signum or sign function;
- {% math %}t{% /math %} is {% math %}\sqrt{-\ln[\min(U, 1-U)^2]}{% /math %}; and
- the constants are:
  - {% math %}c_0 = 2.515517{% /math %}
  - {% math %}c_1 = 0.802853{% /math %}
  - {% math %}c_2 = 0.010328{% /math %}
  - {% math %}d_1 = 1.532788{% /math %}
  - {% math %}d_2 = 0.189268{% /math %}
  - {% math %}d_3 = 0.001308{% /math %}

<!--
$$
Z = \text{sgn}\left(U-\frac{1}{2}\right) \left( t - \frac{c_{0}+c_{1} t+c_{2} t^{2}}{1+d_{1} t+d_{2} t^{2} + d_{3} t^{3}} \right)
$$
-->

- Implement this formula in Hoon to produce normally-distributed random numbers.

```hoon
!:
=<
|=  n=@ud  :: n is the number of values to return
^-  (list @rs)
=/  values  (rip 5 (~(lcg gen 20.220.524) n))
=/  mask-clear           0b111.1111.1111.1111.1111.1111
=/  mask-fill   0b11.1111.0000.0000.0000.0000.0000.0000
=/  clears    (turn values |=(a=@rs (dis mask-clear a)))
=/  uniforms  (turn clears |=(a=@ (sub:rs (mul:rs .2 (con mask-fill a)) .1.0)))
(turn uniforms normal)
|%
++  sgn
  |=  x=@rs
  ^-  @rs
  ?:  (lth:rs x .0)
    .-1
  ?:  (gth:rs x .0)
    .1
  .0
++  factorial
  :: integer factorial, not gamma function
  |=  x=@rs
  ^-  @rs
  =/  t=@rs  .1
  |-  ^-  @rs
  ?:  |(=(x .1) (lth x .1))  t
  $(x (sub:rs x .1), t (mul:rs t x))
++  absrs
  |=  x=@rs  ^-  @rs
  ?:  (gth:rs x .0)
    x
  (sub:rs .0 x)
++  exp
  |=  x=@rs
  ^-  @rs
  =/  rtol  .1e-5
  =/  p   .1
  =/  po  .-1
  =/  i   .1
  |-  ^-  @rs
  ?:  (lth:rs (absrs (sub:rs po p)) rtol)  p
  $(i (add:rs i .1), p (add:rs p (div:rs (pow-n x i) (factorial i))), po p)
++  pow-n
  ::  restricted power, based on integers only
  |=  [x=@rs n=@rs]
  ^-  @rs
  ?:  =(n .0)  .1
  =/  p  x
  |-  ^-  @rs
  ?:  (lth:rs n .2)  p
  $(n (sub:rs n .1), p (mul:rs p x))
++  ln
  ::  natural logarithm, z > 0
  |=  z=@rs
  ^-  @rs
  =/  rtol  .1e-5
  =/  p   .0
  =/  po  .-1
  =/  i   .0
  |-  ^-  @rs
  ?:  (lth:rs (absrs (sub:rs po p)) rtol)
    (mul:rs (div:rs (mul:rs .2 (sub:rs z .1)) (add:rs z .1)) p)
  =/  term1  (div:rs .1 (add:rs .1 (mul:rs .2 i)))
  =/  term2  (mul:rs (sub:rs z .1) (sub:rs z .1))
  =/  term3  (mul:rs (add:rs z .1) (add:rs z .1))
  =/  term  (mul:rs term1 (pow-n (div:rs term2 term3) i))
  $(i (add:rs i .1), p (add:rs p term), po p)
++  powrs
  ::  general power, based on logarithms
  ::  x^n = exp(n ln x)
  |=  [x=@rs n=@rs]
  (exp (mul:rs n (ln x)))
++  minrs
  |=  [a=@rs b=@rs]
  ?:  (lth:rs a b)  a  b
++  normal
  |=  u=@rs
  =/  c0  .2.515517
  =/  c1  .0.802853
  =/  c2  .0.010328
  =/  d1  .1.532788
  =/  d2  .0.189268
  =/  d3  .0.001308
  =/  t  (sqt:rs (powrs (sub:rs .1 (ln (minrs u (sub:rs .1 u)))) .2))
  =/  znum  :(add:rs c0 (mul:rs c1 t) (mul:rs c2 (mul:rs t t)))
  =/  zden  :(add:rs .1 (mul:rs d1 t) (mul:rs d2 (mul:rs t t)) (mul:rs d3 (powrs t .3)))
  (mul:rs (sgn (sub:rs u .0.5)) (sub:rs t (div:rs znum zden)))
++  gen
  |_  [z=@ud]
  ++  lcg
    |=  n=@ud                 :: n is the number of bits to return
    =/  a  742.938.285        :: a is the multiplier
    =/  e  31                 :: e is the exponent
    =/  m  (sub (pow 2 e) 1)  :: modulus
    =/  index  0
    =/  accum  *@ub
    |-  ^-  @ub
    ?:  =(index n)  accum
    %=  $
      index  +(index)
      z      (mod (mul a z) m)
      accum  (cat 5 z accum)
    ==
  --
--
```

##  Hashing

### Hoon Operations

The Hoon standard library supports fast insecure hashing with {% tooltip
label="++mug" href="/language/hoon/reference/stdlib/2e#mug" /%}, which
accepts any {% tooltip label="noun" href="/glossary/noun" /%} and
produces an atom of the hash.

```hoon
> `@ux`(mug 1)
0x715c.2a60

> `@ux`(mug 2)
0x718b.9468

> `@ux`(mug 3)
0x72a8.ef1a

> `@ux`(mug 1.000.000)
0x5145.9d7d

> `@ux`(mug .)
0x6c91.8422
```

`++mug` operates on the raw form of the noun however, without
Hoon-specific metadata like aura:

```hoon
> (mug 0x5)
721.923.263

> (mug 5)
721.923.263
```

Hoon also includes [SHA-256 and
SHA-512](https://en.wikipedia.org/wiki/SHA-2)
[tooling](/language/hoon/reference/stdlib/3d).
({% tooltip label="++og" href="/language/hoon/reference/stdlib/3d#og"
/%}, the random number generator, is based on SHA-256 hashing.)

- {% tooltip label="++shax" href="/language/hoon/reference/stdlib/3d#shax" /%} produces
    a hashed atom of 256 bits from any {% tooltip label="atom"
    href="/glossary/atom" /%}.

    ```hoon > (shax 1)
    69.779.012.276.202.546.540.741.613.998.220.636.891.790.827.476.075.440.677.599.814.057.037.833.368.907
    
    > `@ux`(shax 1)
    0x9a45.8577.3ce2.ccd7.a585.c331.d60a.60d1.e3b7.d28c.bb2e.de3b.c554.4534.2f12.f54b

    > `@ux`(shax 2)
    0x86d9.5764.98ea.764b.4924.3efe.b05d.f625.0104.38c6.a55d.5b57.8de4.ff00.c9b4.c1db

    > `@ux`(shax 3)
    0xc529.ffad.9a5a.b611.62b1.1d61.6b63.9e00.586b.a846.746a.197d.4daf.78b9.08ed.4f08

    > `@ux`(shax 1.000.000)
    0x84a4.929b.1d69.708e.d4b7.0fb8.ca97.cc85.c4a6.1aae.4596.f753.d0d2.6357.e7b9.eb0f
    ```

- {% tooltip label="++shaz" href="/language/hoon/reference/stdlib/3d#shaz" /%} produces
  a hashed atom of 512 bits from any atom.

    ```hoon
    > (shaz 1)
    3.031.947.054.025.992.811.210.838.487.475.158.569.967.793.095.050.169.760.709.406.427.393.828.309.497.273.121.275.530.382.185.415.047.474.588.395.933.812.689.047.905.034.106.140.802.678.745.778.695.328.891

    > `@ux`(shaz 1)
    0x39e3.d936.c6e3.1eaa.c08f.cfcf.e7bb.4434.60c6.1c0b.d5b7.4408.c8bc.c35a.6b8d.6f57.00bd.cdde.aa4b.466a.e65f.8fb6.7f67.ca62.dc34.149e.1d44.d213.ddfb.c136.68b6.547b

    > `@ux`(shaz 2)
    0xcadc.698f.ca01.cf29.35f7.6027.8554.b4e6.1f35.4539.75a5.bb45.3890.0315.9bc8.485b.7018.dd81.52d9.cc23.b6e9.dd91.b107.380b.9d14.ddbf.9cc0.37ee.53a8.57b6.c948.b8fa

    > `@ux`(shaz 3)
    0x4ba.a6ba.4a01.12e6.248b.5e89.9389.4786.aced.1a59.136b.78c6.7076.eb90.2221.d7a5.453a.56d1.446d.17d1.33cd.b468.f798.eb6b.dcee.f071.7040.7a2f.aa94.df7d.81f5.5be4

    > `@ux`(shaz 1.000.000)
    0x4c13.ef8b.09cf.6e59.05c4.f203.71a4.9cec.3432.ba26.0174.f964.48f1.5475.b2dd.2c59.98c2.017c.9c03.cbea.9d5f.591b.ff23.bbff.b0ae.9c67.a4a9.dd8d.748a.8e14.c006.cbcc
    ```
