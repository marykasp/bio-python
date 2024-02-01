# Working With Files

Need to be able to extract data from a file to then be used in the program. Also better to separate data from the code.

We're lucky in biology in that many of the types of data that we work with are stored in text files which are relatively simple to process using Python. Chief among these, of course, are DNA and protein sequence data, which can be stored in a variety of formats. But there are many other types of data – sequencing reads, quality scores, SNPs, phylogenetic trees, read maps, geographical sample data, genetic distance matrices – which we can access from within our Python programs.

Another reason for our interest in file input/output is the need for our Python programs to work as part of a pipeline or work flow involving other, existing tools. When it comes to using Python in the real world, we often want Python to either accept data from, or provide data to, another program. Often the easiest way to do this is to have Python read, or write, files in a format that the other program already understands.

## Reading Text From File

Text files contain characters and lines - something that could be opened and viewed in a text editor

- _FASTA_ files of DNA sequences
- files containing output from command line programs (_BLAST_)
- _FASTQ_ containing DNA seq reads
- HTML files

Most files are **binary** files - ones made up of bytes

- image files
- compressed files (ZIP files)
- audio and video files

## Open & Read File

`open()` takes one argument (string which contains the name of the file) and returns a **file object**

```python
my_file = open("dna.txt")
```

`read()` - method which returns a string value of the file contents

```python
my_file = open("dna.txt")
file_contents = my_file.read()
print(file_contents)
```

#### Files, contents, filenames

```python
my_file_name = "dna.txt"
my_file = open(my_file_name)
file_contents = my_file.read()
```

Use the variable that stores name of file in the `open()` function which returns the file object. Then call the `read()` method on the file object, store the resulting string in a variable.

`my_file_name` - string stores the name of the file
`my_file` - file object
`file_contents` - string, stores the stext that is in the file

Simple program that reads the DNA sequence from a file and prints it out along with its length

```python
# open file
dna_file = open("dna.txt")

# read file contents
my_dna = dna_file.read()

# calculate the length
dna_length = len(my_dna)

print("sequence is " + my_dna + " and length is "  + str(dna_length))
```

Python adds a newline character at the end of the text file as part of its contents. The variable `my_dna` has a newline character at the end of it. When counting the length of the contents will also include the newline

`ACTGTACGTGCACTGATC\n`

**SOLUTION**: Strings have a method for removing newlings - `rstrip()`, takes one string argument which is the character that you want to remove.

```python
# open file
dna_file = open("dna.txt")

# read file contents
file_contents = dna_file.read()

# remove the newling from end of file
my_dna = file_contents.rstrip("\n")

# all in one:
my_dna = dna_file.read().rstrip("\n")

# calculate the length
dna_length = len(my_dna)

print("sequence is " + my_dna + " and length is "  + str(dna_length))
```

### Error: Missing Files

`IOError` - no such file or directory

### Writing Text to Files

To open a file for writing, use two argument version of `open()` function, where the second argument is a short string describing what we want to do to the file

- `r` for reading (default second argument)
- `w` for writing, if open a file that already exists then will overwrite the current contents with whatever new data we write
- `a` for appending, if open an existing file it will add new data onto th end , but will not remove any existing content

`write()` method write text to the file object - takes a single string argument

```python
my_file = open("out.txt", "w")
my_file.write("Hello world")

# open new file
new_file = open("out.txt")
contents = new_file.read().rstrip("\n")
```

### Closing Files

`close()` - file method that closes a file, returns no values

```python
my_file = open("out.txt", "w")
my_file.write("Hello")

# close the file
my_file.close()
```

## Paths and Folders

Need to give full path (seq of folder names that tells you the location of the file). Just give the path of the file as argument to `open()` rather than the file name.
