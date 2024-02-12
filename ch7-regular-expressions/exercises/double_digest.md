# Double Digest

Find fragment length of DNA sequence if digested with a RE

- open and read the file
- `re.finditer()` to figure out the positions of the cut sites, may be multiple
- pattern for AbcI site: `ANT/AAT` - `N` means any base
  `A[AGTC]TAAT`

- pattern for AbcII site: `GCRW/TC` - `R` means A or G, `W` means A or T
  `GC[AG][AT]TG`

```python
dna = open("dna.txt").read().rstrip("\n")

print("AbcI RE site starts at: ")
# iterate over list of match options to get start position of pattern that matches
for match in re.finditer(r"A[AGTC]TAAT", dna):
  print(match.start())


print("AbcI cuts at: ")
for match in re.finditer(r"A[AGTC]TAAT", dna):
  print(match.start() + 3)
```

Save these cut positions in a list include start index and final index

```python
all_cuts = [0]

for match in re.finditer(r"A[AGTC]TAAT", dna):
  all_cuts.append(match.start() + 3)

all_cuts.append(len(dna))
print(all_cuts)
```

Loop over a range from 1 to length of dna and get fragment lengths

```python

for i in range(1, len(dna)):
  this_cut_position = all_cuts[i]
  previous_cut_position = all_cuts[i-1]
  fragment_length = this_cut_position - previous_cut_position
  print("one fragment size is: " + fragment_length)
```
