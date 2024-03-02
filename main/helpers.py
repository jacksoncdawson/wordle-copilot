def read_words(path):
  with open(path, 'r') as f:
    words = f.readlines()
  words = [word.strip() for word in words]

  return words

def read_to_set(path):
  words_set = set()
  with open(path, 'r') as f:
    for line in f:
      words = line.split()
      words_set.update(words)
  return words_set