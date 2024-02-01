# Problem:  DNA sequence comprises two exons and one intro. First exon runs from the start of the seqeuence to base number 63
# Second econ runs from base 91 (count from 1) to end of sequence
# Write a program that will just print the coding regions of the sequence - Exon is coding region


dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

# splicesome - splits a DNA seq at 2 specified locations - creates 3 pieces

# extract exon 1 - start counting form 1 including base number 63
exon1 = dna[1:64]
print("Exon1: " + exon1)
exon2 = dna[91:] # starts counting from 
print("Exon2: " + exon2)

# print the coding region
print("Coding Region: " + exon1 + exon2)


## Splicing Introns Part Two: Using data from part one, write a program that will calculate what percentage of the DNA sequence is coding

dna_length = len(dna)
coding_length = len(exon1 + exon2)

print("DNA sequence length: " + str(dna_length))
print("Coding sequence length: " + str(coding_length))

percentage_coding = coding_length / dna_length * 100
print("Percentage of Coding: " + str(percentage_coding))
