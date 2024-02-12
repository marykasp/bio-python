# Problem: Write a program that will print only the accession names that satisfy this criteria - treat each criterion separately

"""
- contains number 5
- contains letter d or e
- contain the letters d and e 
- contain the letters d and e in that order with a single letter
- start with x or y
- start with x or y and end with e
- contain 3 or more digits in a row
- end with d followed by either a, r, or p
"""
import re
# accession_names = open("accessions.txt").read()
# print(accession_names)

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']


print("Accession names with number 5:")
for acc in accessions:
  # print if passes test
  if re.search(r"5", acc):
    print(acc)

# find names that contain d or e
print("Accession names with d or e character:")
for acc in accessions:
  if re.search(r"(d|e)", acc):
    print(acc)

print("Accession names that contain both d and e in that order:")
# period any character, asterik character or grouup is optional, so any of those characters following g are optional
for acc in accessions:
  if re.search(r"d.*e", acc):
    print(acc)

print("Names that contain both d and e in that order with a single letter between")
for acc in accessions:
  if re.search(r"d.e", acc):
    print(acc)

print("Names with d and e in any order")
for acc in accessions:
  if re.search(r"(d.*e|e.*d)", acc):
    print(acc)


print("Names that start with x or y")
for acc in accessions:
  if re.search(r"^(x|y)", acc):
    print(acc)

print("Ends with e")
for acc in accessions:
  if re.search(r"^(x|y).*e$", acc):
    print(acc)

print("contains 3 or more digits in a row")
# for acc in accessions:
#   if re.search(r"[0123456789]{3, 100}", acc):
#     print(acc)

# character group of all digits is common that there is a built in shorthand \d
for acc in accessions:
  if re.search(r"\d{3,}", acc): 
    print(acc)

print("end with d followed by either a, r, or p")
for acc in accessions:
  if re.search(r"d[arp]$", acc):
    print(acc)
