# Regular Expressions

In biology there is a lot of searching for patterns in strings.

- protein domains
- DNA transcription factor binding motifs
- restriction enzyme cut sites
- degenerate PCR primer sites
- runs of mononucleotides

Most of other types of data to deal with comes in the form of strings inside text files

- read mapping locations
- taxonomic names
- gene names
- gene accession numbers
- BLAST search results

Some tools that involve pattern recognition in strings, searching for a pattern:

- counting amino acid residues in proteins
- identify RE cut sites in DNA sequences

More flexible pattern problems:

1. given a DNA sequence, what's the length of the poly A tail?
2. given a gene accession name, extract the part between the third character and the underscore
3. given protein sequence, determine if it contains a highly redundant protein domain motif

## Modules in Python

Examples include tools for doing advanced mathematical calculations, for downloading data from the web, for running external programs, and for manipulating date.

Each collection of specialized tools is just a collection of functions and data types (**module**)

Python does not make these specialized modules available in each new program, instead of have explicitly load each module of tools we want to use.

`import` statement allows us to import modules
`import re` - imports program that uses regular expression tools

When we then want to use one of the tools from a module, we have to prefix it with the module name. `re.search(pattern, string)`

### Raw strings

Writing regular expressions requires a lot of special characters
If put `r` before the opening of a quotation mark, then any specialized character inside the string are ignored. `r` stands for raw, which is python's description for a string where special characters are ignored.

```python
import re

print(r"\n\t") # new line and tab character ignored
#\n\t
```

This special _raw_ notation will be used in all regular expression code examples

## Searching for a pattern in a string

`re.search()` - true/false function that determines whether or not a pattern appears somewhere in a string

- accepts 2 strings as arguments - first is pattern you want to search for, and the second is the string you want to search in

EX. See if a DNA sequence contains en **EcoRI** restriction site

```python
dna = "ATCGCGAATTCAC"

if re.search(r"GAATTC", dna):
  print("restriction site found in " + dna)
```

EX. Check for presence of an **AvaII** recognition site (`GGACC and GGTCC`)

```python
dna = "ATCGCGAATTCAC"

if re.search(r"GGACC", dna) or re.search(r"GGTCC", dna):
  print("restriction site found for AVaII")
```

### Alternation

**ALternation** - represent a number of different alternatives, write inside `()` by a `|` character

`GG(A|T)CC`

```python
dna = "ATCGCGAATTCAC"

# use alternation to capture use a single capture to capture all variations searching for
if re.search(r"GG(A|T)CC", dna):
  print("restriction site found for AVaII")
```

## Character Groups

EX. **BisI** RE cuts a wide range of motifs that have the pattern `GGNGC`

`GG(A|T|G|C)GC`

Can write the above pattern more concisely by using a pair of `[]`
`GG[ATGC]GC` - GGAGC, GGTGC, GGGGC, GGCGC

```python
dna = "ATCGCGAATTCA"

if re.search(r"GG[ATGC]GC", dna):
  print("restriction site found")
```

1. Want a character in a pattern to match **any** character in the input use a period

`GC.GC` would match all four possibilites for BisI, but would also match any character that is not a DNA base like `N`

2. Can specify characters don't want to match `[^XYZ]`, will negate it and match any characters not in this group, match all characters besides X, Y, and Z

## Quantifiers

**quantifiers** let us describe variation in the number of times a section of a pattern is repeated

1. `GAT?C` - a question mark following a character means that character is optional - it can match either zero or one times

`GAT?C` - `T` is optional, `GATC` or `GAC`

2. `GGA+TTT` - a plus sign following a character or group means that the character or group **must** be present that can be repeated any number of times - will mach more than one time

`GGA+TTT` - `GGATTT`, `GGAATTT`, `GGAAATTT`

3. `GGGA*TTT` - asterik following a character or group means that the character or group is **optional**, but can also be repeated

- will match zero or more times

`GGGA*TTT` - `GGGATTT`, `GGGAATTT`, `GGGAAATTT`, `GGGTTT`

4. `{}` to match a specific number of repeats

`GA{5}T` - `GAAAAAT`

5. `{2,4}` will match a range of repeats

`GA{2,4}T` - `GAAT`, `GAAAT`, `GAAAAT`

## Positions

Represent positions in the input string. `^` matches the **start** of a string, and the `$` matches **end** of a string

`^AAA` - AAATTT but not GGGAAATTT, 3 As need to be at the beginning of sequence
`GGG$` - AAAGGG but not AAAGGGCCC, sequence ends in 3 Gs

## Combining - character groups, quantifiers (?, +, \*, {}), positions (^, $)

`^AUG[AUGC]{30, 1000}A{5,10}$`

- `ATG` start codon at beginning of sequence
- followed by between 30 to 1000 bases which can be `A, U, G, C`
- followed by a poly A tail between 5 and 10 bases at the end of the sequence

`re.match(pattern, string)` - will only identify a pattern if it matches the **entire** string
`re.search(pattern, string)` - will identify a pattern occurring **anywhere** in the string

## Using Patterns

### Extracting part that matched

Want to find if a patttern matched, but **what part** of the string was matched

`re.search(pattern, string).group()`

- if `re.search()` finds a match it returns an objecgt that is evaluated as true in a conditional context, returns a _match object_
- _match object_ - represents the results of a regular expression search, has useful methods for extracting data out of it
- `group()` method on match object - returns the portion of the input string that matched the pattern

EX. determine if a DNA sequence contains any bases that are NOT A, T, G, or C

- use negated character group

```python
dna = "ATCGCGNAATTCAC"

# returns true if dna sequence contains a character that is NOT part of these listed
if re.search(r"[^ATGC]", dna):
  print("ambigious base found")

# if returns true then the DNA sequence contains a non-ATCG base, but won't tell what the base was
m = re.search(r"[^ATGC]", dna):

if m:
  print("ambigious base found")
  ambigious_base = m.group()
  print("the base is " + ambigious_base)

# ambigious base found
# the base is N
```

### Extracting multiple groups

```python
scientific_name = "Homo sapiens"

# . is all characters
# + repeated one more many times
# followed by space with same pattern
m = re.search(r"(.+) (.+)", scientific_name)
print("match object " + m)

if m:
  genus = m.group(1)
  species = m.group(2)
  print("genus is " + genus + " " + "species is " + species)
```

`()` in regular expressions:

1. surrounding alternatives in an alternation
2. grouping parts of a pattern for use with quantifier, quantifiers follow the group (`+, ?, *, {}`)
3. defining parts of a pattern to be extracted after the match

### Getting match positions

As well as containing information abot the **contents** of a match, the match object also holds information abou the **position** of the match.

- `start()` and `end()` methods get the positions of the start and end of the pattern on the string

```python
m = re.search(r"[^ATGC]", dna):
# returns true if any ambigious bases found

if m:
  print("ambigious base found")
  ambigious_base = m.group()
  print("the base is " + ambigious_base)
  print("at position " + str(m.start()))
```

### Multiple Matches

The above method can only find a single ambigious base, `re.search` only finds a single match anywhere in the string. To process multiple matches, we need to switch to `re.finditer()`, which returns a list of match objects which can be processed with a loop

```python
dna = "CGCTCNTAGATGCGCRATGATGCAVTGC"

matching = re.finditer(r"[^AGTC]", dna)

for m in matches:
  base = m.group()
  pos = m.start()
  print(base + " found at position " + str(pos))

# N found at position 5
# R found at position 15
# Y found at position 25
```

### Getting multiple matches as strings
