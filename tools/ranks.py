# Used to generate the ranks of the letters in the words.txt file.
# Not used in the main program.

import helpers_tools
import json

ranks = {'a':{0:0, 1:0, 2:0, 3:0, 4:0}, 'b':{0:0, 1:0, 2:0, 3:0, 4:0}, 'c':{0:0, 1:0, 2:0, 3:0, 4:0}, 'd':{0:0, 1:0, 2:0, 3:0, 4:0}, 'e':{0:0, 1:0, 2:0, 3:0, 4:0}, 
         'f':{0:0, 1:0, 2:0, 3:0, 4:0}, 'g':{0:0, 1:0, 2:0, 3:0, 4:0}, 'h':{0:0, 1:0, 2:0, 3:0, 4:0}, 'i':{0:0, 1:0, 2:0, 3:0, 4:0}, 'j':{0:0, 1:0, 2:0, 3:0, 4:0}, 
         'k':{0:0, 1:0, 2:0, 3:0, 4:0}, 'l':{0:0, 1:0, 2:0, 3:0, 4:0}, 'm':{0:0, 1:0, 2:0, 3:0, 4:0}, 'n':{0:0, 1:0, 2:0, 3:0, 4:0}, 'o':{0:0, 1:0, 2:0, 3:0, 4:0}, 
         'p':{0:0, 1:0, 2:0, 3:0, 4:0}, 'q':{0:0, 1:0, 2:0, 3:0, 4:0}, 'r':{0:0, 1:0, 2:0, 3:0, 4:0}, 's':{0:0, 1:0, 2:0, 3:0, 4:0}, 't':{0:0, 1:0, 2:0, 3:0, 4:0},
         'u':{0:0, 1:0, 2:0, 3:0, 4:0}, 'v':{0:0, 1:0, 2:0, 3:0, 4:0}, 'w':{0:0, 1:0, 2:0, 3:0, 4:0}, 'x':{0:0, 1:0, 2:0, 3:0, 4:0}, 'y':{0:0, 1:0, 2:0, 3:0, 4:0},
         'z':{0:0, 1:0, 2:0, 3:0, 4:0}}

# reads in file of words, updates the ranks dictionary with the frequency of each letter in each position
def ranks_get(words_path):
  
  words = helpers_tools.read_words(words_path)

  for word in words:
    for i in range(5):
      letter = word[i] 
      ranks[letter][i] += 1 
  return ranks

# normalizes the ranks dictionary to managable numbers but keeping the relative frequency of each letter in each position
def ranks_normalize(ranks):
  for letter in ranks:
    for i in range(5):
      ranks[letter][i] = round(ranks[letter][i] % 130)
  return ranks

# prints the ranks dictionary
def ranks_print(ranks):
  for letter in ranks:
    print(f"{letter}: {ranks[letter]}")

# writes the ranks dictionary to a json file
def ranks_to_json(ranks):
  with open('ranks.json', 'w') as f:
    json.dump(ranks, f)

if __name__ == "__main__":

  try:
    ranks = ranks_normalize(ranks_get("/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.txt"))
  except:
    print('Error getting ranks')
    exit(1)

  ranks_to_json(ranks)

  exit(0)