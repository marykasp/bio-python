bases = ["A", "G", "T", "C"]
dna = "AATGATGAACGAC"

all_counts = {}
# instaed of using list create list using nested for loop
for base1 in bases:
  for base2 in bases:
    dinucleotide = base1 + base2
    count = dna.count(dinucleotide)
    # if count is not 0 add key:value pair to dict
    if count > 0:
      all_counts[dinucleotide] = count

print(all_counts)
