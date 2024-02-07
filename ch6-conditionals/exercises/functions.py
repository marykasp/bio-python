data = open("data.csv")

def get_data(file):
  all_data = []
  for line in file:
    data_list = line.rstrip("\n").split(",")
    species = data_list[0]
    sequence = data_list[1]
    gene = data_list[2]
    expression = data_list[3]

    all_data.append([species, sequence, gene, expression])
  
  return all_data

print(get_data(data))

