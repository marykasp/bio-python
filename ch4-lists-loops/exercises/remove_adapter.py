# Problem: File input contains a number of DNA seqs, one per line
# Each sequence starts with a 14 base pair fragment - adapter
# Trim this adapter and write the cleaned sequences to a a new file

# open the file
dna_file = open("input.txt")

# create an output file
output = open("trimmed.txt", "w")

# loop over the lines in the file object
for sequence in dna_file:
  print(sequence)
  # adapter sequence
  adapter = sequence[0:14]

  # get the substring from 15 base to end
  trimmed_sequence = sequence[14:]

  # get the length of the trimmed sequence
  trimmed_length = len(trimmed_sequence)

  # write clean sequence to new file
  output.write(trimmed_sequence)

  # print out the adapter sequence
  print("adapter sequence: " + adapter)
  # print the length of each sequence to screen
  print("processed sequence with new length: " + str(trimmed_length))
