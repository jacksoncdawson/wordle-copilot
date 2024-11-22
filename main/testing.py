import probability as prob
import json

# DATA

words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.json"
test_words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/test_words.json"

states_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/states.json"

words = json.load(open(words_path))
test_words = json.load(open(test_words_path))
states = json.load(open(states_path))


# TESTING FUNCTIONS

def test_entropy(word: str) -> None:

  print(f"Entropy of {word}: {round(prob.entropy(word), 3)}")

  return

def test_words_narrow(words: list[str], word: str, state: str) -> None:
  
  remaining = prob.words_narrow(words, state, word)
  len_remaining = len(remaining) 
  
  print(f"Remaining word count: {len_remaining}")
  if len_remaining < 30:
    print(f"Remaining words: {remaining}")

  return

def test_pmf_get(word: str) -> None:

  pmf = prob.pmf_get(word)
  prob.pmf_graph(word, pmf)

  print(f"PMF of {word} calculated for {len(pmf)} states.")

  return

def test_all(words: list[str], word: str, state: str) -> None:

  # clear screen
  print("\033[H\033[J", end="")

  # run tests
  test_entropy(word)
  test_words_narrow(words, word, state)
  # test_pmf_get(word)

  return

if __name__ == "__main__":

  word = "eeeee"
  state = "xxxxx"

  test_all(words, word, state)
