# Manipulating Text

Biologists are interested in types of texts called sequences - DNA and protein that constitute much of the data dealt with

- programs biologists write need to work as part of a pipeline
- code needs to understand the output from some other program: `parsing` or produce output in a format that another program can operate on

**String** - refers to a piece of text in a computer program, sequence of characters

## Print

```python
# print a friendly greeting
print("Hello World")

```

1. _Statement_ - the entire line
2. _Function_ - `print()` built in python function
3. _Arguments_ - the value inside the `()`, parameters passed into functions

## Errors

1. `SyntaxError` - invalid syntax, Python can't understand the code - breaks the rules

- `EOL` - End of Line, starts reading a string in quiotes and got to end of line before encountered the closing quotation

2. `NameError` - shows the entire line where error occurred and which word Python doesn't understand

3. `AttributeError` - occurs when using an incorrect method on a data type

## Special Characters

```python
# Creates a newline in the middle of the string
print("Hello\nworld")
```

`\n` - adds a newline
`\t` - adds a tab character
`\r` - carriage return character, puts cursor back to start of the line, but doesn't start a new line, so you can use it to overwrite output

## Variables

- Containers that store values
- Variable now points to that value - assigning a variable

```python
# store short DNA seq in a variable
my_dna = "ATGGTA"

# print the sequence
print(my_dna)
```

## String Methods

Python has built in functions and methods (tools) for carrying out common operations on string values

### Concatenation

Concatenate (join) two strings together using the `+` symbol.

```python
# concatetnate strings
my_dna = "AATT" + "GGCC"

# AATTGGCC

upstream_dna = "AAA"
print(upstream_dna + my_dna)
# AAAAATTGGCC
```

### Length

`len()` function takes a single string argument, and returns the length of the string, outputing a number value
`str()` - takes a number as argument and returns a string
`int()` - takes a string argument, and returns a number representing the string

`int('4')` returns `4`

```python
# store return value of len() function in a variable
dna_length = len("ATCG")
print(dna_length) #4

print("The length of the DNA seq is" + str(dna_length))
```

### Changing Case

Can convert a string to lower and upper case using string _methods_

- _Methods_ - a function that belongs to a particular type, method is called on a data type
- returns a copy of the variable in lowercase - does NOT mutate the variable

```python
my_dna = "ATCG"
print("before" + my_dna)

lowercase_dna = my_dna.lower()
# print dna in lowercase
print(lowercase_dna)

print("after" + my_dna) # not mutated, remains the same

uppercase_dna = lowercase_dna.upper()
```

### Replacement

Replaces a string with another string, returns a copy

`replace()` - method that takes two string arguments, and returns a copy of the variable where all the occurrences of the first string are replaced by the second string

```python
protein = "vlspadktnv"

# replace valine with tyrosine
print(protein.replace("v", "y"))

# replace more than one character
print(protein.replace("vls", "ymt"))

# original variable is NOT mutated
print(protein) # vlspadktnv
```

### String Extraction

Extract a substring from a string. Get a _substring_ by following the variable name with a pair of square brackets which enclose a start and stop position, separated by a colon

```python
protein = "vlspadktnv"

# print pos 3 to 5
print(protein[3:5])
# pa
```

- start counting from position 0
- positions are inclusive at start
- exclusive at stop - does not include stop position

```python
print(protein[0:6])
# outpout: vlspad

# don't provide stop position goes to end of string
print(protein[2:])

# single number returns single character
print(protein[2]) # s
```

### Finding Substrings

A common job in biology is to count the number of times a pattern ocurs in a DNA or protein sequence. Counting the number of times a substring occurs in a string.

`count()`- takes a single argument and returns the number of times that argument is found in the variable (method)

```python
protein = "vlspadktnv"
# count amino acid residues - returns a number value
valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')
```

May also need to be able to find the location of a substring. Want to know where all the proline residues are in a sequence

`find()` method - takes a string argument, returns a number which is the position at which the substring first appears in the string, returns the `index` of the substring

- if unable to find the substring will return `-1`
- only works when finding exact substrings
- will not help if need to count the number of occurrencces of a variable protein motif or a variable TF binding site

```python
protein = "vlspadktnv"
print(str(protein.find('p')))
# output: 3
print(str(protein.find('kt')))
# output: 6
print(str(protein.find('w')))
# output: -1
```
