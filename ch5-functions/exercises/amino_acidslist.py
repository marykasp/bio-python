# function should accep a list of amino acid residues or have a default value
# return the percentage of the amino acid residues

def get_percentage_aa(protein, aa_list=["A", "I", "L", "M", "F", "W", "Y", "V"]):
  # print(protein)
  protein = protein.upper()
  length = len(protein)
  print("protein length: " + str(length))

  total = 0
  # need to check for each amino acid residue in the list
  for aa in aa_list:
    aa_count = protein.count(aa.upper())
    total = total + aa_count

  print("Total count of : " + str(aa_list) + "in protein: " + str(total))
  # this way introduces a rounded error
  # percentage = (total / length) * 100
  percentage = (total * 100) / length
  return percentage

print(get_percentage_aa("MSRSLLLRFLLFLLLLPPLP", ["M"]))
print(get_percentage_aa("MSRSLLLRFLLFLLLLPPLP", ["M", "L"]))

assert get_percentage_aa("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_percentage_aa("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_percentage_aa("MSRSLLLRFLLFLLLLPPLP") == 65
