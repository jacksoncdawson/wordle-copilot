# About: This file contains helper functions for the tools used for setup
# Not used in the main program.

# reads in file of words, returns a list of the words
def read_words(path):
  with open(path, 'r') as f:
    words = f.readlines()
  words = [word.strip() for word in words]

  return words
