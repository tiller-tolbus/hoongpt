# Hoon School Complete Documentation

---
+++
title = "Hoon School"
weight = 5
sort_by = "weight"
insert_anchor_links = "right"
+++

Hoon School is designed to teach you Hoon without assuming you have an
extensive programming background.  You should be able to following most
of it even if you have no programming experience at all yet, though of
course experience helps.  We strongly encourage you to try out all the
examples of each lesson.  Hoon School is meant for the beginner, but
it's not meant to be skimmed.  Each lesson consists of:

- **Explanations**, which are prose-heavy commentary on the Hoon fundamentals.

- **Exercises**, which challenge you to clarify or expand your own understanding in practice.

- **Tutorials**, which are line-by-line commentary on example programs.

There are two flavors of Hoon School:  the Hoon School Live cohort
class, in which you work through lessons with other students and receive
a certification (`%gora`) for completion, and these written Hoon School
docs.  To sign up for a future cohort of Hoon School Live, please [let
us know of your interest here](/courses) and we'll be in touch.


##  Why Hoon?

The short version is that Hoon uses Urbit's provisions and protocols to
enable very fast application development with shared primitives,
sensible affordances, and straightforward distribution.

Urbit consists of an identity protocol ({% tooltip label="\"Azimuth\""
href="/glossary/azimuth" /%}, or “Urbit ID”) and a system protocol ({%
tooltip label="\"Arvo\"" href="/glossary/arvo" /%}, or “Urbit OS”).
These two parts work hand-in-hand to build your hundred-year computer.

1. **Urbit ID (Azimuth)** is a general-purpose public-key infrastructure
   (PKI) on the Ethereum blockchain, used as a platform for Urbit
   identities.  It provides a system of scarce and immutable identities
   which are cryptographically secure.

