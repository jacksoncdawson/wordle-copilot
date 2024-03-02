import helpers_tools
import json

ranks = {'a':{0:0, 1:0, 2:0, 3:0, 4:0}, 'b':{0:0, 1:0, 2:0, 3:0, 4:0}, 'c':{0:0, 1:0, 2:0, 3:0, 4:0}, 'd':{0:0, 1:0, 2:0, 3:0, 4:0}, 'e':{0:0, 1:0, 2:0, 3:0, 4:0}, 
         'f':{0:0, 1:0, 2:0, 3:0, 4:0}, 'g':{0:0, 1:0, 2:0, 3:0, 4:0}, 'h':{0:0, 1:0, 2:0, 3:0, 4:0}, 'i':{0:0, 1:0, 2:0, 3:0, 4:0}, 'j':{0:0, 1:0, 2:0, 3:0, 4:0}, 
         'k':{0:0, 1:0, 2:0, 3:0, 4:0}, 'l':{0:0, 1:0, 2:0, 3:0, 4:0}, 'm':{0:0, 1:0, 2:0, 3:0, 4:0}, 'n':{0:0, 1:0, 2:0, 3:0, 4:0}, 'o':{0:0, 1:0, 2:0, 3:0, 4:0}, 
         'p':{0:0, 1:0, 2:0, 3:0, 4:0}, 'q':{0:0, 1:0, 2:0, 3:0, 4:0}, 'r':{0:0, 1:0, 2:0, 3:0, 4:0}, 's':{0:0, 1:0, 2:0, 3:0, 4:0}, 't':{0:0, 1:0, 2:0, 3:0, 4:0},
         'u':{0:0, 1:0, 2:0, 3:0, 4:0}, 'v':{0:0, 1:0, 2:0, 3:0, 4:0}, 'w':{0:0, 1:0, 2:0, 3:0, 4:0}, 'x':{0:0, 1:0, 2:0, 3:0, 4:0}, 'y':{0:0, 1:0, 2:0, 3:0, 4:0},
         'z':{0:0, 1:0, 2:0, 3:0, 4:0}}

def ranks_get(words_path):
  
  words = helpers_tools.read_words(words_path)

  # get the rank of each letter in each position
  for word in words:
    for i in word:
      letter = word[i] 
      ranks[letter][i] += 1 
  return ranks

def ranks_print(ranks):
  for letter in ranks:
    print(f"{letter}: {ranks[letter]}")

def ranks_to_json(ranks):
  with open('ranks.json', 'w') as f:
    json.dump(ranks, f)

if __name__ == "__main__":

  try:
    ranks = ranks_get("/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.txt")
  except:
    print('Error getting ranks')
    exit(1)

  ranks_to_json(ranks)

  exit(0)