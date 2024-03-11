import json

words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.json"

words = json.load(open(words_path))

def words_narrow(words, state, guess):
  for i in range(5):
    if state[i] == "g":
      words = [word for word in words if word[i] == guess[i]]
    elif state[i] == "y":
      words = [word for word in words if (word[i] != guess[i]) and (guess[i] in word)]
    elif state[i] == "x":
      # if the letter has not been seen in a "g" or "y" position, remove all words with that letter
      if not any(guess[i] == guess[j] and state[j] in ["g", "y"] for j in range(5)):
        words = [word for word in words if guess[i] not in word]
      else:
        # if the letter has been seen in a "g" or "y" position, remove all words with that letter in the same position
        words = [word for word in words if guess[i] != word[i]]
  return words

# given a word (e.g. "weary") and state (e.g. "xxxxx"), what is the probability of the word being in that state (all things being equal)
# given the above example, there will be 2102 possible words remaining
# the probability of the word being in that state is 2102 / 14855 = 0.1415
def prob_of_state(word, state):
  remaining_words = words_narrow(words, state, word)
  return (len(remaining_words) / len(words)), remaining_words

if __name__ == "__main__":
  
  prob, remaining = prob_of_state("weary", "xxxxx")
  print(prob)
  print(len(remaining))
  print(len(words))
