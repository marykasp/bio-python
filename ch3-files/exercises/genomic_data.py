# Write a program that will split the genomic DNA into coding and non-coding parts (exons and introns)
# Write the sequence to two separate files

# Open and read the genomic dna text file
dna_file = open("genomic_data.txt")
dna_seq = dna_file.read().rstrip("\n")

# Print the full DNA sequence
print("DNA sequence: " + dna_seq)

# Split into exons and introns
exon1 = dna_seq[0:64] # 1 - 63 base
exon2 = dna_seq[91:] # base 91 to end of sequence
intron = dna_seq[64:91] # between both exons, starts at 64

# create a new write file
coding_file = open("coding_dna.txt", "w")
# add the exons to the file
coding_file.write(exon1 + exon2)

noncoding_file = open("noncoding_dna.txt", "w")
noncoding_file.write(intron)

