header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
seq_3 = seq_3.replace("-", "")

# create and write fasta files for each sequence, file name of header
fasta_seq1 = open(header_1 + ".fasta", "w")
fasta_seq1.write(">" + header_1 + "\n" + seq_1 + "\n")

fasta_seq2 = open(header_2 + ".fasta", "w")
fasta_seq2.write(">" + header_2 + "\n" + seq_2 + "\n")

fasta_seq3 = open(header_3 + ".fasta", "w")
fasta_seq3.write(">" + header_3 + "\n" + seq_3 + "\n")
