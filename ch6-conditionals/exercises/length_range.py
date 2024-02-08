data = open("data.csv")

for line in data:
  data_list = line.rstrip("\n").split(",")
  # species = data_list[0]
  sequence = data_list[1]
  gene = data_list[2]
  # expression = data_list[3]

  if len(sequence) > 90 and len(sequence) < 110:
    print(gene)
