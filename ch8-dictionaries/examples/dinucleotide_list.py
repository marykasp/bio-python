
dna = "ATGATCGATCGAGTGA"

dinucleotides = ['AA','AT','AG','AC',
                 'TA','TT','TG','TC',
                 'GA','GT','GG','GC',
                 'CA','CT','CG','CC']

# iterate over the list of dinucleoties to count each in the dna sequence
all_counts = []
for dinucleotide in dinucleotides:
  count = dna.count(dinucleotide)
  print("count is " + str(count) + " for " + dinucleotide)
  all_counts.append(count)

print(all_counts)

# find index of TG
i = dinucleotides.index("TG")
print(all_counts[i])