2. **Urbit OS (Arvo)** is an operating system which provides the
   software for the personal server platform that constitutes the
   day-to-day usage of Urbit.  Arvo works over a
   [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer)
   [end-to-end-encrypted](https://en.wikipedia.org/wiki/End-to-end_encryption)
   network to interact with other Urbit ships (or unique instances).

Arvo is an axiomatic operating system which restricts itself to pure
mathematical functions, making it
[deterministic](https://en.wikipedia.org/wiki/Deterministic_algorithm)
and
[functional-as-in-programming](https://en.wikipedia.org/wiki/Functional_programming).
Such strong guarantees require an operating protocol, the [Nock virtual
machine](/language/nock/reference/definition), which will be persistent across
hardware changes and always provide an upgrade path for necessary
changes.

It's hard to write a purely functional operating system on hardware
which doesn't make such guarantees, so Urbit OS uses a new language,
Hoon, which compiles to Nock and hews to the necessary conceptual models
for a platform like Urbit.  [The Hoon overview](/language/hoon) covers
more of the high-level design decisions behind the language, as does
[developer ~rovnys-ricfer's
explanation](https://urbit.org/blog/why-hoon/).

Hoon School introduces and explains the fundamental concepts you need in
order to understand Hoon's semantics.  It then introduces a number of
key examples and higher-order abstractions which will make you a more
fluent Hoon programmer.

Once you have completed Hoon School, you should work through [App
School](/courses/app-school) to learn how to build full applications on
Urbit.

##  Environment Setup

An Urbit ship is a particular realization of an _identity_ and an _event
log_ or _state_.  Both of these are necessary.

Since live network identities (_liveships_) are finite, scarce, and
valuable, most developers prefer to write new code using fake identities
(_fakeships_ or _fakezods_).  A fakeship is also different from a comet,
which is an unkeyed liveship.

Two fakeships can communicate with each other on the same machine, but
have no awareness of the broader Urbit network.  We won't need to use
this capability in Hoon School Live, but it will be helpful later when
you start developing networked apps.

Before beginning, you'll need to get a development ship running and
configure an appropriate editor.  See the [Environment
Setup](/courses/environment) guide for details.

Once you have a `dojo>` prompt, the system is ready to go and waiting on input.

##  Getting started

Once you've created your development ship, let's try a basic command.
Type `%-  add  [2 2]` at the prompt and hit `Return`.  (Note the double
spaces before and after `add`.)  Your screen now shows:

```hoon {% copy=true %}
fake: ~zod
ames: czar: ~zod on 31337 (localhost only)
http: live (insecure, public) on 80
http: live (insecure, loopback) on 12321
> %-  add  [2 2]
4
~zod:dojo>
```

You just used a function from the Hoon standard library, `add`, which
for reasons that will become clear later is frequently written {%
tooltip label="++add" href="/language/hoon/reference/stdlib/1a#add" /%}.
Next, quit Urbit by entering {% tooltip label="|exit"
href="/manual/os/dojo-tools#exit" /%} :

```hoon {% copy=true %}
> %-  add  [2 2]
4
~zod:dojo> |exit
$
```

Your ship isn't running anymore and you're back at your computer's
normal terminal prompt.  If your ship is ~zod, then you can restart the
ship by typing:

```hoon {% copy=true %}
urbit zod
```

You've already used a standard library function to produce one value, in
the Dojo. Now that your ship is running again, let's try another. Enter
the number `17`.

(We won't show the `~zod:dojo>` prompt from here on out.  We'll just
show the echoed command along with its result.)

You'll see:

```hoon {% copy=true %}
> 17
17
```

You asked Dojo to evaluate `17` and it echoed the number back at you.
This value is a {% tooltip label="noun" href="/glossary/noun" /%}. We'll
talk more about nouns in the next lesson.

Basically, every Hoon expression operates on the values it is given
until it reduces to some form that can't evaluate any farther.  This is
then returned as the result of the evaluation.

One more:

```hoon {% copy=true %}
> :-  1  2
[1 2]
```

This `:-` rune takes two values and composes them into a {% tooltip
label="cell" href="/glossary/cell" /%}, a pair of values.


##  Pronouncing Hoon

Hoon uses {% tooltip label="runes" href="/glossary/rune" /%}, or
two-character ASCII symbols, to describe its structure.  (These are
analogous to keywords in other programming languages.)  Because there
has not really been a standard way of pronouncing, say, `#` (hash,
pound, number, sharp, hatch) or `!` (exclamation point, bang, shriek,
pling), the authors of Urbit decided to adopt a one-syllable mnemonic to
uniquely refer to each.

It is highly advisable for you to learn these pronunciations, as the
documentation and other developers employ them frequently.  For
instance, a rune like `|=` is called a “bartis”, and you will find it
designated as such in the docs, in the source code, and among the
developers.

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
weight = 11
nodes = [110, 113]
objectives = ["Distinguish nouns, cells, and atoms.", "Apply auras to transform an atom.", "Identify common Hoon molds, such as cells, lists, and tapes.", "Pin a face to the subject.", "Make a decision at a branch point.", "Distinguish loobean from boolean operations.", "Slam a gate (call a function)."]
+++

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS110 - Syntax.mp4" /%}

_This module will discuss the fundamental data concepts of Hoon and how
programs handle control flow._

The study of Hoon can be divided into two parts: syntax and semantics.

1. The **syntax** of a programming language is the set of rules that
   determine what counts as admissible code in that language. It
   determines which characters may be used in the source, and also how
   these characters may be assembled to constitute a program. Attempting
   to run a program that doesn’t follow these rules will result in a
   syntax error.

2. The **semantics** of a programming language concerns the meaning of
   the various parts of that language’s code.

In this lesson we will give a general overview of Hoon’s syntax. By the
end of it, you should be familiar with all the basic elements of Hoon
code.

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

### Exercise:  Aura Conversions

Convert between some of the given auras at the {% tooltip label="Dojo"
href="/glossary/dojo" /%} prompt, e.g.:

- `100` to `@p`
- `0b1100.0101` to `@p`
- `0b1100.0101` to `@ux`
- `0b1100.0101` to `@ud`
- `~` to any other aura

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

{% /callout %}

##  Verbs (Runes)

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS113 - Basic Coding.mp4" /%}

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

### Exercise:  Identifying Unknown Runes

Here is a lightly-edited snippet of Hoon code.  Anything written after a
`::` {% tooltip label="colcol"
href="/language/hoon/reference/rune/col#-colcol" /%} is a _comment_ and
is ignored by the computer.  (Comments are useful for human-language
explanations.)

```hoon {% copy=true %}
%-  send
::  forwards compatibility with next-dill
?@  p.kyz  [%txt p.kyz ~]
?:  ?=  %hit  -.p.kyz
  [%txt ~]
?.  ?=  %mod  -.p.kyz
  p.kyz
=/  =@c
  ?@  key.p.kyz  key.p.kyz
    ?:  ?=  ?(%bac %del %ret)  -.key.p.kyz 
      `@`-.key.p.kyz
    ~-
?:  ?=  %met  mod.p.kyz  [%met c]  [%ctl c]
```

1. Mark each rune.
2. For each rune, find its corresponding children.  (You don't need to
   know what a rune does to identify how things slot together.)
3. Consider these questions:
    - Is every pair of punctuation marks a rune?
    - How can you tell a rune from other kinds of marks?
 
One clue:  every rune in Hoon (except for one, not in the above code)
has _at least one child_.

### Exercise:  Inferring Rune Behavior

Here is a snippet of Hoon code:
 
```hoon {% copy=true %}
^-  list
:~  [hen %slip %e %init ~]
    [hen %slip %d %init ~]
    [hen %slip %g %init ~]
    [hen %slip %c %init ~]
    [hen %slip %a %init ~]
==
```

Without looking it up first, what does the `==` {% tooltip
label="tistis" href="/language/hoon/reference/rune/terminators#-tistis"
/%} do for the `:~` {% tooltip label="colsig"
href="/language/hoon/reference/rune/col#-colsig" /%} rune?  Hint: some
runes can take any number of arguments.

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

### Exercise:  A Large Power of Two

Create two numbers named `two` and `twenty`, with appropriate values,
using the `=/` tisfas rune.
 
Then use these values to calculate 2²⁰ with `++pow` and `%-` cenhep.


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

### Exercise:  Comparing Cells

Enter the following cells:

```hoon {% copy=true %}
[1 2 3]
[1 [2 3]]
[[1 2] 3]
[[1 2 3]]
[1 [2 [3]]]
[[1 2] [3 4]]
[[[1 2] [3 4]] [[5 6] [7 8]]]
```

Note which are the same as each other, and which are not.  We'll look at
the deeper structure of cells later when we consider trees.

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

<!--$$
H(x)
=
\begin{cases} 1, & x > 0 \\ 0, & x \le 0 \end{cases}
$$-->

_However_, we don't yet know how to represent a negative value!  All of
the decimal values we have used thus far are unsigned (non-negative)
values, `@ud`.  For now, the easiest solution is to just translate the
Heaviside function so it activates at a different value:

{% math block=true %}
H_{10}(x)
=
\begin{cases} 1, & x > 10 \\\ 0, & x \le 10 \end{cases}
{% /math %}

<!--$$
H_{10}(x)
=
\begin{cases} 1, & x > 10 \\ 0, & x \le 10 \end{cases}
$$-->

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

### Exercise:  “Absolute” Value (Around Ten)

Implement a version of the absolute value function, {% math %}|x|{% /math %},
similar to the Heaviside implementation above.  (Translate it to 10 as
well since we still can't deal with negative numbers; call this
{% math %}|x|_{10}{% /math %}.)

{% math block=true %}
|x|_{10}
=
\begin{cases} x-10, & x > 10 \\\ 10-x & 0 \le x \le 10 \end{cases}
{% /math %}

Test it on a few values like 8, 9, 10, 11, and 12.


# C-azimuth.md

---

+++
title = "2. Azimuth (Urbit ID)"
weight = 12
nodes = [102, 112]
objectives = ["Understand the role of the public-key infrastructure in Urbit.", "Describe the high-level architecture of the Urbit ID address space and distinguish types of points.", "Interpret and apply the Azimuth point naming scheme.", "Identify point features such as activity.", "List at least two services/roles provided by a galaxy for the network.", "List at least two services provided by a star for its planets.", "Use Hoon to map the Azimuth address space domains and boundaries.", "Identify points, sponsors, neighbors, etc. from `@p` identifiers and simple operations."]
+++

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS102 - Azimuth.mp4" /%}

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

### Exercise:  Finding neighbors

A neighbor of a point is a point which occupies the point immediately
above or below that point's `@ud` number.

For instance, the `@ud` of ~sampel-palnet may be found by:

```hoon
> `@ud`~sampel-palnet
1.624.961.343
```

The previous neighbor of ~sampel-palnet is thus:

```hoon
> %-(sub [1.624.961.343 1])
1.624.961.342

> `@p`1.624.961.342
~datwyn-lavrud
```

- Find the next neighbor of ~sampel-palnet.

### Exercise:  Finding the sponsor of a neighbor

The sponsor of ~sampel-palnet may be found by:

```hoon
> (sein:title our now ~sampel-palnet)
~talpur
```

The sponsor of the previous neighbor of ~sampel-palnet is thus:

```hoon
> %-(sub [1.624.961.343 1])
1.624.961.342

> `@p`1.624.961.342
~datwyn-lavrud

> (sein:title our now ~datwyn-lavrud)
~talnep
```

- Find the sponsor of the next neighbor of ~sampel-palnet.

### Exercise:  Finding the child of a point

A point has many children, but the first moon of a planet is located at
that point plus 2³² = `4.294.967.296`.

The first moon of ~sampel-palnet is:

```hoon
> `@p`%-(add [~sampel-palnet 4.294.967.296])
~doznec-sampel-palnet
```

- What are the first moon children of ~sampel-palnet's neighbors?

- What is the first planet of the star ~sampel?  (Check the above text
  to determine the offset.)



# D-gates.md

---

+++
title = "3. Gates (Functions)"
weight = 13
nodes = [111, 115, 120]
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

### Exercise:  Converting Between Forms

Convert each of the following irregular forms into the correct regular runic syntax.

1. `(add 1 2)`
2. `` `@ub`16 ``
3. `[%lorem %ipsum]`
4. `[%lorem %ipsum %dolor]` (can do two ways)

Convert each of the following regular forms into the correct irregular syntax.

1. `:-  %lemon  %jello`
2. `^-  @p  ^-  @  256`
3. `%-  pow  :-  2  16`


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

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS120 - Gates.mp4" /%}

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


##  Coordinating Files

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS111 - Filesystem.mp4" /%}

In pragmatic terms, an Urbit ship is what results when you successfully
boot a new ship.  If you are in the host OS, what you see is an
apparently-empty folder:

```sh
$ ls zod
$
```

(For this lesson in particular take pains to distinguish the host OS
prompt `$ ` from the Urbit Dojo prompt `> `.  You should look into
particular system setup instructions for Windows, macOS, and Linux
hosts.) <!-- TODO -->

Contrast that apparently empty folder with what the `+ls %` command
shows you from inside of your Urbit (at the Dojo prompt):

```hoon
> +ls %
app/ desk/bill gen/ lib/ mar/ sur/ sys/ ted/
```

Urbit organizes its internal view of data and files as _desks_, which
are associated collections of code and data.  These are not visible to
the host operating system unless you explicitly mount them, and changes
on one side are not made clear to the other until you “commit” them.
(Think of Dropbox, except that you have to explicitly synchronize to see
changes somewhere else.)

Inside of your ship (“Mars”), you can mount a particular desk to the
host operating system (“Earth”):

```hoon
> |mount %base
```

Now check what happens outside of your ship:

```sh
$ ls zod
base/
$ ls zod/base
app/  desk.bill gen/ lib/ mar/ sur/ sys/ ted/
```

If we make a change in the folder on Earth, the contents will only
update on Mars if we explicitly tell the two systems to coordinate.

On Earth:

```sh
$ cp zod/base/desk.bill zod/base/desk.txt
```

On Mars:

```hoon
> |commit %base
+ /~zod/base/2/desk/txt
```

You can verify the contents of the copied files are the same using the
{% tooltip label="+cat" href="/manual/os/dojo-tools#cat" /%} command:

```hoon
> +cat %/desk/bill

> +cat %/desk/txt
```

(Dojo does know what a `bill` file is, so it displays the contents slightly formatted.  They are actually identical.)

We will use this {% tooltip label="|commit"
href="/manual/os/dojo-tools#commit" /%} pattern to store persistent code
as files, editing on Earth and then synchronizing to Mars.


##  Building Code

The missing piece to really tie all of this together is the ability to
store a gate and use it at a later time, not just in the same long Dojo
session.  Enter the {% tooltip label="generator"
href="/glossary/generator" /%}.

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

(Any time you write code to use later, you should include some comments
to explain what the code does and perhaps how it does that.)

### The Process

1. Open a text editor.
2. Copy the gate above into the text editor.  (Double-check that
   two-space gaps are still gaps; some text editors chew them up into
   single-space aces.)
3. Save the gate as `square.hoon` in the `base/gen` folder of your
   fakeship.
4. In the Dojo, `|commit %base`.  _You should see a message indicating
   that the file has been loaded._
5. Run the generator with `+square 5`.

Any generator can be run the same way, beginning with the `+` lus
character and followed by the name of a file in the `base/gen`
directory.

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

**Note**: If you're using VS Code on Windows, you might need to manually
change the line endings from Windows-style `CRLF` to Unix-style `LF` in
the status bar at the bottom.  Urbit requires Unix-style line endings
for Hoon files.

### Exercise:  Triangular Function
 
- Implement the triangular function as a gate and save it as a generator
  `tri.hoon`.

    ![](https://lh4.googleusercontent.com/zdauTDEWvhhOkFEb6VcDEJ4SITsHOgcStf4NYFQSIVjTDPjaCqYGdin9TDCCeTG3OyMrUUdq-JtViiu_c9wuojim_mHpV6-DoTNwZzYz5_6qVVvN5fc3hEuSna2GwY15RQ=w740)

### Coding Piecemeal

If you need to test code without completing it, you can stub out
as-yet-undefined arms with the `!!` {% tolltip label="zapzap"
href="/language/hoon/reference/rune/zap#-zapzap" /%} crash rune.  `!!`
is the only rune which has no children, and it's helpful when you need
something to satisfy Hoon syntax but aren't ready to flesh out the
program yet.

### Building Code Generally

A generator gives us on-demand access to code, but it is helpful to load
and use code from files while we work in the Dojo.

A conventional library import with `/+` {% tooltip label="faslus"
href="/language/hoon/reference/rune/fas#-faslus" /%} will work in a
generator or another file, but won't work in Dojo, so you can't use `/+`
faslus interactively.

Instead, you need to use the {% tooltip label="-build-file"
href="/manual/os/dojo-tools#-build-file" /%} thread to load the code.
Most commonly, you will do this with library code when you need a
particular core's functionality.

`-build-file` accepts a file path and returns the built operational
code, to which you can then attach a `face`.  For instance:

```hoon
> =ntw -build-file %/lib/number-to-words/hoon

> one-hundred:numbers:ntw  
100

> (to-words:eng-us:numbers:ntw 19)
[~ "nineteen"]
```

There are also a number of other import runes which make library,
structure, and mark code available to you.  Right now, the only one you
need to worry about is `/+` faslus.

For simplicity, everything we do will take place on the `%base` desk for
now.  We will learn how to create a library in a subsequent lesson.

### Exercise:  Loading a Library

In a generator, load the `number-to-words` library using the `/+` faslus
rune.  (This must take place at the very top of your file.)
 
Use this to produce a gate which accepts an unsigned decimal integer and
returns the text interpretation of its increment.


# E-types.md

---

+++
title = "4. Molds (Types)"
weight = 14
nodes = [125]
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

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS156 - Molds.mp4" /%}

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
weight = 15
nodes = [130, 133]
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

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS130 - Traps.mp4" /%}

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

### Exercise:  Calculate a sequence of numbers

Produce a gate (generator) which accepts a `@ud` value and calculates
the series where the {% math %}i^\text{th}{% /math %} term in the series
is given by the equation

{% math block=true %}
n_{i} = i^{2}
\textrm{,}
{% /math %}

<!--
$$
n_{i} = i^{2}
\textrm{,}
$$
-->

that is, the first numbers are 0, 1, 4, 9, 16, 25, etc.

For this exercise, you do not need to store these values in a list.
Calculate each one but only return the final value.

### Exercise:  Output each letter in a `tape`

Produce a gate (generator) which accepts a {% tooltip label="tape"
href="/glossary/tape" /%} value and returns a `(list @ud)` containing
the ASCII value of each character.  Use a `|-` {% tooltip label="barhep"
href="/language/hoon/reference/rune/bar#--barhep" /%} {% tooltip
label="trap" href="/glossary/trap" /%}.
The previous code simply modified a value by addition.  You can
generalize this to other arithmetic processes, like multiplication, but
you can also grow a data structure like a {% tooltip label="list"
href="/glossary/list" /%}.

For example, given the `tape` `"hello"`, the generator should return the
list `[104 101 108 108 111 ~]`.  (A list is structurally a
null-terminated tuple, or rightwards-branching cell ending in `~` or
`0`.)  We can equivalently write `~[104 101 108 108 111]` which is a
special syntax reducing to the same thing.

Two tools that may help:

- You can retrieve the _n_^th^ element in a `tape` using the {% tooltip
  label="++snag" href="/language/hoon/reference/stdlib/2b#snag" /%}
  gate, e.g. ``(snag 3 `(list @ud)`~[1 2 3 4 5])`` yields `4` (so
  `++snag` is zero-indexed; it counts from zero).
- You can join an element to a list using the
  [`++snoc`](/language/hoon/reference/stdlib/2b#snoc) gate, e.g. ``(snoc
  `(list @ud)`~[1 2 3] 4)`` yields `~[1 2 3 4]`.

```hoon {% copy=true %}
|=  [input=tape]
=/  counter  0
=/  results  *(list @ud)
|-
?:  =(counter (lent input))
  results
=/  ascii  `@ud`(snag counter input)
%=  $
  counter  (add counter 1)
  results  (snoc results ascii)
==
```


##  Cores

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS133 - Cores.mp4" /%}

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

### Exercise:  Produce a Gate Arm

- Compose a core which contains arms for multiplying a value by two and
  for dividing a value by two.

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
Some children's songs like [“Yon
Yonson”](https://en.wikipedia.org/wiki/Yon_Yonson) or [“The Song That
Never Ends”](https://en.wikipedia.org/wiki/The_Song_That_Never_Ends)
rely on such recursive humor.

> This is the song that never ends
> Yes, it goes on and on, my friends
> Some people started singing it not knowing what it was
> And they′ll continue singing it forever just because—
>
> This is the song that never ends
> . . .

You need to make sure when you compose a {% tooltip label="trap"
href="/glossary/trap" /%} that it has a base case which returns a noun.
The following trap results in an infinite loop:

```hoon {% copy=true %}
=/  index  1
|-
?:  (lth index 1)  ~
$(index +(index))
```

If you find yourself caught in such a loop, press `Ctrl`+`C` to stop
execution.

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

<!--
F_n = F_{n-1} + F_{n-2}
-->

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

<!--
\begin{array}{lcl}
\operatorname{A}(0, n) & = & n + 1 \\
\operatorname{A}(m+1, 0) & = & \operatorname{A}(m, 1) \\
\operatorname{A}(m+1, n+1) & = & \operatorname{A}(m, \operatorname{A}(m+1, n))
\end{array}
-->

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

### Exercise:  The Sudan Function

The [Sudan function](https://en.wikipedia.org/wiki/Sudan_function) is
related to the Ackermann function.

{% math block=true %}
\begin{array}{lll}
F_0 (x, y) & = x+y \\\\
F_{n+1} (x, 0) & = x & \text{if } n \ge 0 \\\\
F_{n+1} (x, y+1) & = F_n (F_{n+1} (x, y), F_{n+1} (x, y) + y + 1) & \text{if } n\ge 0
\end{array}
{% /math %}

- Implement the Sudan function as a gate.


# G-trees.md

---

+++
title = "6. Trees and Addressing"
weight = 16
nodes = [135, 140, 156]
objectives = ["Address nodes in a tree using numeric notation.", "Address nodes in a tree using lark notation.", "Address data in a tree using faces.", "Distinguish `.` and `:` notation.", "Diagram Hoon structures such as gates into the corresponding abstract syntax tree.", "Use lists to organize data.", "Convert between kinds of lists (e.g. tapes).", "Diagram lists as binary trees.", "Operate on list elements using `snag`, `find`, `weld`, etc.", "Explain how Hoon manages the subject and wing search paths.", "Explain how to skip to particular matches in a wing search path through the subject.", "Identify common Hoon patterns: batteries, and doors, arms, wings, and legs."]
+++

_Every noun in Urbit is an atom or a cell.  This module will elaborate
how we can use this fact to locate data and evaluate code in a given
expression.  It will also discuss the important `list` mold builder and
a number of standard library operations._

##  Trees

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS135 - Trees.mp4" /%}

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

### Exercise:  Map Nouns to Tree Diagrams

- Consider each of the following nouns.  Which tree diagram do they
  correspond to?  (This is a matching exercise.)

    | Noun | Tree Diagram |
    | ---- | ------------ |
    | 1. `[[[1 2] 3] 4]` | A. ![](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-exercise-1.png) | 
    | 2. `[[1 2] 3 4]` | B. ![](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-exercise-2.png) | 
    | 3. `[1 2 3 4]` | C. ![](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-exercise-3.png) | 

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

### Exercise:  Tapes for Text
 
A {% tooltip label="tape" href="/glossary/tape" /%} is one way of
representing a text message in Hoon.  It is written with double quotes:
 
```hoon {% copy=true %}
"I am the very model of a modern Major-General"
```

A `tape` is actually a `(list @t)`, a binary tree of single characters
which only branches rightwards and ends in a `~`:
 
![](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-tape.png)

- What are the addresses of each letter in the tree for the Gilbert &
  Sullivan quote above?  Can you see the pattern?  Can you get the
  address of EVERY letter through `l`?

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

### Exercise:  Address the Fruit Tree

Produce the numeric and lark-notated equivalent addresses for each of
the following nodes in the binary fruit tree:

![A fruit tree](https://media.urbit.org/docs/userspace/hoon-school/binary-tree-fruit.png)

- 🍇
- 🍌
- 🍉
- 🍏
- 🍋
- 🍑
- 🍊
- 🍍
- 🍒

There is a solution at the bottom of the page.

### Exercise:  Lark Notation

- Use a lark expression to obtain the value 6 in the following noun
  represented by a binary tree:

    ```
              .
             / \
            /   \
           /     \
          .       .
         / \     / \
        /   .   10  .
       /   / \     / \
      .   8   9   11  .
     / \             / \
    5   .           12  13
       / \
      6   7
    ```

- Use a lark expression to obtain the value `9` in the following noun:
  `[[[5 6 7] 8 9] 10 11 12 13]`.

Solutions to these exercises may be found at the bottom of this lesson.

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

Solution #1 in the [Rhonda Numbers](/language/hoon/examples/rhonda) tutorial in the Hoon Workbook illustrates using `^` ket to skip `$` buc matches.

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

### Exercise:  Resolving Wings

Enter the following into dojo:

```hoon {% copy=true %}
=a [[[b=%bweh a=%.y c=8] b="no" c="false"] 9]
```

- Test your knowledge from this lesson by evaluating the following
  expressions and then checking your answer in the dojo or see the
  solutions below.

    1.  `b:a(a [b=%skrt a="four"])`
    2.  `^b:a(a [b=%skrt a="four"])`
    3.  `^^b:a(a [b=%skrt a="four"])`
    4.  `b.a:a(a [b=%skrt a="four"])`
    5.  `a.a:a(a [b=%skrt a="four"])`
    6.  `+.a:a(a [b=%skrt a="four"])`
    7.  `a:+.a:a(a [b=%skrt a="four"])`
    8.  `a(a a)`
    9.  `b:-<.a(a a)`
    10. How many times does the atom `9` appear in `a(a a(a a))`?

    The answers are at the bottom of the page.

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

  **Exercise:  `++flop` Yourself:** Without using flop, write a gate
  that takes a `(list @)` and returns it in reverse order.  There is a
  solution at the bottom of the page.

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

    **Exercise:  `++weld` Yourself:** Without using weld, write a gate
    that takes a `[(list @) (list @)]` of which the product is the
    concatenation of these two lists.  There is a solution at the bottom
    of the page.

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

### Exercise:  Evaluating Expressions

- Without entering these expressions into the Dojo, what are the
  products of the following expressions?

    ```hoon {% copy=true %}
    (lent ~[1 2 3 4 5])
    (lent ~[~[1 2] ~[1 2 3] ~[2 3 4]])
    (lent ~[1 2 (weld ~[1 2 3] ~[4 5 6])])
    ```

### Exercise:  Welding Nouns

First, bind these faces.

```hoon {% copy=true %}
=b ~['moon' 'planet' 'star' 'galaxy']
=c ~[1 2 3]
```

- Determine whether the following Dojo expressions are valid, and if so,
  what they evaluate to.

    ```hoon
    > (weld b b)

    > (weld b c)

    > (lent (weld b c))

    > (add (lent b) (lent c))
    ```

### Exercise:  Palindrome

- Write a gate that takes in a list `a` and returns `%.y` if `a` is a
  palindrome and `%.n` otherwise.  You may use the {% tooltip
  label="++flop" href="/language/hoon/reference/stdlib/2b#flop" /%} function.

## Solutions to Exercises

- Fruit Tree:

  - 🍇 `9` or `-<+`
  - 🍌 `11` or `->+`
  - 🍉 `12` or `+<-`
  - 🍏 `16` or `-<-<`
  - 🍋 `27` or `+<+>`
  - 🍊 `30` or `+>+<`
  - 🍑 `42` or `->->-`
  - 🍒 `62` or `+>+>-`
  - 🍍 `87` or `->->+>`
  

- Resolving Lark Expressions

    ```hoon
    > =b [[[5 6 7] 8 9] 10 11 12 13]

    > -<+<:b
    6
    ```

- Resolving Wing Expressions

    1.  `%bweh`
    2.  `"no"`
    3.  Error: `ford: %slim failed:`
    4.  `%skrt`
    5.  `"four"`
    6.  `a="four"` - Note that this is different from the above!
    7.  `"four"`
    8.  `[[[b=%bweh a=[[[b=%bweh a=%.y c=8] b="no" c="false"] 9] c=8] b="no" c="false"] 9]`
    9.  `%bweh`
    10.  `9` appears 3 times:
    
    ```hoon
    > a(a a(a a))
    [[[ b=%bweh a [[[b=%bweh a=[[[b=%bweh a=%.y c=8] b="no" c="false"] 9] c=8] b="no" c="false"] 9] c=8] b="no" c="false"] 9]
    ```

- Roll-Your-Own-`++flop`:

    ```hoon {% copy=true %}
    ::  /gen/flop.hoon
    ::
    |=  a=(list @)
    =|  b=(list @)
    |-  ^-  (list @)
    ?~  a  b
    $(b [i.a b], a t.a)
    ```

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

- `++weld` expressions

    Running each one in the Dojo:

    ```hoon
    > (weld b b)
    <|moon planet star galaxy moon planet star galaxy|>
    ```

    This will not run because `weld` expects the elements of both lists to be of the same type:

    ```hoon
    > (weld b c)
    ```

    This also fails for the same reason, but it is important to note
    that in some languages that are more lazily evaluated, such an
    expression would still work since it would only look at the length
    of `b` and `c` and not worry about what the elements were.  In that
    case, it would return `7`.

    ```hoon
    > (lent (weld b c))
    ```

    We see here the correct way to find the sum of the length of two
    lists of unknown type.

    ```hoon
    > (add (lent b) (lent c))
    7
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
title = "7. Libraries"
weight = 17
nodes = [145, 153, 175]
objectives = ["Import a library using `/+` faslus.", "Create a new library in `/lib`.", "Identify the role of a desk in the Clay filesystem.", "Identify the components of a beak.", "Identify filesystem locations (including desks).", "Identify the components of a path.", "Build code samples with `-build-file` thread.", "Discuss Ford import runes."]
+++

_Libraries allow you to import and share processing code.  This module
will discuss how libraries can be produced, imported, and used._

##  Importing a Library

If you have only built {% tooltip label="generators"
href="/glossary/generator" /%}, you will soon or later become frustrated
with the apparent requirement that you manually reproduce helper cores
and arms every time you need them in a different generator. Libraries
are {% tooltip label="cores" href="/glossary/core" /%} stored in `/lib`
which provide access to {% tooltip label="arms" href="/glossary/arm" /%}
and legs (operations and data).  While the Hoon standard library is
directly available in the regular {% tooltip label="subject"
href="/glossary/subject" /%}, many other elements of functionality have
been introduced by software authors.

### Building Code Generally

A generator gives us on-demand access to code, but it is helpful to load
and use code from files while we work in the {% tooltip label="Dojo"
href="/glossary/dojo" /%}.

A conventional library import with `/+` {% tooltip label="faslus"
href="/language/hoon/reference/rune/fas#-faslus" /%} will work in a
generator or another file, but won't work in Dojo, so you can't use `/+`
faslus interactively.  The first line of many generators will include an
import line like this:

```hoon {% copy=true %}
/+  number-to-words
```

Subsequent invocations of the {% tooltip label="core"
href="/glossary/core" /%} require you to refer to it by name:

**/gen/n2w.hoon**

```hoon {% copy=true %}
/+  number-to-words
|=  n=@ud
(to-words:eng-us:numbers:number-to-words n)
```

Since `/` fas runes don't work in the Dojo, you need to instead use the
{% tooltip label="-build-file" href="/manual/os/dojo-tools#-build-file" /%} thread
to load the code. Most commonly, you will do this with
library code when you need a particular {% tooltip label="gate's"
href="/glossary/gate" /%} functionality for interactive coding.

`-build-file` accepts a file path and returns the built operational
code.  For instance:

```hoon
> =ntw -build-file %/lib/number-to-words/hoon

> one-hundred:numbers:ntw  
100

> (to-words:eng-us:numbers:ntw 19)
[~ "nineteen"]
```

There are also a number of other import {% tooltip label="runes"
href="/glossary/rune" /%} which make library, structure, and mark code
available to you.  For now, the only one you need to worry about is
`/+` {% tooltip label="faslus"
href="/language/hoon/reference/rune/fas#-faslus" /%}.

For simplicity, everything we do will take place on the `%base` {%
tooltip label="desk" href="/glossary/desk" /%} for now.  We will learn
how to create a library in a subsequent lesson.

### Exercise: Loading a Library

In a {% tooltip label="generator" href="/glossary/generator" /%}, load
the `number-to-words` library using the `/+` {% tooltip label="tislus"
href="/language/hoon/reference/rune/tis#-tislus" /%} rune.  (This must
take place at the very top of your file.)

Use this to produce a {% tooltip label="gate" href="/glossary/gate" /%}
which accepts an unsigned decimal integer and returns the text
interpretation of its increment.

## Helper Cores

Another common design pattern besides creating a library is to sequester
core-specific behavior in a helper {% tooltip label="core"
href="/glossary/core" /%}, which sits next to the interface operations.
Two runes are used to compose expressions together so that the subject
has everything it needs to carry out the desired calculations.

- `=>` {% tooltip label="tisgar"
  href="/language/hoon/reference/rune/tis#-tisgar" /%} composes two
  expressions so that the first is included in the second's {% tooltip
  label="subject" href="/glossary/subject" /%} (and thus can see it).
- `=<` {% tooltip label="tisgal"
  href="/language/hoon/reference/rune/tis#-tisgal" /%} inverts the order
  of composition, allowing heavier helper cores to be composed after the
  core's logic but still be available for use.

Watch for these being used in generators and libraries over the next few
modules.

### Exercise:  A Playing Card Library

In this exercise, we examine a library that can be used to represent a
deck of 52 playing cards.  The {% tooltip label="core"
href="/glossary/core" /%} below builds such a library, and can be
accessed by programs.  You should recognize most of the things this
program does aside from the `++shuffle-deck` arm which uses a
[door](/courses/hoon-school/K-doors) to produce
[randomness](/courses/hoon-school/O-subject).  This is fairly idiomatic
Hoon and it relies a lot on the convention that heavier code should be
lower in the expression.  This means that instead of `?:` {% tooltip
label="wutcol" href="/language/hoon/reference/rune/wut#-wutcol" /%} you
may see `?.` {% tooltip label="wutdot"
href="/language/hoon/reference/rune/wut#-wutdot" /%}, which inverts the
order of the true/false {% tooltip label="arms" href="/glossary/arm"
/%}, as well as other new constructions.

```hoon {% copy=true mode="collapse" %}
|%
+$  suit  ?(%hearts %spades %clubs %diamonds)
+$  darc  [sut=suit val=@ud]  :: see below about naming
+$  deck  (list darc)
++  make-deck
  ^-  deck
  =/  mydeck  *deck
  =/  i  1
  |-
  ?:  (gth i 4)
    mydeck
  =/  j  2
  |-
  ?.  (lte j 13)
    ^$(i +(i))
  %=  $
    j       +(j)
    mydeck  [[(num-to-suit i) j] mydeck]
  ==
++  num-to-suit
  |=  val=@ud
  ^-  suit
  ?+  val  !!
    %1  %hearts
    %2  %spades
    %3  %clubs
    %4  %diamonds
  ==
++  shuffle-deck
  |=  [unshuffled=deck entropy=@]
  ^-  deck
  =/  shuffled  *deck
  =/  random  ~(. og entropy)
  =/  remaining  (lent unshuffled)
  |-
  ?:  =(remaining 1)
    :_  shuffled
    (snag 0 unshuffled)
  =^  index  random  (rads:random remaining)
  %=  $
    shuffled      [(snag index unshuffled) shuffled]
    remaining     (dec remaining)
    unshuffled    (oust [index 1] unshuffled)
  ==
++  draw
  |=  [n=@ud d=deck]
  ^-  [hand=deck rest=deck]
  :-  (scag n d)
  (slag n d)
--
```

The `|%` {% tooltip label="barcen"
href="/language/hoon/reference/rune/bar#-barcen" /%} core created at the
top of the file contains the entire library's code, and is closed by
`--` {% tooltip label="hephep"
href="/language/hoon/reference/rune/terminators#---hephep" /%} on the
last line.

To create three types we're going to need, we use `+$` {% tooltip
label="lusbuc" href="/language/hoon/reference/rune/lus#-lusbuc" /%},
which is an {% tooltip label="arm" href="/glossary/arm" /%} used to
define a type.

- `+$  suit  ?(%hearts %spades %clubs %diamonds)` defines `+$suit`,
  which can be either `%hearts`, `%spades`, `%clubs`, or `%diamonds`.
  It's a type union created by the irregular form of `$?` {% tooltip
  label="bucwut" href="/language/hoon/reference/rune/buc#-bucwut" /%}.

- `+$  darc  [sut=suit val=@ud]` defines `+$darc`, which is a pair of
  `suit` and a `@ud`. By pairing a suit and a number, it represents a
  particular playing card, such as “nine of hearts”.  Why do we call it
  `darc` and not `card`?  Because `card` already has a meaning in {%
  tooltip label="Gall" href="/glossary/gall" /%}, the {% tooltip
  label="Arvo" href="/glossary/arvo" /%} app module, where one would
  likely to use this (or any) library.  It's worthwhile to avoid any
  confusion over names.

- `+$  deck  (list darc)` is simply a {% tooltip label="list"
  href="/glossary/list" /%} of `darc`.

One way to get a feel for how a library works is to skim the `++` {%
tooltip label="luslus" href="/language/hoon/reference/rune/lus#-luslus"
/%} arm-names before diving into any specific {% tooltip label="arm"
href="/glossary/arm" /%}.  In this library, the arms are `++make-deck`,
`++num-to-suit`, `++shuffle-deck`, and `++draw`. These names should be
very clear, with the exception of `++num-to-suit` (although you could
hazard a guess at what it does).  Let's take a closer look at it first:

```hoon {% copy=true %}
++  num-to-suit
  |=  val=@ud
  ^-  suit
  ?+  val  !!
    %1  %hearts
    %2  %spades
    %3  %clubs
    %4  %diamonds
  ==
```

`++num-to-suit` defines a gate which takes a single `@ud` unsigned
decimal integer and produces a `suit`.  The `?+` {% tooltip
label="wutlus" href="/language/hoon/reference/rune/wut#-wutlus" /%} rune
creates a structure to switch against a value with a default in case
there are no matches.  (Here the default is to crash with `!!` {%
tooltip label="zapzap" href="/language/hoon/reference/rune/zap#-zapzap"
/%}.)  We then have options 1–4 which each resulting in a different
suit.

```hoon {% copy=true %}
++  make-deck
  ^-  deck
  =/  mydeck  *deck
  =/  i  1
  |-
  ?:  (gth i 4)
    mydeck
  =/  j  2
  |-
  ?.  (lte j 14)
    ^$(i +(i))
  %=  $
    j       +(j)
    mydeck  [[(num-to-suit i) j] mydeck]
  ==
```

`++make-deck` assembles a deck of 52 cards by cycling through every
possible suit and number and combining them.  It uses `++num-to-suit`
and a couple of loops to go through the counters.  It has an interesting
`^$` loop skip where when `j` is greater than 14 it jumps instead to the
outer loop, incrementing `i`.

`?.` {% tooltip label="wutdot"
href="/language/hoon/reference/rune/wut#-wutdot" /%} may be an
unfamiliar rune; it is simply the inverted version of `?:` {% tooltip
label="wutcol" href="/language/hoon/reference/rune/wut#-wutcol" /%}, so
the first branch is actually the if-false branch and the second is the
if-true branch.  This is done to keep the “heaviest” branch at the
bottom, which makes for more idiomatic and readable Hoon code.

```hoon {% copy=true %}
++  draw
  |=  [n=@ud d=deck]
  ^-  [hand=deck rest=deck]
  :-  (scag n d)
  (slag n d)
```

`++draw` takes two arguments:  `n`, an unsigned integer, and `d`, a
`deck`.  The gate will produce a cell of two `decks` using {% tooltip
label="++scag" href="/language/hoon/reference/stdlib/2b#scag" /%} and {%
tooltip label="++slag" href="/language/hoon/reference/stdlib/2b#slag"
/%}. {% tooltip label="++scag"
href="/language/hoon/reference/stdlib/2b#scag" /%} is a standard library
{% tooltip label="gate" href="/glossary/gate" /%} produces the first `n`
elements from a {% tooltip label="list" href="/glossary/list" /%},
while {% tooltip label="++slag" href="/language/hoon/reference/stdlib/2b#slag"
/%} is a standard library gate that produces the remaining elements of a
list starting after the `n`th element.  So we use `++scag` to produce
the drawn hand of `n` cards in the head of the cell as `hand`, and
`++slag` to produce the remaining deck in the tail of the cell as
`rest`.

```hoon {% copy=true %}
++  shuffle-deck
  |=  [unshuffled=deck entropy=@]
  ^-  deck
  =/  shuffled  *deck
  =/  random  ~(. og entropy)
  =/  remaining  (lent unshuffled)
  |-
  ?:  =(remaining 1)
    :_  shuffled
    (snag 0 unshuffled)
  =^  index  random  (rads:random remaining)
  %=  $
    shuffled      [(snag index unshuffled) shuffled]
    remaining     (dec remaining)
    unshuffled    (oust [index 1] unshuffled)
  ==
```

Finally we come to `++shuffle-deck`.  This gate takes two arguments:  a
`deck`, and a `@` as a bit of `entropy` to seed the {% tooltip
label="og" href="/language/hoon/reference/stdlib/3d#og" /%}
random-number {% tooltip label="core" href="/glossary/core" /%}.  It
will produce a `deck`.

We add a bunted `deck`, then encounter a very interesting statement that
you haven't run into yet.  This is the irregular form of `%~` {% tooltip
label="censig" href="/language/hoon/reference/rune/cen#-censig" /%},
which “evaluates an arm in a door.”  For our purposes now, you can see
it as a way of creating a random-value arm that we'll use later on with
`++rads:random`.

With `=/  remaining  (lent unshuffled)`, we get the length of the
unshuffled deck with {% tooltip label="++lent"
href="/language/hoon/reference/stdlib/2b#lent" /%}.

`?:  =(remaining 1)` checks if we have only one card remaining. If
that's true, we produce a {% tooltip label="cell" href="/glossary/cell"
/%} of `shuffled` and the one card left in `unshuffled`. We use the
`:_` {% tooltip label="colcab"
href="/language/hoon/reference/rune/col#_-colcab" /%} rune here, so that
the “heavier” expression is at the bottom.

If the above conditional evaluates to `%.n` false, we need to do a
little work. `=^` {% tooltip label="tisket"
href="/language/hoon/reference/rune/tis#-tisket" /%} is a rune that pins
the head of a pair and changes a leg in the {% tooltip label="subject"
href="/glossary/subject" /%} with the tail.  It's useful for interacting
with the {% tooltip label="og"
href="/language/hoon/reference/stdlib/3d#og" /%} core arms, as many of
them produce a pair of a random numbers and the next state of the core.
We're going to put the random number in the {% tooltip label="subject"
href="/glossary/subject" /%} with the {% tooltip label="face"
href="/glossary/face" /%} `index` and change `random` to be the next
core.

With that completed, we use `%=` {% tooltip label="centis"
href="/language/hoon/reference/rune/cen#-centis" /%} to call `$` buc to
recurse back up to `|-` {% tooltip label="barhep"
href="/language/hoon/reference/rune/bar#--barhep" /%} with a few
changes:

- `shuffled` gets the `darc` from `unshuffled` at `index` added to the
  front of it.

- `remaining` gets decremented. Why are we using a counter here instead
  of just checking the length of `unshuffled` on each loop? {% tooltip
  label="++lent" href="/language/hoon/reference/stdlib/2b#lent" /%}
  traverses the entire list every time it's called so maintaining a
  counter in this fashion is much faster.

- `unshuffled` becomes the result of using {% tooltip label="++oust"
  href="/language/hoon/reference/stdlib/2b#oust" /%} to remove 1 `darc` at
  `index` on `unshuffled`.

This is a very naive shuffling algorithm.  We leave the implementation
of a better shuffling algorithm as an exercise for the reader.


### Exercise:  Using the Playing Card Library

Unfortunately `/` {% tooltip label="fas"
href="/language/hoon/reference/rune/fas" /%} runes don't work in the {%
tooltip label="Dojo" href="/glossary/dojo" /%} right now, so we need to
build code using the {% tooltip label="-build-file"
href="/manual/os/dojo-tools#-build-file" /%} thread if we want to use
the library directly.

- Import the `/lib/playing-cards.hoon` library and use it to shuffle and
  show a deck and a random hand of five cards.

    We first import the library:

    ```hoon {% copy=true %}
    =playing-cards -build-file /===/lib/playing-cards/hoon
    ```

    We then invoke it using the _entropy_ or system randomness.  (This
    is an unpredictable value we will use when we want a process to be
    random.  We will discuss it in detail when we talk about
    [subject-oriented programming](/courses/hoon-school/O-subject).)

    ```hoon
    > =deck (shuffle-deck:playing-cards make-deck:playing-cards eny)

    > deck
    ~[
      [sut=%spades val=12]
      [sut=%spades val=8]
      [sut=%hearts val=5]
      [sut=%clubs val=2]
      [sut=%diamonds val=10]
      ...
      [sut=%spades val=2]
      [sut=%hearts val=6]
      [sut=%hearts val=12]
    ]
    ```

    Draw a hand of five cards from the deck:

    ```hoon
    > (draw:playing-cards 5 deck)
    [   hand
      ~[
        [sut=%spades val=12]
        [sut=%spades val=8]
        [sut=%hearts val=5]
        [sut=%clubs val=2]
        [sut=%diamonds val=10]
      ]
        rest
      ~[
        [sut=%hearts val=2]
        [sut=%clubs val=7]
        [sut=%clubs val=9]
        [sut=%diamonds val=6]
        [sut=%diamonds val=8]
        ...
        [sut=%spades val=2]
        [sut=%hearts val=6]
        [sut=%hearts val=12]
      ]
    ]
    ```

    Of course, since the deck was shuffled once, any time we draw from
    the same deck we will get the same hand.  But if we replace the deck
    with the `rest` remaining, then we can continue to draw new hands.


##  Desks

A {% tooltip label="desk" href="/glossary/desk" /%} organizes a
collection of files, including {% tooltip label="generators"
href="/glossary/generator" /%}, libraries, {% tooltip label="agents"
href="/glossary/agent" /%}, and system code, into one coherent bundle. A
desk is similar to a file drive in a conventional computer, or a Git
branch.  Desks are supported by the {% tooltip label="Clay"
href="/glossary/clay" /%} {% tooltip label="vane" href="/glossary/vane"
/%} in {% tooltip label="Arvo" href="/glossary/arvo" /%}, the Urbit OS.

At this point, you've likely only worked on the `%base` desk.  You can
see data about any particular desk using the {% tooltip label="+vats"
href="/manual/os/dojo-tools#vats" /%} generator:

```hoon
> +vats %base
%base
  /sys/kelvin:           [%zuse 413]
  base hash ends in:     hih5c
  %cz hash ends in:      hih5c
  app status:            running
  pending updates:       ~

> +vats %base, =verb %.y
%base
  /sys/kelvin:      [%zuse 413]
  base hash:        0v2.vhcjk.rj42q.e3la7.1679q.u2qs2.35vnn.9n1jm.mj66h.kgpe5.hih5c
  %cz hash:         0v2.vhcjk.rj42q.e3la7.1679q.u2qs2.35vnn.9n1jm.mj66h.kgpe5.hih5c
  app status:       running
  force on:         ~
  force off:        ~
  publishing ship:  ~
  updates:          remote
  source ship:      ~marnec-dozzod-marzod
  source desk:      %kids
  source aeon:      43
  kids desk:        %kids
  pending updates:  ~
```

You'll see a slightly different configuration on the particular {%
tooltip label="ship" href="/glossary/ship" /%} you are running.

### Aside:  Filesystems

A filesystem is responsible for providing access to blobs of data
somewhere on a disk drive.  If you have worked with Windows or macOS,
you have become accustomed to using a file browser to view and interact
with files.  Mobile devices tend to obscure the nature of files more, in
favor of just providing an end-user interface for working with or
viewing the data.  To use files effectively, you need to know a few
things:

1. How to identify the data.
2. How to locate the data.
3. How to read or interpret the data.

Files are identified by a _file name_, which is typically a short
descriptor like `Waterfall Visit 5.jpg` (if produced by a human) or
`DSC_54694.jpg` (if produced by a machine).

Files are located using the _path_ or _file path_.  Colloquially, this
is what we mean when we ask which folder or directory a file is located
in.  It's an address that users and programs can use to uniquely locate
a particular file, even if that file has the same name as another file.

An Earth filesystem and path orients itself around some key metaphor:

- Windows machines organize the world by drive, e.g. `C:\`.
- Unix machines (including macOS and Linux) organize the world from `/`,
  the root directory.

**Absolute paths** are like street addresses, or latitude and longitude.
They let you unambiguously locate a file or folder.  **Relative paths**
are more like informal (but correct) instructions:  “It's on the right
just three houses past the church.”  They are often shorter but require
the user to know the starting point.

Once you have located a particular file, you need to load the data.
Conventionally, _file extensions_ indicate what kind of file you are
dealing with:  `.jpg`, `.png`, and `.gif` are image files, for instance;
`.txt`, `.docx`, and `.pdf` are different kinds of documents; and `.mp3`
and `.ogg` are audio files.  Simply changing the extension on the file
doesn't change the underlying data, but it can either elicit a stern
warning from the OS or confuse it, depending on the OS.  Normally you
have to open the file in an appropriate program and save it as a new
type if such a conversion is possible.

### File Data in Urbit

On Mars, we treat a filesystem as a way of organizing arbitrary access
to blocks of persistent data.  There are some concessions to Earth-style
filesystems, but {% tooltip label="Clay" href="/glossary/clay" /%}
(Urbit's filesystem) organizes everything with respect to a {% tooltip
label="desk" href="/glossary/desk" /%}, a discrete collection of static
data on a particular {% tooltip label="ship" href="/glossary/ship" /%}.
Of course, like everything else in Hoon, a desk is a tree as well.

So far everything we have done has taken place on the `%base` desk.  You
have by this point become proficient at synchronizing Earthling data
(Unix data) and Martian data (Urbit data), using {% tooltip
label="|mount" href="/manual/os/dojo-tools#mount" /%} and {% tooltip
label="|commit" href="/manual/os/dojo-tools#commit" /%}, and every time
you've done this with `%base` that has been recorded in the update
report the {% tooltip label="Dojo" href="/glossary/dojo" /%} makes to
you.

```hoon
> |commit %base
>=
+ /~zod/base/2/gen/demo/hoon
```

This message says that a file `demo.hoon` was added to the Urbit
filesystem at the path in `/gen`.  What is the rest of it, though, the
first three components?  We call this the {% tooltip label="beak"
href="/system/kernel/clay/reference/data-types#beak" /%}.  The beak lets
Clay globally identify any resource on any ship at any point in time.  A
beak has three components:

1. The **ship**, here `~zod`.  (You can find this out on any ship using
   `our`.)
2. The **desk**, here `%base`.
3. A **revision number** or **timestamp**, here `2`.  (The current
   system time is available as `now`.)  Clay tracks the history of each
   file, so older versions can be accessed by their revision number.
   (This is uncommon to need to do today.)

The beak is commonly constructed with the `/` fas prefix and `=` tis
signs for the three components:

```hoon
> /===
[~.~zod ~.base ~.~2022.6.14..18.13.35..ccaf ~]
```

Any one of those can be replaced as necessary:

```hoon
> /=sandbox=
[~.~zod %sandbox ~.~2022.6.14..18.14.49..a3da ~]
```

You'll also sometimes see `%` cen stand in for the whole including the
“current” desk.  The current desk is a Dojo concept, since for {%
tooltip label="Clay" href="/glossary/clay" /%} we can access any desk at
any time (with permission).

```hoon
> %
[~.~zod ~.base ~.~2022.6.14..18.15.10..698c ~]
```

### Paths and Files

A `path` is a `(list @ta)`, a list of text identifiers.  The first three
are always the beak and the last one conventionally refers to the mark
by which the file is represented.

For instance, the {% tooltip label="+cat"
href="/manual/os/dojo-tools#cat" /%} generator displays the contents of
any path, e.g.

```hoon
> +cat /===/gen/ls/hoon
/~zod/base/~2022.6.14..18.16.53..2102/gen/ls/hoon
::  LiSt directory subnodes
::
::::  /hoon/ls/gen
  ::
/?    310
/+    show-dir
::
::::
  ::
~&  %
:-  %say
|=  [^ [arg=path ~] vane=?(%g %c)]
=+  lon=.^(arch (cat 3 vane %y) arg)
tang+[?~(dir.lon leaf+"~" (show-dir vane arg dir.lon))]~
```

If no data are located at the given path, `+cat` simply shows `~` null:

```hoon
> +cat /=landscape=/gen/ls/hoon
~ /~zod/landscape/~2022.6.14..18.17.16..07ff/gen/ls/hoon
```

Every desk has a standard directory structure:

-   `/app` for {% tooltip label="agents" href="/glossary/agent" /%}
-   `/gen` for {% tooltip label="generators" href="/glossary/generator" /%}
-   `/lib` for library and helper files
-   `/mar` for {% tooltip label="marks" href="/glossary/mark" /%}
-   `/sur` for shared structures
-   `/ted` for {% tooltip label="threads" href="/glossary/thread" /%}

To run a generator from a different desk in Dojo, you need to prefix the
desk name to the generator; to run `/=landscape=/gen/tally/hoon`, you
would say:

```hoon
> +landscape!tally

tallied your activity score! find the results below.
to show non-anonymized resource identifiers, +tally |
counted from groups and channels that you are hosting.
groups are listed with their member count.
channels are listed with activity from the past week:
  - amount of top-level content
  - amount of unique authors

the date is ~2022.6.14..18.19.30..8c94
you are in 0 group(s):

you are hosting 0 group(s):
```

### Marks

{% tooltip label="Marks" href="/glossary/mark" /%} play the role of file
extensions, with an important upgrade:  they are actually {% tooltip
label="molds" href="/glossary/mold" /%} and define conversion paths.  We
won't write them in Hoon School, but you will encounter them when you
begin writing apps. They are used more broadly than merely as file
types, because they act as smart molds to ingest and yield data
structures such as JSON and HTML from Hoon data structures.

In brief, each mark has a `++grab` arm to convert from other types to
it; a `++grow` arm to convert it to other types; and a `++grad` arm for
some standard operations across marks.  You can explore the marks in
`/mar`.


##  Other Ford Runes

The `++ford` arm of Clay builds Hoon code.  It provides [a number of
runes](/language/hoon/reference/rune/fas) which allow fine-grained
control over building and importing files.  These must be in the
specific order at the top of any file.  (They also don't work in Dojo;
see {% tooltip label="-build-file"
href="/manual/os/dojo-tools#-build-file" /%} for a workaround.)  The
runes include:

- `/-` {% tooltip label="fashep"
  href="/language/hoon/reference/rune/fas#--fashep" /%} imports a
  structure file from `/sur`.  Structure files are a way to share common
  data structures (across agents, for instance).
- `/+` {% tooltip label="faslus"
  href="/language/hoon/reference/rune/fas#-faslus" /%} imports a library
  file from `/lib`.

    Both `/-` fashep and `/+` faslus allow you to import by affecting
    the name of the exposed core:
    
    1.  With the default name:

        ```hoon {% copy=true %}
        /+  apple
        ```

    2.  With no name:

        ```hoon {% copy=true %}
        /-  *orange
        ```

    3.  With a new name:

        ```hoon {% copy=true %}
        /+  pomme=apple
        ```

    `*` is useful when importing libraries with unwieldy names, but
    otherwise should be avoided as it can shadow names in your current
    subject.

- `/=` {% tooltip label="fastis"
  href="/language/hoon/reference/rune/fas#-fastis" /%} builds a
  user-specified path and wraps it with a given {% tooltip label="face"
  href="/glossary/face" /%}.
- `/*` {% tooltip label="fastar"
  href="/language/hoon/reference/rune/fas#-fastar" /%} imports the
  contents of a file, applies a {% tooltip label="mark"
  href="/glossary/mark" /%} to convert it, and wraps it with a given
  face.


# I-testing.md

---

+++
title = "8. Testing Code"
weight = 18
nodes = [170, 190]
objectives = ["Run existing unit tests.", "Produce a unit test.", "Employ a debugging strategy to identify and correct errors in Hoon code."]
+++

_This module will discuss how we can have confidence that a program does
what it claims to do, using unit testing and debugging strategies.  It
may be considered optional and skipped if you are speedrunning Hoon
School._

> Code courageously.
>
> If you avoid changing a section of code for fear of awakening the
> demons therein, you are living in fear. If you stay in the comfortable
> confines of the small section of the code you wrote or know well, you
> will never write legendary code. All code was written by humans and can
> be mastered by humans.
>
> It's natural to feel fear of code; however, you must act as though you
> are able to master and change any part of it. To code courageously is to
> walk into any abyss, bring light, and make it right.
>
> ~wicdev-wisryt

When you produce software, how much confidence do you have that it does
what you think it does?  Bugs in code are common, but judicious testing
can manifest failures so that the bugs can be identified and corrected.
We can classify a testing regimen for Urbit code into a couple of
layers:  fences and unit tests.

### Fences

_Fences_ are barriers employed to block program execution if the state
isn’t adequate to the intended task. Typically, these are implemented
with `assert` or similar enforcement.  In Hoon, this means `?>` {%
tooltip label="wutgar" href="/language/hoon/reference/rune/wut#-wutgar"
/%}, `?<` {% tooltip label="wutgal"
href="/language/hoon/reference/rune/wut#-wutgal" /%}, and `?~` {%
tooltip label="wutsig" href="/language/hoon/reference/rune/wut#-wutsig"
/%}, or judicious use of `^-` {% tooltip label="kethep"
href="/language/hoon/reference/rune/ket#--kethep" /%} and `^+` {%
tooltip label="ketlus" href="/language/hoon/reference/rune/ket#-ketlus"
/%}. For conditions that must succeed, the failure branch in Hoon should
be `!!`, which crashes the program.

### Unit Tests

> Unit tests are so called because they exercise the functionality of
> the code by interrogating individual functions and methods. Functions
> and methods can often be considered the atomic units of software because
> they are indivisible. However, what is considered to be the smallest
> code unit is subjective. The body of a function can be long are short,
> and shorter functions are arguably more unit-like than long ones.
>
> (Katy Huff, [“Python Testing and Continuous Integration”](https://mq-software-carpentry.github.io/python-testing/05-units/))
    
In many languages, unit tests refer to functions, often prefixed `test`,
that specify (and enforce) the expected behavior of a given function.
Unit tests typically contain setup, assertions, and tear-down. In
academic terms, they’re a grading script.

In Hoon, the `tests/` directory contains the relevant tests for the
testing framework to grab and utilize.  These can be invoked with the {%
tooltip label="-test" href="/manual/os/dojo-tools#-test" /%} {% tooltip
label="thread" href="/glossary/thread" /%}:

```hoon
> -test /=landscape=/tests ~  
built   /tests/lib/pull-hook-virt/hoon  
built   /tests/lib/versioning/hoon  
>   test-supported: took 1047µs  
OK      /lib/versioning/test-supported  
>   test-read-version: took 28317µs  
OK      /lib/versioning/test-read-version  
>   test-is-root: took 28786µs  
OK      /lib/versioning/test-is-root  
>   test-current-version: took 507µs  
OK      /lib/versioning/test-current-version  
>   test-append-version: took 4804µs  
OK      /lib/versioning/test-append-version  
>   test-mule-scry-bad-time: took 8437µs  
OK      /lib/pull-hook-virt/test-mule-scry-bad-time  
>   test-mule-scry-bad-ship: took 8279µs  
OK      /lib/pull-hook-virt/test-mule-scry-bad-ship  
>   test-kick-mule: took 4614µs  
OK      /lib/pull-hook-virt/test-kick-mule  
ok=%.y    
```

(Depending on when you built your fakeship, particular tests may or may
not be present.  You can download them from [the Urbit
repo](https://github.com/urbit/urbit) and add them manually if you like.
Regarding the example above (`%landscape` {% tooltip label="desk"
href="/glossary/desk" /%}), the tests are likely missing, so download
them from
[here](https://github.com/urbit/urbit/tree/master/pkg/landscape) if you
want to run them.)

Hoon unit tests come in two categories:

1.   `++expect-eq` (equality of two values)
2.   `++expect-fail` (failure/crash)

Let's look at a practical example first, then dissect these.

### Exercise:  Testing a Library

Consider an absolute value arm `++absolute` for `@rs` values. The unit
tests for `++absolute` should accomplish a few things:

-   Verify correct behavior for positive numeric input.
-   Verify correct behavior for negative numeric input.
-   For the purpose of demonstrating `++expect-fail`, verify an
    exception is raised on input of zero. (Properly speaking Hoon
    doesn't have exceptions because Nock is crash-only; tools like
    `unit` are a way of dealing with failed computations.)

(You may also think we would need to verify `++absolute` calls only
succeed if the input is an `@rs`, but arvo already handles this for us,
as a hoon file will not build if a gate call contains an argument that
does not match the sample type. So even if you wanted to add an
`++expect-fail` test for it, your test file would not build.)

By convention any testing suite has the import line `/+  *test` at the
top.

**/tests/lib/absolute.hoon**

```hoon {% copy=true mode="collapse" %}
/+  *test, *absolute
|%
++  test-absolute
  ;:  weld
  %+  expect-eq
    !>  .1
    !>  (absolute .-1)
  %+  expect-eq
    !>  .1
    !>  (absolute .1)
  %-  expect-fail
    |.  (absolute .0)
  ==
--
```

Note that at this point we don’t care what the function looks like, only
how it behaves.

**/lib/absolute.hoon**

```hoon {% copy=true %}
|%
++  absolute
  |=  a=@rs
  ?:  (gth a .0)  a
  (sub:rs .0 a)
--
```

- Use the tests to determine what is wrong with this library code and
  correct it.

The dcSpark blog post [“Writing Robust Hoon — A Guide To Urbit Unit
Testing”](https://medium.com/dcspark/writing-robust-hoon-a-guide-to-urbit-unit-testing-82b2631fe20a)
covers some more good ideas about testing Hoon code.

### `/lib/test.hoon`

In `/lib/test.hoon` we find a core with a few gates:  `++expect`,
`++expect-eq`, and `++expect-fail`, among others.

`++expect-eq` checks whether two vases are equal and pretty-prints the
result of that test.  It is our workhorse.  The source for `++expect-eq`
is:

```hoon {% copy=true mode="collapse" %}
++  expect-eq
  |=  [expected=vase actual=vase]
  ^-  tang
  ::
  =|  result=tang
  ::
  =?  result  !=(q.expected q.actual)
    %+  weld  result
    ^-  tang
    :~  [%palm [": " ~ ~ ~] [leaf+"expected" (sell expected) ~]]
        [%palm [": " ~ ~ ~] [leaf+"actual  " (sell actual) ~]]
    ==
  ::
  =?  result  !(~(nest ut p.actual) | p.expected)
    %+  weld  result
    ^-  tang
    :~  :+  %palm  [": " ~ ~ ~]
        :~  [%leaf "failed to nest"]
            (~(dunk ut p.actual) %actual)
            (~(dunk ut p.expected) %expected)
    ==  ==
  result
```

Test code deals in {% tooltip label="vases" href="/glossary/vase" /%},
which are produced by `!>` {% tooltip label="zapgar"
href="/language/hoon/reference/rune/zap#-zapgar" /%} as a {% tooltip
label="cell" href="/glossary/cell" /%} of the type of a value and the
value.

`++expect-fail` by contrast take a `|.` {% tooltip label="bardot"
href="/language/hoon/reference/rune/bar#-bardot" /%} trap (a trap that
has the `$` buc {% tooltip label="arm" href="/glossary/arm" /%} but
hasn't been called yet) and verifies that the code within fails.

```hoon
> (expect-fail:test |.(!!))
~

> (expect-fail:test |.((sub 0 1)))
~

> (expect-fail:test |.((sub 1 1)))
~[[%leaf p="expected failure - succeeded"]]
```

(Recall that `~` null is `%.y` true.)


##  Producing Error Messages

Formal error messages in Urbit are built of tanks.

- A `tank` is a structure for printing data.
  - `leaf` is for printing a single noun.
  - `palm` is for printing backstep-indented lists.
  - `rose` is for printing rows of data.
- A `tang` is a `(list tank)`.

As your code evaluates, the Arvo runtime maintains a _stack trace_, or
list of the evaluations and expressions that got the program to its
notional point of computation.  When the code fails, any error hints
currently on the stack are dumped to the terminal for you to see what
has gone wrong.

- The `~_` {% tooltip label="sigcab"
  href="/language/hoon/reference/rune/sig#_-sigcab" /%} rune, described
  as a “user-formatted tracing printf”, can include an error message for
  you, requiring you to explicitly build the `tank`. (`printf` is a
  reference to [C's I/O
  library](https://en.wikipedia.org/wiki/Printf_format_string).)
- The `~|` {% tooltip label="sigbar"
  href="/language/hoon/reference/rune/sig#-sigbar" /%} rune, a “tracing
  printf”, can include an error message from a simple `@t` {% tooltip
  label="cord" href="/glossary/cord" /%}.
    What this means is that these print to the stack trace if something
    fails, so you can use either rune to contribute to the error
    description:

    ```hoon {% copy=true %}
    |=  a=@ud
    ~_  leaf+"This code failed"
    !!
    ```
- The `!:` {% tooltip label="zapcol"
  href="/language/hoon/reference/rune/zap#-zapcol" /%} rune turns on
  line-by-line stack tracing, which is extremely helpful when debugging
  programs.  Drop it in on the first Hoon line (after `/` {% tooltip
  label="fas" href="/language/hoon/reference/rune/fas" /%} imports) of a
  {% tooltip label="generator" href="/glossary/generator" /%} or library
  while developing.

    ```hoon
    > (sub 0 1)
    subtract-underflow
    dojo: hoon expression failed

    > !:((sub 0 1))
    /~zod/base/~2022.6.14..20.47.19..3b7a:<[1 4].[1 13]>
    subtract-underflow
    dojo: hoon expression failed
    ```

When you compose your own library {% tooltip label="cores"
href="/glossary/core" /%}, include error messages for likely failure
modes.


##  Test-Driven Development

_In extremis_, rigorous unit testing yields test-driven development
(TDD). Test-driven development refers to the practice of fully
specifying desired function behavior before composing the function
itself. The advantage of this approach is that it forces you to clarify
ahead of time what you expect, rather than making it up on the fly.

For instance, one could publish a set of tests which characterize the
behavior of a Roman numeral translation library sufficiently that when
such a library is provided it is immediately demonstrable.

**/tests/lib/roman.hoon**

```hoon {% copy=true mode="collapse" %}
/+  *test, *roman
|%
++  test-output-one
  =/  src  "i"
  =/  trg  1
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (from-roman src)
  %+  expect-eq
    !>  trg
    !>  (from-roman (cuss src))
  ==
++  test-output-two
  =/  src  "ii"
  =/  trg  2
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (from-roman src)
  %+  expect-eq
    !>  trg
    !>  (from-roman (cuss src))
  ==
:: and so forth
++  test-input-one
  =/  trg  "i"
  =/  src  1
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (to-roman src)
  ==
++  test-input-two
  =/  trg  "ii"
  =/  src  2
  ;:  weld
  %+  expect-eq
    !>  trg
    !>  (to-roman src)
  ==
:: and so forth
--
```

By composing the unit tests ahead of time, you exercise a discipline of
thinking carefully through details of the interface and implementation
before you write a single line of implementation code.


##  Debugging Common Errors

Let’s enumerate the errors you are likely to have encountered by this
point:

### `nest-fail`

A {% tooltip label="nest-fail"
href="/language/hoon/reference/hoon-errors#nest-fail" /%} may be the
most common.  Likely you are using an {% tooltip label="atom"
href="/glossary/atom" /%} or a {% tooltip label="cell"
href="/glossary/cell" /%} where the other is expected.

```hoon
> (add 'a' 'b')
195

> (add "a" "b")
-need.@
-have.[i=@tD t=""]
nest-fail
dojo: hoon expression failed
```

### `mint-nice`

`mint-nice` arises from typechecking errors:

```hoon
> ^-(tape ~[78 97 114 110 105 97])
mint-nice  
-need.?(%~ [i=@tD t=""])  
-have.[@ud @ud @ud @ud @ud @ud %~]  
nest-fail  
dojo: hoon expression failed
```

Conversion without casting via {% tooltip label="auras"
href="/glossary/aura" /%} fails because the atom types (auras) don't
nest without explicit downcasting to `@`.

```hoon
> `(list @ud)`~[0x0 0x1 0x2]
mint-nice
-need.?(%~ [i=@ud t=it(@ud)])
-have.[@ux @ux @ux %~]
nest-fail
dojo: hoon expression failed

> `(list @ud)``(list @)`~[0x0 0x1 0x2]
~[0 1 2]
```

### `fish-loop`

A `fish-loop` arises when using a recursive mold definition like {%
tooltip label="list" href="/glossary/list" /%}. (The relevant mnemonic
is that `++fish` goes fishing for the type of an expression.)  Alas,
this fails today:

```hoon
> ?=((list @) ~[1 2 3 4])
[%test ~[[%.y p=2]]]
fish-loop
```

### `generator-build-fail`

A `generator-build-fail` most commonly results from composing code with
mismatched {% tooltip label="runes" href="/glossary/rune" /%} (and thus
the wrong children including hanging expected-but-empty slots).

Also check if you are using Windows-style line endings, as Unix-style
line endings should be employed throughout Urbit.

### Misusing the `$` buc Arm

Another common mistake is to attempt to use the default `$` buc arm in
something that doesn't have it.  This typically happens for one of two
reasons:

- `$.+2` means that `%-` {% tooltip label="cenhep"
  href="/language/hoon/reference/rune/cen#-cenhep" /%} or equivalent
  function call cannot locate a {% tooltip label="battery"
  href="/glossary/battery" /%}.  This can occur when you try to use a
  non-gate as a {% tooltip label="gate" href="/glossary/gate" /%}.  In
  particular, if you mask the name of a {% tooltip label="mold"
  href="/glossary/mold" /%} (such as {% tooltip label="list"
  href="/glossary/list" /%}), then a subsequent expression that requires
  the mold will experience this problem.
    ```hoon
    > =/  list  ~[1 2 3]
     =/  a  ~[4 5 6]
     `(list @ud)`a
    -find.$.+2
    ```

- `-find.$` similarly looks for a `$` buc {% tooltip label="arm"
  href="/glossary/arm" /%} in something that _is_ a core but doesn't
  have the `$` buc arm present.

    ```hoon
    > *tape
    ""
    > (tape)
    ""
    > *(tape)
    -find.$
    ```

- [“Hoon Errors”](/language/hoon/reference/hoon-errors)

### Debugging Strategies

What are some strategies for debugging?

-   **Debugging stack.**  Use the `!:` {% tooltip label="zapcol"
    href="/language/hoon/reference/rune/zap#-zapcol" /%} rune to turn on
    the debugging stack, `!.` {% tooltip label="zapdot"
    href="/language/hoon/reference/rune/zap#-zapdot" /%} to turn it off
    again.  (Most of the time you just pop this on at the top of a
    generator and leave it there.)
-   **`printf` debugging.**  If your code will compile and run, employ
    `~&` {% tooltip label="sigpam"
    href="/language/hoon/reference/rune/sig#-sigpam" /%} frequently to
    make sure that your code is doing what you think it’s doing.
-   **Typecast.**  Include `^` {% tooltip label="ket"
    href="/language/hoon/reference/rune/ket" /%} casts frequently
    throughout your code.  Entire categories of error can be excluded by
    satisfying the Hoon typechecker.
-   **The only wolf in Alaska.**  Essentially a bisection search, you
    split your code into smaller modules and run each part until you
    know where the bug arose (where the wolf howled).  Then you keep
    fencing it in tighter and tighter until you know where it arose. You
    can stub out arms with `!!` {% tooltip label="zapzap"
    href="/language/hoon/reference/rune/zap#-zapzap" /%}.
-   **Build it again.**  Remove all of the complicated code from your
    program and add it in one line at a time.  For instance, replace a
    complicated function with either a `~&` sigpam and `!!` zapzap, or
    return a known static hard-coded value instead.  That way as you
    reintroduce lines of code or parts of expressions you can narrow
    down what went wrong and why.
-  **Run without networking**.  If you run the Urbit executable with
   `-L`, you cut off external networking.  This is helpful if you want
   to mess with a _copy_ of an actual ship without producing remote
   effects.  That is, if other parts of {% tooltip label="Ames"
   href="/glossary/ames" /%} don’t know what you’re doing, then you can
   delete that copy (COPY!) of your pier and continue with the original.
   This is an alternative to using fakezods which is occasionally
   helpful in debugging userspace apps in {% tooltip label="Gall"
   href="/glossary/gall" /%}. You can also develop using a {% tooltip
   label="moon" href="/glossary/moon" /%} if you want to.


# J-stdlib-text.md

---

+++
title = "9. Text Processing I"
weight = 19
nodes = [160, 163]
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

What is a written character? Essentially it is a representation of human
semantic content (not sound strictly). (Note that we don't refer to
_alphabets_, which prescribe a particular relationship of sound to
symbol:  there are ideographic and logographic scripts, syllabaries, and
other representations.  Thus, _characters_ not _letters_.)  Characters
can be combined—particularly in ideographic languages like Mandarin
Chinese.

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

    **Exercise:  `++snag` Yourself**

    - Without using `++snag`, write a gate that returns the `n`th item
      of a list.  There is a solution at the bottom of the page.

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

    **Exercise:  Count the Number of Characters in Text**

    - There is a built-in `++lent` function that counts the number of
      characters in a `tape`.  Build your own `tape`-length character
      counting function without using `++lent`.

    You may find the `?~` {% tooltip label="wutsig"
    href="/language/hoon/reference/rune/wut#-wutsig" /%} rune to be
    helpful.  It tells you whether a value is `~` or not.  (How would
    you do this with a regular `?:` {% tooltip label="wutcol"
    href="/language/hoon/reference/rune/wut#-wutcol" /%}?)

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

Hoon has a sophisticated parser built into it that [we'll use
later](/courses/hoon-school/P-stdlib-io).  There are a lot of rules to
deciding what is and isn't a rune, and how the various parts of an
expression relate to each other.  We don't need that level of power to
work with basic text operations, so we'll instead use basic `list` tools
whenever we need to extract or break text apart for now.

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

##  Exercise:  Building Your Own Library

Let's take some of the code we've built above for processing text and
turn them into a library we can use in another generator.

- Take the space-breaking code and the element-counting code gates from
  above and include them in a `|%` {% tooltip label="barcen"
  href="/language/hoon/reference/rune/bar#-barcen" /%} core.  Save this
  file as `lib/text.hoon` in the `%base` {% tooltip label="desk"
  href="/glossary/desk" /%} of your fakeship and commit.

- Produce a generator `gen/text-user.hoon` which accepts a {% tooltip
  label="tape" href="/glossary/tape" /%} and returns the number of words
  in the text (separated by spaces).  (How would you obtain this from
  those two operations?)


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


##  `%say` Generators

A naked {% tooltip label="generator" href="/glossary/generator" /%} is
merely a {% tooltip label="gate" href="/glossary/gate" /%}:  a {%
tooltip label="core" href="/glossary/core" /%} with a `$` arm that Dojo
knows to call.  However, we can also invoke a generator which is a cell
of a metadata tag and a core.  The next level-up for our generator
skills is the `%say` generator, a cell of `[%say core]` that affords
slightly more sophisticated evaluation.

We use `%say` generators when we want to provide something else in {%
tooltip label="Arvo" href="/glossary/arvo" /%}, the Urbit operating
system, with metadata about the generator's output. This is useful when
a generator is needed to pipe data to another program, a frequent
occurrence.

To that end, `%say` generators use `mark`s to make it clear, to other
Arvo computations, exactly what kind of data their output is. A {%
tooltip label="mark" href="/glossary/mark" /%} is akin to a MIME type on
the Arvo level. A `mark` describes the data in some way, indicating that
it's an `%atom`, or that it's a standard such as `%json`, or even that
it's an application-specific data structure like `%talk-command`.
`mark`s are not specific to `%say` generators; whenever data moves
between programs in Arvo, that data is marked.

So, more formally, a `%say` generator is a {% tooltip label="cell"
href="/glossary/cell" /%}. The head of that cell is the `%say` tag, and
the tail is a `gate` that produces a `cask` -- a pair of the output data
and the `mark` describing that data. -- Save this example as `add.hoon`
in the `/gen` directory of your `%base` desk:

```hoon {% copy=true %}
:-  %say
|=  *
:-  %noun
(add 40 2)
```

Run it with:

```hoon
> |commit %base

> +add
42
```

Notice that we used no argument, something that is possible with `%say`
generators but impossible with naked generators. We'll explain that in a
moment. For now, let's focus on the code that is necessary to make
something a `%say` generator.

```hoon {% copy=true %}
:-  %say
```

Recall that the rune `:-` {% tooltip label="colhep"
href="/language/hoon/reference/rune/col#--colhep" /%} produces a cell,
with the first following expression as its head and the second following
expression as its tail.

The expression above creates a cell with `%say` as the head. The tail is
the `|= *` expression on the line that follows.

```hoon {% copy=true %}
|=  *
:-  %noun
(add 40 2)
```

`|= *` constructs a {% tooltip label="gate" href="/glossary/gate" /%}
that takes a noun. This `gate` will itself produce a `cask`, which is
cell formed by the prepending `:-`. The head of that `cask` is `%noun`
and the tail is the rest of the program, `(add 40 2)`. The tail of the
`cask` will be our actual data produced by the body of the program: in
this case, just adding 40 and 2 together.

A `%say` generator has access to values besides those passed into it and
the Hoon standard subject.  Namely, a `%say` generator knows about
`our`, `eny`, and `now`, as well as the current desk:

- `our` is our current ship identity.
- `eny` is entropy, a source of randomness.
- `now` is the current system timestamp.
- `bec` is the current path (beak).

These values can be stubbed out with `*` or `^` if they are not needed
in a particular generator.

### `%say` generators with arguments

We can modify the boilerplate code to allow arguments to be passed into
a `%say` generator, but in a way that gives us more power than we would
have if we just used a naked generator.

Naked generators are limited because they have no way of accessing data
that exists in Arvo, such as the date and time or pieces of fresh
entropy.  In `%say` generators, however, we can access that kind of {%
tooltip label="subject" href="/glossary/subject" /%} by identifying them
in the gate's sample, which we only specified as `*` in the previous few
examples. But we can do more with `%say` generators if we do more with
that sample.  Any valid sample will follow this 3-tuple scheme:

`[[now=@da eny=@uvJ bec=beak] [list of unnamed arguments] [list of named arguments]]`

This entire structure is a {% tooltip label="noun" href="/glossary/noun"
/%}, which is why `*` is a valid sample if we wish to not use any of the
information here in a generator. But let's look at each of these three
elements, piece by piece.

##  Exercise:  The Magic 8-Ball

This Magic 8-Ball generator returns one of a variety of answers in
response to a call.  In its entirety:

```hoon {% copy=true mode="collapse" %}
!:
:-  %say
|=  [[* eny=@uvJ *] *]
:-  %noun
^-  tape
=/  answers=(list tape)
  :~  "It is certain."
      "It is decidedly so."
      "Without a doubt."
      "Yes - definitely."
      "You may rely on it."
      "As I see it, yes."
      "Most likely."
      "Outlook good."
      "Yes."
      "Signs point to yes."
      "Reply hazy, try again"
      "Ask again later."
      "Better not tell you now."
      "Cannot predict now."
      "Concentrate and ask again."
      "Don't count on it."
      "My reply is no."
      "My sources say no."
      "Outlook not so good."
      "Very doubtful."
  ==
=/  rng  ~(. og eny)
=/  val  (rad:rng (lent answers))
(snag val answers)
```

`~(. og eny)` starts a random number generator with a seed from the
current entropy.  Right now we don't know quite enough to interpret this
line, but we'll revisit the {% tooltip label="++og"
href="/language/hoon/reference/stdlib/3d#og" /%} aspect of this `%say`
generator in [the lesson on
subject-oriented-programming](/courses/hoon-school/O-subject).  For now,
just know that it allows us to produce a random (unpredictable) integer
using `++rad:rng`.  We slam the `++rad:rng` gate which returns a random
number from 0 to _n_-1 inclusive.  This gives us a random value from the
list of possible answers.

Since this is a `%say` generator, we can run it without arguments:

```hoon
> +magic-8
"Ask again later."
```

If we need to include optional arguments to a generator, we separate
them using a `,` com:

```hoon
+cat /===/gen/cat/hoon, =vane %c
```

##  Exercise:  Using the Playing Card Library

Recall the playing card library `/lib/playing-cards.hoon` in `/lib`.
Let's use it with a `%say` generator.

**`/gen/cards.hoon`**

```hoon {% copy=true %}
/+  playing-cards
:-  %say
|=  [[* eny=@uv *] *]
:-  %noun
(shuffle-deck:playing-cards make-deck:playing-cards eny)
```

Having already saved the library as `/lib/playing-cards.hoon`, you can
import it with the `/+` {% tooltip label="faslus"
href="/language/hoon/reference/rune/fas#-faslus" /%} rune.  When
`cards.hoon` gets built, the Hoon builder will pull in the requested
library and also build that.  It will also create a dependency so that
if `/lib/playing-cards.hoon` changes, this file will also get rebuilt.

Below `/+  playing-cards`, you have the standard `say` generator
boilerplate that allows us to get a bit of entropy from `arvo` when the
generator is run. Then we feed the entropy and a `deck` created by
`make-deck` into `shuffle-deck` to get back a shuffled `deck`.

#### Solutions to Exercises

- Roll-Your-Own-`++snag`:

    ```hoon {% copy=true %}
    ::  snag.hoon
    ::
    |=  [a=@ b=(list @)]
    ?~  b  !!
    ?:  =(0 a)  i.b
    $(a (dec a), b t.b)
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

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS150 - Doors.mp4" /%}

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

### Exercise:  Adding Arms to a Door

Recall the quadratic equation {% tooltip label="door"
href="/glossary/door" /%}.

```hoon {% copy=true %}
|_  [a=@ud b=@ud c=@ud]
++  quad
  |=  x=@ud
  (add (add (mul a (mul x x)) (mul b x)) c)
--
```

- Add an {% tooltip label="arm" href="/glossary/arm" /%} to the door
  which calculates the linear function _a_ × _x_
  + _b_.

- Add another arm which calculates the derivative of the first quadratic
  function, 2 × _a_ × _x_ + _b_.


##  Key-Value Pairs:  `map` as Door

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS183 - Maps and Sets.mp4" /%}

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

### Exercise:  Display Cards

- Recall the `/lib/playing-cards.hoon` library.  Use a map to
  pretty-print the `darc`s as Unicode card symbols.

    The map type should be `(map darc @t)`.  We'll use {% tooltip
    label="++malt" href="/language/hoon/reference/stdlib/2l#malt" /%} to
    build it and associate the fancy (if tiny) [Unicode playing card
    symbols](https://en.wikipedia.org/wiki/Playing_cards_in_Unicode).

    Add the following {% tooltip label="arms" href="/glossary/arm" /%}
    to the library {% tooltip label="core" href="/glossary/core" /%}:

    ```hoon {% copy=true mode="collapse" %}
    ++  pp-card
      |=  c=darc
      (~(got by card-table) c)
    ++  card-table
      %-  malt
      ^-  (list [darc @t])
      :~  :-  [sut=%clubs val=1]  '🃑'
          :-  [sut=%clubs val=2]  '🃒'
          :-  [sut=%clubs val=3]  '🃓'
          :-  [sut=%clubs val=4]  '🃔'
          :-  [sut=%clubs val=5]  '🃕'
          :-  [sut=%clubs val=6]  '🃖'
          :-  [sut=%clubs val=7]  '🃗'
          :-  [sut=%clubs val=8]  '🃘'
          :-  [sut=%clubs val=9]  '🃙'
          :-  [sut=%clubs val=10]  '🃚'
          :-  [sut=%clubs val=11]  '🃛'
          :-  [sut=%clubs val=12]  '🃝'
          :-  [sut=%clubs val=13]  '🃞'
          :-  [sut=%diamonds val=1]  '🃁'
          :-  [sut=%diamonds val=2]  '🃂'
          :-  [sut=%diamonds val=3]  '🃃'
          :-  [sut=%diamonds val=4]  '🃄'
          :-  [sut=%diamonds val=5]  '🃅'
          :-  [sut=%diamonds val=6]  '🃆'
          :-  [sut=%diamonds val=7]  '🃇'
          :-  [sut=%diamonds val=8]  '🃈'
          :-  [sut=%diamonds val=9]  '🃉'
          :-  [sut=%diamonds val=10]  '🃊'
          :-  [sut=%diamonds val=11]  '🃋'
          :-  [sut=%diamonds val=12]  '🃍'
          :-  [sut=%diamonds val=13]  '🃎'
          :-  [sut=%hearts val=1]  '🂱'
          :-  [sut=%hearts val=2]  '🂲'
          :-  [sut=%hearts val=3]  '🂳'
          :-  [sut=%hearts val=4]  '🂴'
          :-  [sut=%hearts val=5]  '🂵'
          :-  [sut=%hearts val=6]  '🂶'
          :-  [sut=%hearts val=7]  '🂷'
          :-  [sut=%hearts val=8]  '🂸'
          :-  [sut=%hearts val=9]  '🂹'
          :-  [sut=%hearts val=10]  '🂺'
          :-  [sut=%hearts val=11]  '🂻'
          :-  [sut=%hearts val=12]  '🂽'
          :-  [sut=%hearts val=13]  '🂾'
          :-  [sut=%spades val=1]  '🂡'
          :-  [sut=%spades val=2]  '🂢'
          :-  [sut=%spades val=3]  '🂣'
          :-  [sut=%spades val=4]  '🂤'
          :-  [sut=%spades val=5]  '🂥'
          :-  [sut=%spades val=6]  '🂦'
          :-  [sut=%spades val=7]  '🂧'
          :-  [sut=%spades val=8]  '🂨'
          :-  [sut=%spades val=9]  '🂩'
          :-  [sut=%spades val=10]  '🂪'
          :-  [sut=%spades val=11]  '🂫'
          :-  [sut=%spades val=12]  '🂭'
          :-  [sut=%spades val=13]  '🂮'
      ==
    ```

    Import the library in Dojo (or use `/+` {% tooltip label="faslus"
    href="/language/hoon/reference/rune/fas#-faslus" /%} in a {% tooltip
    label="generator" href="/glossary/generator" /%}) and build a deck:

    ```hoon
    > =playing-cards -build-file /===/lib/playing-cards/hoon
    
    > =deck (shuffle-deck:playing-cards make-deck:playing-cards eny)
    > deck
    ~[
      [sut=%spades val=12]
      [sut=%spades val=8]
      [sut=%hearts val=5]
      [sut=%clubs val=2]
      [sut=%diamonds val=10]
      ...
      [sut=%spades val=2]
      [sut=%hearts val=6]
      [sut=%hearts val=12]
    ]
    ```

    Finally, render each card in the hand to a `@t` cord:

    ```hoon
    > =new-deck (draw:playing-cards 5 deck)

    > =/  index  0
      =/  hand  *(list @t)
      |-
      ?:  =(index (lent hand:new-deck))
        hand
      $(index +(index), hand (snoc hand (pp-card:playing-cards (snag index hand:new-deck))))
    <|🂭 🂨 🂵 🃒 🃊|>
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

##### Further Exercise

1.  Take the example {% tooltip label="generator"
    href="/glossary/generator" /%} and modify it to add a second layer
    of shifts.
2.  Extend the example generator to allow for use of characters other
    than a-z. Make it shift the new characters independently of the
    alpha characters, such that punctuation is only encoded as other
    punctuation marks.
3.  Build a gate that can take a Caesar shifted `tape` and produce all
    possible unshifted `tapes`.
4.  Modify the example generator into a `%say` generator.


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

#### Example:  Hoon Workbook

Other examples demonstrating {% tooltip label="++map"
href="/language/hoon/reference/stdlib/2o#map" /%} are available in the
[Hoon Workbook](/language/hoon/examples), such as Solution #2 in the
[Rhonda Numbers](/language/hoon/examples/rhonda) tutorial.


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


# M-typecheck.md

---

+++
title = "12. Type Checking"
weight = 22
nodes = [183]
objectives = ["Use assertions to enforce type constraints."]
+++

_In this module we'll cover how the Hoon compiler infers type, as well
as various cases in which a type check is performed._


## Type Casting

Casting is used to explain to the Hoon compiler exactly what it is we
mean with a given data structure.  As you get in the habit of casting
your data structures, it will not only help anyone reading your code,
but it will help you in hunting down bugs in your code.

{% tooltip label="++list" href="/language/hoon/reference/stdlib/1c#list" /%} is
a mold builder that is used to produce a {% tooltip label="mold"
href="/glossary/mold" /%}, i.e. a list of a particular type (like `(list
@)` for a list of atoms).  A list can be thought of as an ordered
arrangement of zero or more elements terminated by a `~` (null).  There
is a difference to Hoon, however, between something explicitly tagged as
a `list` of some kind and a null-terminated tuple.

```hoon
> -:!>(~[1 2 3])
#t/[@ud @ud @ud %~]

> -:!>(`(list @)`~[1 2 3])
#t/it(@)
```

The former is inflexible and doesn't have the `i`/`t` faces that a list
presents.  By marking the type explicitly as a `(list @)` for the
compiler, we achieve some stronger guarantees that many of the `list`
operators require.

However, we still don't get the {% tooltip label="faces"
href="/glossary/face" /%} for free:

```hoon
> =a `(list @)`~[1 2 3]

> i.a
-find.i.a
find-fork
dojo: hoon expression failed
```

What's going on?  Formally, a {% tooltip label="list"
href="/glossary/list" /%} can be either null or non-null.  When the list
contains only `~` and no items, it's the null list.  Most lists are,
however, non-null lists, which have items preceding the `~`. Non-null
lists, called _lests_, are {% tooltip label="cells"
href="/glossary/cell" /%} in which the head is the first list item, and
the tail is the rest of the list.  The tail is itself a list, and if
such a list is also non-null, the head of this sublist is the second
item in the greater list, and so on.  To illustrate, let's look at a
list `[1 2 3 4 ~]` with the cell-delineating brackets left in:

```hoon
[1 [2 [3 [4 ~]]]]
```

It's easy to see where the heads are and where the nesting tails are.
The head of the above list is the atom `1` and the tail is the list `[2
[3 [4 ~]]]`, (or `[2 3 4 ~]`).  Recall that whenever {% tooltip
label="cell" href="/glossary/cell" /%} brackets are omitted so that
visually there appears to be more than two child {% tooltip
label="nouns" href="/glossary/noun" /%}, it is implicitly understood
that the right-most nouns constitute a cell.

You can construct {% tooltip label="lists" href="/glossary/list" /%} of
any type. `(list @)` indicates a list of atoms, `(list ^)` indicates a
list of cells, `(list [@ ?])` indicates a list of cells whose head is an
atom and whose tail is a flag, etc.

```hoon
> `(list @)`~
~

> `(list @)`[1 2 3 4 5 ~]
~[1 2 3 4 5]

> `(list @)`[1 [2 [3 [4 [5 ~]]]]]
~[1 2 3 4 5]

> `(list @)`~[1 2 3 4 5]
~[1 2 3 4 5]
```

Notice how the last Dojo command has a different construction, with the
`~` in front of the bracketed items.  This is just another way of
writing the same thing; `~[1 2]` is semantically identical to `[1 2 ~]`.

Back to our earlier example:

```hoon
> =a `(list @)`~[1 2 3]

> i.a
-find.i.a
find-fork
dojo: hoon expression failed
```

Any time we see a `find-fork` error, it means that the type checker
considers the value to be underspecified.  In this case, it can't
guarantee that `i.a` exists because although `a` is a list, it's not
known to be a non-null lest.  If we enforce that constraint, then
suddenly we can use the faces:

```hoon
> ?:  ?=(~ a)  !!  i.a
1
```

It's important to note that performing tests like this will actually
transform a {% tooltip label="list" href="/glossary/list" /%} into a
`lest`, a non-null list.  Because `lest` is a different type than
`list`, performing such tests can come back to bite you later in
non-obvious ways when you try to use some standard library functions
meant for lists.


### Casting Nouns (`^` ket Runes)

As the Hoon compiler compiles your Hoon code, it does a type check on
certain expressions to make sure they are guaranteed to produce a value
of the correct type.  If it cannot be proved that the output value is
correctly typed, the compile will fail with a {% tooltip
label="nest-fail" href="/language/hoon/reference/hoon-errors#nest-fail"
/%} crash.  In order to figure out what type of value is produced by a
given expression, the compiler uses type inference on that code.

Let's enumerate the most common cases where a type check is called for
in Hoon.

The most obvious case is when there is a casting `^` {% tooltip
label="ket" href="/language/hoon/reference/rune/ket" /%} rune in your
code.  These runes don't directly have any effect on the compiled result
of your code; they simply indicate that a type check should be performed
on a piece of code at compile-time.

#### `^-` kethep Cast with a Type

You've already seen one rune that calls for a type check:
`^-` {% tooltip label="kethep"
href="/language/hoon/reference/rune/ket#--kethep" /%}:

```hoon
> ^-(@ 12)
12

> ^-(@ 123)
123

> ^-(@ [12 14])
nest-fail

> ^-(^ [12 14])
[12 14]

> ^-(* [12 14])
[12 14]

> ^-(* 12)
12

> ^-([@ *] [12 [23 43]])
[12 [23 43]]

> ^-([@ *] [[12 23] 43])
nest-fail
```

#### `^+` ketlus Cast with an Example Value

The rune `^+` {% tooltip label="ketlus"
href="/language/hoon/reference/rune/ket#-ketlus" /%} is like `^-` {%
tooltip label="kethep" href="/language/hoon/reference/rune/ket#--kethep"
/%}, except that instead of using a type name for the cast, it uses an
example value of the type in question.  E.g.:

```hoon
> ^+(7 12)
12

> ^+(7 123)
123

> ^+(7 [12 14])
nest-fail
```

The `^+` {% tooltip label="ketlus"
href="/language/hoon/reference/rune/ket#-ketlus" /%} rune takes two
subexpressions.  The first subexpression is evaluated and its type is
inferred.  The second subexpression is evaluated and its inferred type
is compared against the type of the first.  If the type of the second
provably nests under the type of the first, the result of the `^+`
ketlus expression is just the value of its second subexpression.
Otherwise, the code fails to compile.

This rune is useful for casting when you already have a noun—or an
expression producing a noun—whose type you may not know or be able to
construct easily.  If you want your output value to be of the same type,
you can use `^+` ketlus.

More examples:

```hoon
> ^+([12 13] [123 456])
[123 456]

> ^+([12 13] [123 [12 14]])
nest-fail

> ^+([12 [1 2]] [123 [12 14]])
[123 12 14]
```

### Arm Checks

Whenever an {% tooltip label="arm" href="/glossary/arm" /%} is evaluated
in Hoon it expects to have some version of its parent {% tooltip
label="core" href="/glossary/core" /%} as the {% tooltip label="subject"
href="/glossary/subject" /%}.  Specifically, a type check is performed
to see whether the arm subject is of the appropriate type.  We see this
in action whenever a {% tooltip label="gate" href="/glossary/gate" /%}
or a multi-arm {% tooltip label="door" href="/glossary/door" /%} is
called.

A gate is a one-armed core with a {% tooltip label="sample"
href="/glossary/sample" /%}.  When it is called, its `$` buc arm is
evaluated with (a mutated copy of) the gate as the {% tooltip
label="subject" href="/glossary/subject" /%}. The only part of the core
that might change is the {% tooltip label="payload"
href="/glossary/payload" /%}, including the sample. Of course, we want
the sample to be able to change.  The sample is where the argument(s) of
the function call are placed.  For example, when we call {% tooltip
label="add" href="/language/hoon/reference/stdlib/1a#add" /%} the `$`
buc arm expects two {% tooltip label="atoms" href="/glossary/atom" /%}
for the sample, i.e., the two numbers to be added.  When the type check
occurs, the payload must be of the appropriate type.  If it isn't, the
result is a {% tooltip label="nest-fail"
href="/language/hoon/reference/hoon-errors#nest-fail" /%} crash.

```hoon
> (add 22 33)
55

> (add [10 22] [10 33])
nest-fail

> (|=(a=@ [a a]) 15)
[15 15]

> (|=(a=@ [a a]) 22)
[22 22]

> (|=(a=@ [a a]) [22 22])
nest-fail
```

We'll talk in more detail about the various kinds of type-checking that
can occur at arm evaluation [when we discuss type
polymorphism](/courses/hoon-school/R-metals).

This isn't a comprehensive list of the type checks in Hoon:  for
instance, some other runes that include a type check are `=.` {% tooltip
label="tisdot" href="/language/hoon/reference/rune/tis#-tisdot" /%} and
`%_` {% tooltip label="cencab"
href="/language/hoon/reference/rune/cen#_-cencab" /%}.


##  Type Inference

Hoon infers the type of any given expression.  How does this inference
work?  Hoon has available various tools for inferring the type of any
given expression:  literal syntax, cast expressions, gate sample
definitions, conditional expressions, and more.

### Literals

[Literals](https://en.wikipedia.org/wiki/Literal_%28computer_programming%29)
are expressions that represent fixed values.  {% tooltip label="Atom"
href="/glossary/atom" /%} and {% tooltip label="cell"
href="/glossary/cell" /%} literals are supported in Hoon, and every
supported {% tooltip label="aura" href="/glossary/aura" /%} has an
unambiguous representation that allows the parser to directly infer the
type from the form.  Here are a few examples of auras and associated
literal formats:

| Type | Literal |
| ---- | ------- |
| `@ud` | `123`, `1.000` |
| `@ux` | `0x1234`, `0x12.3456` |
| `@ub` | `0b1011.1110` |
| `[@ud @ud]` | `[12 14]` |
| `[@ux @t ?]` | `[0x1f 'hello' %.y]` |

### Casts

Casting with `^` {% tooltip label="ket"
href="/language/hoon/reference/rune/ket" /%} runes also shape how Hoon
understands an expression type, as outlined above.  The inferred type of
a cast expression is just the type being cast for.  It can be inferred
that, if the cast didn't result in a {% tooltip label="nest-fail"
href="/language/hoon/reference/hoon-errors#nest-fail" /%}, the value
produced must be of the cast type. Here are some examples of cast
expressions with the inferred output type on the right:

| Type | Cast |
| ---- | ---- |
| `@ud` | `^-(@ud 123)` |
| `@` | `^-(@ 123)` |
| `^` | `^-(^ [12 14])` |
| `[@ @]` | `^-([@ @] [12 14])` |
| `*` | `^-(* [12 14])` |
| `@ud` | `^+(7 123)` |
| `[@ud @ud]` | `^+([7 8] [12 14])` |
| `[@ud @ud]` | `^+([44 55] [12 14])` |
| `[@ux @ub]` | `^+([0x1b 0b11] [0x123 0b101])` |

You can also use the irregular `` ` `` syntax for casting in the same
way as `^-` {% tooltip label="kethep"
href="/language/hoon/reference/rune/ket#--kethep" /%}; e.g., `` `@`123
`` for `^-(@ 123)`.

Since casts can throw away type information, if the cast type is more
general, then the more specific type information is lost.  Consider the
literal `[12 14]`.  The inferred type of this expression is `[@ @]`,
i.e., a {% tooltip label="cell" href="/glossary/cell" /%} of two {%
tooltip label="atoms" href="/glossary/atom" /%}.  If we cast over `[12
14]` with `^-(^ [12 14])` then the inferred type is just `^`, the set of
all cells.  The information about what kind of cell it is has been
thrown away.  If we cast over `[12 14]` with `^-(* [12 14])` then the
inferred type is `*`, the set of all {% tooltip label="nouns"
href="/glossary/noun" /%}.  All interesting type information is thrown
away on the latter cast.

It's important to remember to include a cast {% tooltip label="rune"
href="/glossary/rune" /%} with each {% tooltip label="gate"
href="/glossary/gate" /%} and {% tooltip label="trap"
href="/glossary/trap" /%} expression.  That way it's clear what the
inferred product type will be for calls to that core.

### (Dry) Gate Sample Definitions

By now you've used the `|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%} rune to define
several {% tooltip label="gates" href="/glossary/gate" /%}.  This rune
is used to produce a _dry gate_, which has different type-checking and
type-inference properties than a _wet gate_ does.  We won't explain the
distinction until [a later module](/courses/hoon-school/R-metals)—for
now, just keep in mind that we're only dealing with one kind of gate
(albeit the more common kind).

The first subexpression after the `|=` defines the {% tooltip
label="sample" href="/glossary/sample" /%} type.  Any faces used in this
definition have the type declared for it in this definition.  Consider
an addition generator `/gen/sum.hoon`:

```hoon {% copy=true %}
|=  [a=@ b=@]
^-  @
?:  =(b 0)
  a
$(a +(a), b (dec b))
```

We run it in the {% tooltip label="Dojo" href="/glossary/dojo" /%} using
a cell to pass the two arguments:

```hoon
> +sum [12 14]
26

> +sum 22
nest-fail
-need.[a=@ b=@]
-have.@ud
```

If you try to call this gate with the wrong kind of argument, you get
a {% tooltip label="nest-fail"
href="/language/hoon/reference/hoon-errors#nest-fail" /%}.  If the call
succeeds, then the argument takes on the type of the {% tooltip
label="sample" href="/glossary/sample" /%} definition: `[a=@ b=@]`.
Accordingly, the inferred type of `a` is `@`, and the inferred type of
`b` is `@`.  In this case some type information has been thrown away;
the inferred type of `[12 14]` is `[@ud @ud]`, but the addition program
takes all atoms, regardless of {% tooltip label="aura"
href="/glossary/aura" /%}.

### Inferring Type (`?` wut Runes)

#### Using Conditionals for Inference by Branch

You have learned about a few conditional runes (e.g., `?:` {% tooltip
label="wutcol" href="/language/hoon/reference/rune/wut#-wutcol" /%} and
`?.` {% tooltip label="wutdot"
href="/language/hoon/reference/rune/wut#-wutdot" /%}), but other runes
of the `?` family are used for branch-specialized type inference.  The
`?@` {% tooltip label="wutpat"
href="/language/hoon/reference/rune/wut#-wutpat" /%}, `?^` {% tooltip
label="wutket" href="/language/hoon/reference/rune/wut#-wutket" /%}, and
`?~` {% tooltip label="wutsig"
href="/language/hoon/reference/rune/wut#-wutsig" /%} conditionals each
take three subexpressions, which play the same basic role as the
corresponding subexpressions of `?:` wutcol—the first is the test
condition, which evaluates to a flag `?`.  If the test condition is
true, the second subexpression is evaluated; otherwise the third.  These
second and third subexpressions are the ‘branches’ of the conditional.

There is also a `?=` {% tooltip label="wuttis"
href="/language/hoon/reference/rune/wut#-wuttis" /%} rune for
pattern-matching expressions by type, returning `%.y` for a match and
`%.n` otherwise.

##### `?=` wuttis Non-recursive Type Match Test

The `?=` {% tooltip label="wuttis"
href="/language/hoon/reference/rune/wut#-wuttis" /%} rune takes two
subexpressions.  The first subexpression should be a type.  The second
subexpression is evaluated and the resulting value is compared to the
first type.  If the value is an instance of the type, `%.y` is produced.
Otherwise, `%.n`.  Examples:

```hoon
> ?=(@ 12)
%.y

> ?=(@ [12 14])
%.n

> ?=(^ [12 14])
%.y

> ?=(^ 12)
%.n

> ?=([@ @] [12 14])
%.y

> ?=([@ @] [[12 12] 14])
%.n
```

`?=` {% tooltip label="wuttis"
href="/language/hoon/reference/rune/wut#-wuttis" /%} expressions ignore
{% tooltip label="aura" href="/glossary/aura" /%} information:

```hoon
> ?=(@ud 0x12)
%.y

> ?=(@ux 'hello')
%.y
```

We haven't talked much about types that are made with a type constructor
yet.  We'll discuss these more soon, but it's worth pointing out that
every list type qualifies as such, and hence should not be used with
`?=`:

```hoon
> ?=((list @) ~[1 2 3 4])
fish-loop
```

Using these non-basic constructed types with the `?=` {% tooltip
label="wuttis" href="/language/hoon/reference/rune/wut#-wuttis" /%} rune
results in a `fish-loop` error.

The `?=` {% tooltip label="wuttis"
href="/language/hoon/reference/rune/wut#-wuttis" /%} rune is
particularly useful when used with the `?:` {% tooltip label="wutcol"
href="/language/hoon/reference/rune/wut#-wutcol" /%} rune, because in
these cases Hoon uses the result of the `?=` wuttis evaluation to infer
type information.  To see how this works lets use `=/` {% tooltip
label="tisfas" href="/language/hoon/reference/rune/tis#-tisfas" /%} to
define a {% tooltip label="face" href="/glossary/face" /%}, `b`, as a
generic noun:

```hoon
> =/(b=* 12 b)
12
```

The inferred type of the final `b` is just `*`, because that's how `b`
was defined earlier.  We can see this by using `?` in the Dojo to see
the product type:

```hoon
> ? =/(b=* 12 b)
  *
12
```

(Remember that `?` isn't part of Hoon -- it's a Dojo-specific
instruction.)

Let's replace that last `b` with a `?:` {% tooltip label="wutcol"
href="/language/hoon/reference/rune/wut#-wutcol" /%} expression whose
condition subexpression is a `?=` {% tooltip label="wuttis"
href="/language/hoon/reference/rune/wut#-wuttis" /%} test.  If `b` is an
`@`, it'll produce `[& b]`; otherwise `[| b]`:

```hoon
> =/(b=* 12 ?:(?=(@ b) [& b] [| b]))
[%.y 12]
```

You can't see it here, but the inferred type of `b` in `[& b]` is `@`.
That subexpression is only evaluated if `?=(@ b)` evaluates as true;
hence, Hoon can safely infer that `b` must be an {% tooltip label="atom"
href="/glossary/atom" /%} in that subexpression.  Let's set `b` to a
different initial value but leave everything else the same:

```hoon
> =/(b=* [12 14] ?:(?=(@ b) [& b] [| b]))
[%.n 12 14]
```

You can't see it here either, but the inferred type of `b` in `[| b]` is
`^`.  That subexpression is only evaluated if `?=(@ b)` evaluates as
false, so `b` can't be an atom there.  It follows that it must be
a {% tooltip label="cell" href="/glossary/cell" /%}.

##### The Type Spear

What if you want to see the inferred type of `b` for yourself for each
conditional branch?  One way to do this is with the _type spear_.  The
`!>` {% tooltip label="zapgar"
href="/language/hoon/reference/rune/zap#-zapgar" /%} rune takes one
subexpression and constructs a {% tooltip label="cell"
href="/glossary/cell" /%} from it.  The subexpression is evaluated and
becomes the tail of the product cell, with a `q` {% tooltip label="face"
href="/glossary/face" /%} attached.  The head of the product cell is the
inferred type of the subexpression.

```hoon
> !>(15)
[#t/@ud q=15]

> !>([12 14])
[#t/[@ud @ud] q=[12 14]]

> !>((add 22 55))
[#t/@ q=77]
```

The `#t/` is the pretty-printer's way of indicating a type.

To get just the inferred type of a expression, we only want the head of
the `!>` product, `-`.  Thus we should use our mighty weapon, the type
spear, `-:!>`.

```hoon
> -:!>(15)
#t/@ud

> -:!>([12 14])
#t/[@ud @ud]

> -:!>((add 22 55))
#t/@
```

Now let's try using `?=` {% tooltip label="wuttis"
href="/language/hoon/reference/rune/wut#-wuttis" /%} with `?:` {%
tooltip label="wutcol" href="/language/hoon/reference/rune/wut#-wutcol"
/%} again.  But this time we'll replace `[& b]` with `[& -:!>(b)]` and
`[| b]` with `[| -:!>(b)]`. With `b` as `12`:

```hoon
> =/(b=* 12 ?:(?=(@ b) [& -:!>(b)] [| -:!>(b)]))
[%.y #t/@]
```

… and with `b` as `[12 14]`:

```hoon
> =/(b=* [12 14] ?:(?=(@ b) [& -:!>(b)] [| -:!>(b)]))
[%.n #t/[* *]]
```

In both cases, `b` is defined initially as a generic {% tooltip
label="noun" href="/glossary/noun" /%}, `*`.  But when using `?:` with
`?=(@ b)` as the test condition, `b` is inferred to be an {% tooltip
label="atom" href="/glossary/atom" /%}, `@`, when the condition is true;
otherwise `b` is inferred to be a {% tooltip label="cell"
href="/glossary/cell" /%}, `^` (identical to `[* *]`).

###### `mint-vain`

Expressions of the form `?:(?=(a b) c d)` should only be used when the
previously inferred type of `b` isn't specific enough to determine
whether it nests under `a`.  This kind of expression is only to be used
when `?=` can reveal new type information about `b`, not to confirm
information Hoon already has.

For example, if you have a wing expression (e.g., `b`) that is already
known to be an atom, `@`, and you use `?=(@ b)` to test whether `b` is
an atom, you'll get a {% tooltip label="mint-vain"
href="/language/hoon/reference/hoon-errors#mint-vain-and-mint-lost" /%}
crash.  The same thing happens if `b` is initially defined to be a {%
tooltip label="cell" href="/glossary/cell" /%} `^`:

```hoon
> =/(b=@ 12 ?:(?=(@ b) [& b] [| b]))
mint-vain

> =/(b=^ [12 14] ?:(?=(@ b) [& b] [| b]))
mint-vain
```

In the first case it's already known that `b` is an atom.  In the second
case it's already known that `b` isn't an atom.  Either way, the check
is superfluous and thus one of the `?:` wutcol branches will never be
taken.  The `mint-vain` crash indicates that it's provably the case one
of the branches will never be taken.

#### `?@` wutpat Atom Match Tests

The `?@` {% tooltip label="wutpat"
href="/language/hoon/reference/rune/wut#-wutpat" /%} rune takes three
subexpressions.  The first is evaluated, and if its value is an instance
of `@`, the second subexpression is evaluated.  Otherwise, the third
subexpression is evaluated.

```hoon
> =/(b=* 12 ?@(b %atom %cell))
%atom

> =/(b=* [12 14] ?@(b %atom %cell))
%cell
```

If the second `?@` {% tooltip label="wutpat"
href="/language/hoon/reference/rune/wut#-wutpat" /%} subexpression is
evaluated, Hoon correctly infers that `b` is an {% tooltip label="atom"
href="/glossary/atom" /%}.  if the third subexpression is evaluated,
Hoon correctly infers that `b` is a {% tooltip label="cell"
href="/glossary/cell" /%}.

```hoon
> =/(b=* 12 ?@(b [%atom -:!>(b)] [%cell -:!>(b)]))
[%atom #t/@]

> =/(b=* [12 14] ?@(b [%atom -:!>(b)] [%cell -:!>(b)]))
[%cell #t/[* *]]
```

If the inferred type of the first `?@` {% tooltip label="wutpat"
href="/language/hoon/reference/rune/wut#-wutpat" /%} subexpression nests
under `@` then one of the conditional branches provably never runs.
Attempting to evaluate the expression results in a {% tooltip
label="mint-vain"
href="/language/hoon/reference/hoon-errors#mint-vain-and-mint-lost" /%}:

```hoon
> ?@(12 %an-atom %not-an-atom)
mint-vain

> ?@([12 14] %an-atom %not-an-atom)
mint-vain

> =/(b=@ 12 ?@(b %an-atom %not-an-atom))
mint-vain

> =/(b=^ [12 14] ?@(b %an-atom %not-an-atom))
mint-vain
```

`?@` {% tooltip label="wutpat"
href="/language/hoon/reference/rune/wut#-wutpat" /%} should only be used
when it allows for Hoon to infer new type information; it shouldn't be
used to confirm type information Hoon already knows.

#### `?^` wutket Cell Match Tests

The `?^` {% tooltip label="wutket"
href="/language/hoon/reference/rune/wut#-wutket" /%} rune is just like
`?@` {% tooltip label="wutpat"
href="/language/hoon/reference/rune/wut#-wutpat" /%} except it tests for
a cell match instead of for an atom match.  The first subexpression is
evaluated, and if the resulting value is an instance of `^` the second
subexpression is evaluated. Otherwise, the third is run.

```hoon
> =/(b=* 12 ?^(b %cell %atom))
%atom

> =/(b=* [12 14] ?^(b %cell %atom))
%cell
```

Again, if the second subexpression is evaluated Hoon infers that `b` is
a cell; if the third, Hoon infers that `b` is an atom.  If one of the
conditional branches is provably never evaluated, the expression crashes
with a {% tooltip label="mint-vain"
href="/language/hoon/reference/hoon-errors#mint-vain-and-mint-lost" /%}:

```hoon
> =/(b=@ 12 ?^(b %cell %atom))
mint-vain

> =/(b=^ 12 ?^(b %cell %atom))
nest-fail
```

#### Tutorial:  Leaf Counting

{% tooltip label="Nouns" href="/glossary/noun" /%} can be understood as
binary trees in which each 'leaf' of the tree is an {% tooltip
label="atom" href="/glossary/atom" /%}.  Let's look at a program that
takes a noun and returns the number of leaves in it, i.e., the number of
atoms.

```hoon {% copy=true %}
|=  a=*
^-  @
?@  a
  1
(add $(a -.a) $(a +.a))
```

Save this as `/gen/leafcount.hoon` in your fakeship's {% tooltip
label="pier" href="/glossary/pier" /%} and run it from the {% tooltip
label="Dojo" href="/glossary/dojo" /%}:

```hoon
> +leafcount 12
1

> +leafcount [12 14]
2

> +leafcount [12 [63 [829 12] 23] 13]
6
```

This program is pretty simple.  If the noun `a` is an atom, then it's a
tree of one leaf; return `1`.  Otherwise, the number of leaves in `a` is
the sum of the leaves in the head, `-.a`, and the tail, `+.a`.

We have been careful to use `-.a` and `+.a` only on a branch for which
`a` is proved to be a {% tooltip label="cell" href="/glossary/cell" /%}
-- then it's safe to treat `a` as having a head and a tail.

#### Tutorial:  Cell Counting

Here's a program that counts the number of cells in a noun:

```hoon {% copy=true %}
|=  a=*
=|  c=@
|-  ^-  @
?@  a
  c
%=  $
  c  $(c +(c), a -.a)
  a  +.a
==
```

Save this as `/gen/cellcount.hoon` and run it from the Dojo:

```hoon
> +cellcount 12
0

> +cellcount [12 14]
1

> +cellcount [12 14 15]
2

> +cellcount [[12 [14 15]] 15]
3

> +cellcount [[12 [14 15]] [15 14]]
4

> +cellcount [[12 [14 15]] [15 [14 22]]]
5
```

This code is a little more tricky.  The basic idea, however, is simple.
We have a counter value, `c`, whose initial value is `0` (`=|` {%
tooltip label="tisbar" href="/language/hoon/reference/rune/tis#-tisbar"
/%} pins the {% tooltip label="bunt" href="/glossary/bunt" /%} of the
value with the given {% tooltip label="face" href="/glossary/face"
/%}).  We trace through the noun `a`, adding `1` to `c` every time we
come across a cell.  For any part of the noun that is just an atom, `c`
is returned unchanged.

What makes this program is little harder to follow is that it recurses
within a recursion call.  The first recursion expression on line 6 makes
changes to two face values:  `c`, the counter, and `a`, the input noun.
The new value for `c` defined in the line `$(c +(c), a -.a)` is another
recursion call (this time in irregular syntax).  The new value for `c`
is to be the result of running the same function on the the head of `a`,
`-.a`, and with `1` added to `c`.  We add `1` because we know that `a`
must be a {% tooltip label="cell" href="/glossary/cell" /%}.  Otherwise,
we're asking for the number of cells in the rest of `-.a`.

Once that new value for `c` is computed from the head of `a`, we're
ready to check the tail of `a`, `+.a`.  We've already got everything we
want from `-.a`, so we throw that away and replace `a` with `+.a`.

### Lists

You learned about lists earlier in the chapter, but we left out a little
bit of information about the way Hoon understands {% tooltip
label="list" href="/glossary/list" /%} types.

A non-null list is a cell.  If `b` is a non-null list then the head of
`b` is the first item of `b` _with an `i` face on it_.  The tail of `b`
is the rest of the list.  The 'rest of the list' is itself another list
_with a `t` {% tooltip label="face" href="/glossary/face" /%} on it_.
We can (and should) use these `i` and `t` faces in list functions.

To illustrate: let's say that `b` is the list of the atoms `11`, `22`,
and `33`.  Let's construct this in stages:

```hoon
[i=11 t=[rest-of-list-b]]

[i=11 t=[i=22 t=[rest-of-list-b]]]

[i=11 t=[i=22 t=[i=33 t=~]]]
```

(There are lists of every type.  Lists of `@ud`, `@ux`, `@` in general,
`^`, `[^ [@ @]]`, etc.  We can even have lists of lists of `@`, `^`, or
`?`, etc.)

#### Tutorial:  List Spanning Values

Here's a program that takes atoms `a` and `b` and returns a list of all
atoms from `a` to `b`:

```hoon {% copy=true %}
|=  [a=@ b=@]
^-  (list @)
?:  (gth a b)
  ~
[i=a t=$(a +(a))]
```

This program is very simple.  It takes two `@` as input, `a` and `b`,
and returns a `(list @)`, i.e., a list of `@`.  If `a` is greater than
`b` the {% tooltip label="list" href="/glossary/list" /%} is finished:
return the null list `~`.  Otherwise, return a non-null list: a pair in
which the head is `a` with an `i` {% tooltip label="face"
href="/glossary/face" /%} on it, and in which the tail is another list
with the `t` face on it.  This embedded list is the product of a
recursion call: add `1` to `a` and run the function again.

Save this code as `/gen/gulf.hoon` and run it from the Dojo:

```hoon
> +gulf [1 10]
~[1 2 3 4 5 6 7 8 9 10]

> +gulf [10 20]
~[10 11 12 13 14 15 16 17 18 19 20]

> +gulf [20 10]
~
```

Where are all the `i`s and `t`s???  For the sake of neatness the Hoon
pretty-printer doesn't show the `i` and `t` faces of lists, just the
items.

In fact, we could have left out the `i` and `t` faces in the program
itself:

```hoon {% copy=true %}
|=  [a=@ b=@]
^-  (list @)
?:  (gth a b)
  ~
[a $(a +(a))]
```

Because there is a cast to a `(list @)` on line 2, Hoon will silently
include `i` and `t` faces for the appropriate places of the {% tooltip
label="noun" href="/glossary/noun" /%}. Remember that {% tooltip
label="faces" href="/glossary/face" /%} are recorded in the type
information of the noun in question, not as part of the noun itself.

We called this program `gulf.hoon` because it replicates the {% tooltip
label="gulf" href="/language/hoon/reference/stdlib/2b#gulf" /%} function
in the Hoon standard library:

```hoon
> (gulf 1 10)
~[1 2 3 4 5 6 7 8 9 10]

> (gulf 10 20)
~[10 11 12 13 14 15 16 17 18 19 20]
```

#### `?~` wutsig Null Match Test

The `?~` {% tooltip label="wutsig"
href="/language/hoon/reference/rune/wut#-wutsig" /%} rune is a lot like
`?@` {% tooltip label="wutpat"
href="/language/hoon/reference/rune/wut#-wutpat" /%} and `?^` {% tooltip
label="wutket" href="/language/hoon/reference/rune/wut#-wutket" /%}.  It
takes three subexpressions, the first of which is evaluated to see
whether the result is `~` null. If so, the second subexpression is
evaluated.  Otherwise, the third one is evaluated.

```hoon
> =/(b=* ~ ?~(b %null %not-null))
%null

> =/(b=* [12 13] ?~(b %null %not-null))
%not-null
```

The inferred type of `b` must not already be known to be null or
non-null; otherwise, the expression will crash with a {% tooltip
label="mint-vain"
href="/language/hoon/reference/hoon-errors#mint-vain-and-mint-lost" /%}:

```hoon
> =/(b=~ ~ ?~(b %null %not-null))
mint-vain

> =/(b=^ [10 12] ?~(b %null %not-null))
mint-vain

> ?~(~ %null %not-null)
mint-vain
```

Hoon will infer that `b` either is or isn't null based on which `?~`
branch is evaluated after the test.

##### Using `?~` wutsig With Lists

`?~` {% tooltip label="wutsig"
href="/language/hoon/reference/rune/wut#-wutsig" /%} is especially
useful for working with lists.  Is a list null, or not?  You probably
want to do different things based on the answer to that question.
Above, we used a pattern of `?:` {% tooltip label="wutcol"
href="/language/hoon/reference/rune/wut#-wutcol" /%} and `?=` {% tooltip
label="wuttis" href="/language/hoon/reference/rune/wut#-wuttis" /%} to
answer the question, but `?~` wutsig will let us know in one step.
Here's a program using `?~` wutsig to calculate the number of items in a
list of atoms:

```hoon {% copy=true %}
|=  a=(list @)
=|  c=@
|-  ^-  @
?~  a
  c
$(c +(c), a t.a)
```

This function takes a list of `@` and returns an `@`.  It uses `c` as a
counter value, initially set at `0` on line 2.  If `a` is `~` (i.e., a
null list) then the computation is finished; return `c`.  Otherwise `a`
must be a non-null {% tooltip label="list" href="/glossary/list" /%}, in
which case there is a recursion to the `|-` {% tooltip label="barhep"
href="/language/hoon/reference/rune/bar#--barhep" /%} on line 3, but with
`c` incremented, and with the head of the list `a` thrown away.

It's important to note that if `a` is a list, you can only use `i.a` and
`t.a` after Hoon has inferred that `a` is non-null.  A null list has no
`i` or `t` in it!  You'll often use `?~` to distinguish the two kinds of
list (null and non-null).  If you use `i.a` or `t.a` without showing
that `a` is non-null you'll get a `find-fork` crash.

A non-null `list` is called a `lest`.

Save the above code as `/gen/lent.hoon` and run it from the Dojo:

```hoon
> +lent ~[11 22 33]
3

> +lent ~[11 22 33 44 55 77]
6

> +lent ~[0xff 0b11 'howdy' %hello]
4
```

#### Tutorial:  Converting a Noun to a List of its Leaves

Here's a program that takes a noun and returns a {% tooltip label="list"
href="/glossary/list" /%} of its 'leaves' (atoms) in order of their
appearance:

```hoon {% copy=true %}
|=  a=*
=/  lis=(list @)  ~
|-  ^-  (list @)
?@  a
  [i=a t=lis]
$(lis $(a +.a), a -.a)
```

The input noun is `a`.  The list of atoms to be output is `lis`, which
is given an initial value of `~`.  If `a` is just an atom, return a
non-null list whose head is `a` and whose tail is `lis`.  Otherwise, the
somewhat complicated recursion `$(lis $(a +.a), a -.a)` is evaluated, in
effect looping back to the `|-` with modifications made to `lis` and
`a`.

The modification to `lis` in line 6 is to `$(a +.a)`.  The latter is a
recursion to `|-` but with `a` replaced by its tail.  This evaluates to
the list of `@` in the tail of `a`.  So `lis` becomes the list of atoms
in the tail of `a`, and `a` becomes the head of `a`, `-.a`.

Save the above code as `/gen/listleaf.hoon` and run it from the Dojo:

```hoon
> +listleaf [[[[12 13] [33 22] 12] 11] 33]
~[12 13 33 22 12 11 33]
```

### Other Kinds of Type Inference

So far you've learned about four kinds of type inference:

1.  literals
2.  explicit casts
3.  gate sample definitions
4.  branch specialization using runes in the `?` family

There are several other ways that Hoon infers type.  Any rune expression
that evaluates to a `?` flag, e.g., `.=` {% tooltip label="dottis"
href="/language/hoon/reference/rune/dot#-dottis" /%}, will be inferred
from accordingly.  The `.+` {% tooltip label="dotlus"
href="/language/hoon/reference/rune/dot#-dotlus" /%} rune always
evaluates to an `@`, and Hoon knows that too.  The cell constructor
runes, `:-` {% tooltip label="colhep"
href="/language/hoon/reference/rune/col#--colhep" /%}, `:+` {% tooltip
label="collus" href="/language/hoon/reference/rune/col#-collus" /%},
`:^` {% tooltip label="colket"
href="/language/hoon/reference/rune/col#-colket" /%}, and `:*` {%
tooltip label="coltar" href="/language/hoon/reference/rune/col#-coltar"
/%} are all known to produce cells.

More subtly, the `=+` {% tooltip label="tislus"
href="/language/hoon/reference/rune/tis#-tislus" /%}, `=/` {% tooltip
label="tisfas" href="/language/hoon/reference/rune/tis#-tisfas" /%}, and
`=|` {% tooltip label="tisbar"
href="/language/hoon/reference/rune/tis#-tisbar" /%} runes modify the {%
tooltip label="subject" href="/glossary/subject" /%} by pinning values
to the head.  Hoon infers from this that the subject has a new type:  a
cell whose head is the type of the pinned value and whose tail is the
type of the (old) subject.

In general, anything that modifies the subject modifies the type of the
subject.  Type inference can work in subtle ways for various
expressions.  However, we have covered enough that it should be
relatively clear how to anticipate how type inference works for the vast
majority of ordinary use cases.


## Auras as 'Soft' Types

It's important to understand that Hoon's type system doesn't enforce {%
tooltip label="auras" href="/glossary/aura" /%} as strictly as it does
other types. Auras are 'soft' type information. To see how this works,
we'll take you through the process of converting the aura of an {%
tooltip label="atom" href="/glossary/atom" /%} to another aura.

