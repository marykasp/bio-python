# Write a program that will create a FASTA file for 3 sequences

header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
seq_3 = seq_3.replace("-", "")
# print(seq_3)

fasta_output = open("sequences.fasta", "w")

fasta_output.write(">" + header_1 + "\n" + seq_1 + "\n")

fasta_output.write(">" + header_2 + "\n" + seq_2.upper() + "\n")

fasta_output.write(">" + header_3 + "\n" + seq_3 + "\n")

