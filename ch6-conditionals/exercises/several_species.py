# Problem: Print out the gene names for all genes belonging to Drosophila melanogaster or Drosophila simulans

data = open("data.csv")

for line in data:
  data_list = line.rstrip("\n").split(",")
  species = data_list[0]
  sequence = data_list[1]
  gene = data_list[2]
  expression = data_list[3]
  if species == "Drosophila melanogaster" or species == "Drosophila simulans":
    print(gene)