Hoon makes an effort to enforce that the correct aura is produced by an
expression:

```hoon
> ^-(@ud 0x10)
nest-fail

> ^-(@ud 0b10)
nest-fail

> ^-(@ux 100)
nest-fail
```

But there are ways around this. First, you can cast to a more general
aura, as long as the current aura nests under the cast aura. E.g., `@ub`
to `@u`, `@ux` to `@u`, `@u` to `@`, etc. By doing this you're
essentially telling Hoon to throw away some aura information:

```hoon
> ^-(@u 0x10)
16

> ? ^-(@u 0x10)
  @u
16

> ^-(@u 0b10)
2

> ? ^-(@u 0b10)
  @u
2
```

In fact, you can cast any atom all the way to the most general case `@`:

```hoon
> ^-(@ 0x10)
16

> ? ^-(@ 0x10)
  @
16

> ^-(@ 0b10)
2

> ? ^-(@ 0b10)
  @
2
```

Anything of the general {% tooltip label="aura" href="/glossary/aura"
/%} `@` can, in turn, be cast to more specific auras. We can show this
by embedding a cast expression inside another cast:

```hoon
> ^-(@ud ^-(@ 0x10))
16

> ^-(@ub ^-(@ 0x10))
0b1.0000

> ^-(@ux ^-(@ 10))
0xa
```

