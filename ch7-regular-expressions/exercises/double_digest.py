import re

dna = open("dna.txt").read().rstrip("\n")

# print(dna)

all_cuts = [0]
print("AbcI cut sites: ")
for matches in re.finditer(r"A[AGTC]TAAT", dna):
  print(matches.start() + 3)
  all_cuts.append(matches.start() + 3)


print("AbcII cut sites: ")
for matches in re.finditer(r"GC[AG][AT]TG", dna):
  print(matches.start() + 4)
  all_cuts.append(matches.start() + 4)

all_cuts.append(len(dna))
print(all_cuts)
sorted_cuts = sorted(all_cuts)
print(sorted_cuts)

# iterate over the cut sites, find the current cut site and previous to calculate fragment length
for i in range(1, len(sorted_cuts)):
  current_cut_position = sorted_cuts[i]
  previous_cut_pos = sorted_cuts[i-1]
  fragment_length = current_cut_position - previous_cut_pos
  print("one fragment size is: " + str(fragment_length))
