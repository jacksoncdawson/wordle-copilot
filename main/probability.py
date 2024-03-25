import json
import plotly.express as px
import math

words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.json"
states_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/states.json"

test_words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/test_words.json"

words = json.load(open(words_path))
states = json.load(open(states_path))

def words_narrow(words: list[str], state: str, guess: str) -> list[str]:

  letter_count = {}

  for i in range(5):

    if guess[i] not in letter_count:
      letter_count[guess[i]] = 0

    if state[i] == "g":
      letter_count[guess[i]] += 1
      words = [word for word in words if word[i] == guess[i]]
    elif state[i] == "y":
      letter_count[guess[i]] += 1
      words = [word for word in words if (word[i] != guess[i]) and (guess[i] in word)] 
    elif state[i] == "x":
      # if the letter has not been seen in a "g" or "y" position, remove all words with that letter
      if not any(guess[i] == guess[j] and state[j] in ["g", "y"] for j in range(5)):
        words = [word for word in words if guess[i] not in word]
      else:
        # if the letter has been seen in a "g" or "y" position, remove all words with that letter in the same position
        words = [word for word in words if guess[i] != word[i]]

  # remove any words left that have less than the recorded count of each letter
  for letter in letter_count:
    words = [word for word in words if word.count(letter) >= letter_count[letter]]

  return words

# given a word (e.g. "weary") and state (e.g. "xxxxx"): returns the probability of the word having that state (assuming all words are equally likely)
def prob_of_state(word: str, state: str) -> float:
  remaining_words = words_narrow(words, state, word)
  return (len(remaining_words) / len(words))

# given a word (e.g. "weary"): returns a list of tuples of the form (state, probability) sorted by probability in descending order
def pmf_of_word(word: str) -> list[tuple]:
  state_probabilities = []

  for state in states:
    prob = prob_of_state(word, state)
    state_probabilities.append((state, prob))
  
  # Sort states and probabilities together based on probabilities in descending order
  state_probabilities_sorted = sorted(state_probabilities, key=lambda x: x[1], reverse=True)

  return state_probabilities_sorted

# given a word (e.g. "weary"): graphs a bar chart of the probability mass distribution of the word as a function of state using plotly
def graph_pmf(word: str) -> None:

  # get pmf of word as a list of tuples
  state_probabilities = pmf_of_word(word)

  # unzip sorted data into separate lists
  sorted_states, sorted_probabilities = zip(*state_probabilities)

  # Create bar chart
  fig = px.bar(x=sorted_states, 
               y=sorted_probabilities, 
               labels={'x': 'State', 'y': 'Probability'},
               title=f'Probability Mass Distribution for "{word}" as a function of state')

  fig.update_traces(marker_color='lightblue', hoverinfo='x+y')

  fig.update_xaxes(showticklabels=False)

  fig.show()

  return

# given a word (e.g. "weary"): returns the entropy of the word
def entropy(word: str) -> float:

  # get pmf of word as a list of tuples
  state_probabilities = pmf_of_word(word)

  expected_info = 0

  # calculate entropy
  for state, prob in state_probabilities:
    if prob > 0:
      information = -math.log2(prob)
      expected_info += prob * information

  return expected_info

# collects naive 1st guess entropy data for all words in the library
def collect_entropy_data() -> None:

  entropy_data = {}
  count = 0

  for word in words:
    # add entropy data to dictionary
    entropy_data[word] = entropy(word)

    # print progress
    count += 1
    print(f"completed {count} of 12953 ({round(count/12953 * 100, 2)}%)")

  with open('/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/naive-entropy.json', 'w') as f:
    json.dump(entropy_data, f)

  return

if __name__ == "__main__":

  # word = "tares"
  # graph_pmf(word)
  # print(word, entropy(word))

  collect_entropy_data()