# Problem: Write a program that will print out the AT content of this DNA sequence (proportion of bases that are either A OR T)
# AT_content = A + T / sequence length

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_length = len(dna)

# count A content
a_content = dna.count("A")
t_content = dna.count("T")

print("length: " + str(dna_length))
print("A count: " + str(a_content))
print("T count: " + str(t_content))

at_content = (a_content + t_content) / dna_length

print("AT content of dna sequence is: " + str(at_content))
# print(37 / 54)
