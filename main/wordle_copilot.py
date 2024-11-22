import json
from collections import deque

ranks_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/ranks.json"
words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.json"

def input_verify(guess, state):
  if (len(guess) != 5) or (not guess.isalpha()):
    print("Invalid guess")
    print("Guess must be 5 letters long and only contain lowercase letters")
    return False
  elif (len(state) != 5) or any(char not in "xyg" for char in state):
    print("Invalid state")
    print("State must be 5 letters long and only contain 'x', 'y', or 'g'")
    return False
  return True

def words_narrow(words, state, guess):
  for i in range(5):
    if state[i] == "g":
      words = [word for word in words if word[i] == guess[i]]
    elif state[i] == "y":
      words = [word for word in words if (word[i] != guess[i]) and (guess[i] in word)]
    elif state[i] == "x":
      # if the letter has not been 
      if not any(guess[i] == guess[j] and state[j] in ["g", "y"] for j in range(5)):
        words = [word for word in words if guess[i] not in word]
      else:
        words = [word for word in words if guess[i] != word[i]]
  return words

def get_best_word(words, ranks, guess):
  
  choices = deque(maxlen=5)
  best_word = ""
  best_rank = 0
  for word in words:
    rank = 0
    for i in range(5):
      rank += ranks[word[i]][str(i)]
    if rank > best_rank:
      best_rank = rank
      best_word = word

      choices.append(word)
        
    elif rank == best_rank:
      if sum([1 for i in range(5) if word[i] == guess[i]]) < sum([1 for i in range(5) if best_word[i] == guess[i]]):
        best_word = word
    
  return best_word, choices

def setup_library():
  words = json.load(open(words_path))
  ranks = json.load(open(ranks_path))
  return words, ranks

def main():

  words, ranks = setup_library()

  while True:
    guess = input("Guess: ")
    state = input("State: ")

    # verify input
    if not input_verify(guess, state):
      return False

    # narrow down words based on the state
    words = words_narrow(words, state, guess)
  
    if len(words) > 20:
      print("Remaining number of words: ", len(words))
    else:
      print("Remaining words: ", words)

    # find the word with the highest rank
    best_options = get_best_word(words, ranks, guess)

    print("Best Guess: ", best_options[0])

    print("Best Other Choices: ", best_options[1])
    
  
  return True

if __name__ == "__main__":
  
  try:
    if main() == False:
      exit(1)
  except Exception as e: 
    print(f'Error Occurred in main() function: {e}') 
    exit(1)
  
  exit(0)
