# Dictionaries

## Storing paired data

If want to generate a complete list of counts by base pair for a sequence

Ex. Create a list of 16 possible dinucleotdies to iterate over, calculate count for each one in a sequence, and store all counts as list

```python
dna = "ATGATCGATCGAGTGA"
dinucleotides = ['AA','AT','AG','AC',
                 'TA','TT','TG','TC',
                 'GA','GT','GG','GC',
                 'CA','CT','CG','CC']
all_counts = []
for dinucleotide in dinucleotides:
    count = dna.count(dinucleotide)
    print("count is " + str(count) + " for " + dinucleotide)
    all_counts.append(count)
print(all_counts)
```

Now there are two lists have to keep track of, the list of dinucleotides to get index of a specific dinucleotide and using that index to find the count for that dinucleotide in all_counts list. As the list grows Python needs to iterate over each item in the list one at a time until it finds one looking for. So as size of list grows, the time taken to look up the count for a given elment will grow alongside it.

We need a way of storing pairs of data (dinucleotides and their counts) in a way that is efficient to look up the count for any given dinucleotide.

- protein sequence names and their sequence
- DNA RE names and their motifs key:list
- codons and their associated amino acid residues
- sample names and coodinates
- words and their definitions

dinucleotide - count
protein name - sequence
RE name - motif
codon - amino acid residue
sample - coordinates

## Creating Dictionary

Use `{}`, each pair of data consists of a key and value (item)

```python
enzymes = { 'EcoRI':r'GAATTC','AvaII':r'GG(A|T)CC', 'BisI':r'GC[ATGC]GC' }

enzymes = {
    'EcoRI' : r'GAATTC',
    'AvaII' : r'GG(A|T)CC',
    'BisI'  : r'GC[ATGC]GC'
}
```

To retrieve data from the dictionary use the key name

```python
print(enzymes['BisI'])
# r'GC[ATCG]GC'
```

## Building dictionaries

Create an empty dictionary then add key:value pairs to it

```python
enzymes = {}
enzymes['EcoRI'] = r'GAATTC'
enzymes['AvaII'] =  r'GG(A|T)CC'
enzymes['BisI'] =  r'GC[ATGC]GC'
```

`pop()` - method deletes key value from dictionary and returns the value

```python
enzymes.pop('EcoRI') # r"GAATTC"
```
