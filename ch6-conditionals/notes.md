# Conditional Tests

Most real life problems require decision making: to examine a property of some bit of data and decide what to do with it.
**Conditional statements** are features of python that allow us to build decision points in code. Allow programs to decide which out of a number of possible courses of action to take

## Conditions

Condition is a bit of code that produces `True` or `False` (boolean values)

```python
print(3 == 5) # false
print(3 > 5) # false
print(3 <=5) # true
print(len("ATGC") > 5) # false
print("GAATTC".count("T") > 1) # true
print("ATGCTT".startswith("ATG")) # true
print("ATGCTT".endswith("TTT")) # false
print("ATGCTT".isupper()) # true
print("ATGCTT".islower()) # false
print("V" in ["V", "W", "L"]) # true
```

- equals (represented by ==)
- greater and less than (represented by > and <)
- greater and less than or equal to (represented by >= and <=)
- not equal (represented by !=)
- is a value in a list (represented by `in`)
- are two objects the same1 (represented by `is`)

Many data types also provide methods that return True or False values, which are often a lot more convenient to use than the building blocks above. We've already seen a few in the code sample above: for example, strings have a startswith() method that returns True if the string on which the method is called starts with the string given as an argument.

#### `if` statements

```python
expression_level = 125
if expression_level > 100:
  print("gene is highly expressed")

# list of gene accession names
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']

for accession in accs:
  if accession.startswith('a'):
    print(accession)

```

#### `else` statements

Often we need an either/or type of decision, where have two possible actions to take.

```python
expression_level = 125
if expression_level > 100:
  print("gene is highly expressed")
else:
  print("gene is lowly expressed")
```

Ex. split up a list of accession names into two different files - those that start with `a` go into first file, and all other accessions go into second file

```python
file1 = open("one.txt", "w")
file2 = open("two.txt", "w")

accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']

for accession in accs:
  if accession.startswith('a'):
    file1.write(accession + "\n")
  else:
    file2.write(accession + "\n")

```

#### `elif` statements

If want more than two possible branches can use an `elif` statement:

```python
file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")

accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    elif accession.startswith('b'):
        file2.write(accession + "\n")
    else:
        file3.write(accession + "\n")

```

This kind of `if/elif/else` structure is very useful when we have several mutually-exclusive options. In the example above, only one branch can be true for each accession number – a string can't start with both "a" and "b". If we have a situation where the branches are not mutually exclusive – i.e. where more than one branch can be taken – then we simply need a series of if statements:

```python
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    if accession.endswith('z'):
        file2.write(accession + "\n")
    if len(accession) == 4:
        file3.write(accession + "\n")
    if accession.count('j') > 5:
        file4.write(accession + "\n")
```

### `while` loops

Can use conditions to determine when to exit a loop

- loops that iterate over a collection of elements (`list`, `string`, `file object`) - runs a set number of times
- `while` loop runs until a certain condition is met

```python
# increments a count variable once each time round the loop, stops when the count variable reaches 10
count = 0
while count<10:
    print(count)
    count = count + 1
```

## Complex Conditions

Imagine we want to go through our list of accessions and print out only the ones that start with "a" and end with "3". We could use two nested if statements:

```python
# both conditions must be true
for accession in accs:
  if accession.startswith("a") and accession.endswith("3"):
    print(accession)

# either conditions are true
for accession in accs:
    if accession.startswith('a') or accession.startswith('b'):
        print(accession)
```

Can use `and` `or` (logical conditionals, boolean operators) produce complex conditions that will be `true` if either of the two simple conditions are true

```python
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if (acc.startswith('a') or acc.startswith('b')) and acc.endswith('4'):
        print(acc)
```

Finally, we can negate any type of condition by prefixing it with the word `not`.

```python
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if acc.startswith('a') and not acc.endswith('6'):
        print(acc)
```

## `True/False` Functions

Sometimes want to write a function that can be used in a condition. Just make sure the function always returns a boolean

```python
def is_at_rich(dna):
  length = len(dna)
  a_count = dna.upper().count("A")
  t_count = dna.upper().count("T")
  at_content = (a_count + t_count) / length

  return at_content > 0.65


print(is_at_rich("ATTATCTACTA")) # True
print(is_at_rich("CGGCAGCGCT")) # False

# can be used as a condition
if is_at_rich(dna):
  # perform some task if returns true
```

## Recap

In this short section, we've dealt with two things: conditions, and the statements that use them. We've seen how simple conditions can be joined together to make more complex ones, and how the concepts of truth and falsehood are built in to Python on a fundamental level. We've also seen how we can incorporate True and False in our own functions in a way that allows them to be used as part of conditionsWe've been introduced to four different tools that use conditions – if, else, elif, and while – in approximate order of usefulness.
