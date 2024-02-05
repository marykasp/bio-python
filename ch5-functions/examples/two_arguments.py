def get_at_content(dna, sig_figs):
  dna = dna.upper()

  length = len(dna)
  a_count = dna.count("A")
  t_count = dna.count("T")

  at_content = (a_count + t_count) / length
  return round(at_content, sig_figs)

test_dna = "ATGCATGCAACTGTAGC"
print(get_at_content(test_dna, 1))
print(get_at_content(test_dna, 2))
print(get_at_content(test_dna, 3))
