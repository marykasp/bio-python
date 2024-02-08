# for each gene print out a message giving the gene name 

data = open("data.csv")

def get_at_content(dna):
  seq_length = len(dna)
  a_content = dna.upper().count("A")
  t_content = dna.upper().count("T")

  at_content = (a_content + t_content) / seq_length
  return at_content


for line in data:
  data_list = line.rstrip("\n").split(",")
  species = data_list[0]
  sequence = data_list[1]
  gene = data_list[2]
  expression = int(data_list[3])

  if get_at_content(sequence) > 0.65:
    print(gene + " has high AT content")
  elif get_at_content(sequence) < 0.45:
    print(gene + " has low AT content")
  else:
    print(gene + " has medium AT content")
