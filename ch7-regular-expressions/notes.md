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
