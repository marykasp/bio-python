# Lists and Loops

String manipulation - process single sequences
Writing/Reading Files - writing and reading a file at a time

Common situation in research is to have a large collection of data (DNA seqs, SNP positions, gene expression measurements) that all need to be processed in the same way.

To make our programs able to process **multiple pieces of data** we need a new complex data type that can hold many pieces of information at the same time -> `list`

`loops` are useful since they allow for repitition of code with slight variation.

## Creating Lists

```python
apes = ["homo sapiens", "pan troglodytes", "gorilla gorilla"]
conserved_sites = [25, 56, 132]
```

- each individual item in a list is called an **element**
- to get an element from a list write the name of the list followed by the **index** of the element in `[]`

```python
apes = ["homo sapiens", "pan troglodytes", "gorilla gorilla"]
conserved_sites = [25, 56, 132]

print(apes[2]) # gorilla gorilla
first_site = conserved_sites[0]
```

If we know which element we want but don't know the index can use `index()` method

```python
apes = ["homo sapiens", "pan troglodytes", "gorilla gorilla"]
conserved_sites = [25, 56, 132]

chimp_index = apes.index("pan troglodytes")
print(chimp_index) # 1

last_ape = apes[-1]
```

- get more than one item from a list use `[start:stop]`
- numbers inclusive at start, exclusive at end

```python
ranks = ["kingdom","phylum", "class", "order", "family"]
lower_ranks = ranks[2:5]
# lower ranks are class, order and family

```

#### Working with list elements

`append()` - add another onto end of existing list, called on list and takes a data type as an argument

- mutates the variable on which it is called

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
print(apes)
apes.append("Pan paniscus")
print(apes)
# ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla", "Pan pniscus"]
```

`len()` function returns the length of the list

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
print("There are " + str(len(apes)) + " apes")
# There are 3 apes

apes.append("Pan paniscus")
print("Now there are " + str(len(apes)) + " apes")
# There are 4 apes
```

Concatenate lists using `+` symbol - doesn't change the original lists, just makes a brand new list which contains elements from both lists

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
monkeys = ["Papio ursinus", "Macaca mulatta"]
primates = apes + monkeys

print(str(len(apes)) + " apes")
print(str(len(monkeys)) + " monkeys")
print(str(len(primates)) + " primates")
```

`extend()` - behaves like `append()` but takes a list of as its arguments rather than a single element

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
print(apes)
apes.extend(["Pan paniscus", "homo sapiens"])
print(apes)
```

`reverse()` - change the order of the elements in list, mutate the list called on
`sort()` - change order of elements, mutate list

```python
ranks = ["kingdom","phylum", "class", "order", "family"]
print("at the start : " + str(ranks))
# at the start : ['kingdom', 'phylum', 'class', 'order', 'family']

ranks.reverse()
print("after reversing : " + str(ranks))
# after reversing : ['family', 'order', 'class', 'phylum', 'kingdom']

ranks.sort()
print("after sorting : " + str(ranks))
# after sorting : ['class', 'family', 'kingdom', 'order', 'phylum']
```

### Writing a loop

If we wanted to do something with eache element in a list we can use a loop

Ex. For each element in the list of apes, print out the element, followed by the words "is an ape".

```python
for ape in apes:
  print(ape + " is an ape")
```

`for x in y` - y is the name of the list we want to process and x is the name we want to use for the current element each time round the loop

- `x` is just a variable name, the value of the variable will be automatically set to each element of the list in turn of the loop, so will be different each time round the loop
- first line of loop ends with `:` and all subsequent lines are indented (`block` of code)
- indented block is called the `body` of the looop and the lines inside will be executed once for each element in the list

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]

for ape in apes:
  name_length = len(ape)
  first_letter = ape[0]

  print(ape + " is an ape. Its name starts with " + first_letter)
  print("Its name has " + str(name_length) + " letters")
```

#### Indentation Errors

`IndentationError` - will occur when a line of code in the block does NOT match the others with indentation

`IndentationError: unindent does not match any outer indentation level`

### Using string as a list

A string has similar methods to a list - list index notation to get individual characters or substrings from a string, can also loop nottation to process a string as though it were a list

- each character in a string is treated as a separate element

```python
name = "python"
for character in name:
    print("one character is " + character)
```

**Iteration** - process of repeating a set of instructions for each element of a list (or character in a string) - iterate over a list or string

#### Splitting a string to make a list

These methods help produce lists as their outputs:
`split()` - called on strings, takes a single argument **delimiter** and splits the original string wherever it sees the delimiter, producing a list

```python
names = "melanogaster,simulans,yakuba,ananassae"
species = names.split(",")
print(str(species))
# ['melanogaster', 'simulans', 'yakuba', 'ananassae']
```

#### Iterating over lines in a file

A file object can also be iterated over - each line becomes an individual element

```python
file = open("some_input.txt") # returns a file object
for line in file:
    # do something with the line
```

Notice that in this example we are iterating over the file object, not over the file contents. If we iterate over the file contents like this:

```python
file = open("some_input.txt")
contents = file.read() # returns content of file object
for line in contents:
    # warning: line contains just a single character!
```

then each time round the loop we will be dealing with a single character, which is probably not what we want. A good way to avoid this mistake is to ask yourself, whenever you open a file, whether you want to get the contents as one big string (in which case you should use read()) or line-by-line (in which case you should iterate over the file object).

`File objects` are **exhaustible** - once we have iterated over a file object, python remembers that it is already at the end of the file, so when try to iterate over it again with another loop, there are no lines remaining to be read.

```python
# print the length of each line
file = open("some_input.txt")
for line in file:
    print("The length is " + str(len(line)))
file.close()

# print the first character of each line
file = open("some_input.txt")
for line in file:
    print("The first character is " + line[2])
file.close()
```

A better approach is to read the lines of the file into a list, then iterate over the list (which we can safely do multiple times). The file object readlines() method returns a list of all the lines in a file, and we can use it like this:

`readlines()` method returns a list of all the lines in a file

```python
# first store a list of lines in the file
file = open("some_input.txt")
all_lines = file.readlines()

# print the lengths
for line in all_lines:
    print("The length is " + str(len(line)))

# print the first characters
for line in all_lines:
    print("The first character is " + line[2])
```

### Looping with ranges

Iterating over a list of numbers

```python
protein = "vlspadktnv"
```

Ex. print out first 3 residues, then first four, etc....

```python
print(protein[0:1])
print(protein[0:2])
print(protein[0:3])
```

but this seems cumbersome, and only works if we know the length of the protein sequence in advance. A better solution is to use the range() function. range() is a built in Python function that generates lists of numbers. The behaviour of range() depends on how many arguments we give it. Below are a few examples, with the output following directly after the code.

`range()` built in function that generates a list of numbers

- single argument will count up from 0 to that number, exluding that number

```python
for num in range(6):
  print(num)
  # 0 1 2 3 4 5
```

- with two numbers range will count from from the first number to the second (exclusive)

```python
for num in range(3, 8):
  print(num)
  # 3 4 5 6 7
```

- With three numbers, range() will count up from the first to the second with the step size given by the third:

```python
for num in range(2, 14, 4):
  print(num)
  # 2 6 10
```
