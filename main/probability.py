import json
import plotly.express as px
import math

words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.json"
states_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/states.json"

test_words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/test_words.json"

words = json.load(open(words_path))
states = json.load(open(states_path))

# new edit
def words_narrow(words: list[str], state: str, guess: str) -> list[str]:

  letter_count = {}
  green = {}
  yellow = {}

  for i in range(5):
    if guess[i] not in letter_count:
      letter_count[guess[i]] = 0

  # lock-in greens
  for i in range(5):
    if state[i] == "g":

      letter_count[guess[i]] += 1

      # update green dict
      if guess[i] in green:
        green[guess[i]].append(i)
      else:
        green[guess[i]] = [i] # e.g. green = {"e": [4]}

      words = [word for word in words if word[i] == guess[i]]
  
  # lock-out yellows
  for i in range(5):
    if state[i] == "y":

      letter_count[guess[i]] += 1

      # update yellow dict
      if guess[i] in yellow:
        yellow[guess[i]].append(i)
      else:
        yellow[guess[i]] = [i] # e.g. yellow = {"s": [0]}

      words = [word for word in words if (word[i] != guess[i]) and (guess[i] in word)]

  # handle greys
  for i in range(5):
    if state[i] == "x":
      if guess[i] in green: 
        # remove all words with the letter in every position except the green positions
        words = [word for word in words if all((word[j] != guess[i]) or (j in green[guess[i]]) for j in range(5))]
      elif guess[i] in yellow: 
        # remove all words with the letter in the current position
        words = [word for word in words if word[i] != guess[i]]
      else:
        # remove all words with the letter in any position
        words = [word for word in words if guess[i] not in word]

  # remove any words left that have less than or more than the recorded count of each letter
  for letter in letter_count:
    words = [word for word in words if word.count(letter) >= letter_count[letter]]

  return words

def prob_of_state(word: str, state: str) -> float:
  remaining_words = words_narrow(words, state, word)
  return (len(remaining_words) / len(words))

def pmf_of_word(word: str) -> list[tuple]:
  state_probabilities = []

  for state in states:
    prob = prob_of_state(word, state)
    state_probabilities.append((state, prob))
  
  # Sort states and probabilities together based on probabilities in descending order
  state_probabilities_sorted = sorted(state_probabilities, key=lambda x: x[1], reverse=True)

  return state_probabilities_sorted

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

def entropy(word: str) -> float:

  # get pmf of word as a list of tuples
  state_probabilities = pmf_of_word(word)

  # calculate entropy
  expected_info = sum([-prob * math.log2(prob) for state, prob in state_probabilities if prob > 0])

  return expected_info

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


# tooling
def avg_remaining_words(word: str) -> float:

  avg_remaining = 0
  for state in states:
    avg_remaining += len(words_narrow(words, state, word))
  
  return avg_remaining / 243

if __name__ == "__main__":

  word = "salon"

  print(entropy(word))

  print(avg_remaining_words(word))

  remaining = words_narrow(words, "gggxx", word)
  print(remaining)


  
