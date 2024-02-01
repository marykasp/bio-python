# Problem: Write a program that will print the complement of this sequence
# dna = "ATCG" complement_dna = "TAGC"

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

# replace() method returns a new string
replacement = dna.replace("A", "t")
# print(replacement)
replacement1 = replacement.replace("T", "a")
# print(replacement1)
replacement2 = replacement1.replace("C", "g")
replacement3 = replacement2.replace("G", "c")

dna_complement = replacement3.upper()

print("Orginal DNA: " + dna)
print("Complement: " + dna_complement)
