# About: Confirms that the scraped answers are included in the words.txt file.
# Not used in the main program.

import helpers_tools

# Verify that all answers are included in the words.txt file.
def answers_verify(path_words, path_answers):

  words = helpers_tools.read_words(path_words)

  # get array of all answers
  with open(path_answers, 'r') as f:
    answers = f.readlines()
  answers = [answer.strip() for answer in answers]

  # check if any answers are not in all words
  not_included = []
  for answer in answers:
    if answer not in words:
      not_included.append(answer)

  return not_included

if __name__ == "__main__":
  
  try:
    missing_words = answers_verify("/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.txt",
                                   "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/answers.txt")
    
    if len(missing_words) == 0:
      print('All words are included')
    else:
      print('The following words are missing:')
      print(missing_words)
  except:
    print('Error verifying words')
    exit(1)

  exit(0)