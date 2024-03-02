import json
import helpers
import string

answers_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/answers.txt"
ranks_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/main/ranks.json"
words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.txt"

def main(guess, state):
  

  print("check 1")
  # check if the guess and state are valid
  if (len(guess) != 5) or (not guess.isalpha()):
    print("Invalid guess")
    print("Guess must be 5 letters long and only contain lowercase letters")
    return True
  elif (len(state) != 5) or any(char not in "xyg" for char in state):
    print("Invalid state")
    print("State must be 5 letters long and only contain 'x', 'y', or 'g'")
    return True

  print("check 2")
  words = helpers.read_to_set(words_path)
  # answers = helpers.read_to_set(answers_path)
  ranks = json.load(open(ranks_path))
  

  # for each letter in the guess, first check if the matching position in state is 
  # "g"=(in the right spot), "y"=(in the word but not in the right spot), or "x"=(not in the word)
  # if the letter is "g", remove all words that don't have that letter in that position
  # if the letter is "y", remove all words that have that letter in that position and all words that don't have that letter in any position
  # if the letter is "x", remove all words that have that letter in any position

  print("check 3")
  for i in range(5):
    if state[i] == "g":
      words = {word for word in words if word[i] == guess[i]}
    elif state[i] == "y":
      words = {word for word in words if word[i] != guess[i]}
    elif state[i] == "x":
      words = {word for word in words if guess[i] not in word}

  # for each word left, sum the ranks of the letters in the word
  # keep track of the word with the highest rank
  # if there are multiple words with the same highest rank, keep track of the one with the fewest letters in common with the guess (to maximize the amount of information gained) 
  # return the word with the highest rank

  print("check 4")
  max_rank = -1
  best_word = ""
  for word in words:
    print("check 4.1")

    rank = 0
    for i in range(5):
      for j in range(5):
        if i != j:
          rank += ranks[i][j] if word[i] == guess[j] else 0

    print("check 4.2")
    if rank > max_rank:
      max_rank = rank
      best_word = word
      print(best_word)

  print("check 5")
  print(best_word)
  return True

if __name__ == "__main__":
  
  try:
    main("print", "yxxxg")
  except:
    print('Error Occurred in main() function.')
    exit(1)
  
  exit(0)


# brine
# gxxyx