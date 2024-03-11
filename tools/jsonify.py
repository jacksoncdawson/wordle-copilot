import json

words_path = "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.txt"

# reformat words.txt into a json file
def jsonify_words(words_path):
  with open(words_path, 'r') as f:
    words = f.readlines()
  words = [word.strip() for word in words]
  with open('/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.json', 'w') as f:
    json.dump(words, f)

if __name__ == "__main__":
  jsonify_words(words_path)
  exit(0)