Hoon uses the outermost cast to infer the type:

```hoon
> ? ^-(@ub ^-(@ 0x10))
  @ub
0b1.0000
```

As you can see, an atom with one aura can be converted to another aura.
For a convenient shorthand, you can do this conversion with irregular
cast syntax, e.g. `` `@ud` ``, rather than using the `^-` {% tooltip
label="kethep" href="/language/hoon/reference/rune/ket#--kethep" /%}
rune twice:

```hoon
> `@ud`0x10
16

> `@ub`0x10
0b1.0000

> `@ux`10
0xa
```

This is what we mean when we call auras 'soft' types. The above examples
show that the programmer can get around the type system for auras by
casting up to `@` and then back down to the specific aura, say `@ub`; or
by casting with `` `@ub` `` for short.

**Note**:  there is currently a type system issue that causes some of
these functions to fail when passed a list `b` after some type inference
has been performed on `b`.  For an illustration of the bug, let's set
`b` to be a `(list @)` of `~[11 22 33 44]` in the Dojo:

```hoon
> =b `(list @)`~[11 22 33 44]

> b
~[11 22 33 44]
```

Now let's use `?~` {% tooltip label="wutsig"
href="/language/hoon/reference/rune/wut#-wutsig" /%} to prove that `b`
isn't null, and then try to snag it:

```hoon
> ?~(b ~ (snag 0 b))
nest-fail
```

The problem is that {% tooltip label="++snag"
href="/language/hoon/reference/stdlib/2b#snag" /%} is expecting a raw
list, not a list that is known to be non-null.

You can cast `b` back to `(list)` to work around this:

```hoon
> ?~(b ~ (snag 0 `(list)`b))
11
```

### Pattern Matching and Assertions

To summarize, as values get passed around and checked at various points,
the Hoon compiler tracks what the possible data structure or {% tooltip
label="mold" href="/glossary/mold" /%} looks like.  The following runes
are particularly helpful when inducing the compiler to infer what it
needs to know:

- `?~` {% tooltip label="wutsig"
  href="/language/hoon/reference/rune/wut#-wutsig" /%} asserts non-null.
- `?^` {% tooltip label="wutket"
  href="/language/hoon/reference/rune/wut#-wutket" /%} asserts cell.
- `?@` {% tooltip label="wutpat"
  href="/language/hoon/reference/rune/wut#-wutpat" /%} asserts atom.
- `?=` {% tooltip label="wuttis"
  href="/language/hoon/reference/rune/wut#-wuttis" /%} tests for a
  pattern match in type.

There are two additional assertions which can be used with the type
system:

- `?>` {% tooltip label="wutgar"
  href="/language/hoon/reference/rune/wut#-wutgar" /%} is a positive
  assertion (`%.y` or crash).
- `?<` {% tooltip label="wutgal"
  href="/language/hoon/reference/rune/wut#-wutgal" /%} is a negative
  assertion (`%.n` or crash).

If you are running into `find-fork` errors in more complicated data
structures (like {% tooltip label="marks" href="/glossary/mark" /%} or
JSONs), consider using these assertions to guide the typechecker.


# N-logic.md

---

+++
title = "13. Conditional Logic"
weight = 23
nodes = [184]
objectives = ["Produce loobean expressions.", "Reorder conditional arms.", "Switch against a union with or without default."]
+++

{% video src="https://media.urbit.org/docs/hoon-school-videos/HS184 - Logical Operations.mp4" /%}

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

### Exercise:  Design a `NAND` Function

The logical operation `NAND` (i.e. _p_ ↑ _q_) produces false if both
operands are true.  `NAND` can be calculated by ¬(_p_ ∧ _q_).

|             `NAND`            | `%.y` | `%.n` |
|-------------------------------|-------|-------|
| `%.y`{% class="font-bold" %}  | `%.n` | `%.y` |
| `%.n`{% class="font-bold" %}  | `%.y` | `%.y` |

- Implement `NAND` as a gate in Hoon.

### Exercise:  Design a `NOR` Function

The logical operation `NOR` (i.e. _p_ ↓ _q_) produces true if both
operands are false.  `NOR` can be calculated by ¬(_p_ ∨ _q_).

|             `NOR`            | `%.y` | `%.n` |
|------------------------------|-------|-------|
| `%.y`{% class="font-bold" %} | `%.n` | `%.n` |
| `%.n`{% class="font-bold" %} | `%.n` | `%.y` |

- Implement `NAND` as a gate in Hoon.

### Exercise:  Implement a Piecewise Boxcar Function

The boxcar function is a piecewise mathematical function which is equal
to zero for inputs less than zero and one for inputs greater than or
equal to zero.  We implemented the similar Heaviside function
[previously](/courses/hoon-school/B-syntax) using the `?:` {% tooltip
label="wutcol" href="/language/hoon/reference/rune/wut#-wutcol" /%}
rune.

- Compose a gate which implements the boxcar function,

    {% math block=true %}
    \text{boxcar}(x)
    :=
    \left(
    \begin{matrix}
    1, & 10 \leq x < 20 \\\\
    0, & \text{otherwise} \\\\
    \end{matrix}
    \right)
    {% /math %}

    <!--
    $$
    \text{boxcar}(x)
    :=
    \begin{matrix}
    1, & 10 \leq x < 20 \\
    0, & \text{otherwise} \\
    \end{matrix}
    $$
    -->

    Use Hoon logical operators to compress the logic into a single
    statement using at least one `AND` or `OR` operation.


# O-subject.md

---

+++
title = "14. Subject-Oriented Programming"
weight = 24
nodes = [165, 180]
objectives = ["Review subject-oriented programming as a design paradigm.", "Discuss stateful v. stateless applications and path dependence.", "Enumerate Hoon's tools for dealing with state:  `=.` tisdot, `=^` tisket, `;<` micgal, `;~` micsig.", "Defer a computation."]
+++

_This module discusses how Urbit's subject-oriented programming paradigm
structures how cores and values are used and maintain state, as well as
how deferred computations and remote value lookups ({% tooltip
label="\"scrying\"" href="/glossary/scry" /%}) are handled.  This
module does not cover {% tooltip label="core" href="/glossary/core" /%}
genericity and variance, which will be explained in [a later
module](/courses/hoon-school/R-metals)._


