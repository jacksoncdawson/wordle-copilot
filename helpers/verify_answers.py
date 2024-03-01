# Verify that all answers are included in the words.txt file.

def verify_answers(wordsPath, answersPath):

  # get array of all words
  with open(wordsPath, 'r') as f:
    words = f.readlines()
  words = [word.strip() for word in words]

  # get array of all answers
  with open(answersPath, 'r') as f:
    answers = f.readlines()
  answers = [answer.strip() for answer in answers]

  # check if any answers are not in all words
  notIncluded = []
  for answer in answers:
    if answer not in words:
      notIncluded.append(answer)

  return notIncluded

if __name__ == "__main__":
  
  try:
    missingWords = verify_answers("/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/words.txt",
                                  "/Users/jackcdawson/Desktop/dev/Python Projects/wordle-copilot/Library/answers.txt")
    
    if len(missingWords) == 0:
      print('All words are included')
    else:
      print('The following words are missing:')
      print(missingWords)
  except:
    print('Error verifying words')
    exit(1)

  exit(0)