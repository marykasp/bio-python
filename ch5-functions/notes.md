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

### Functions w/o arguments

```python
def get_a_number():
  return 42
```
