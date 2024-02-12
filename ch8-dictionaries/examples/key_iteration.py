# keys() method returns a list of keys in the dict

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

print(dinucleotide_counts.keys())

for dinucleotide in dinucleotide_counts.keys():
  if dinucleotide_counts.get(dinucleotide) == 2:
    print(dinucleotide)
