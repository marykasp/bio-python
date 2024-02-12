dna = "ATGATCGATCGAGTGA"

dinucleotides = ['AA','AT','AG','AC',
                 'TA','TT','TG','TC',
                 'GA','GT','GG','GC',
                 'CA','CT','CG','CC']

dinucleotide_counts = {}

for dinucleotide in dinucleotides:
  count = dna.count(dinucleotide)
  dinucleotide_counts[dinucleotide] = count

print(dinucleotide_counts)
print(dinucleotide_counts["AA"])
