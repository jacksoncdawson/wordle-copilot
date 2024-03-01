# use selenium to get the answer key from https://www.wordunscrambler.net/word-list/wordle-word-list
# and save it to a file: "answers.txt"

from selenium import webdriver;
from selenium.webdriver.common.by import By

def getWords():
  # open the website
  driver = webdriver.Chrome()
  driver.get('https://www.wordunscrambler.net/word-list/wordle-word-list')

  # get the words
  words = driver.find_elements(By.XPATH, '//li[@class="invert light"]/a')

  # save the words to a file
  for word in words:
    with open('answers.txt', 'a') as f:
      f.write(word.text + '\n')

  # close the browser and return
  driver.quit()
  return

if __name__ == "__main__":
 
  try:
    words = getWords()
  except:
    print('Error getting words')
    exit(1)

  print('Words saved to answers.txt')
  exit(0)
