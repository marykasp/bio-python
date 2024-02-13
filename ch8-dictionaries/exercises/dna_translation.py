gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# DNA to split into codons and turn into a protein sequence
dna = "ATGTTCGGT"
# print("dna length: " + str(len(dna)))
# substring notation
codon1 = dna[0:3]
codon2 = dna[3:6]
codon3 = dna[6:]
# print(codon1, codon2, codon3)

# use range to generate a sequence of numbers starting from 0, stepwise of 3
# start at 0, stop at 3 less than length of dna sequence
  
def translate_dna(dna):
  protein = ""

  last_pos = len(dna) - 2 
  for start_pos in range(0, last_pos, 3):
    codon = dna[start_pos:start_pos+3]
    aa = gencode.get(codon, "X")
    print("codon: " + codon)
    # string concatenation
    protein = protein + aa

  return protein

print(translate_dna(dna))
print(translate_dna("ATGTTCGGTA"))

# trying sequence with undetermined base
print(translate_dna("ATGTTNCGGT"))

