# Problem: Sequence contains recognition site for `EcoRI` RE, which cuts at motif `G*AATTC`, write a program which will calculate the size of the two fragments produced when the DNA is digested by EcoRI

dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

dna_length = len(dna)
# print("Sequence length: " + str(len(dna)))
# Find the substring index where EcoRI cuts
ecoRI_cutsite = dna.find("GAATTC")
print("cutsite at index: " + str(ecoRI_cutsite))

fragment1_length = ecoRI_cutsite + 1
print("Fragment 1 length: " + str(fragment1_length))

fragment2_length = dna_length - fragment1_length 
print("Fragment 2 length: " + str(fragment2_length))