##  The Subject

As we've said before:

> The Urbit operating system hews to a conceptual model wherein each
> expression takes place in a certain context (the {% tooltip
> label="subject" href="/glossary/subject" /%}).  While
> sharing a lot of practicality with other programming paradigms and
> platforms, Urbit's model is mathematically well-defined and
> unambiguously specified.  Every expression of Hoon is evaluated relative
> to its subject, a piece of data that represents the environment, or the
> context, of an expression.

Subject-oriented programming means that every expression is evaluated
with respect to some {% tooltip label="subject" href="/glossary/subject"
/%}.  Every {% tooltip label="arm" href="/glossary/arm" /%} of a {%
tooltip label="core" href="/glossary/core" /%} is evaluated with its
parent core as the subject.

You have also seen how wings work as search paths to identify {% tooltip
label="nouns" href="/glossary/noun" /%} in the {% tooltip
label="subject" href="/glossary/subject" /%}, and you have learned three
ways to access values by address:  numeric addressing, lark notation,
and wing search expressions.

Generally speaking, the following {% tooltip label="rune"
href="/glossary/rune" /%} families allow you to do certain things to
the {% tooltip label="subject" href="/glossary/subject" /%}:

- `|` {% tooltip label="bar" href="/language/hoon/reference/rune/bar"
  /%} runes create {% tooltip label="cores" href="/glossary/core" /%},
  i.e. largely self-contained expressions
- `^` {% tooltip label="ket" href="/language/hoon/reference/rune/ket"
  /%} runes transform cores, i.e. change core properties
- `%` {% tooltip label="cen" href="/language/hoon/reference/rune/cen"
  /%} runes pull arms in cores
- `=` {% tooltip label="tis" href="/language/hoon/reference/rune/tis"
  /%} runes modify the subject by introducing or replacing values

Different kinds of cores can expose or conceal functionality (such as
their sample) based on their variance model.  We don't need to be
concerned about that yet, but if you are building certain kinds of
library code or intend to build code expressions directly, you'll need
to read [that module](/courses/hoon-school/R-metals) as well.

### Accessing the Subject

Usually the subject of a Hoon expression isn't shown explicitly.  In
fact, only when using `:`/`.` wing lookup expressions have we made the
{% tooltip label="subject" href="/glossary/subject" /%} explicit.

An arm is always evaluated with its parent core as its subject.  We've
briefly mentioned that one can use helper cores (e.g. for generators) by
composing the cores side-by-side using `=<` {% tooltip label="tisgal"
href="/language/hoon/reference/rune/tis#-tisgal" /%} and `=>` {% tooltip
label="tisgar" href="/language/hoon/reference/rune/tis#-tisgar" /%}.
This way we can make sure that the arms fall within each other's subject
horizon.

Why must an {% tooltip label="arm" href="/glossary/arm" /%} have its
parent core as the subject, when it's computed? As stated previously,
the {% tooltip label="payload" href="/glossary/payload" /%} of a core
contains all the data needed for computing the arms of that core.  Arms
can only access data in the subject.  By requiring that the parent core
be the subject we guarantee that each arm has the appropriate data
available to it.  The tail of its subject contains the `payload` and
thus all the values therein.  The head of the subject is the {% tooltip
label="battery" href="/glossary/battery" /%}, which allows for making
reference to sibling arms of that same core.

In the Dojo, if you use `+1` by itself, you can see the current {%
tooltip label="subject" href="/glossary/subject" /%}.

```hoon
> +1
[ [ our=~zod
    now=~2024.5.7..21.47.30..818c
      eny
    0vb6.cve93.67frc.2gtoj.jfl3i.odojg.urrce.o53d3.44h4o.sf3o5.va2mh.ra1ec.jrkej.u512k.l4lin.f003v.li030.l2e6t.ah7ge.6t5cg.epuil
  ]
  <15.eah 40.ihi 14.tdo 54.xjm 77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
]
```

`.` does the same thing:  it always refers to the current subject.

If `.` is the subject, then `..arm` is the subject of a given {% tooltip
label="arm" href="/glossary/arm" /%} (the second `.` dot being the wing
resolution operator).  You can check the details of the parent {%
tooltip label="core" href="/glossary/core" /%} using something like
`..add`.  This trick is used when producing agents that have highly
nested operations (search `..` in the `/app` directory), or when
composing
[jets](/system/runtime/guides/jetting#edit-the-hoon-source-code), for
instance.

Another use case for the `..arm` syntax is when there is a core in the
subject without a {% tooltip label="face" href="/glossary/face" /%}
bound to it; i.e., the core might be nameless. In that case you can use
an arm name in that {% tooltip label="core" href="/glossary/core" /%} to
refer to the whole core.

```hoon
> ..add
<33.uof 1.pnw %138>
```

#### Tutorial:  The Core Structure of `hoon.hoon`

Let's take a deeper look at how cores can be combined with `=>` {%
tooltip label="tisgar" href="/language/hoon/reference/rune/tis#-tisgar"
/%} to build up larger structures.  `=>  p=hoon  q=hoon` yields the
product of `q` with the product of `p` taken as the subject; i.e. it
composes Hoon statements, like {% tooltip label="cores"
href="/glossary/core" /%}.

We use this to set the context of cores.  Recall that the {% tooltip
label="payload" href="/glossary/payload" /%} of a {% tooltip
label="gate" href="/glossary/gate" /%} is a cell of `[sample context]`.
For example:

```hoon
> =foo =>([1 2] |=(@ 15))

> +3:foo
[0 1 2]
```

Here we have created a gate with `[1 2]` as its context that takes in an
`@` and returns `15`.  `+3:foo` shows the payload of the core to be `[0
[1 2]]`.  Here `0` is the default value of `@` and is the sample, while
`[1 2]` is the context that was given to `foo`.

`=>` {% tooltip label="tisgar"
href="/language/hoon/reference/rune/tis#-tisgar" /%} (and its reversed
version `=<` {% tooltip label="tisgal" href="/language/hoon/reference/rune/tis#-tisgal"
/%}) are used extensively to put cores into the context of other cores.

```hoon {% copy=true %}
=>
|%
++  foo
  |=  a=@
  (mul a 2)
--
|%
++  bar
  |=  a=@
  (mul (foo a) 2)
--
```

At the level of {% tooltip label="arms" href="/glossary/arm" /%},
`++foo` is in the {% tooltip label="subject" href="/glossary/subject"
/%} of `++bar`, and so `++bar` is able to call `++foo`. On the other
hand, `+bar` is not in the subject of `++foo`, so `++foo` cannot call
`++bar` - you will get a `-find.bar` error.

At the level of cores, the `=>` sets the context of the core containing
`++bar` to be the core containing `++foo`.  Recall that arms are
evaluated with the parent {% tooltip label="core" href="/glossary/core"
/%} as the subject.  Thus `++bar` is evaluated with the core containing
it as the subject, which has the core containing `++foo` in its context.
This is why `++foo` is in the scope of `++bar` but not vice versa.

Let's look inside `/sys/hoon.hoon`, where the standard library is
located, to see how this can be used.

The first core listed here has just one arm.

```hoon
=>  %138  =>
|%
++  hoon-version  +
--
```

This is reflected in the {% tooltip label="subject"
href="/glossary/subject" /%} of `hoon-version`.

```hoon
> ..hoon-version
<1.pnw %138>
```

After several lines that we'll ignore for pedagogical purposes, we see

```hoon
|%
::  #  %math
::    unsigned arithmetic
+|  %math
++  add
  ~/  %add
  ::  unsigned addition
  ::
  ::  a: augend
  ::  b: addend
  |=  [a=@ b=@]
  ::  sum
  ^-  @
  ?:  =(0 a)  b
  $(a (dec a), b +(b))
::
++  dec
```

and so on, down to

```hoon
++  unit
  |$  [item]
  ::    maybe
  ::
  ::  mold generator: either `~` or `[~ u=a]` where `a` is the
  ::  type that was passed in.
  ::
  $@(~ [~ u=item])
--
```

This core contains the arms in [sections 1a–1c of the standard library
documentation](/language/hoon/reference/stdlib/1a).  If you count them,
there are 33 arms in the core from `++  add` down to `++  unit`.  We
again can see this fact reflected in the dojo by looking at the subject
of `add`.

```hoon
> ..add
<33.uof 1.pnw %138>
```

Here we see that core containing `hoon-version` is in the {% tooltip
label="subject" href="/glossary/subject" /%} of the section 1 core.

Next, [section 2](/language/hoon/reference/stdlib/2a) starts:

```hoon
=>
::                                                      ::
::::  2: layer two                                      ::
```
...
```hoon
|%
::                                                      ::
::::  2a: unit logic                                    ::
  ::                                                    ::
  ::    biff, bind, bond, both, clap, drop,             ::
  ::    fall, flit, lift, mate, need, some              ::
  ::
++  biff                                                ::  apply
  |*  {a/(unit) b/$-(* (unit))}
  ?~  a  ~
  (b u.a)
```

If you counted the arms in this core by hand, you'll come up with 139
arms. This is also reflected in the dojo:

```hoon
> ..biff
<139.oyl 33.uof 1.pnw %138>
```

and we also see the section 1 core and the core containing
`hoon-version` in the subject.

We can also confirm that {% tooltip label="++add"
href="/language/hoon/reference/stdlib/1a#add" /%} is in the subject
of {% tooltip label="++biff" href="/language/hoon/reference/stdlib/2a#biff"
/%}

```hoon
> add:biff
<1.otf [[a=@ b=@] <33.uof 1.pnw %138>]>
```

and that `++biff` is not in the subject of `++add`.

```hoon
> biff:add
-find.biff
```

Lastly, let's check the subject of the last arm in `hoon.hoon` (as of
May 2024):

```hoon
> ..pi-tell
<77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
```

This confirms for us, then, that `hoon.hoon` consists of six nested
cores, with one inside the {% tooltip label="payload"
href="/glossary/payload" /%} of the next, with the `hoon-version` core
most deeply nested.

### Exercise:  Explore `hoon.hoon`

- Pick a couple of arms in `hoon.hoon` and check to make sure that they
  are only referenced in its parent {% tooltip label="core"
  href="/glossary/core" /%} or core(s) that have the parent core put in
  its context via the `=>` or `=<` runes.


### Axes of the Subject

The core {% tooltip label="Arvo" href="/glossary/arvo" /%} subject
exposes several axes (plural of `+$axis` which is the tree address) in
the {% tooltip label="subject" href="/glossary/subject" /%}.  You've
encountered these before:

- `our` is the {% tooltip label="ship's" href="/glossary/ship" /%}
  identity.

    ```hoon
    > -<..
    our=~nec
    ```

- `now` is 128-bit timestamp sourced from the wall clock time, Linux's
  `gettimeofday()`.

    ```hoon
    > ->-..
    now=~2022.6.22..20.41.18..82f4
    ```

- `eny` is 512 bits of entropy as `@uvJ`, sourced from a
  [CSPRNG](https://en.wikipedia.org/wiki/Cryptographically-secure_pseudorandom_number_generator)
  and hash-iterated using
  [`++shax`](/language/hoon/reference/stdlib/3d#shax).  (`eny` is shared
  between {% tooltip label="vanes" href="/glossary/vane" /%} during an
  event, so there are currently limits on how much it should be relied
  on until the Urbit kernel is security-hardened, but it is unique
  within each {% tooltip label="Gall" href="/glossary/gall" /%} agent
  activation.)

    ```hoon
    > ->+..
    eny
    0vmr.qobqc.fd9f0.h5hf4.dkurh.b4s37.lt4qf.2k505.j3sir.cnshk.ldpm0.jeppc.ti7gs.vtpru.u09sm.0imu0.cgdln.fvoqc.mt41e.3iga5.qpct7
    ```


##  State and Applications

Default Hoon expressions are stateless.  This means that they don't
really make reference to any other transactions or events in the system.
They don't preserve the results of previous calculations beyond their
own transient existence.

However, clearly regular applications, such as Gall {% tooltip
label="agents" href="/glossary/agent" /%}, are stateful, meaning that
they modify their own {% tooltip label="subject"
href="/glossary/subject" /%} regularly.

There are several ways to manage state.  One approach, including `%=` {%
tooltip label="centis" href="/language/hoon/reference/rune/cen#-centis"
/%}, directly modifies the subject using a {% tooltip label="rune"
href="/glossary/rune" /%}.  Another method is to use the other runes to
compose or sequence changes together (e.g. as a pipe of {% tooltip
label="gates" href="/glossary/gate" /%}).  By and large the `=` {%
tooltip label="tis" href="/language/hoon/reference/rune/tis" /%} runes
are responsible for modifying the subject, and the `;` {% tooltip
label="mic" href="/language/hoon/reference/rune/mic" /%} runes permit
chaining deferred computations together.

To act in a stateful manner, a core must mutate itself and then pin the
mutated copy in its place.  Most of the time this is handled by Arvo's
Gall {% tooltip label="vane" href="/glossary/vane" /%}, by the {%
tooltip label="Dojo" href="/glossary/dojo" /%}, or another system
service, but we need to explicit modify and manage state for cores as we
work within these kinds of applications.

We will use `%say` {% tooltip label="generators"
href="/glossary/generator" /%} as a bridge concept.  We will produce
some short applications that maintain state while carrying out a
calculation; they still result in a single return value, but gesture at
the big-picture approach to maintaining state in persistent {% tooltip
label="agents" href="/glossary/agent" /%}.

[As you may recall](/courses/hoon-school/J-stdlib-text), a `%say`
generator is like a naked generator except rather than being simply a {%
tooltip label="gate" href="/glossary/gate" /%}, it is a {% tooltip
label="cell" href="/glossary/cell" /%} of `%say` (as a tag) and a gate.
This gate can receive more information as gate arguments as part of its
`sample`, such as a timestamp `now`, some entropy `eny`, and a file
system beak `bec`. These allow us to think about how a core can modify
and maintain state. Although a `%say` generator, like all generators,
ultimately simply terminates, a Gall agent will be a persistent core
with state that can continue to be used.

Here are a couple of new runes for modifying the subject and chaining
computations together, aside from `%=` {% tooltip label="centis"
href="/language/hoon/reference/rune/cen#-centis" /%} which you've
already seen:

- `=.` {% tooltip label="tisdot"
  href="/language/hoon/reference/rune/tis#-tisdot" /%} is used to change
  a leg in the {% tooltip label="subject" href="/glossary/subject" /%}.
- `=~` {% tooltip label="tissig"
  href="/language/hoon/reference/rune/tis#-tissig" /%} composes many
  expressions together serially.

#### Tutorial:  Bank Account

In this section, we will write a {% tooltip label="door"
href="/glossary/door" /%} that can act as a bank account with the
ability to withdraw, deposit, and check the account's balance. This door
replaces the sample of the door with the new values as each transaction
proceeds.

```hoon {% copy=true mode="collapse" %}
:-  %say
|=  *
:-  %noun
=<  =~  new-account
      (deposit 100)
      (deposit 100)
      (withdraw 50)
      balance
    ==
|%
++  new-account
  |_  balance=@ud
  ++  deposit
    |=  amount=@ud
    +>.$(balance (add balance amount))
  ++  withdraw
    |=  amount=@ud
    +>.$(balance (sub balance amount))
  --
--
```

We start with the three boilerplate lines we have in every
`%say` {% tooltip label="generator" href="/glossary/generator" /%}:

```hoon {% copy=true %}
:-  %say
|=  *
:-  %noun
```

In the above code chunk, we're creating a {% tooltip label="cell"
href="/glossary/cell" /%}.  The head of this cell is `%say`.  The tail
is a {% tooltip label="gate" href="/glossary/gate" /%} (`|=  *`) that
produces another cell (`:- %noun`) with a head of the {% tooltip
label="mark" href="/glossary/mark" /%} of a the kind of data we are
going to produce, a `%noun`; the tail of the second cell is the rest of
the program.

```hoon {% copy=true %}
=<  =~  new-account
      (deposit 100)
      (deposit 100)
      (withdraw 50)
      balance
    ==
```

In this code above, we're going to compose two runes using `=<`, which
has inverted arguments. We use this rune to keep the heaviest twig to
the bottom of the code.

The `=~` {% tooltip label="tissig"
href="/language/hoon/reference/rune/tis#-tissig" /%} rune composes
multiple expressions together; we use it here to make the code more
readable.  We take `new-account` and use that as the subject for the
call to `deposit`.  `deposit` and `withdraw` both produce a new version
of the {% tooltip label="door" href="/glossary/door" /%} that's used in
subsequent calls, which is why we are able to chain them in this
fashion.  The final reference is to `balance`, which is the account
balance contained in the {% tooltip label="core" href="/glossary/core"
/%} that we examine below.

```hoon {% copy=true %}
|%
++  new-account
  |_  balance=@ud
  ++  deposit
    |=  amount=@ud
    +>.$(balance (add balance amount))
  ++  withdraw
    |=  amount=@ud
    +>.$(balance (sub balance amount))
  --
--
```

We've chosen here to wrap our {% tooltip label="door"
href="/glossary/door" /%} in its own core to emulate the style of
programming that is used when creating libraries.  `++new-account` is
the name of our door.  A door is a core with one or more arms that has a
sample.  Here, our door has a sample of one `@ud` with the face
`balance` and two {% tooltip label="arms" href="/glossary/arm" /%}
`++deposit` and `++withdraw`.

Each of these arms produces a {% tooltip label="gate"
href="/glossary/gate" /%} which takes an `@ud` argument.  Each of these
gates has a similar bit of code inside:

```hoon {% copy=true %}
+>.$(balance (add balance amount))
```

`+>` is a kind of wing syntax, lark notation.  This particular wing
construction looks for the tail of the tail (the third element) in `$`
buc, the {% tooltip label="subject" href="/glossary/subject" /%} of the
gate we are in.  The `++withdraw` and `++deposit` arms create gates with
the entire `new-account` door as the context in their cores' `[battery
sample context]`, in the "tail of the tail" slot.  We change `balance`
to be the result of adding `balance` and `amount` and produce the door
as the result.  `++withdraw` functions the same way only doing
subtraction instead of addition.

It's important to notice that the sample, `balance`, is stored as part
of the {% tooltip label="door" href="/glossary/door" /%} rather than
existing outside of it.

### Exercise:  Bank Account

- Modify the `%say` {% tooltip label="generator"
  href="/glossary/generator" /%} above to accept a `@ud` unsigned
  decimal dollar amount and a `?(%deposit %withdraw)` term and returns
  the result of only that operation on the starting balance of the bank
  account.  (Note that this will only work once on the {% tooltip
  label="door" href="/glossary/door" /%}, and the state will not persist
  between generator calls.)

### Deferred Computations

_Deferred computation_ means that parts of the {% tooltip
label="subject" href="/glossary/subject" /%} have changes that may be
underdetermined at first.  These must be calculated later using the
appropriate {% tooltip label="runes" href="/glossary/rune" /%} as new or
asynchronous information becomes available.

For instance, a network service call may take a while or may fail.  How
should the calculation deal with these outcomes?  In addition, the
successful result of the network data is unpredictable in content (but
should not be unpredictable in format!).

We have some more tools available for managing deferred or chained
computations, in addition to `=~` {% tooltip label="tissig"
href="/language/hoon/reference/rune/tis#-tissig" /%} and `=*` {% tooltip
label="tistar" href="/language/hoon/reference/rune/tis#-tistar" /%}:

- `=^` {% tooltip label="tisket"
  href="/language/hoon/reference/rune/tis#-tisket" /%} is used to change
  a leg in the tail of the {% tooltip label="subject"
  href="/glossary/subject" /%} then evaluate against it.  This is
  commonly used for events that need to be ordered in their resolution
  e.g. with a `%=` {% tooltip label="centis"
  href="/language/hoon/reference/rune/cen#-centis" /%}.  (Used in {%
  tooltip label="Gall" href="/glossary/gall" /%} agents frequently.)
- `=*` {% tooltip label="tistar"
  href="/language/hoon/reference/rune/tis#-tistar" /%} defers an
  expression (rather like a macro).
- `;<` {% tooltip label="micgal"
  href="/language/hoon/reference/rune/mic#-micgal" /%} sequences two
  computations, particularly for an asynchronous event like a remote
  system call.  (Used in {% tooltip label="threads"
  href="/glossary/thread" /%}.)
- `;~` {% tooltip label="micsig"
  href="/language/hoon/reference/rune/mic#-micsig" /%} produces a
  pipeline, a way of piping the output of one {% tooltip label="gate"
  href="/glossary/gate" /%} into another in a chain.  (This is
  particularly helpful when parsing text.)

### `++og` Randomness

A _random number generator_ provides a stream of calculable but
unpredictable values from some _distribution_.  In [a later
lesson](/courses/hoon-school/S-math), we explain how random numbers can
be generated from entropy; for now, let's see what's necessary to use
such a random-number generator.

An RNG emits a sequence of values given a starting _seed_.  For
instance, a very simple RNG could emit digits of the number _π_ given a
seed which is the number of digits to start from.

- seed 1:  1, 4, 1, 5, 9, 2, 6, 5, 3, 5
- seed 3:  1, 5, 9, 2, 6, 5, 3, 5, 8, 9
- seed 100:  8, 2, 1, 4, 8, 0, 8, 6, 5, 1

Every time you start this “random” number generator with a given seed,
it will reproduce the same sequence of numbers.

While RNGs don't work like our _π_-based example, a given seed will
reliably produce the same result every time it is run.

The basic RNG core in Hoon is {% tooltip label="++og"
href="/language/hoon/reference/stdlib/3d#og" /%}.  `++og` is a door
whose sample is its seed.  We need to use `eny` to seed it
non-deterministically, but we can also pin the state using `=^` {%
tooltip label="tisket" href="/language/hoon/reference/rune/tis#-tisket"
/%}. {% tooltip label="++rads:rng"
href="/language/hoon/reference/stdlib/3d#radsog" /%} produces a cell of
a random whole number in a given range and a new modified core to
continue the random sequence.

```hoon
> =+  rng=~(. og eny)
  [-:(rads:rng 100) -:(rads:rng 100)]
[60 60]
```

Since the `rng` starts from the same seed value every single time, both
of the numbers will always be the same.  What we have to do is pin the
updated version of the RNG (the tail of `++rads:og`'s return {% tooltip
label="cell" href="/glossary/cell" /%}) to the subject using `=^` {%
tooltip label="tisket" href="/language/hoon/reference/rune/tis#-tisket"
/%}, e.g.,

```hoon
> =/  rng  ~(. og eny)
  =^  r1  rng  (rads:rng 100)
  =^  r2  rng  (rads:rng 100)
  [r1 r2]
[21 47]
```

#### Tutorial:  Magic 8-Ball

The Magic 8-Ball returns one of a variety of answers in response to a
call.  In its entirety:

```hoon {% copy=true mode="collapse" %}
!:
:-  %say
|=  [[* eny=@uvJ *] *]
:-  %noun
^-  tape
=/  answers=(list tape)
  :~  "It is certain."
      "It is decidedly so."
      "Without a doubt."
      "Yes - definitely."
      "You may rely on it."
      "As I see it, yes."
      "Most likely."
      "Outlook good."
      "Yes."
      "Signs point to yes."
      "Reply hazy, try again"
      "Ask again later."
      "Better not tell you now."
      "Cannot predict now."
      "Concentrate and ask again."
      "Don't count on it."
      "My reply is no."
      "My sources say no."
      "Outlook not so good."
      "Very doubtful."
  ==
=/  rng  ~(. og eny)
=/  val  (rad:rng (lent answers))
(snag val answers)
```

Zoom in on these lines:

```hoon
=/  rng  ~(. og eny)
=/  val  (rad:rng (lent answers))
```

`~(. og eny)` starts a random number generator with a seed from the
current entropy.  A [random number
generator](https://en.wikipedia.org/wiki/Random_number_generation) is a
stateful mathematical function that produces an unpredictable result
(unless you know the algorithm AND the starting value, or seed).  Here
we pull the subject of {% tooltip label="++og"
href="/language/hoon/reference/stdlib/3d#og" /%}, the randomness {%
tooltip label="core" href="/glossary/core" /%} in Hoon, to start the
RNG.  An RNG like `++og` maintains its own state, but we will find that
we have to preserve state changes to continue to produce novel random
numbers.

We slam the `++rad:rng` gate which returns a random number from 0 to
_n_-1 inclusive.  This gives us a random value from the list of possible
answers.

```hoon
> +magic-8
"Ask again later."
```

##  Tutorial:  Dice Roll

Let's look at an example that uses all three parts. Save the code below
in a file called `dice.hoon` in the `/gen` directory of your
`%base` {% tooltip label="desk" href="/glossary/desk" /%}.

```hoon {% copy=true %}
:-  %say
|=  [[now=@da eny=@uvJ bec=beak] [n=@ud ~] [bet=@ud ~]]
:-  %noun
[(~(rad og eny) n) bet]
```

This is a very simple dice program with an optional betting
functionality. In the code, our sample specifies {% tooltip
label="faces" href="/glossary/face" /%} on all of the {% tooltip
label="Arvo" href="/glossary/arvo" /%} data, meaning that we can easily
access them. We also require the argument `[n=@ud ~]`, and allow the
_optional_ argument `[bet=@ud ~]`.

We can run this {% tooltip label="generator" href="/glossary/generator"
/%} like so:

```hoon
> +dice 6, =bet 2
[4 2]

> +dice 6
[5 0]

> +dice 6
[2 0]

> +dice 6, =bet 200
[0 200]

> +dice
nest-fail
```

We get a different value from the same generator between runs, something
that isn't possible with a naked generator. Another novelty is the
ability to choose to not use the second argument.

##  Scrying (In Brief)

A _peek_ or a {% tooltip label="scry" href="/glossary/scry" /%} is a
request to Arvo to tell you something about the state of part of the
Urbit OS.  Scries are used to determine the state of an agent or a vane.
The `.^` {% tooltip label="dotket"
href="/language/hoon/reference/rune/dot#-dotket" /%} rune sends the scry
request to a particular vane with a certain _care_ or type of scry.  The
request is then routed to a particular path in that {% tooltip
label="vane" href="/glossary/vane" /%}. Scries are discused in detail in
[App School](/courses/app-school/10-scry).  We will only briefly
introduce them here as we can use them later to find out about Arvo's
system state, such as file contents and {% tooltip label="agent"
href="/glossary/agent" /%} state.

### `%c` Clay

The {% tooltip label="Clay" href="/glossary/clay" /%} filesystem stores
nouns persistently at hierarchical path addresses.  These {% tooltip
label="nouns" href="/glossary/noun" /%} can be accessed using {% tooltip
label="marks" href="/glossary/mark" /%}, which are rules for structuring
the data.  We call the nouns “files” and the path addresses “folders”.

If we want to retrieve the contents of a file or folder, we can directly
ask Clay for the data using a {% tooltip label="scry"
href="/glossary/scry" /%} with an appropriate {% tooltip label="care"
href="/system/kernel/clay/reference/data-types#care" /%}.

For instance, the `%x` care to the `%c` Clay {% tooltip label="vane"
href="/glossary/vane" /%} returns the {% tooltip label="noun"
href="/glossary/noun" /%} at a given address as a `@` {% tooltip
label="atom" href="/glossary/atom" /%}.

```hoon
> .^(@ %cx /===/gen/hood/hi/hoon)
3.548.750.706.400.251.607.252.023.288.575.526.190.856.734.474.077.821.289.791.377.301.707.878.697.553.411.219.689.905.949.957.893.633.811.025.757.107.990.477.902.858.170.125.439.223.250.551.937.540.468.638.902.955.378.837.954.792.031.592.462.617.422.136.386.332.469.076.584.061.249.923.938.374.214.925.312.954.606.277.212.923.859.309.330.556.730.410.200.952.056.760.727.611.447.500.996.168.035.027.753.417.869.213.425.113.257.514.474.700.810.203.348.784.547.006.707.150.406.298.809.062.567.217.447.347.357.039.994.339.342.906
```

There are tools like `/lib/pretty-file/hoon` which will render this
legible to you by using formatted text `tank`s:

```hoon
> =pretty-file -build-file %/lib/pretty-file/hoon

> (pretty-file .^(noun %cx /===/gen/hood/hi/hoon))
~[
  [%leaf p="::  Helm: send message to an urbit"]
  [%leaf p="::"]
  [%leaf p="::::  /hoon/hi/hood/gen"]
  [%leaf p="  ::"]
  [%leaf p="/?    310"]
  [%leaf p=":-  %say"]
  [%leaf p="|=([^ [who=ship mez=$@(~ [a=tape ~])] ~] helm-send-hi+[who ?~(mez ~ `a.mez)])"]
]
```

Similarly, you can request the contents at a particular directory path:

```hoon
> .^(arch %cy /===/gen/hood)
[ fil=~
    dir
  { [p=~.resume q=~]
    [p=~.install q=~]
    [p=~.pass q=~]
    [p=~.doze q=~]
    ...
    [p=~.mount q=~]
  }
]
```

There are many more options with Clay than just accessing file and
folder data.  For instance, we can also scry all of the {% tooltip
label="desks" href="/glossary/desk" /%} on our current ship with the
`%d` care of `%c` Clay:

```hoon
> .^((set desk) %cd /=//=)
{%base %landscape %webterm %kids}
```

Other vanes have their own scry interfaces, which are well-documented in
[the Arvo docs](/system/kernel/arvo).


# P-stdlib-io.md

---

+++
title = "15. Text Processing II"
weight = 25
nodes = [185]
objectives = ["Identify tanks, tangs, wains, walls, and similar formatted printing data structures.", "Interpret logging message structures (`%leaf`, `$rose`, `$palm`).", "Interpolate to tanks with `><` syntax.", "Produce useful error annotations using `~|` sigbar."]
+++

_This module will elaborate on text representation in Hoon, including
formatted text and `%ask` {% tooltip label="generators"
href="/glossary/generator" /%}.  It may be considered optional and
skipped if you are speedrunning Hoon School._


##  Text Conversions

We frequently need to convert from text to data, and between different
text-based representations.  Let's examine some specific {% tooltip
label="arms" href="/glossary/arm" /%}:

- How do we convert text into all lower-case?
    - {% tooltip label="++cass" href="/language/hoon/reference/stdlib/4b#cass" /%}

- How do we turn a `cord` into a {% tooltip label="tape"
  href="/glossary/tape" /%}?
    - {% tooltip label="++trip" href="/language/hoon/reference/stdlib/4b#trip" /%}

- How can we make a {% tooltip label="list" href="/glossary/list" /%} of
  a null-terminated tuple?
    - {% tooltip label="++le:nl" href="/language/hoon/reference/stdlib/2m#lenl" /%}

- How can we evaluate {% tooltip label="Nock" href="/glossary/nock" /%} expressions?
    - {% tooltip label="++mink" href="/language/hoon/reference/stdlib/4n#mink" /%}

(If you see a `|*` {% tooltip label="bartar"
href="/language/hoon/reference/rune/bar#-bartar" /%} rune in the code,
it's similar to a `|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%}, but produces
what's called a [_wet gate_](/courses/hoon-school/R-metals).)

