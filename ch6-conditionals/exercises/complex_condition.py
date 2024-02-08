# Problem: print out the gene names for all genes whose name begins with k or h except those belonging to Drosophila melanogaster

data = open("data.csv")

for line in data:
  data_list = line.rstrip("\n").split(",")
  species = data_list[0]
  sequence = data_list[1]
  gene = data_list[2]
  expression = int(data_list[3])

  if (gene.startswith("k") or gene.startswith("h")) and species != "Drosophila melanogaster":
    print(gene)

