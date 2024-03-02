def read_words(path):
  with open(path, 'r') as f:
    words = f.readlines()
  words = [word.strip() for word in words]

  return words