The `++html` core of the standard libary contains some additional
important tools for working with web-based data, such as [MIME
types](https://en.wikipedia.org/wiki/Media_type) and [JSON
strings](https://en.wikipedia.org/wiki/JSON).

- To convert a `@ux` hexadecimal value to a `cord`:

    ```hoon
    > (en:base16:mimes:html [3 0x12.3456])  
    '123456'
    ```

- To convert a `cord` to a `@ux` hexadecimal value:

    ```hoon
    > `@ux`q.+>:(de:base16:mimes:html '123456')
    0x12.3456
    ```

- There are tools for working with Bitcoin wallet base-58 values, JSON
  strings, XML strings, and more.

    ```hoon
    > (en-urlt:html "https://hello.me")
    "https%3A%2F%2Fhello.me"
    ```


##  Formatted Text

Hoon produces messages at the {% tooltip label="Dojo"
href="/glossary/dojo" /%} (or otherwise) using an internal formatted
text system, called `tank`s.  A `+$tank` is a formatted print tree.
Error messages and the like are built of `tank`s.  `tank`s are defined
in `hoon.hoon`:

```hoon
::  $tank: formatted print tree
::
::    just a cord, or
::    %leaf: just a tape
::    %palm: backstep list
::           flat-mid, open, flat-open, flat-close
::    %rose: flat list
::           flat-mid, open, close
::
+$  tank
  $~  leaf/~
  $@  cord
  $%  [%leaf p=tape]
      [%palm p=(qual tape tape tape tape) q=(list tank)]
      [%rose p=(trel tape tape tape) q=(list tank)]
  ==
+$ tang (list tank) :: bottom-first error
```

The {% tooltip label="++ram:re"
href="/language/hoon/reference/stdlib/4c#ramre" /%} arm is used to
convert these to actual formatted output as a {% tooltip label="tape"
href="/glossary/tape" /%}, e.g.

```hoon
> ~(ram re leaf+"foo")
"foo"
> ~(ram re [%palm ["|" "(" "!" ")"] leaf+"foo" leaf+"bar" leaf+"baz" ~])
"(!foo|bar|baz)"
> ~(ram re [%rose [" " "[" "]"] leaf+"foo" leaf+"bar" leaf+"baz" ~])
"[foo bar baz]"
```

Many {% tooltip label="generators" href="/glossary/generator" /%} build
sophisticated output using `tank`s and the short-format {% tooltip
label="cell" href="/glossary/cell" /%} builder `+`, e.g. in
`/gen/azimuth-block/hoon`:

```hoon {% copy=true %}
[leaf+(scow %ud block)]~
```

which is equivalent to

```hoon {% copy=true %}
~[[%leaf (scow %ud block)]]
```

`tank`s are the primary output mechanism for more advanced generators.
Even if you don't end up writing them much, you will encounter them as
you delve into the Urbit codebase.

#### Tutorial:  Deep Dive into `ls.hoon`

The {% tooltip label="+ls" href="/manual/os/dojo-tools#ls" /%} generator
shows the contents at a particular path in {% tooltip label="Clay"
href="/glossary/clay" /%}:

```hoon
> +cat /===/gen/ls/hoon
/~nec/base/~2022.6.22..17.25.54..1034/gen/ls/hoon
::  LiSt directory subnodes
::
::::  /hoon/ls/gen
  ::
/?    310
/+    show-dir
::
::::
  ::
~&  %
:-  %say
|=  [^ [arg=path ~] vane=?(%g %c)]
=+  lon=.^(arch (cat 3 vane %y) arg)
tang+[?~(dir.lon leaf+"~" (show-dir vane arg dir.lon))]~
```

Let's go line by line:

```hoon
/?    310
/+    show-dir
```

The first line `/?` faswut represents now-future functionality which
will allow the version number of the kernel to be pinned.  It is
currently non-functioning but you will see it in many Urbit-shipped
files.

Then the `show-dir` library is imported.

```hoon
~&  %
```

A separator `%` is printed.

```hoon
:-  %say
```

A `%say` {% tooltip label="generator" href="/glossary/generator" /%} is
a cell with a metadata tag `%say` as the head and the {% tooltip
label="gate" href="/glossary/gate" /%} as the tail.

```hoon
|=  [^ [arg=path ~] vane=?(%g %c)]
```

This generator requires a path argument in its sample and optionally
accepts a {% tooltip label="vane" href="/glossary/vane" /%} tag (`%g` {%
tooltip label="Gall" href="/glossary/gall" /%} or `%c` {% tooltip
label="Clay" href="/glossary/clay" /%}).  Most of the time, {% tooltip
label="+cat" href="/manual/os/dojo-tools#cat" /%} is used with Clay, so
`%c` as the last entry in the type union serves as the {% tooltip
label="bunt" href="/glossary/bunt" /%} value.

```hoon
=+  lon=.^(arch (cat 3 vane %y) arg)
```

We saw `.^` {% tooltip label="dotket"
href="/language/hoon/reference/rune/dot#-dotket" /%} for the first time
in [the previous module](/courses/hoon-school/O-subject), where we
learned that it performs a _peek_ or {% tooltip label="scry"
href="/glossary/scry" /%} into the state of an Arvo {% tooltip
label="vane" href="/glossary/vane" /%}.  Most of the time this
functionality is used to ask `%c` {% tooltip label="Clay"
href="/glossary/clay" /%} or `%g` {% tooltip label="Gall"
href="/glossary/gall" /%} for information about a path, {% tooltip
label="desk" href="/glossary/desk" /%}, {% tooltip label="agent"
href="/glossary/agent" /%}, etc.  In this case, `(cat 3 %c %y)` is a
fancy way of collocating the two `@tas` terms into `%cy`, a Clay file or
directory lookup.  The type of this lookup is `+$arch`, and the location
of the file or directory is given by `arg` from the sample.

```hoon
tang+[?~(dir.lon leaf+"~" (show-dir vane arg dir.lon))]~
```

The result of the lookup on the previous line is adapted into a
formatted text block with a head of `%tang` and different results
depending on whether the request was `~` null or not.

#### Tutorial:  Deep Dive into `cat.hoon`

For instance, how does {% tooltip label="+cat"
href="/manual/os/dojo-tools#cat" /%} work?  Let's look at the structure
of `/gen/cat/hoon`:

```hoon {% copy=true mode="collapse" %}
::  ConCATenate file listings
::
::::  /hoon/cat/gen
  ::
/?    310
/+    pretty-file, show-dir
::
::::
  ::
:-  %say
|=  [^ [arg=(list path)] vane=?(%g %c)]
=-  tang+(flop `tang`(zing -))
%+  turn  arg
|=  pax=path
^-  tang
=+  ark=.^(arch (cat 3 vane %y) pax)
?^  fil.ark
  ?:  =(%sched -:(flop pax))
    [>.^((map @da cord) (cat 3 vane %x) pax)<]~
  [leaf+(spud pax) (pretty-file .^(noun (cat 3 vane %x) pax))]
?-     dir.ark                                          ::  handle ambiguity
    ~
  [rose+[" " `~]^~[leaf+"~" (smyt pax)]]~
::
    [[@t ~] ~ ~]
  $(pax (welp pax /[p.n.dir.ark]))
