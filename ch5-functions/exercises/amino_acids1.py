# Problem: Write a function that takes 2 argumens - a protein sequence and an amino acid residue
# Returns the percentage % of the protein that the amino acid makes up

def get_percentage_aa(protein, aa):
  # print(protein)
  protein = protein.upper()
  length = len(protein)
  aa_count = protein.count(aa.upper())

  percentage = (aa_count / length) * 100
  return percentage


print(get_percentage_aa("MSRMM", "M"))


assert get_percentage_aa("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_percentage_aa("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_percentage_aa("msrslllrfllfllllpplp", "L") == 50
assert get_percentage_aa("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
