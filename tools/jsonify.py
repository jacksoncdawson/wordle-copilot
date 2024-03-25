import json

file_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/possible_words.txt"

def jsonify_words(file_path):
  with open(file_path, 'r') as f:
    words = f.readlines()
  words = [word.strip() for word in words]
  with open('/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/solutions.json', 'w') as f:
    json.dump(words, f)

if __name__ == "__main__":

  jsonify_words(file_path)
  exit(0)