::
    *
  =-  [palm+[": " ``~]^-]~
  :~  rose+[" " `~]^~[leaf+"*" (smyt pax)]
      `tank`(show-dir vane pax dir.ark)
  ==
==
```

- What is the top-level structure of the {% tooltip label="generator"
  href="/glossary/generator" /%}?  (A {% tooltip label="cell"
  href="/glossary/cell" /%} of `%say` and the {% tooltip label="gate"
  href="/glossary/gate" /%}, what Dojo recognizes as a `%say`
  generator.)

- Some points of interest include:
  - `/?` faswut pins the expected Arvo {% tooltip label="kelvin version"
    href="/glossary/kelvin" /%}; right now it doesn't do anything.
  - `.^` {% tooltip label="dotket"
    href="/language/hoon/reference/rune/dot#-dotket" /%} loads a value
    from Arvo (called a {% tooltip label="\"scry\""
    href="/glossary/scry" /%}).
  - {% tooltip label="++smyt" href="/language/hoon/reference/stdlib/4m#smyt" /%}
    pretty-prints a path.
  - `=-` {% tooltip label="tishep"
    href="/language/hoon/reference/rune/tis#--tishep" /%} combines a {%
    tooltip label="faced" href="/glossary/face" /%} noun with the {%
    tooltip label="subject" href="/glossary/subject" /%}, inverted
    relative to `=+` {% tooltip label="tislus"
    href="/language/hoon/reference/rune/tis#-tislus" /%}/`=/` {% tooltip
    label="tisfas" href="/language/hoon/reference/rune/tis#-tisfas" /%}.

You can see how much of the generator is concerned with formatting the
content of the file into a formatted text `tank` by prepending `%rose`
tags and so forth.

- Work line-by-line through the file and clarify parts that are muddy to
  you at first glance.

### Producing Error Messages

Formal error messages in Urbit are built of tanks.  “A `tang` is a {%
tooltip label="list" href="/glossary/list" /%} of `tank`s, and a `tank`
is a structure for printing data.  There are three types of `tank`:
`leaf`, `palm`, and `rose`.  A `leaf` is for printing a single noun, a
`rose` is for printing rows of data, and a `palm` is for printing
backstep-indented lists.”

One way to include an error message in your code is the `~_` {% tooltip
label="sigcab" href="/language/hoon/reference/rune/sig#_-sigcab" /%}
rune, described as a “user-formatted tracing printf”, or the `~|` {%
tooltip label="sigbar" href="/language/hoon/reference/rune/sig#-sigbar"
/%} rune, a “tracing printf”.  What this means is that these print to
the stack trace if something fails, so you can use either {% tooltip
label="rune" href="/glossary/rune" /%} to contribute to the error
description:

```hoon {% copy=true %}
|=  a=@ud
~_  leaf+"This code failed"
!!
```

When you compose your own library functions, consider including error
messages for likely failure points.


##  `%ask` Generators

Previously, we introduced the concept of a `%say` {% tooltip
label="generator" href="/glossary/generator" /%} to produce a more
versatile form of standalone single computation than a simple naked
generator ({% tooltip label="gate" href="/glossary/gate" /%}) allowed.
Another elaboration, the `%ask` generator, takes things further.

We use an `%ask` generator when we want to create an interactive program
that prompts for inputs as it runs, rather than expecting arguments to
be passed in at the time of initiation.

This section will briefly walk through an `%ask` generator to give you a
taste of how they work.  The [CLI app
guide](/userspace/apps/guides/cli-tutorial) walks through the libraries
necessary for working with `%ask` generators in greater detail.  We also
recommend reading [~wicdev-wisryt's “Input and Output in
Hoon”](https://urbit.org/blog/io-in-hoon) for an extended consideration
of relevant input/output issues.

##### Tutorial:  `%ask` Generator

The code below is an `%ask` {% tooltip label="generator"
href="/glossary/generator" /%} that checks if the user inputs `"blue"`
when prompted [per a classic Monty Python
scene](https://www.youtube.com/watch?v=L0vlQHxJTp0).  Save it as
`/gen/axe.hoon` in your `%base` {% tooltip label="desk"
href="/glossary/desk" /%}.

```hoon {% copy=true mode="collapse" %}
/-  sole
/+  generators
=,  [sole generators]
:-  %ask
|=  *
^-  (sole-result (cask tang))
%+  print    leaf+"What is your favorite color?"
%+  prompt   [%& %prompt "color: "]
|=  t=tape
%+  produce  %tang
?:  =(t "blue")
  :~  leaf+"Oh. Thank you very much."
      leaf+"Right. Off you go then."
  ==
:~  leaf+"Aaaaagh!"
    leaf+"Into the Gorge of Eternal Peril with you!"
==
```

Run the generator from the {% tooltip label="Dojo" href="/glossary/dojo"
/%}:

```hoon
> +axe

What is your favorite color?
: color:
```

Something new has happened.  Instead of simply returning something, your
Dojo's prompt changed from `~your-urbit:dojo>` to `~your-urbit:dojo:
color:`, and now expects additional input.  Let's give it an answer:

```hoon
: color: red
Into the Gorge of Eternal Peril with you!
Aaaaagh!
```

Let's go over what exactly is happening in this code.

```hoon
/-  sole
/+  generators
=,  [sole generators]
```

Here we bring in some of the types we are going to need from `/sur/sole`
and gates we will use from `/lib/generators`. We use some special {%
tooltip label="runes" href="/glossary/rune" /%} for this.

- `/-` {% tooltip label="fashep"
  href="/language/hoon/reference/rune/fas#--fashep" /%} is a Ford rune
  used to import types from `/sur`.
- `/+` {% tooltip label="faslus"
  href="/language/hoon/reference/rune/fas#-faslus" /%} is a Ford rune
  used to import libraries from `/lib`.
- `=,` {% tooltip label="tiscom"
  href="/language/hoon/reference/rune/tis#-tiscol" /%} is a rune that
  allows us to expose a namespace. We do this to avoid having to write
  `sole-result:sole` instead of `sole-result` or `print:generators`
  instead of `print`.

```hoon
:-  %ask
|=  *
```

This code might be familiar. Just as with their `%say` cousins, `%ask`
generators need to produce a `cell`, the head of which specifies what
kind of generator we are running.

With `|= *`, we create a {% tooltip label="gate" href="/glossary/gate"
/%} and ignore the standard arguments we are given, because we're not
using them.

```hoon
^-  (sole-result (cask tang))
```

`%ask` {% tooltip label="generators" href="/glossary/generator" /%} need
to have the second half of the {% tooltip label="cell"
href="/glossary/cell" /%} be a gate that produces a `sole-result`, one
that in this case contains a `cask` of `tang`.  We use the `^-` {%
tooltip label="kethep" href="/language/hoon/reference/rune/ket#--kethep"
/%} rune to constrain the generator's output to such a `sole-result`.

A `cask` is a pair of a {% tooltip label="mark" href="/glossary/mark"
/%} name and a {% tooltip label="noun" href="/glossary/noun" /%}.  We
previously described a `mark` as a kind of complicated {% tooltip
label="mold" href="/glossary/mold" /%}; here we add that a `mark` can be
thought of as an Arvo-level [MIME](https://en.wikipedia.org/wiki/MIME)
type for data.

A `tang` is a {% tooltip label="list" href="/glossary/list" /%} of
`tank`, and a `tank` is a structure for printing data, as described
above.  There are three types of `tank`: `leaf`, `palm`, and `rose`.  A
`leaf` is for printing a single noun, a `rose` is for printing rows of
data, and a `palm` is for printing backstep-indented lists.

```hoon
%+  print    leaf+"What is your favorite color?"
%+  prompt   [%& %prompt "color: "]
|=  t=tape
%+  produce  %tang
```

Because we imported {% tooltip label="generators"
href="/glossary/generator" /%}, we can access its contained gates, three
of which we use in `axe.hoon`: `++print`, `++prompt`, and `++produce`.

- `print` is used for printing a `tank` to the console.

    In our example, `%+` {% tooltip label="cenlus"
    href="/language/hoon/reference/rune/cen#-cenlus" /%} is used to call
    the gate `++print`, with two arguments. The first argument is a
    `tank` to print.  The `+` here is syntactic sugar for `[%leaf "What
    is your favorite color?"]` that just makes it easier to write. The
    second argument is the output of the call to `++prompt`.

- `prompt` is used to construct a prompt for the user to provide input.
  The first argument is a tuple. The second argument is a gate that
  returns the output of a call to `++produce`. Most `%ask` generators
  will want to use the `++prompt` gate.

    The first element of the `++prompt` tuple/sample is a flag that
    indicates whether what the user typed should be echoed out to them
    or hidden. `%&` will produce echoed output and `%|` will hide the
    output (for use in passwords or other secret text).

    The second element of the `++prompt` sample is intended to be
    information for use in creating autocomplete options for the prompt.
    This functionality is not yet implemented.

    The third element of the `++prompt` sample is the {% tooltip
    label="tape" href="/glossary/tape" /%} that we would like to use to
    prompt the user. In the case of our example, we use `"color: "`.

- `produce` is used to construct the output of the generator. In our
  example, we produce a `tang`.

```hoon
|=  t=tape
```

Our gate here takes a `tape` that was produced by `++prompt`.  If we
needed another type of data we could use `++parse` to obtain it.

The rest of this generator should be intelligible to those with Hoon
knowledge at this point.

One quirk that you should be aware of, though, is that `tang` prints in
reverse order from how it is created.  The reason for this is that
`tang` was originally created to display stack trace information, which
should be produced in reverse order.  This leads to an annoyance: we
either have to specify our messages backwards or construct them in the
order we want and then {% tooltip label="++flop"
href="/language/hoon/reference/stdlib/2b#flop" /%} the `list`.


# Q-func.md

---

+++
title = "16. Functional Programming"
weight = 26
nodes = [233]
objectives = ["Reel, roll, turn a list.", "Curry, cork functions.", "Change arity of a gate.", "Tokenize text simply using `find` and `trim`.", "Identify elements of parsing:  `nail`, `rule`, etc.", "Use `++scan` to parse `tape` into atoms.", "Construct new rules and parse arbitrary text fields."]
+++

_This module will discuss some gates-that-work-on-gates and other
assorted operators that are commonly recognized as functional
programming tools._

Given a {% tooltip label="gate" href="/glossary/gate" /%}, you can
manipulate it to accept a different number of values than its sample
formally requires, or otherwise modify its behavior.  These techniques
mirror some of the common tasks used in other [functional programming
languages](https://en.wikipedia.org/wiki/Functional_programming) like
Haskell, Clojure, and OCaml.

Functional programming, as a paradigm, tends to prefer rather
mathematical expressions with explicit modification of function
behavior.  It works as a formal system of symbolic expressions
manipulated according to given rules and properties.  FP was derived
from the [lambda
calculus](https://en.wikipedia.org/wiki/Lambda_calculus), a cousin of
combinator calculi like {% tooltip label="Nock" href="/glossary/nock"
/%}.  (See also
[APL](https://en.wikipedia.org/wiki/APL_%28programming_language%29).)

##  Changing Arity

If a gate accepts only two values in its sample, for instance, you can
chain together multiple calls automatically using the `;:` {% tooltip
label="miccol" href="/language/hoon/reference/rune/mic#-miccol" /%}
rune.

```hoon
> (add 3 (add 4 5))
12

> :(add 3 4 5)
12

> (mul 3 (mul 4 5))
60

> :(mul 3 4 5)
60
```

This is called changing the
[_arity_](https://en.wikipedia.org/wiki/Arity) of the gate.  (Does this
work on {% tooltip label="++mul:rs"
href="/language/hoon/reference/stdlib/3b#mulrs" /%}?)


##  Binding the Sample

[_Currying_](https://en.wikipedia.org/wiki/Currying) describes taking a
function of multiple arguments and reducing it to a set of functions
that each take only one argument.  _Binding_, an allied process, is used
to set the value of some of those arguments permanently.

If you have a {% tooltip label="gate" href="/glossary/gate" /%} which
accepts multiple values in the {% tooltip label="sample"
href="/glossary/sample" /%}, you can fix one of these.  To fix the head
of the sample (the first argument), use {% tooltip label="++cury"
href="/language/hoon/reference/stdlib/2n#cury" /%}; to bind the tail,
use [`++curr`](/language/hoon/reference/stdlib/2n#curr).

Consider calculating _a x² + b x + c_, a situation we earlier resolved
using a door.  We can resolve the situation differently using currying:

```hoon
> =full |=([x=@ud a=@ud b=@ud c=@ud] (add (add (mul (mul x x) a) (mul x b)) c))

> (full 5 4 3 2)
117

> =one (curr full [4 3 2])  

> (one 5)  
117
```

One can also {% tooltip label="++cork"
href="/language/hoon/reference/stdlib/2n#cork" /%} a gate, or arrange it
such that it applies to the result of the next gate.  This pairs well
with `;:` {% tooltip label="miccol"
href="/language/hoon/reference/rune/mic#-miccol" /%}.  (There is
also {% tooltip label="++corl"
href="/language/hoon/reference/stdlib/2n#corl" /%}, which composes
backwards rather than forwards.) This example decrements a value then
converts it to `@ux` by corking two gates:

```hoon
> ((cork dec @ux) 20)  
0x13
```

### Exercise:  Bind Gate Arguments

- Create a gate `++inc` which increments a value in one step, analogous
  to {% tooltip label="++dec"
  href="/language/hoon/reference/stdlib/1a#dec" /%}.

### Exercise:  Chain Gate Values

- Write an expression which yields the parent {% tooltip label="galaxy"
  href="/glossary/galaxy" /%} of a {% tooltip label="planet's"
  href="/glossary/planet" /%} sponsoring {% tooltip label="star"
  href="/glossary/star" /%} by composing two gates.

##  Working Across `list`s

The {% tooltip label="++turn"
href="/language/hoon/reference/stdlib/2b#turn" /%} function takes a list
and a {% tooltip label="gate" href="/glossary/gate" /%}, and returns a
list of the products of applying each item of the input list to the
gate. For example, to add 1 to each item in a list of {% tooltip
label="atoms" href="/glossary/atom" /%}:

```hoon
> (turn `(list @)`~[11 22 33 44] |=(a=@ +(a)))
~[12 23 34 45]
```
Or to double each item in a {% tooltip label="list"
href="/glossary/list" /%} of atoms:

```hoon
> (turn `(list @)`~[11 22 33 44] |=(a=@ (mul 2 a)))
~[22 44 66 88]
```
`++turn` is Hoon's version of Haskell's map.

We can rewrite the Caesar cipher program using turn:

```hoon {% copy=true %}
|=  [a=@ b=tape]
^-  tape
?:  (gth a 25)
  $(a (sub a 26))
%+  turn  b
|=  c=@tD
?:  &((gte c 'A') (lte c 'Z'))
  =.  c  (add c a)
  ?.  (gth c 'Z')  c
  (sub c 26)
?:  &((gte c 'a') (lte c 'z'))
  =.  c  (add c a)
  ?.  (gth c 'z')  c
  (sub c 26)
c
```

{% tooltip label="++roll" href="/language/hoon/reference/stdlib/2b#roll" /%} and
{% tooltip label="++reel" href="/language/hoon/reference/stdlib/2b#reel" /%} are used to
left-fold and right-fold a {% tooltip label="list" href="/glossary/list"
/%}, respectively.  To fold a list is similar to {% tooltip
label="++turn" href="/language/hoon/reference/stdlib/2b#turn" /%},
except that instead of yielding a `list` with the values having had each
applied, `++roll` and `++reel` produce an accumulated value.

```hoon
> (roll `(list @)`[1 2 3 4 5 ~] add)
15

> (reel `(list @)`[1 2 3 4 5 ~] mul)
120
```

### Exercise:  Calculate a Factorial

- Use `++reel` to produce a {% tooltip label="gate"
  href="/glossary/gate" /%} which calculates the factorial of a number.


##  Classic Operations

Functional programmers frequently rely on three design patterns to
produce operations on collections of data:

1. Map.  The Map operation describes applying a function to each item of
   a set or iterable object, resulting in the same final number of items
   transformed.  In Hoon terms, we would say slamming a gate on each
   member of a `list` or `set`.  The standard library arms that
   accomplish this include {% tooltip label="++turn"
   href="/language/hoon/reference/stdlib/2b#turn" /%} for a {% tooltip
   label="list" href="/glossary/list" /%}, {% tooltip label="++run:in"
   href="/language/hoon/reference/stdlib/2h#repin" /%} for a {% tooltip
   label="set" href="/language/hoon/reference/stdlib/2o#set" /%}, and {%
   tooltip label="++run:by"
   href="/language/hoon/reference/stdlib/2i#runby" /%} for a {% tooltip
   label="map" href="/language/hoon/reference/stdlib/2o#map" /%}.

2. Reduce.  The Reduce operation applies a function as a sequence of
   pairwise operations to each item, resulting in one summary value. The
   standard library {% tooltip label="arms" href="/glossary/arm" /} that
   accomplish this are {% tooltip label="++roll"
   href="/language/hoon/reference/stdlib/2b#roll" /%} and {% tooltip
   label="++reel" href="/language/hoon/reference/stdlib/2b#reel" /%} for
   a {% tooltip label="list" href="/glossary/list" /%}, {% tooltip
   label="++rep:in" href="/language/hoon/reference/stdlib/2h#repin" /%}
   for a {% tooltip label="set"
   href="/language/hoon/reference/stdlib/2o#set" /%}, and {% tooltip
   label="++rep:by" href="/language/hoon/reference/stdlib/2i#repby" /%}
   for a {% tooltip label="map"
   href="/language/hoon/reference/stdlib/2o#map" /%}.

3. Filter.  The Filter operation applies a true/false function to each
   member of a collection, resulting in some number of items equal to or
   fewer than the size of the original set.  In Hoon, the library arms
   that carry this out include {% tooltip label="++skim"
   href="/language/hoon/reference/stdlib/2b#skim" /%}, {% tooltip
   label="++skid" href="/language/hoon/reference/stdlib/2b#skid" /%}, {%
   tooltip label="++murn" href="/language/hoon/reference/stdlib/2b#murn"
   /%} for a {% tooltip label="list" href="/glossary/list" /%}, and {%
   tooltip label="++rib:by"
   href="/language/hoon/reference/stdlib/2i#ribby" /%} for a {% tooltip
   label="map" href="/language/hoon/reference/stdlib/2o#map" /%}.


# Q2-parsing.md

---

+++
title = "17. Text Processing III"
weight = 27
nodes = [283, 383]
objectives = ["Tokenize text simply using `find` and `trim`.", "Identify elements of parsing:  `nail`, `rule`, etc.", "Use `++scan` to parse `tape` into atoms.", "Construct new rules and parse arbitrary text fields."]
+++

_This module covers text parsing.  It may be considered optional and
skipped if you are speedrunning Hoon School._

We need to build a tool to accept a {% tooltip label="tape"
href="/glossary/tape" /%} containing some characters, then turn it into
something else, something computational.

For instance, a calculator could accept an input like `3+4` and return
`7`.  A command-line interface may look for a program to evaluate (like
Bash and `ls`).  A search bar may apply logic to the query (like Google
and `-` for `NOT`).

The basic problem all parsers face is this:

1. You need to accept a character string.
2. You need to ingest one or more characters and decide what they
   “mean”, including storing the result of this meaning.
3. You need to loop back to #1 again and again until you are out of
   characters.

## The Hoon Parser

We could build a simple parser out of a {% tooltip label="trap"
href="/glossary/trap" /%} and {% tooltip label="++snag"
href="/language/hoon/reference/stdlib/2b#snag" /%}, but it would be
brittle and difficult to extend.  The Hoon parser is very sophisticated,
since it has to take a file of ASCII characters (and some UTF-8 strings)
and turn it via an AST into {% tooltip label="Nock"
href="/glossary/nock" /%} code.  What makes parsing challenging is that
we have to wade directly into a sea of new types and processes.  To wit:

-   A {% tooltip label="tape" href="/glossary/tape" /%} is the string to
    be parsed.
-   A `hair` is the position in the text the parser is at, as a cell of
    column & line, `[p=@ud q=@ud]`.
-   A `nail` is parser input, a cell of `hair` and `tape`.
-   An `edge` is parser output, a cell of `hair` and a `unit` of `hair`
    and `nail`.  (There are some subtleties around failure-to-parse here
    that we'll defer a moment.)
-   A `rule` is a parser, a gate which applies a `nail` to yield an
    `edge`.

Basically, one uses a `rule` on `[hair tape]` to yield an `edge`.

A substantial swath of the standard library is built around parsing for
various scenarios, and there's a lot to know to effectively use these
tools.  **If you can parse arbitrary input using Hoon after this lesson,
you're in fantastic shape for building things later.**  It's worth
spending extra effort to understand how these programs work.

There is a [full guide on parsing](/language/hoon/guides/parsing) which
goes into more detail than this quick overview.

## Scanning Through a `tape`

{% tooltip label="++scan" href="/language/hoon/reference/stdlib/4g#scan" /%} parses
a `tape` or crashes, simple enough.  It will be our workhorse.  All we
really need to know in order to use it is how to build a `rule`.

Here we will preview using {% tooltip label="++shim"
href="/language/hoon/reference/stdlib/4f#shim" /%} to match characters
with in a given range, here lower-case.  If you change the character
range, e.g. putting `' '` in the `++shim` will span from ASCII `32`, `'
'` to ASCII `122`, `'z'`.

```hoon
> `(list)`(scan "after" (star (shim 'a' 'z')))  
~[97 102 116 101 114]  

> `(list)`(scan "after the" (star (shim 'a' 'z')))
{1 6}  
syntax error  
dojo: hoon expression failed
```

## `rule` Building

The `rule`-building system is vast and often requires various components
together to achieve the desired effect.

### `rule`s to parse fixed strings

- {% tooltip label="++just" href="/language/hoon/reference/stdlib/4f#just" /%} takes
  in a single `char` and produces a `rule` that attempts to match that
  `char` to the first character in the `tape` of the input `nail`.

    ```hoon
    > ((just 'a') [[1 1] "abc"])
    [p=[p=1 q=2] q=[~ [p='a' q=[p=[p=1 q=2] q="bc"]]]]
    ```

- {% tooltip label="++jest" href="/language/hoon/reference/stdlib/4f#jest" /%} matches
  a `cord`. It takes an input `cord` and produces a `rule` that
  attempts to match that `cord` against the beginning of the input.

    ```hoon
    > ((jest 'abc') [[1 1] "abc"])
    [p=[p=1 q=4] q=[~ [p='abc' q=[p=[p=1 q=4] q=""]]]]

    > ((jest 'abc') [[1 1] "abcabc"])
    [p=[p=1 q=4] q=[~ [p='abc' q=[p=[p=1 q=4] q="abc"]]]]
    
    > ((jest 'abc') [[1 1] "abcdef"])
    [p=[p=1 q=4] q=[~ [p='abc' q=[p=[p=1 q=4] q="def"]]]]
    ```

    (Keep an eye on the structure of the return `edge` there.)

- {% tooltip label="++shim" href="/language/hoon/reference/stdlib/4f#shim" /%} parses
  characters within a given range. It takes in two atoms and returns a `rule`.

    ```hoon
    > ((shim 'a' 'z') [[1 1] "abc"])
    [p=[p=1 q=2] q=[~ [p='a' q=[p=[p=1 q=2] q="bc"]]]]
    ```

- {% tooltip label="++next" href="/language/hoon/reference/stdlib/4f#next" /%} is
  a simple `rule` that takes in the next character and returns it as the parsing result.

    ```hoon
    > (next [[1 1] "abc"])
    [p=[p=1 q=2] q=[~ [p='a' q=[p=[p=1 q=2] q="bc"]]]]
    ```

### `rule`s to parse flexible strings

So far we can only parse one character at a time, which isn't much
better than just using {% tooltip label="++snag"
href="/language/hoon/reference/stdlib/2b#snag" /%} in a {% tooltip
label="trap" href="/glossary/trap" /%}.

```hoon
> (scan "a" (shim 'a' 'z'))  
'a'  

> (scan "ab" (shim 'a' 'z'))  
{1 2}  
syntax error  
dojo: hoon expression failed
```

How do we parse multiple characters in order to break things up
sensibly?

- {% tooltip label="++star" href="/language/hoon/reference/stdlib/4f#star" /%} will
  match a multi-character list of values.

    ```hoon
    > (scan "a" (just 'a'))
    'a'

    > (scan "aaaaa" (just 'a'))
    ! {1 2}
    ! 'syntax-error'
    ! exit

    > (scan "aaaaa" (star (just 'a')))
    "aaaaa"
    ```

- {% tooltip label="++plug" href="/language/hoon/reference/stdlib/4e#plug" /%} takes
  the `nail` in the `edge` produced by one rule and passes it to the
  next `rule`, forming a {% tooltip label="cell" href="/glossary/cell"
  /%} of the results as it proceeds.

    ```hoon
    > (scan "starship" ;~(plug (jest 'star') (jest 'ship')))
    ['star' 'ship']
    ```

- {% tooltip label="++pose" href="/language/hoon/reference/stdlib/4e#pose" /%} tries
    each `rule` you hand it successively until it finds one that works.

    ```hoon
    > (scan "a" ;~(pose (just 'a') (just 'b')))
    'a'
    
    > (scan "b" ;~(pose (just 'a') (just 'b')))
    'b'
    
    > (;~(pose (just 'a') (just 'b')) [1 1] "ab")
    [p=[p=1 q=2] q=[~ u=[p='a' q=[p=[p=1 q=2] q=[i='b' t=""]]]]]
    ```

- {% tooltip label="++glue" href="/language/hoon/reference/stdlib/4e#glue" /%} parses
  a delimiter (a `rule`) in between each `rule` and forms a {% tooltip
  label="cell" href="/glossary/cell" /%} of the results of each
  non-delimiter `rule`.  Delimiters representing each symbol used in
  Hoon are named according to their [aural ASCII](/glossary/aural-ascii)
  pronunciation. Sets of characters can also be used as delimiters, such
  as `prn` for printable characters ([more
  here](/language/hoon/reference/stdlib/4i)).

    ```hoon
    > (scan "a b" ;~((glue ace) (just 'a') (just 'b')))  
    ['a' 'b']

    > (scan "a,b" ;~((glue com) (just 'a') (just 'b')))
    ['a' 'b']
    
    > (scan "a,b,a" ;~((glue com) (just 'a') (just 'b')))
    {1 4}
    syntax error
    
    > (scan "a,b,a" ;~((glue com) (just 'a') (just 'b') (just 'a')))
    ['a' 'b' 'a']
    ```

- The `;~` {% tooltip label="micsig"
  href="/language/hoon/reference/rune/mic#-micsig" /%} will create
  `;~(combinator (list rule))` to use multiple `rule`s.

    ```hoon
    > (scan "after the" ;~((glue ace) (star (shim 'a' 'z')) (star (shim 'a' 'z'))))  
    [[i='a' t=<|f t e r|>] [i='t' t=<|h e|>]
    
    > (;~(pose (just 'a') (just 'b')) [1 1] "ab")  
    [p=[p=1 q=2] q=[~ u=[p='a' q=[p=[p=1 q=2] q=[i='b' t=""]]]]]
    ```

    <!-- TODO
    ~tinnus-napbus:
    btw you should almost always avoid recursive welding cos weld has to traverse the entire first list in order to weld it
    so you potentially end up traversing the list thousands of times
    which involves chasing a gorillion pointers
    as a rule of thumb you wanna avoid the recursive use of stdlib list functions in general
    -->

At this point we have two problems:  we are just getting raw `@t` atoms
back, and we can't iteratively process arbitrarily long strings. {%
tooltip label="++cook" href="/language/hoon/reference/stdlib/4f#cook"
/%} will help us with the first of these:

- {% tooltip label="++cook" href="/language/hoon/reference/stdlib/4f#cook" /%} will
  take a `rule` and a {% tooltip label="gate" href="/glossary/gate" /%}
  to apply to the successful parse.

    ```hoon
    > ((cook ,@ud (just 'a')) [[1 1] "abc"])
    [p=[p=1 q=2] q=[~ u=[p=97 q=[p=[p=1 q=2] q="bc"]]]]

    > ((cook ,@tas (just 'a')) [[1 1] "abc"])
    [p=[p=1 q=2] q=[~ u=[p=%a q=[p=[p=1 q=2] q="bc"]]]]

    > ((cook |=(a=@ +(a)) (just 'a')) [[1 1] "abc"])
    [p=[p=1 q=2] q=[~ u=[p=98 q=[p=[p=1 q=2] q="bc"]]]]

    > ((cook |=(a=@ `@t`+(a)) (just 'a')) [[1 1] "abc"])
    [p=[p=1 q=2] q=[~ u=[p='b' q=[p=[p=1 q=2] q="bc"]]]]
    ```

However, to parse iteratively, we need to use the {% tooltip
label="++knee" href="/language/hoon/reference/stdlib/4f#knee" /%}
function, which takes a noun as the {% tooltip label="bunt"
href="/glossary/bunt" /%} of the type the `rule` produces, and produces
a `rule` that recurses properly.  (You'll probably want to treat this as
a recipe for now and just copy it when necessary.)

```hoon {% copy=true %}
|-(;~(plug prn ;~(pose (knee *tape |.(^$)) (easy ~))))
```

There is an example of a calculator [in the parsing
guide](/language/hoon/guides/parsing#recursive-parsers) that's worth a
read at this point.  It uses {% tooltip label="++knee"
href="/language/hoon/reference/stdlib/4f#knee" /%} to scan in a set of numbers
at a time.

### Example:  Parse a String of Numbers

A simple {% tooltip label="++shim"
href="/language/hoon/reference/stdlib/4f#shim" /%}-based parser:

```hoon
> (scan "1234567890" (star (shim '0' '9')))  
[i='1' t=<|2 3 4 5 6 7 8 9 0|>]
```

A refined {% tooltip label="++cook"
href="/language/hoon/reference/stdlib/4f#cook" /%}/{% tooltip label="++cury" href="/language/hoon/reference/stdlib/2n#cury" /%}/{% tooltip label="++jest" href="/language/hoon/reference/stdlib/4f#jest" /%} parser:

```hoon
> ((cook (cury slaw %ud) (jest '1')) [[1 1] "123"])  
[p=[p=1 q=2] q=[~ u=[p=[~ 1] q=[p=[p=1 q=2] q="23"]]]]  

> ((cook (cury slaw %ud) (jest '12')) [[1 1] "123"])
[p=[p=1 q=3] q=[~ u=[p=[~ 12] q=[p=[p=1 q=3] q="3"]]]]
```

### Example:  Hoon Workbook

More examples demonstrating parser usage are available in the [Hoon
Workbook](/language/hoon/examples), such as the [Roman
Numeral](/language/hoon/examples/roman) tutorial.


# R-metals.md

---

+++
title = "18. Generic and Variant Cores"
weight = 28
nodes = [288, 299]
objectives = ["Distinguish dry and wet cores.", "Describe use cases for wet gates (using genericity).", "Enumerate and distinguish use cases for dry cores (using variance):", "- Covariant (`%zinc`)", "- Contravariant (`%iron`)", "- Bivariant (`%lead`)", "- Invariant (`%gold`)"]
+++

_This module introduces how {% tooltip label="cores"
href="/glossary/core" /%} can be extended for different behavioral
patterns.  It may be considered optional and skipped if you are
speedrunning Hoon School._

Cores can expose and operate with many different assumptions about their
inputs and structure.  `[battery payload]` describes the top-level
structure of a core, but within that we already know other requirements
can be enforced, like `[battery [sample context]]` for a {% tooltip
label="gate" href="/glossary/gate" /%}, or no `sample` for a {% tooltip
label="trap" href="/glossary/trap" /%}.  Cores can also expose and
operate on their input values with different relationships.  This lesson
is concerned with examining
[_genericity_](https://en.wikipedia.org/wiki/Generic_programming)
including certain kinds of [parametric
polymorphism](https://en.wikipedia.org/wiki/Parametric_polymorphism),
which allows flexibility in type, and
[_variance_](https://en.wikipedia.org/wiki/Covariance_and_contravariance_%28computer_science%29),
which allows cores to use different sets of rules as they evaluate.

If cores never changed, we wouldn't need polymorphism.  Of course, nouns
are immutable and never change, but we use them as templates to
construct new nouns around.

Suppose we take a core, a {% tooltip label="cell" href="/glossary/cell"
/%} `[battery payload]`, and replace `payload` with a different {%
tooltip label="noun" href="/glossary/noun" /%}. Then, we invoke an {%
tooltip label="arm" href="/glossary/arm" /%} from the {% tooltip
label="battery" href="/glossary/battery" /%}.

Is this legal?  Does it make sense?  Every function call in Hoon does
this, so we'd better make it work well.

The full core stores _both_ {% tooltip label="payload"
href="/glossary/payload" /%} types:  the type that describes the
`payload` currently in the {% tooltip label="core" href="/glossary/core"
/%}, and the type that the core was compiled with.

In the [Bertrand Meyer tradition of type
theory](https://en.wikipedia.org/wiki/Object-Oriented_Software_Construction),
there are two forms of polymorphism:  _variance_ and _genericity_.  In
Hoon this choice is per core:  a core can be either `%wet` or `%dry`.
Dry polymorphism relies on variance; wet polymorphism relies on
genericity.

This lesson discusses both genericity and variance for core management.
These two sections may be read separately or in either order, and all of
this content is not a requirement for working extensively with Gall
agents.  If you're just starting off, {% tooltip label="wet gates"
href="/glossary/wet-gate" /%} (genericity) make the most sense to have
in your toolkit now.


##  Genericity

Polymorphism is a programming concept that allows a piece of code to use
different types at different times.  It's a common technique in most
languages to make code that can be reused for many different situations,
and Hoon is no exception.

### Dry Cores

A dry gate is the kind of gate that you're already familiar with:  a
one-armed {% tooltip label="core" href="/glossary/core" /%} with a
sample.  A {% tooltip label="wet gate" href="/glossary/wet-gate" /%} is
also a one-armed core with a {% tooltip label="sample"
href="/glossary/sample" /%}, but there is a difference in how types are
handled.  With a dry gate, when you pass in an argument and the code
gets compiled, the type system will try to cast to the type specified by
the {% tooltip label="gate" href="/glossary/gate" /%}; if you pass
something that does not fit in the specified type, for example a `cord`
instead of a `cell` you will get a {% tooltip label="nest-fail"
href="/language/hoon/reference/hoon-errors#nest-fail" /%} error.

A core's {% tooltip label="payload" href="/glossary/payload" /%} can
change from its original value.  In fact, this happens in the typical
function call:  the default {% tooltip label="sample"
href="/glossary/sample" /%} is replaced with an input value.  How can we
ensure that the core's {% tooltip label="arms" href="/glossary/arm" /%}
are able to run correctly, that the payload type is still appropriate
despite whatever changes it has undergone?

There is a type check for each {% tooltip label="arm"
href="/glossary/arm" /%} of a dry core, intended to verify that the
arm's parent core has a {% tooltip label="payload"
href="/glossary/payload" /%} of the correct type.

When the `$` buc arm of a dry {% tooltip label="gate"
href="/glossary/gate" /%} is evaluated it takes its parent core—the dry
gate itself—as the {% tooltip label="subject" href="/glossary/subject"
/%}, often with a modified sample value.  But any change in sample type
should be conservative; the modified sample value must be of the same
type as the default sample value (or possibly a subtype).  When the `$`
buc arm is evaluated it should have a subject of a type it knows how to
use.

### Wet Gates

When you pass arguments to a {% tooltip label="wet gate"
href="/glossary/wet-gate" /%}, their types are preserved and type
analysis is done at the definition site of the gate rather than at the
call site.  In other words, for a wet gate, we ask:  “Suppose this core
was actually _compiled_ using the modified {% tooltip label="payload"
href="/glossary/payload" /%} instead of the one it was originally built
with?  Would the {% tooltip label="Nock" href="/glossary/nock" /%}
formula we generated for the original template actually work for the
modified `payload`?” Basically, wet gates allow you to hot-swap code at
runtime and see if it “just works”—they defer the actual substitution in
the {% tooltip label="sample" href="/glossary/sample" /%}.  Wet gates
are rather like
[macros](https://en.wikipedia.org/wiki/Macro_%28computer_science%29) in
this sense.

Consider a function like {% tooltip label="++turn"
href="/language/hoon/reference/stdlib/2b#turn" /%} which transforms each
element of a list. To use `++turn`, we install a {% tooltip label="list"
href="/glossary/list" /%} and a transformation function in a generic
core.  The type of the list we produce depends on the type of the list
and the type of the transformation function.  But the Nock formulas for
transforming each element of the list will work on any function and any
list, so long as the function's argument is the list item.

A wet gate is defined by a `|*` {% tooltip label="bartar"
href="/language/hoon/reference/rune/bar#-bartar" /%} rune rather than a
`|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%}.  More generally,
cores that contain wet arms **must** be defined using `|@` {% tooltip
label="barpat" href="/language/hoon/reference/rune/bar#-barpat" /%}
instead of `|%` {% tooltip label="barcen"
href="/language/hoon/reference/rune/bar#-barcen" /%} (`|*` expands to a
`|@` core with `$` buc arm). There is also `|$` {% tooltip
label="barbuc" href="/language/hoon/reference/rune/bar#-barbuc" /%}
which defines the wet gate {% tooltip label="mold" href="/glossary/mold"
/%} builder (remember, we like gates that build gates).

In a nutshell, compare these two gates:

```hoon
> =dry |=([a=* b=*] [b a])

> =wet |*([a=* b=*] [b a])

> (dry %cat %dog)
[6.778.724 7.627.107]

> (wet %cat %dog)
[%dog %cat]
```

The dry gate does not preserve the type of `a` and `b`, but downcasts it
to `*`; the {% tooltip label="wet gate" href="/glossary/wet-gate" /%}
does preserve the input types.  It is good practice to include a cast in
all {% tooltip label="gates" href="/glossary/gate" /%}, even wet gates.
But in many cases the desired output type depends on the input type.
How can we cast appropriately?  Often we can cast by example, using the
input values themselves (using `^+` {% tooltip label="ketlus"
href="/language/hoon/reference/rune/ket#-ketlus" /%}).

Wet gates are therefore used when incoming type information is not well
known and needs to be preserved.  This includes parsing, building, and
structuring arbitrary {% tooltip label="nouns" href="/glossary/noun"
/%}.  (If you are familiar with them, you can think of C++'s templates
and operator overloading, and Haskell's typeclasses.)  Wet gates are
very powerful; they're enough rope to hang yourself with.  Don't use
them unless you have a specific reason to do so.  (If you see `mull-*`
errors then something has gone wrong with using wet gates.)

- [~timluc-miptev, “Wet Gates”](https://blog.timlucmiptev.space/wetgates.html)

### Exercise:  The Trapezoid Rule

The [trapezoid rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)
solves a definite integral.  It approximates the area under the curve by
a trapezoid or (commonly) a series of trapezoids.  The rule requires a
function as one of the inputs, i.e. it applies _for a specific
function_.  We will use {% tooltip label="wet gates"
href="/glossary/wet-gate" /%} to accomplish this without stripping type
information of the input {% tooltip label="gate" href="/glossary/gate"
/%} core.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Integration_num_trapezes_notation.svg/573px-Integration_num_trapezes_notation.svg.png)

<!-- equation too long to fit on page  so have to wrap with a div to make text smaller to compress it -->
{% div class="text-xs" %}
{% math block=true %}
\int_a^b f(x) \, dx \approx \sum_{k=1}^N \frac{f(x_{k-1}) + f(x_k)}{2} \Delta x_k = \tfrac{\Delta x}{2}\left(f(x_0) + 2f(x_1)+2f(x_2)+ 2f(x_3)+2f(x_4)+\cdots+2f(x_{N-1}) + f(x_N)\right)
{% /math %}
{% /div %}

<!--
\int_a^b f(x) \, dx \approx \sum_{k=1}^N \frac{f(x_{k-1}) + f(x_k)}{2} \Delta x_k = \tfrac{\Delta x}{2}\left(f(x_0) + 2f(x_1)+2f(x_2)+ 2f(x_3)+2f(x_4)+\cdots+2f(x_{N-1}) + f(x_N)\right)
-->

- Produce a trapezoid-rule integrator which accepts a wet gate (as a
  function of a single variable) and a {% tooltip label="list"
  href="/glossary/list" /%} of _x_ values, and yields the integral as a
  `@rs` floating-point value.  (If you are not yet familiar with these,
  you may wish to skip ahead to the next lesson.)

```hoon {% copy=true %}
++  trapezint
  |*  [a=(list @rs) b=gate]
  =/  n  (lent a)
  =/  k  1
  =/  sum  .0
  |-  ^-  @rs
  ?:  =(+(k) n)  (add:rs sum (b (snag k a)))
  ?:  =(k 1)
    $(k +(k), sum (add:rs sum (b (snag k a))))
  $(k +(k), sum (mul:rs .2 (add:rs sum (b (snag k a)))))
```

The meat of this gate is concerned with correctly implementing the
mathematical equation.  In particular, wetness is required because `b`
can be _any_ gate (although it should only be a gate with one argument,
lest the whole thing `mull-grow` fail).  If you attempt to create the
equivalent dry gate (`|=` {% tooltip label="bartis"
href="/language/hoon/reference/rune/bar#-bartis" /%}), Hoon fails to
build it with a {% tooltip label="nest-fail"
href="/language/hoon/reference/hoon-errors#nest-fail" /%} due to the
loss of type information from the gate `b`.

#### Tutorial:  `++need`

{% tooltip label="Wet gates" href="/glossary/wet-gate" /%} and wet cores
are used in Hoon when type information isn't well-characterized ahead of
time, as when constructing {% tooltip label="++maps"
href="/language/hoon/reference/stdlib/2o#map" /%} or {% tooltip
label="++sets" href="/language/hoon/reference/stdlib/2o#set" /%}.  For
instance, almost all of the arms in {% tooltip label="++by"
href="/language/hoon/reference/stdlib/2i#by" /%} and {% tooltip
label="++in" href="/language/hoon/reference/stdlib/2h#in" /%}, as well
as most {% tooltip label="++list" href="/glossary/list" /%} tools, are
wet gates.

Let's take a look at a particular wet gate from the Hoon standard
library, {% tooltip label="++need"
href="/language/hoon/reference/stdlib/2a#need" /%}.  `++need` works with
a {% tooltip label="unit" href="/language/hoon/reference/stdlib/1c#unit"
/%} to produce the value of a successful `unit` call, or crash on `~`.
(As this code is already defined in your `hoon.hoon`, you do not need to
define it in the Dojo to use it.)

```hoon {% copy=true %}
++  need                                                ::  demand
  |*  a=(unit)
  ?~  a  ~>(%mean.'need' !!)
  u.a
```

Line by line:

```hoon
|*  a=(unit)
```

This declares a wet gate which accepts a `unit`.

```hoon
?~  a  ~>(%mean.'need' !!)
```

If `a` is empty, `~`, then the `unit` cannot be unwrapped.  Crash with
`!!` {% tooltip label="zapzap"
href="/language/hoon/reference/rune/zap#-zapzap" /%}, but use `~>` {%
tooltip label="siggar" href="/language/hoon/reference/rune/sig#-siggar"
/%} to hint to the runtime interpreter how to handle the crash.

```hoon
u.a
```

This returns the value in the `unit` since we now know it exists.

`++need` is wet because we don't want to lose type information when we
extract from the `unit`.

### Parametric Polymorphism

We encountered `|$` {% tooltip label="barbuc"
href="/language/hoon/reference/rune/bar#-barbuc" /%} above as a {%
tooltip label="wet gate" href="/glossary/wet-gate" /%} that is a mold
builder rune which takes in a list of {% tooltip label="molds"
href="/glossary/mold" /%} and produces a new mold.  Here we take another
look at this rune as an implementation of _parametric polymorphism_ in
Hoon.

For example, we have
{% tooltip label="lists" href="/glossary/list" /%}, {% tooltip
label="trees" href="/language/hoon/reference/stdlib/1c#tree" /%}, and {%
tooltip label="sets" href="/language/hoon/reference/stdlib/2o#set" /%}
in Hoon, which are each defined in `hoon.hoon` as wet gate mold
builders. Take a moment to see for yourself. Each `++` arm is followed
by `|$` and a list of labels for input types inside brackets `[ ]`.
After that subexpression comes another that defines a type that is
parametrically polymorphic with respect to the input values. For
example, here is the definition of `list` from `hoon.hoon`:

```hoon {% copy=true %}
++  list
  |$  [item]
  ::    null-terminated list
  ::
  ::  mold generator: produces a mold of a null-terminated list of the
  ::  homogeneous type {a}.
  ::
  $@(~ [i=item t=(list item)])
```

The `|$` {% tooltip label="barbuc"
href="/language/hoon/reference/rune/bar#-barbuc" /%} rune is especially
useful for defining containers of various kinds.  Indeed, `list`s,
`tree`s, and `set`s are all examples of containers that accept subtypes.
You can have a `(list @)`, a `(list ^)`, a `(list *)`, a `(tree @)`, a
`(tree ^)`, a `(tree *)`, etc.  The same holds for `set`.

One nice thing about containers defined by `|$` is that they nest in the
expected way.  Intuitively a `(list @)` should nest under `(list *)`,
because `@` nests under `*`. And so it does:

```hoon
> =a `(list @)`~[11 22 33]

> ^-((list *) a)
~[11 22 33]
```

Conversely, a `(list *)` should not nest under `(list @)`, because `*`
does not nest under `@`:

```hoon
> =b `(list *)`~[11 22 33]

> ^-((list @) b)
nest-fail
```

### Drying Out a Gate

Some functional tools like {% tooltip label="++cury"
href="/language/hoon/reference/stdlib/2n#cury" /%} don't work with {%
tooltip label="wet gates" href="/glossary/wet-gate" /%}.  It is,
however, possible to “dry out“ a wet gate using {% tooltip
label="++bake" href="/language/hoon/reference/stdlib/2b#bake" /%}:

```hoon
> ((curr reel add) `(list @)`[1 2 3 4 ~])
mull-grow
-find.i.a

> ((curr (bake reel ,[(list @) _add]) add) `(list @)`[1 2 3 4 ~])
10
```

Typically it's better to find another way to express your problem than
to `++bake` a wet gate, however.  As we said before, wet gates are
powerful and for that reason not apt for every purpose.


##  Variance

Dry polymorphism works by substituting {% tooltip label="cores"
href="/glossary/core" /%}.  Typically, one core is used as the interface
definition, then replaced with another core which does something useful.

For core `b` to nest within core `a`, the {% tooltip label="batteries"
href="/glossary/battery" /%} of `a` and `b` must have the same tree
shape, and the product of each `b` {% tooltip label="arm"
href="/glossary/arm" /%} must nest within the product of the `a` arm.
Wet arms (described above) are not compatible unless the Hoon expression
is exactly the same.  But for dry cores we also apply a {% tooltip
label="payload" href="/glossary/payload" /%} test that depends on the
rules of variance.

There are four kinds of {% tooltip label="cores" href="/glossary/core"
/%}: `%gold`, `%iron`, `%zinc`, and `%lead`. You are able to use
core-variance rules to create programs which take other programs as
arguments. Which particular rules depends on which kind of core your
program needs to complete.

Before we embark on the following discussion, we want you to know that
[variance](https://en.wikipedia.org/wiki/Covariance_and_contravariance_%28computer_science%29)
is a bright-line idea, much like cores themselves, which once you “get”
illuminates you further about Hoon-nature.  For the most part, though,
you don't need to worry about core variance much unless you are writing
kernel code, since it impinges on how cores evaluate with other cores as
inputs.  Don't sweat it if it takes a while for core variance to click
for you.  (If you want to dig into resources, check out Meyer type
theory.  The rules should make sense if you think about them intuitively
and don't get hung up on terminology.)  You should read up on the
[Liskov substitution
principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle)
if you want to dive deeper.  [Vadzim
Vysotski](https://vadzimv.dev/2019/10/01/generic-programming-part-1-introduction.html)
and [Jamie
Kyle](https://medium.com/@thejameskyle/type-systems-covariance-contravariance-bivariance-and-invariance-explained-35f43d1110f8)
explain the theory of type system variance accessibly, while [Eric
Lippert](https://archive.ph/QmiqB) provides a more technical
description.  There are many wrinkles that particular languages, such as
object-oriented programming languages, introduce which we can elide
here.

<!--
https://stackoverflow.com/questions/37467882/why-does-c-sharp-use-contravariance-not-covariance-in-input-parameters-with-de
https://docs.microsoft.com/en-us/dotnet/standard/generics/covariance-and-contravariance
--->

Briefly, computer scientist Eric Lippert
[clarifies](https://stackoverflow.com/questions/37467882/why-does-c-sharp-use-contravariance-not-covariance-in-input-parameters-with-de)
that “variance is a fact about the preservation of an assignment
compatibility relationship across a transformation of types.”  What
trips learners up about variance is that **variance rules apply to the
input and output of a core, not directly to the core itself**.  A core
has a _variance property_, but that property doesn't manifest until
cores are used together with each other.

Variance describes the four possible relationships that type rules are
able to have to each other.  Hoon imaginatively designates these by {%
tooltip label="metals" href="/glossary/metals" /%}.  Briefly:

1. **Covariance (`%zinc`)** means that specific types nest inside of
   generic types:  it's like claiming that a core that produces a
   `%plant` can produce a `%tree`, a subcategory of `%plant`.
   Covariance is useful for flexibility in return values.

2. **Contravariance (`%iron`)** means that generic types are expected to
   nest inside of specific types:  it's like claiming that a core that
   can accept a `%tree` can accept a `%plant`, the supercategory of
   `%tree`.  (Contravariance seems counterintuitive for many developers
   when they encounter it for the first time.)  Contravariance is useful
   for flexibility in input values (`sample`s).

3. **Bivariance (`%lead`)** means that we can allow both covariant and
   contravariant behavior.  While bivariance is included for
   completeness (including a worked example below), it is not commonly
   used and only a few examples exist in the standard library for
   building shared data structure cores.

4. **Invariance (`%gold`)** means that types must mutually nest
   compatibly:  a core that accepts or produces a `%tree` can only
   accept or produce a `%tree`.  This is the default behavior of cores,
   so it's the strongest model you have imprinted on.  Cores which allow
   variance are changing that behavior.

A `%gold` core can be cast or converted to any metal, and any metal can
be cast or converted to `%lead`.

<!--
TODO
would be nice to explain similar to aura nesting rules, but at the core level
https://medium.com/@thejameskyle/type-systems-covariance-contravariance-bivariance-and-invariance-explained-35f43d1110f8
-->

### `%zinc` Covariance

Covariance means that specific types nest inside of generic types:
`%tree` nests inside of `%plant`.  Covariant data types are sources, or
read-only values.

A zinc core `z` has a read-only {% tooltip label="sample"
href="/glossary/sample" /%} ({% tooltip label="payload"
href="/glossary/payload" /%} head, `+6.z`) and an opaque context
(payload tail, `+7.z`). (_Opaque_ here means that the faces and arms are
not exported into the namespace, and that the values of faces and arms
can't be written to. The object in question can be replaced by something
else without breaking type safety.)  A core `y` which nests within it
must be a gold or zinc core, such that `+6.y` nests within `+6.z`.
Hence, **covariant**.

<!-- If type `x` nests within type `xx`, and type `y` nests within type `yy`, then a core accepting `yy` and producing `x` nests within an iron core accepting `y` and producing `xx`. TODO not adjusted yet -->

You can read from the sample of a `%zinc` core, but not change it:

```hoon
> =mycore ^&(|=(a=@ 1))

> a.mycore
0

> mycore(a 22)
-tack.a
-find.a
ford: %slim failed:
ford: %ride failed to compute type:
```

Informally, a function fits an interface if the function has a more
specific result and/or a less specific argument than the interface.

The `^&` {% tooltip label="ketpam"
href="/language/hoon/reference/rune/ket#-ketpam" /%} rune converts a
core to a `%zinc` covariant core.

### `%iron` Contravariance

Contravariance means that generic types nest inside of specific types.
Contravariant data types are sinks, or write-only values.

An `%iron` core `i` has a write-only {% tooltip label="sample"
href="/glossary/sample" /%} ({% tooltip label="payload"
href="/glossary/payload" /%} head, `+6.i`) and an opaque context
(payload tail, `+7.i`).  A core `j` which nests within it must be a
`%gold` or `%iron` core, such that `+6.i` nests within `+6.j`. Hence,
**contravariant**.

If type `x` nests within type `xx`, and type `y` nests within type `yy`,
then a core accepting `yy` and producing `x` nests within an iron core
accepting `y` and producing `xx`.

Informally, a function fits an interface if the function has a more
specific result and/or a less specific argument than the interface.

For instance, the archetypal {% tooltip label="Gall"
href="/glossary/gall" /%} agents in `/sys/lull.hoon` are composed using
iron gates since they will be used as examples for building actual {%
tooltip label="agent" href="/glossary/agent" /%} cores.  The {% tooltip
label="++rs" href="/language/hoon/reference/stdlib/3b#rs" /%} and sister
gates in `/sys/hoon.hoon` are built using iron doors with specified
rounding behavior so when you actually use the core (like {% tooltip
label="++add:rs" href="/language/hoon/reference/stdlib/3b#addrs" /%})
the core you are using has been built as an example.

The `|~` {% tooltip label="barsig"
href="/language/hoon/reference/rune/bar#-barsig" /%} rune produces an
iron gate.  The `^|` {% tooltip label="ketbar"
href="/language/hoon/reference/rune/ket#-ketbar" /%} rune converts a
`%gold` invariant core to an iron core.

### `%lead` Bivariance

Bivariance means that both covariance and contravariance apply.
Bivariant data types have an opaque {% tooltip label="payload"
href="/glossary/payload" /%} that can neither be read or written to.

A lead core `l` has an opaque `payload` which can be neither read nor
written to.  There is no constraint on the payload of a core `m` which
nests within it.  Hence, **bivariant**.

If type `x` nests within type `xx`, a lead core producing `x` nests
within a lead core producing `xx`.

Bivariant data types are neither readable nor writeable, but have no
constraints on nesting.  These are commonly used for `/mar` {% tooltip
label="marks" href="/glossary/mark" /%} and `/sur` structure files. They
are useful as examples which produce types.

Informally, a more specific {% tooltip label="generator"
href="/glossary/generator" /%} can be used as a less specific generator.

For instance, several archetypal cores in `/sys/lull.hoon` which define
operational data structures for {% tooltip label="Arvo"
href="/glossary/arvo" /%} are composed using lead {% tooltip
label="gates" href="/glossary/gate" /%}.

The `|?` {% tooltip label="barwut"
href="/language/hoon/reference/rune/bar#-barwut" /%} rune produces a
lead trap.  The `^?` {% tooltip label="ketwut"
href="/language/hoon/reference/rune/ket#-ketwut" /%} rune converts any
core to a `%lead` bivariant core.

### `%gold` Invariance

Invariance means that type nesting is disallowed.  Invariant data types
have a read-write {% tooltip label="payload" href="/glossary/payload"
/%}.

A `%gold` {% tooltip label="core" href="/glossary/core" /%} `g` has a
read-write payload; another core `h` that nests within it (i.e., can be
substituted for it) must be a `%gold` core whose `payload` is mutually
compatible (`+3.g` nests in `+3.h`, `+3.h` nests in `+3.g`).  Hence,
**invariant**.

By default, cores are `%gold` invariant cores.


### Illustrations

#### Tutorial:  `%gold` Invariant Polymorphism

Usually it makes sense to cast for a `%gold` core type when you're
treating a core as a state machine.  The check ensures that the payload,
which includes the relevant state, doesn't vary in type.

Let's look at simpler examples here, using the `^+` {% tooltip
label="ketlus" href="/language/hoon/reference/rune/ket#-ketlus" /%}
rune:

```hoon
> ^+(|=(^ 15) |=(^ 16))
< 1.jcu
  [ [* *]
    [our=@p now=@da eny=@uvJ]
    <15.eah 40.ihi 14.tdo 54.xjm 77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
  ]
>

> ^+(|=(^ 15) |=([@ @] 16))
mint-nice
-need.@
-have.*
nest-fail

> ^+(|=(^ 15) |=(* 16))
mint-nice
-need.[* *]
-have.*
nest-fail
```

The first cast goes through because the right-hand gold core has the
same {% tooltip label="sample" href="/glossary/sample" /%} type as the
left-hand gold core. The sample types mutually nest. The second cast
fails because the right-hand sample type is more specific than the
left-hand sample type. (Not all {% tooltip label="cells"
href="/glossary/cell" /%}, `^`, are pairs of {% tooltip label="atoms"
href="/glossary/atom" /%}, `[@ @]`.) And the third cast fails because
the right-hand sample type is broader than the left-hand sample type.
(Not all {% tooltip label="nouns" href="/glossary/noun" /%}, `*`, are
cells, `^`.)

Two more examples:

```
> ^+(=>([1 2] |=(@ 15)) =>([123 456] |=(@ 16)))
<1.xqz [@ @ud @ud]>

> ^+(=>([1 2] |=(@ 15)) =>([123 456 789] |=(@ 16)))
nest-fail
```

In these examples, the `=>` rune is used to give each core a simple
context. The context of the left-hand core in each case is a pair of
atoms, `[@ @]`. The first cast goes through because the right-hand core
also has a pair of atoms as its context. The second cast fails because
the right-hand core has the wrong type of context -- three atoms, `[@ @
@]`.

#### Tutorial:  `%iron` Contravariant Polymorphism

`%iron` {% tooltip label="gates" href="/glossary/gate" /%} are
particularly useful when you want to pass gates (having various {%
tooltip label="payload" href="/glossary/payload" /%} types) to other
gates.  We can illustrate this use with a very simple example. Save the
following as `/gen/gatepass.hoon` in your `%base` {% tooltip
label="desk" href="/glossary/desk" /%}:

```hoon {% copy=true %}
|=  a=_^|(|=(@ 15))
^-  @
=/  b=@  (a 10)
(add b 20)
```

This {% tooltip label="generator" href="/glossary/generator" /%} is
rather simple except for the first line.  The sample is defined as an
`%iron` gate and gives it the {% tooltip label="face"
href="/glossary/face" /%} `a`.  The function as a whole is for taking
some gate as input, calling it by passing it the value `10`, adding `20`
to it, and returning the result.  Let's try it out in the Dojo:

```hoon
> +gatepass |=(a=@ +(a))
31

> +gatepass |=(a=@ (add 3 a))
33

> +gatepass |=(a=@ (mul 3 a))
50
```

But we still haven't fully explained the first line of the code.  What
does `_^|(|=(@ 15))` mean? The inside portion is clear enough:  `|=(@
15)` produces a normal (i.e., `%gold`) {% tooltip label="gate"
href="/glossary/gate" /%} that takes an atom and returns `15`.  The `^|`
{% tooltip label="ketbar"
href="/language/hoon/reference/rune/ket#-ketbar" /%} rune is used to
turn `%gold` gates to `%iron`.  (Reverse alchemy!)  And the `_`
character turns that `%iron` gate value into a structure, i.e. a type.
So the whole subexpression means, roughly:  “the same type as an iron
gate whose {% tooltip label="sample" href="/glossary/sample" /%} is an
atom, `@`, and whose product is another atom, `@`”. The context isn't
checked at all.  This is good, because that allows us to accept gates
defined and produced in drastically different environments.  Let's try
passing a gate with a different context:

```hoon
> +gatepass =>([22 33] |=(a=@ +(a)))
31
```

It still works.  You can't do that with a gold core sample!

There's a simpler way to define an iron sample. Revise the first line of
`/gen/gatepass.hoon` to the following:

```hoon {% copy=true %}
|=  a=$-(@ @)
^-  @
=/  b=@  (a 10)
(add b 20)
```

If you test it, you'll find that the {% tooltip label="generator"
href="/glossary/generator" /%} behaves the same as it did before the
edits.  The `$-` {% tooltip label="buchep"
href="/language/hoon/reference/rune/buc#--buchep" /%} rune is used to
create an `%iron` gate structure, i.e., an `%iron` gate type.  The first
expression defines the desired {% tooltip label="sample"
href="/glossary/sample" /%} type, and the second subexpression defines
the gate's desired output type.

The sample type of an `%iron` gate is contravariant.  This means that,
when doing a cast with some `%iron` gate, the desired gate must have
either the same sample type or a superset.

Why is this a useful nesting rule for passing gates?  Let's say you're
writing a function `F` that takes as input some gate `G`.  Let's also
say you want `G` to be able to take as input any **mammal**.  The code
of `F` is going to pass arbitrary **mammals** to `G`, so that `G` needs
to know how to handle all **mammals** correctly.  You can't pass `F` a
gate that only takes **dogs** as input, because `F` might call it with a
**cat**.  But `F` can accept a gate that takes all **animals** as input,
because a gate that can handle any **animal** can handle **any mammal**.

`%iron` {% tooltip label="cores" href="/glossary/core" /%} are designed
precisely with this purpose in mind.  The reason that the {% tooltip
label="sample" href="/glossary/sample" /%} is write-only is that we want
to be able to assume, within function `F`, that the sample of `G` is a
**mammal**. But that might not be true when `G` is first passed into
`F`—the default value of `G` could be another **animal**, say, a
**lizard**.  So we restrict looking into the sample of `G` by making the
sample write-only. The illusion is maintained and type safety secured.

Let's illustrate `%iron` core nesting properties:

```hoon
> ^+(^|(|=(^ 15)) |=(^ 16))
< 1|jcu
  [ [* *]
    [our=@p now=@da eny=@uvJ]
    <15.eah 40.ihi 14.tdo 54.xjm 77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
  ]
>

> ^+(^|(|=(^ 15)) |=([@ @] 16))
mint-nice
-need.@
-have.*
nest-fail

> ^+(^|(|=(^ 15)) |=(* 16))
< 1|jcu
  [ [* *]
    [our=@p now=@da eny=@uvJ]
    <15.eah 40.ihi 14.tdo 54.xjm 77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
  ]
>
```

(As before, we use the `^|` {% tooltip label="ketbar"
href="/language/hoon/reference/rune/ket#-ketbar" /%} rune to turn
`%gold` gates to `%iron`.)

The first cast goes through because the two gates have the same sample
type.  The second cast fails because the right-hand gate has a more
specific sample type than the left-hand gate does.  If you're casting
for a gate that accepts any cell, `^`, it's because we want to be able
to pass any cell to it.  A gate that is only designed for pairs of
atoms, `[@ @]`, can't handle all such cases, naturally.  The third cast
goes through because the right-hand gate sample type is broader than the
left-hand gate sample type.  A gate that can take any noun as its
sample, `*`, works just fine if we choose only to pass it cells, `^`.

We mentioned previously that an `%iron` core has a write-only {% tooltip
label="sample" href="/glossary/sample" /%} and an opaque context.  Let's
prove it.

Let's define a trivial {% tooltip label="gate" href="/glossary/gate" /%}
with a context of `[g=22 h=44 .]`, convert it to `%iron` with `^|`, and
bind it to `iron-gate` in the dojo:

```hoon
> =iron-gate ^|  =>([g=22 h=44 .] |=(a=@ (add a g)))

> (iron-gate 10)
32

> (iron-gate 11)
33
```

Not a complicated function, but it serves our purposes.  Normally (i.e.,
with `%gold` cores) we can look at a context value `p` of some gate `q`
with a wing expression: `p.q`. Not so with the iron gate:

```hoon
> g.iron-gate
-find.g.iron-gate
```

And usually we can look at the sample value using the {% tooltip
label="face" href="/glossary/face" /%} given in the gate definition. Not
in this case:

```hoon
> a.iron-gate
-find.a.iron-gate
```

If you really want to look at the sample you can check `+6` of
`iron-gate`:

```hoon
> +6.iron-gate
0
```

… and if you really want to look at the head of the context (i.e., where
`g` is located, `+14`) you can:

```hoon
> +14.iron-gate
22
```

… but in both cases all the relevant type information has been thrown
away:

```hoon
> -:!>(+6.iron-gate)
#t/*

> -:!>(+14.iron-gate)
#t/*
```

#### Tutorial:  `%zinc` Covariant Polymorphism

As with `%iron` {% tooltip label="cores" href="/glossary/core" /%}, the
context of `%zinc` cores is opaque—they cannot be written-to or
read-from.  The {% tooltip label="sample" href="/glossary/sample" /%} of
a `%zinc` core is read-only.  That means, among other things, that
`%zinc` cores cannot be used for function calls.  Function calls in Hoon
involve a change to the sample (the default sample is replaced with the
argument value), which is disallowed as type-unsafe for `%zinc` cores.

We can illustrate the casting properties of `%zinc` cores with a few
examples.  The `^&` {% tooltip label="ketpam"
href="/language/hoon/reference/rune/ket#-ketpam" /%} rune is used to
convert `%gold` cores to `%zinc`:

```hoon
> ^+(^&(|=(^ 15)) |=(^ 16))
< 1&jcu
  [ [* *]
    [our=@p now=@da eny=@uvJ]
    <15.eah 40.ihi 14.tdo 54.xjm 77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
  ]
>

> ^+(^&(|=(^ 15)) |=([@ @] 16))
< 1&jcu
  [ [* *]
    [our=@p now=@da eny=@uvJ]
    <15.eah 40.ihi 14.tdo 54.xjm 77.vsv 236.zqw 51.njr 139.oyl 33.uof 1.pnw %138>
  ]
>

> ^+(^&(|=(^ 15)) |=(* 16))
mint-nice
-need.[* *]
-have.*
nest-fail
```

The first two casts succeed because the right-hand core {% tooltip
label="sample" href="/glossary/sample" /%} type is either the same or a
subset of the left-hand core sample type.  The last one fails because
the right-hand sample type is a superset.

Even though you can't function call a `%zinc` core, the arms of a
`%zinc` core can be computed and the sample can be read.  Let's test
this with a `%zinc` {% tooltip label="gate" href="/glossary/gate" /%} of
our own:

```hoon
> =zinc-gate ^&  |=(a=_22 (add 10 a))

> (zinc-gate 12)
payload-block

> a.zinc-gate
22

> $.zinc-gate
32
```

#### Tutorial:  `%lead` Bivariant Polymorphism

`%lead` cores have more permissive nesting rules than either `%iron` or
`%zinc` cores.  There is no restriction on which {% tooltip
label="payload" href="/glossary/payload" /%} types nest. That means,
among other things, that the payload type of a `%lead` core is both
covariant and contravariant ( ‘bivariant’).

In order to preserve type safety when working with `%lead` cores, a
severe restriction is needed.  The whole payload of a `%lead` core is
opaque—the payload can neither be written-to or read-from.  For this
reason, as was the case with `%zinc` cores, `%lead` cores cannot be
called as functions.

The {% tooltip label="arms" href="/glossary/arm" /%} of a `%lead` core
can still be evaluated, however. We can use the `^?` rune to convert a
`%gold`, `%iron`, or `%zinc` core to lead:

```hoon
> =lead-gate ^?  |=(a=_22 (add 10 a))

> $.lead-gate
32
```

But don't try to read the sample:

```hoon
> a.lead-gate
-find.a.lead-gate
```

#### Tutorial:  `%lead` Bivariant Polymorphism

- Calculate the Fibonacci series using `%lead` and `%iron` cores.

This program produces a list populated by the first ten elements of the
`++fib` {% tooltip label="arm" href="/glossary/arm" /%}.  It consists of
five arms; in brief:

- `++fib` is a trap (core with no sample and default arm `$` buc)
- `++stream` is a {% tooltip label="mold" href="/glossary/mold" /%}
  builder that produces a trap, a function with no argument.  This {%
  tooltip label="trap" href="/glossary/trap" /%} can yield a value or a
  `~`.
- `++stream-type` is a {% tooltip label="wet gate"
  href="/glossary/wet-gate" /%} that produces the type of items stored
  in `++stream`.
- `++to-list` is a wet gate that converts a `++stream` to a {% tooltip
  label="list" href="/glossary/list" /%}.
- `++take` is a wet gate that takes a `++stream` and an atom and yields
  a modified {% tooltip label="subject" href="/glossary/subject" /%} (!)
  and another trap of `++stream`'s type.

**`/gen/fib.hoon`**

```hoon {% copy=true mode="collapse" %}
=<  (to-list (take fib 10))
|%
++  stream
  |*  of=mold
  $_  ^?   |.
  ^-  $@(~ [item=of more=^$])
  ~
++  stream-type
  |*  s=(stream)
  $_  =>  (s)
  ?~  .  !!
  item
++  to-list
  |*  s=(stream)
  %-  flop
  =|  r=(list (stream-type s))
  |-  ^+  r
  =+  (s)
  ?~  -  r
  %=  $
    r  [item r]
    s  more
  ==
++  take
  |*  [s=(stream) n=@]
  =|  i=@
  ^+  s
  |.
  ?:  =(i n)  ~
  =+  (s)
  ?~  -  ~
  :-  item
  %=  ..$
    i  +(i)
    s  more
  ==
++  fib
  ^-  (stream @ud)
  =+  [p=0 q=1]
  |.  :-  q
  %=  .
    p  q
    q  (add p q)
  ==
--
```

Let's examine each arm in detail.

##### `++stream`

```hoon
++  stream
  |*  of=mold
  $_  ^?  |.
  ^-  $@(~ [item=of more=^$])
  ~
```

`++stream` is a mold-builder. It's a {% tooltip label="wet gate"
href="/glossary/wet-gate" /%} that takes one argument, `of`, which is a
{% tooltip label="mold" href="/glossary/mold" /%}, and produces a
`%lead` {% tooltip label="trap" href="/glossary/trap" /%}—a function
with no `sample` and an arm `$` buc, with opaque {%
tooltip label="payload" href="/glossary/payload" /%}.

`$_` {% tooltip label="buccab"
href="/language/hoon/reference/rune/buc#_-buccab" /%} is a rune that
produces a type from an example; `^?` {% tooltip label="ketwut"
href="/language/hoon/reference/rune/ket#-ketwut" /%} converts (casts) a
core to lead; `|.` {% tooltip label="bardot"
href="/language/hoon/reference/rune/bar#-bardot" /%} forms the {%
tooltip label="trap" href="/glossary/trap" /%}.  So to follow this
sequence we read it backwards:  we create a trap, convert it to a lead
trap (making its payload inaccessible), and then use that lead trap as
an example from which to produce a type.

With the line `^- $@(~ [item=of more=^$])`, the output of the trap will
be cast into a new type.  `$@` {% tooltip label="bucpat"
href="/language/hoon/reference/rune/buc#-bucpat" /%} is the rune to
describe a data structure that can either be an {% tooltip label="atom"
href="/glossary/atom" /%} or a {% tooltip label="cell"
href="/glossary/cell" /%}.  The first part describes the atom, which
here is going to be `~`.  The second part describes a cell, which we
define to have the head of type `of` with the {% tooltip label="face"
href="/glossary/face" /%} `item`, and a tail with a face of `more`.  The
expression `^$` is not a rune (no children), but rather a reference to
the enclosing {% tooltip label="wet gate" href="/glossary/wet-gate" /%},
so the tail of this cell will be of the same type produced by this wet
gate.

The final `~` here is used as the type produced when initially calling
this wet gate.  This is valid because it nests within the type we
defined on the previous line.

Now you can see that a `++stream` is either `~` or a pair of a value of
some type and a `++stream`.  This type represents an infinite series.

##### `++stream-type`

```hoon
++  stream-type
  |*  s=(stream)
  $_  =>  (s)
  ?~  .  !!
  item
```

`++stream-type` is a wet gate that produces the type of items stored in
the `stream` {% tooltip label="arm" href="/glossary/arm" /%}.  The
`(stream)` syntax is a shortcut for `(stream *)`; a stream of some type.

Calling a `++stream`, which is a {% tooltip label="trap"
href="/glossary/trap" /%}, will either produce `item` and `more` or it
will produce `~`. If it does produce `~`, the `++stream` is empty and we
can't find what type it is, so we simply crash with `!!` {% tooltip
label="zapzap" href="/language/hoon/reference/rune/zap#-zapzap" /%}.

##### `++take`

```hoon
++  take
  |*  [s=(stream) n=@]
  =|  i=@
  ^+  s
  |.
  ?:  =(i n)  ~
  =+  (s)
  ?~  -  ~
  :-  item
  %=  ..$
    i  +(i)
    s  more
  ==
```

`++take` is another wet gate. This time it takes a `++stream` `s` and an
atom `n`. We add an atom to the {% tooltip label="subject"
href="/glossary/subject" /%} and then make sure that the {% tooltip
label="trap" href="/glossary/trap" /%} we are creating is going to be of
the same type as `s`, the `++stream` we passed in.

If `i` and `n` are equal, the trap will produce `~`.  If not, `s` is
called and has its result put on the front of the subject.  If its value
is `~`, then the trap again produces `~`.  Otherwise the trap produces a
cell of `item`, the first part of the value of `s`, and a new trap that
increments `i`, and sets `s` to be the `more` trap which produces the
next value of the `++stream`.  The result here is a `++stream` that will
only ever produce `n` items, even if the stream otherwise would have
been infinite.

##### `++take`

```hoon
++  to-list
  |*  s=(stream)
  %-  flop
  =|  r=(list (stream-type s))
  |-  ^+  r
  =+  (s)
  ?~  -  r
  %=  $
    r  [item r]
    s  more
  ==
```

`++to-list` is a wet gate that takes `s`, a `++stream`, only here it
will, as you may expect, produce a {% tooltip label="list"
href="/glossary/list" /%}.  The rest of this wet gate is straightforward
but we can examine it quickly anyway.  As is the proper style, this list
that is produced will be reversed, so {% tooltip label="flop"
href="/language/hoon/reference/stdlib/2b#flop" /%} is used to put it in
the order it is in the stream.  Recall that adding to the front of a
list is cheap, while adding to the back is expensive.

`r` is added to the {% tooltip label="subject" href="/glossary/subject"
/%} as an empty {% tooltip label="list" href="/glossary/list" /%} of
whatever type is produced by `s`.  A new {% tooltip label="trap"
href="/glossary/trap" /%} is formed and called, and it will produce the
same type as `r`.  Then `s` is called and has its value added to the
subject. If the result is `~`, the trap produces `r`. Otherwise, we want
to call the trap again, adding `item` to the front of `r` and changing
`s` to `more`.  Now the utility of `take` should be clear.  We don't
want to feed `to-list` an infinite stream as it would never terminate.

##### `++fib`

```hoon
++  fib
  ^-  (stream @ud)
  =+  [p=0 q=1]
  |.  :-  q
  %=  .
    p  q
    q  (add p q)
  ==
```

The final arm in our core is `++fib`, which is a `++stream` of `@ud` and
therefore is a `%lead` {% tooltip label="core" href="/glossary/core"
/%}.  Its subject contains `p` and `q`, which will not be accessible
outside of this {% tooltip label="trap" href="/glossary/trap" /%}, but
because of the `%=` {% tooltip label="centis"
href="/language/hoon/reference/rune/cen#-centis" /%} will be retained in
their modified form in the product trap.  The product of the trap is a
pair (`:-` {% tooltip label="colhep"
href="/language/hoon/reference/rune/col#--colhep" /%}) of an `@ud` and
the trap that will produce the next `@ud` in the Fibonacci series.

```hoon
=<  (to-list (take fib 10))
```

Finally, the first line of our program will take the first 10 elements
of `fib` and produce them as a list.

```unknown
~[1 1 2 3 5 8 13 21 34 55]
```

This example is a bit overkill for simply calculating the Fibonacci
series, but it illustrates how you could use `%lead` cores.  Instead of
`++fib`, you can supply any infinite sequence and `++stream` will
correctly handle it.

### Exercise:  `%lead` Bivariant Polymorphism

- Produce a `%say` {% tooltip label="generator"
  href="/glossary/generator" /%} that yields another self-referential
  sequence, like the [Lucas
  numbers](https://en.wikipedia.org/wiki/Lucas_number) or the
  [Thue–Morse
  sequence](https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence).


# S-math.md

---

+++
title = "19. Mathematics"
weight = 29
nodes = [234, 236, 284]
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

### Exercise:  `++is-close`

The {% tooltip label="++equ:rs"
href="/language/hoon/reference/stdlib/3b#equrs" /%} arm checks for
complete equality of two values.  The downside of this {% tooltip
label="arm" href="/glossary/arm" /%} is that it doesn't find very close
values:

```hoon
> (equ:rs .1 .1)
%.y

> (equ:rs .1 .0.9999999)
%.n
```

- Produce an arm which check for two values to be close to each other by
  an absolute amount.  It should accept three values:  `a`, `b`, and
  `atol`.  It should return the result of the following comparison:

    {% math block=true %}
    |a-b| \leq \texttt{atol}
    {% /math %}

#### Tutorial:  Length Converter

- Write a {% tooltip label="generator" href="/glossary/generator" /%} to
  take a `@tas` input measurement unit of length, a `@rs` value, and a
  `@tas` output unit to which we will convert the input measurement.
  For instance, this generator could convert a number of imperial feet
  to metric decameters.

**`/gen/convert-length.hoon`**

```hoon {% copy=true mode="collapse" %}
|=  [fr-meas=@tas num=@rs to-meas=@tas]
=<
^-  @rs
?.  (check fr-meas to-meas)
  ~|("Invalid Measures" !!)
(output (meters fr-meas num) to-meas)
::
|%
+$  allowed  ?(%inch %foot %yard %furlong %chain %link %rod %fathom %shackle %cable %nautical-mile %hand %span %cubit %ell %bolt %league %megalithic-yard %smoot %barleycorn %poppy-seed %atto %femto %pico %nano %micro %milli %centi %deci %meter %deca %hecto %kilo %mega %giga %tera %peta %exa)
::
++  check
  |=  [fr-meas=@tas to-meas=@tas]
  &(?=(allowed fr-meas) ?=(allowed to-meas))
::
++  meters
  |=  [in=@tas value=@rs]
  =/  factor-one
    (~(got by convert-to-map) in)
  (mul:rs value factor-one)
::
++  output
  |=  [in=@rs out=@tas]
  ?:  =(out %meter)
    in
  (div:rs in (~(got by convert-to-map) out))
::
++  convert-to-map
  ^-  (map @tas @rs)
  %-  malt
  ^-  (list [@tas @rs])
  :~  :-  %atto             .1e-18
      :-  %femto            .1e-15
      :-  %pico             .1e-12
      :-  %nano             .1e-8
      :-  %micro            .1e-6
      :-  %milli            .1e-3
      :-  %poppy-seed       .2.212e-2
      :-  %barleycorn       .8.47e-2
      :-  %centi            .1e-2
      :-  %inch             .2.54e-2
      :-  %deci             .1e-1
      :-  %hand             .1.016e-1
      :-  %link             .2.012e-1
      :-  %span             .2.228e-1
      :-  %foot             .3.048e-1
      :-  %cubit            .4.472e-1
      :-  %megalithic-yard  .8.291e-1
      :-  %yard             .9.145e-1
      :-  %ell              .1.143
      :-  %smoot            .1.7
      :-  %fathom           .1.83
      :-  %rod              .5.03
      :-  %deca             .1e1
      :-  %chain            .2.012e1
      :-  %shackle          .2.743e1
      :-  %bolt             .3.658e1
      :-  %hecto            .1e2
      :-  %cable            .1.8532e2
      :-  %furlong          .2.0117e2
      :-  %kilo             .1e3
      :-  %mile             .1.609e3
      :-  %nautical-mile    .1.850e3
      :-  %league           .4.830e3
      :-  %mega             .1e6
      :-  %giga             .1e8
      :-  %tera             .1e12
      :-  %peta             .1e15
      :-  %exa              .1e18
      :-  %meter            .1
    ==
  --
```

This program shows several interesting aspects, which we've covered
before but highlight here:

- Meters form the standard unit of length.
- `~|` {% tooltip label="sigbar"
  href="/language/hoon/reference/rune/sig#-sigbar" /%} produces an error
  message in case of a bad input.
- `+$` {% tooltip label="lusbuc"
  href="/language/hoon/reference/rune/lus#-lusbuc" /%} is a type
  constructor arm, here for a type union over units of length.

### Exercise:  Measurement Converter

- Add to this {% tooltip label="generator" href="/glossary/generator"
  /%} the ability to convert some other measurement (volume, mass,
  force, or another of your choosing).
- Add an argument to the {% tooltip label="cell" href="/glossary/cell"
  /%} required by the {% tooltip label="gate" href="/glossary/gate" /%}
  that indicates whether the measurements are distance or your new
  measurement.
- Enforce strictly that the `fr-meas` and `to-meas` values are either
  lengths or your new type.
- Create a new map of conversion values to handle your new measurement
  conversion method.
- Convert the functionality into a library.

### `++rs` as a Door

What is `++rs`?  It's a door with 21 arms:

```hoon
> rs
<21|ezj [r=?(%d %n %u %z) <51.njr 139.oyl 33.uof 1.pnw %138>]>
```

The {% tooltip label="battery" href="/glossary/battery" /%} of this {%
tooltip label="core" href="/glossary/core" /%}, pretty-printed as
`21|ezj`, has 21 arms that define functions specifically for `@rs`
atoms.  One of these arms is named `++add`; it's a different `add` from
the standard one we've been using for vanilla atoms, and thus the one we
used above.  When you invoke {% tooltip label="add:rs"
href="/language/hoon/reference/stdlib/3b#addrs" /%} instead of just
`add` in a function call, (1) the `rs` door is produced, and then (2)
the name search for `add` resolves to the special `add` {% tooltip
label="arm" href="/glossary/arm" /%} in `rs`. This produces the {%
tooltip label="gate" href="/glossary/gate" /%} for adding `@rs` atoms:

```hoon
> add:rs
<1.uka [[a=@rs b=@rs] <21.ezj [r=?(%d %n %u %z) <51.njr 139.oyl 33.uof 1.pnw %138>]>]>
```

What about the sample of the `rs` {% tooltip label="door"
href="/glossary/door" /%}?  The pretty-printer shows `r=?(%d %n %u %z)`.
The {% tooltip label="rs" href="/language/hoon/reference/stdlib/3b#rs"
/%} sample can take one of four values: `%d`, `%n`, `%u`, and `%z`.
These argument values represent four options for how to round `@rs`
numbers:

- `%d` rounds down
- `%n` rounds to the nearest value
- `%u` rounds up
- `%z` rounds to zero

The default value is `%z`, round to zero.  When we invoke `++add:rs` to
call the addition function, there is no way to modify the `rs` door
sample, so the default rounding option is used.  How do we change it?
We use the `~( )` notation: `~(arm door arg)`.

Let's evaluate the `add` {% tooltip label="arm" href="/glossary/arm" /%}
of `rs`, also modifying the door {% tooltip label="sample"
href="/glossary/sample" /%} to `%u` for 'round up':

```hoon
> ~(add rs %u)
<1.uka [[a=@rs b=@rs] <21.ezj [r=?(%d %n %u %z) <51.njr 139.oyl 33.uof 1.pnw %138>]>]>
```

This is the gate produced by `add`, and you can see that its sample is a
pair of `@rs` atoms. But if you look in the context you'll see the {%
tooltip label="rs" href="/language/hoon/reference/stdlib/3b#rs" /%}
door. Let's look in the sample of that {% tooltip label="core"
href="/glossary/core" /%} to make sure that it changed to `%u`. We'll
use the wing `+6.+7` to look at the sample of the {% tooltip
label="gate's" href="/glossary/gate" /%} context:

```hoon
> +6.+7:~(add rs %u)
r=%u
```

It did indeed change.  We also see that the door {% tooltip
label="sample" href="/glossary/sample"/%} uses the {% tooltip
label="face" href="/glossary/face" /%} `r`, so let's use that instead of
the unwieldy `+6.+7`:

```hoon
> r:~(add rs %u)
%u
```

We can do the same thing for rounding down, `%d`:

```hoon
> r:~(add rs %d)
%d
```

Let's see the rounding differences in action. Because `~(add rs %u)`
produces a gate, we can call it like we would any other gate:

```hoon
> (~(add rs %u) .3.14159265 .1.11111111)
.4.252704

> (~(add rs %d) .3.14159265 .1.11111111)
.4.2527037
```

This difference between rounding up and rounding down might seem strange
at first.  There is a difference of 0.0000003 between the two answers.
Why does this gap exist?  Single-precision floats are 32-bit and there's
only so many distinctions that can be made in floats before you run out
of bits.

Just as there is a {% tooltip label="door" href="/glossary/door" /%} for
`@rs` functions, there is a Hoon standard library door for `@rd`
functions (double-precision 64-bit floats), another for `@rq` functions
(quad-precision 128-bit floats), and one more for `@rh` functions
(half-precision 16-bit floats).


##  Signed Integer Mathematics

Similar to floating-point representations, [signed
integer](https://en.wikipedia.org/wiki/Signed_number_representations)
representations use an internal bitwise convention to indicate whether a
number should be treated as having a negative sign in front of the
magnitude or not.  There are several ways to represent signed integers:

1. [**Sign-magnitude**](https://en.wikipedia.org/wiki/Signed_number_representations#Sign%E2%80%93magnitude).
   Use the first bit in a fixed-bit-width representation to indicate
   whether the whole should be multiplied by {% math %}-1{% /math %},
   e.g. `0010.1011` for {% math %}43_{10}{% /math %} and `1010.1011` for
   {% math %}-43_{10}{% /math %}.  (This is similar to the
   floating-point solution.)
2. [**One's complement**](https://en.wikipedia.org/wiki/Ones%27_complement).  Use
   the bitwise `NOT` operation to represent the value, e.g. `0010.1011`
   for {% math %}43_{10}{% /math %} and `1101.0100` for {% math
   %}-43_{10}{% /math %}.  This has the advantage that arithmetic
   operations are trivial, e.g. {% math %}43_{10} - 41_{10}{% /math %} =
   `0010.1011` + `1101.0110` = `1.0000.0001`, end-around carry the
   overflow to yield `0000.0010` = 2.  (This is commonly used in
   hardware.)
3. [**Offset binary**](https://en.wikipedia.org/wiki/Offset_binary).
   This represents a number normally in binary _except_ that it counts
   from a point other than zero, like `-256`.
4. [**ZigZag**](https://developers.google.com/protocol-buffers/docs/encoding?hl=en#signed-ints).
   Positive signed integers correspond to even atoms of twice their
   absolute value, and negative signed integers correspond to odd atoms of
   twice their absolute value minus one.

There are tradeoffs in compactness of representation and efficiency of
mathematical operations.

### Hoon Operations

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

- {% tooltip label="++sum:si" href="/language/hoon/reference/stdlib/3a#sumsi" /%}, addition
- {% tooltip label="++dif:si" href="/language/hoon/reference/stdlib/3a#difsi" /%}, subtraction
- {% tooltip label="++pro:si" href="/language/hoon/reference/stdlib/3a#prosi" /%}, multiplication
- {% tooltip label="++fra:si" href="/language/hoon/reference/stdlib/3a#frasi" /%}, division
- {% tooltip label="++rem:si" href="/language/hoon/reference/stdlib/3a#remsi" /%}, modulus (remainder after division), b modulo a as `@s`
- {% tooltip label="++abs:si" href="/language/hoon/reference/stdlib/3a#abssi" /%}, absolute value
- {% tooltip label="++cmp:si" href="/language/hoon/reference/stdlib/3a#synsi" /%}, test for greater value (as index, `>` → `--1`, `<` → `-1`, `=` → `--0`)

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

- Implement `++cosine`.

    {% math block=true %}
    \cos(x)
    = \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} x^{2n}
    = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots
    {% /math %}

    <!--
    \cos(x) = \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!}x^{2n} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots
    -->

- Implement `++tangent`.

    {% math block=true %}
    \tan(x) = \frac{\sin(x)}{\cos(x)}
    {% /math %}

    <!--
    \tan(x) = \frac{\sin(x)}{\cos(x)}
    -->

- As a stretch exercise, look up definitions for [exp
  (e^x)](https://en.wikipedia.org/wiki/Exponentiation#The_exponential_function)
  and [natural
  logarithm](https://en.wikipedia.org/wiki/Natural_logarithm), and
  implement these.  You can implement a general-purpose exponentiation
  function using the formula

    {% math block=true %}
    x^n = \exp(n \\, \text{ln} \\, x)
    {% /math %}

    <!--
    x^n = \exp(n \,\text{ln}\, x)
    -->

    (We will use these in subsequent examples.)

### Exercise:  Calculate the Fibonacci Sequence

The Binet expression gives the {% math %}n^\text{th}{% /math %}
Fibonacci number.

{% math block=true %}
F_n = \frac{\varphi^n - (-\varphi)^{-n}}{\sqrt 5}
= \frac{\varphi^n - (-\varphi)^{-n}}{2 \varphi - 1}
{% /math %}

<!--
F_n = \frac{\varphi^n-(-\varphi)^{-n}}{\sqrt 5} = \frac{\varphi^n-(-\varphi)^{-n}}{2 \varphi - 1}
-->

- Implement this analytical formula for the Fibonacci series as a {%
  tooltip label="gate" href="/glossary/gate" /%}.

##  Date & Time Mathematics

Date and time calculations are challenging for a number of reasons:
What is the correct granularity for an integer to represent?  What value
should represent the starting value?  How should time zones and leap
seconds be handled?

One particularly complicating factor is that there is no [Year
Zero](https://en.wikipedia.org/wiki/Year_zero); 1 B.C. is immediately
followed by A.D. 1. (The date systems used in astronomy
[differ](https://en.wikipedia.org/wiki/Julian_day#cite_note-7) from
standard time in this regard, for instance.)

In computing, absolute dates are calculated with respect to some base
value; we refer to this as the _epoch_.  Unix/Linux systems count time
forward from Thursday 1 January 1970 00:00:00 UT, for instance.  Windows
systems count in 10⁻⁷ s intervals from 00:00:00 1 January 1601.  The
Urbit epoch is `~292277024401-.1.1`, or 1 January 292,277,024,401 B.C.;
since values are unsigned integers, no date before that time can be
represented.

Time values, often referred to as _timestamps_, are commonly represented
by the [UTC](https://www.timeanddate.com/time/aboututc.html) value.
Time representations are complicated by offset such as timezones,
regular adjustments like daylight savings time, and irregular
adjustments like leap seconds.  (Read [Dave Taubler's excellent
overview](https://levelup.gitconnected.com/why-is-programming-with-dates-so-hard-7477b4aeff4c)
of the challenges involved with calculating dates for further
considerations, as well as [Martin Thoma's “What Every Developer Should
Know About Time”
(PDF)](https://zenodo.org/record/1443533/files/2018-10-06-what-developers-should-know-about-time.pdf).)

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

### Tutorial:  Julian Day

Astronomers use the [Julian
day](https://en.wikipedia.org/wiki/Julian_day) to uniquely denote days.
(This is not to be confused with the Julian calendar.)  The following
core demonstrates conversion to and from Julian days using signed
integer (`@sd`) and date (`@da`) mathematics.

```hoon {% copy=true mode="collapse" %}
|%
++  ju
  |%
  ++  to
    |=  =@da  ^-  @sd
    =,  si
    =/  date  (yore da)
    =/  y=@sd  (sun y.date)
    =/  m=@sd  (sun m.date)
    =/  d=@sd  (sun d.t.date)
    ;:  sum
      (fra (pro --1.461 :(sum y --4.800 (fra (sum m -14) --12))) --4)
      (fra (pro --367 :(sum m -2 (pro -12 (fra (sum m -14) --12)))) --12)
      (fra (pro -3 (fra :(sum y --4.900 (fra (sum m -14) --12)) --100)) --4)
      d
      -32.075
    ==
  ++  from
    |=  =@sd  ^-  @da
      =,  si
      :: f = J + 1401 + (((4 × J + 274277) ÷ 146097) × 3) ÷ 4 - 38
      =/  f  ;:  sum 
               sd
               --1.401
               (fra (pro (fra (sum (pro --4 sd) --274.277) --146.097) --3) --4)
               -38
             ==
      :: e = 4 × f + 3
      =/  e  (sum (pro --4 f) --3)
      :: g = mod(e, 1461) ÷ 4
      =/  g  (fra (mod e --1.461) --4)
      :: h = 5 × g + 2
      =/  h  (sum (pro --5 g) --2)
      :: D = (mod(h, 153)) ÷ 5 + 1
      =/  dy  (sum (fra (mod h --153) --5) --1)
      :: M = mod(h ÷ 153 + 2, 12) + 1
      =/  mn  (sum (mod (sum (fra h --153) --2) --12) --1)
      :: Y = (e ÷ p) - y + (n + m - M) ÷ n
      =/  yr  (sum (dif (fra e --1.461) --4.716) (fra (sum --12 (dif --2 mn)) --12))
      =/  dy=@ud  (div dy 2)
      =/  mn=@ud  (div mn 2)
      =/  yr=@ud  (div yr 2)
      (year [[a=(gth yr --0) yr] mn [dy 0 0 0 ~]])
--
```



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

### Entropy

You previously saw entropy introduced when we discussed stateful random
number generation.  Let's dig into what's actually going on with
entropy.

It is not straightforward for a computer, a deterministic machine, to
produce an unpredictable sequence.  We can either use a source of true
randomness (such as the third significant digit of chip temperature or
another [hardware
source](https://en.wikipedia.org/wiki/Hardware_random_number_generator))
or a source of artificial randomness (such as a sequence of numbers the
user cannot predict).

For instance, consider the sequence _3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3_.
If you recognize the pattern as the constant π, you can predict the
first few digits, but almost certainly not more than that.  The sequence
is deterministic (as it is derived from a well-characterized
mathematical process) but unpredictable (as you cannot _a priori_ guess
what the next digit will be).

Computers often mix both deterministic processes (called “pseudorandom
number generators”) with random inputs, such as the current timestamp,
to produce high-quality random numbers for use in games, modeling,
cryptography, and so forth.  The Urbit entropy value `eny` is derived
from the underlying host OS's `/dev/urandom` device, which uses sources
like keystroke typing latency to produce random bits.

### Random Numbers

Given a source of entropy to seed a random number generator, one can
then use the {% tooltip label="++og"
href="/language/hoon/reference/stdlib/3d#og" /%} door to produce various
kinds of random numbers.  The basic operations of `++og` are described
in [the lesson on subject-oriented
programming](/courses/hoon-school/O-subject).

### Exercise:  Implement a random-number generator from scratch

- Produce a random stream of bits using the linear congruential random
  number generator.

The linear congruential random number generator produces a stream of
random bits with a repetition period of {% math %}2^{31}{% /math %}.
Numericist John Cook [explains how LCGs
work](https://www.johndcook.com/blog/2017/07/05/simple-random-number-generator/):

> The linear congruential generator used here starts with an arbitrary seed, then at each step produces a new number by multiplying the previous number by a constant and taking the remainder by {% math %}2^{31} - 1{% /math %}.

**`/gen/lcg.hoon`**

```hoon {% copy=true mode="collapse" %}
|=  n=@ud                 :: n is the number of bits to return
=/  z  20.220.524         :: z is the seed
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
```

Can you verify that `1`s constitute about half of the values in this bit
stream, as Cook illustrates in Python?

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

- Convert the above to a `%say` {% tooltip label="generator"
  href="/glossary/generator" /%} that can optionally accept a seed; if
  no seed is provided, use `eny`.

- Produce a higher-quality Mersenne Twister uniform RNG, such as [per
  this
  method](https://xilinx.github.io/Vitis_Libraries/quantitative_finance/2022.1/guide_L1/RNGs/RNG.html).

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
- How would you implement other random number generators?

<!--
**`/gen/normal2.hoon`**

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
-->

##  Hashing

A [hash function](https://en.wikipedia.org/wiki/Hash_function) is a tool
which can take any input data and produce a fixed-length value that
corresponds to it.  Hashes can be used for many purposes:

1. **Encryption**.  A [cryptographic hash
   function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
   leans into the one-way nature of a hash calculation to produce a
   fast, practically-irreversible hash of a message.  They are
   foundational to modern cryptography.
2. **Attestation or preregistration**.  If you wish to demonstrate that
   you produced a particular message at a later time (including a
   hypothesis or prediction), or that you solved a particular problem,
   hashing the text of the solution and posting the hash publicly allows
   you to verifiably timestamp your work.
3. **Integrity verification**.  By comparing the hash of data to its
   expected hash, you can verify that two copies of data are equivalent
   (such as a downloaded executable file).  The
   [MD5](https://en.wikipedia.org/wiki/MD5) hash algorithm is frequently
   used for this purpose as
   [`md5sum`](https://en.wikipedia.org/wiki/Md5sum).
4. **Data lookup**.  [Hash
   tables](https://en.wikipedia.org/wiki/Hash_table) are one way to
   implement a key→value mapping, such as the functionality offered by
   Hoon's {% tooltip label="++map"
   href="/language/hoon/reference/stdlib/2o#map" /%}.

Theoretically, since the number of fixed-length hashes are finite, an
infinite number of possible programs can yield any given hash.  This is
called a [_hash
collision_](https://en.wikipedia.org/wiki/Hash_collision), but for many
practical purposes such a collision is extremely unlikely.

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

### Exercise:  Produce a secure password tool

- Produce a basic secure password tool.  It should accept a password,
  salt it (add a predetermined value to the password), and hash it.
  _That_ hash is then compared to a reference hash to determine whether
  or not the password is correct.
