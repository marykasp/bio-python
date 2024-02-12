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
# this will return a keyError since AA count is 0 and those were not added to dictionary
# print(dinucleotide_counts["AA"])

if 'AA' in dinucleotide_counts:
  print(dinucleotide_counts['AA'])

print(dinucleotide_counts.get("AT"))
