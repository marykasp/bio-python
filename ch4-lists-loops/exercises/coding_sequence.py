# Problem: extract the exon segments from the genomic dna file, concatenate them and write to a new file

# open genomic dna file, read sequence
dna = open("genomic_dna.txt")
sequence = dna.read()

# print(sequence)

exons = open("exons.txt")

# will store each exon per loop of sequence
coding_sequence = ""
# loop over each line 
# read exon file line by line - split each exon line into two numbers
for exon in exons:
  # split the lines into a list
  positions = exon.split(",")
  # get individual positions from list - conver to integers
  start = int(positions[0])
  stop = int(positions[1])
  # print("start: " + start + " ,stop: " + stop)

  print("sequence: " + sequence)
  # use the start and stop positions to retrieve exon
  exon = sequence[start:stop]
  # add new exon onto coding sequence - concatenate all the exons
  coding_sequence = coding_sequence + exon
  print("exon: " + exon)


print("final coding seqeunce: " + coding_sequence)
# write the coding sequence to a new file
output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()
