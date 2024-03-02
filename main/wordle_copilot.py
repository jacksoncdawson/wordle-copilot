import json
import helpers

answers_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/answers.txt"
ranks_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/main/ranks.json"
words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.txt"

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
      words = {word for word in words if word[i] == guess[i]}
    elif state[i] == "y":
      words = {word for word in words if (word[i] != guess[i] and guess[i] in word)}
    elif state[i] == "x":
      words = {word for word in words if guess[i] not in word}
  return words

def answers_narrow(answers, words):
  return [answer for answer in answers if answer in words]

def get_best_word(words, ranks, guess):
  best_word = ""
  best_rank = 0
  for word in words:
    rank = 0
    for i in range(5):
      rank += ranks[word[i]][str(i)]
    if rank > best_rank:
      best_rank = rank
      best_word = word
    elif rank == best_rank:
      if sum([1 for i in range(5) if word[i] == guess[i]]) < sum([1 for i in range(5) if best_word[i] == guess[i]]):
        best_word = word
  return best_word

def main(guess, state):

  # if input is invalid, return False
  if not input_verify(guess, state):
    return False

  words = helpers.read_words(words_path)
  answers = helpers.read_words(answers_path)
  ranks = json.load(open(ranks_path))

  # narrow down words based on the state
  words = words_narrow(words, state, guess)
  
  if len(words) > 20:
    print("Remaining number of words: ", len(words))
  else:
    print("Remaining words: ", words)

  # narrow down answers based on remaining words
  answers = answers_narrow(answers, words)

  if len(answers) > 20:
    print("Remaining number of answers: ", len(answers))
  else:
    print("Remaining answers: ", answers)

  # find the word with the highest rank
  best_word = get_best_word(words, ranks, guess)

  return best_word

if __name__ == "__main__":
  
  try:
    next_guess = main("dowel", "xxxxx")
  except Exception as e: 
    print(f'Error Occurred in main() function: {e}') 
    exit(1)

  if next_guess == False:
    # input_verify() will print error message
    exit(1)

  print("Best Next guess: ", next_guess)
  
  exit(0)
