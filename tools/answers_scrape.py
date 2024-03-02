# use selenium to get the answer key from https://www.wordunscrambler.net/word-list/wordle-word-list
# and save it to a file: "answers.txt"

from selenium import webdriver;
from selenium.webdriver.common.by import By

def answers_scrape():
  # open the website
  driver = webdriver.Chrome()
  driver.get('https://www.wordunscrambler.net/word-list/wordle-word-list')

  # get the words
  answers = driver.find_elements(By.XPATH, '//li[@class="invert light"]/a')

  # check if all words are there
  if len(answers) < 2309:
    return None

  # save the words to a file
  for word in answers:
    with open('answers.txt', 'a') as f:
      f.write(word.text + '\n')

  # close the browser and return
  driver.quit()
  return answers

if __name__ == "__main__":

  try:
    answers = answers_scrape()
  except:
    print('Error getting words')
    exit(1)

  if answers == None:
    print('Error: Did not get all answers')   
    exit(1)

  print('Words saved to answers.txt')
  exit(0)
