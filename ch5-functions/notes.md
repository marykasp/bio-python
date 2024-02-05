# Functions

Creating own functions to carry out a particular job allows us to reuse the same code many times within a program without having to rewrite every time.

If have to make a change in the code, only have to do in one place where the function is declarted.

Splitting code into functions also allows us to tackle larger problems, so can work on different bits of code independently. Can also reuse code across multiple programs.

### Defining a function

Create a function to calculate the `A` and `T` content of a sequence

- input: single DNA sequence
- output: decimal number

Function will take a single argument of type string and will return a value of type number.

```python
def get_at_content(dna):
  length = len(dna)
  a_content = dna.count("A")
  t_content = dna.count("T")

  at_content = (a_content + t_content) / length

  return at_content
```

`def` - short for **define**, when you write a function you define/declare the function, write name of function followed by arguments inside `()`

- **parameter** - variable name given to input when function is called
- **argument** - value passed into function when invoked
- variables defined in function **body** only exist inside the function (**block scoped**) and cannot be accessed outside the function.

- variable `dna` refers to the sequence that was passsed in as the argument to the function

- last line of function returns the AT content that was calculated in the function body

### Writing Functions:

1. make a clear distinction between defining a function and running it (**calling** a f(x))
2. execute a function by using function name followed by `()`

`get_at_content("ATGCTTGAT")`

This will call the function but the return value will vanish once been calculated since not being stored for future use:

```python
at_content = get_at_content("ATGACTGGACCA")
print(at_content)
print("AT content is " + str(at_content))
```

### Calling and improving f(x)

```python
my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))❶

print(get_at_content("ATGCATGCAACTGTAGC"))❷

# this will not work since inside the function the A and T content is case sensitive - uppercase
print(get_at_content("aactgtagctagctagcagcgta"))
```

`round()` - takes 2 arguments - the number want to round, and the number of significant figuures.

- convert input sequence to uppercase

```python
def get_at_content(dna):
  dna = dna.upper()
  length = len(dna)

  a_count = dna.count("A")
  t_count = dna.count("T")

  at_content = (a_count + t_count) / length

  return round(at_count, 2)

my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTGTAGC"))
print(get_at_content("aactgtagctagctagcagcgta"))
```

Add another argument to the function that accepts the number of significant figures

```python
def get_at_content(dna, sig_figs):
  dna = dna.upper()
  length = len(dna)

  a_count = dna.count("A")
  t_count = dna.count("T")

  at_content = (a_count + t_count) / length

  return round(at_count, sig_figs)

test_dna = "ATGCATGCAACTGTAGC"
print(get_at_content(test_dna, 1))
print(get_at_content(test_dna, 2))
print(get_at_content(test_dna, 3))
```

In the process of writing the code that used the function, we discovered a couple of problems with our original function definition. We were then able to go back and change the function definition, without having to make any changes to the code that used the function.

**encapsulation** - dividing up a complex program into little bits which we can work on independently.

- in the above example the code is divided into 2 parts: the part where we define the function, and the part where it is tested.

### Functions w/o arguments and return values

```python
def get_a_number():
  return 42
```

**keyword arguments** - allows to call functions in a different way, instead of giving a list of arguments in `()`, can supply a list of argument variable names and values

`get_at_content(dna="AGTCGGT", sig_figs=2)`

It doesn't rely on the order of arguments, so we can use whichever order we prefer. These two statements behave identically:

```python
get_at_content(dna="ATCGTGACTCG", sig_figs=2)
get_at_content(sig_figs=2, dna="ATCGTGACTCG")

get_at_content("ATCGTGACTCG", 2)
get_at_content(dna="ATCGTGACTCG", sig_figs=2)
get_at_content("ATCGTGACTCG", sig_figs=2)
```

Can't start off with keyword arguments then use without, will throw an error

`get_at_content(dna="ATCGTGACTCG", 2)`

### Default Arguments

Can specify the default value in the first line of the function definition:

```python
def get_at_content(dna, sig_figs=2):❶
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)
```

Now we have the best of both worlds. If the function is called with two arguments, it will use the number of significant figures specified; if it's called with one argument, it will use the default value of two significant figures. Let's see some examples:

```python
get_at_content("ATCGTGACTCG") # will use default argument
get_at_content("ATCGTGACTCG", 3)
get_at_content("ATCGTGACTCG", sig_figs=4) # will override default argument
```

Function argument defaults allow us to write very flexible functions which can have varying numbers of arguments. It only makes sense to use them for arguments where a sensible default can be chosen – there's no point specifying a default for the dna argument in our example. They are particularly useful for functions where some of the optional arguments are only going to be used infrequently.

## Testing Functions

Important to check that code does what you intend it to do

`assert` pythons built in tool for testing functions

- an assertion consists of the word `assert` followed by call to the function, then two equals signs `==`, then result expected

`assert get_at_content("ATGC") == 0.5`
if assertion turns out to e false then the program will stop and get `AssertionError`

- check if functions are working as intended
- helpful in tracking down errors in program
- if all assertion tests pass but get an unexpected output then can be confident that the error does not lie in the function but in the code that calls it
- checks if by modifying a function we haven't introduced any new errors
- allow for a form of documentation - including a collection of assertion tests alongside a function can show exactly what output is expected from a given input
- can use assertions to test behavior of our function for unusual inputs

`assert get_at_content("ATCGNNNNNN") == 0.5`

This will currently be false since currently counting `N` as a character in the sequence

```python
def get_at_content(dna, sig_figs=2):
  dna = dna.replace("N", "").upper()

  length = len(dna)
  a_count = dna.count("A")
  t_count = dna.count("T")

  at_content = (a_count + t_count) / length
  return round(at_content, sig_figs)

# test suite
assert get_at_content("A") == 1
assert get_at_content("G") == 0
assert get_at_content("ATGC") == 0.5
assert get_at_content("AGG") == 0.33
assert get_at_content("AGG", 1) == 0.3
assert get_at_content("AGG", 5) == 0.33333

```
