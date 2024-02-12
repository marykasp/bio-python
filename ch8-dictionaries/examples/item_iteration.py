dna = "ATGATCGATCGAGTGA"

dinucleotides = ['AA','AT','AG','AC',
                 'TA','TT','TG','TC',
                 'GA','GT','GG','GC',
                 'CA','CT','CG','CC']

dinucleotide_counts = {}

for dinucleotide in dinucleotides:
  count = dna.count(dinucleotide)
  if count > 0:
    dinucleotide_counts[dinucleotide] = count 


print(dinucleotide_counts)

# iterate over key:value pairs
for dinucleotide, count in dinucleotide_counts.items():
  if count == 2:
    print(dinucleotide)
