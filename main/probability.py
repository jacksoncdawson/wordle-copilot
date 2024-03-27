import json
import plotly.express as px
import math

# DATA 

words = json.load(open("/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.json"))
states = json.load(open("/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/states.json"))
entropy_data = json.load(open('/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/naive-entropy.json'))


# HELPER FUNCTIONS

def pmf_graph(word: str, pmf: list[tuple]) -> None:
  '''Graphs the probability mass distribution of a word as a function of state.'''

  sorted_states, sorted_probabilities = zip(*pmf)

  fig = px.bar(x=sorted_states, 
               y=sorted_probabilities, 
               labels={'x': 'State', 'y': 'Probability'},
               title=f'Probability Mass Distribution for "{word}" as a function of state')

  fig.update_traces(marker_color='lightblue', hoverinfo='x+y')

  fig.update_xaxes(showticklabels=False)

  fig.show()

  return

def collect_entropy_data() -> None:
  '''Collects entropy data for all words in the words list and saves it to a json file.'''

  entropy_data = {}
  count = 0

  for word in words:
    entropy_data[word] = entropy(word)

    count += 1
    print(f"completed {count} of 12953 ({round(count/12953 * 100, 2)}%)")

  with open('/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/naive-entropy.json', 'w') as f:
    json.dump(entropy_data, f)

  return

def words_narrow(words: list[str], state: str, guess: str) -> list[str]:
  '''Returns a list of remaining words in accordance with the state and guess.'''

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
        green[guess[i]] = [i] 

      # update words list
      words = [word for word in words if word[i] == guess[i]]
  
  # lock-out yellows
  for i in range(5):
    if state[i] == "y":

      letter_count[guess[i]] += 1

      # update yellow dict
      if guess[i] in yellow:
        yellow[guess[i]].append(i)
      else:
        yellow[guess[i]] = [i] 

      # update words list
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

  # remove any words left that have less than the recorded count of each letter
  for letter in letter_count:
    words = [word for word in words if word.count(letter) >= letter_count[letter]]

  return words

def top_n_words(n: int) -> list[str]:
  '''Returns the top n words based on entropy.'''

  sorted_words = sorted(entropy_data.items(), key=lambda x: x[1], reverse=True)

  print(f"Top {n} words based on entropy:")
  for word in sorted_words[:n]:
    print(f"{word[0]}: {word[1]}")

  return sorted_words[:n]

# PROBABILITY FUNCTIONS

def prob_of_state(word: str, state: str) -> float:
  remaining_words = words_narrow(words, state, word)
  return (len(remaining_words) / len(words))

def pmf_get(word: str) -> list[tuple]:

  state_probabilities = []

  for state in states:
    invalid_state = False
    seen = set()
    
    for i in range(5):
      if (word[i] in seen) and (state[i] == "y"):
        invalid_state = True
        break
      else:
        seen.add(word[i])

    if invalid_state:
      continue
    else:
      prob = prob_of_state(word, state)
      state_probabilities.append((state, prob))
  
  # Sort states and probabilities together based on probabilities in descending order
  state_probabilities_sorted = sorted(state_probabilities, key=lambda x: x[1], reverse=True)

  return state_probabilities_sorted

def entropy(word: str) -> float:

  # get pmf of word as a list of tuples
  state_probabilities = pmf_get(word)

  # calculate entropy
  expected_info = sum([-prob * math.log2(prob) for _, prob in state_probabilities if prob > 0])

  return expected_info


if __name__ == "__main__":

  top_n_words(10)



  
