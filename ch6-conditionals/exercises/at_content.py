# Problem: print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200

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
  expression = data_list[3]

  at_content = get_at_content(sequence)

  if at_content < 0.5 and int(expression) > 200:
    print(gene)



