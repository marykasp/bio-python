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
