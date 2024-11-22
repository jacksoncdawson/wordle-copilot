# Wordle Copilot

Wordle Copilot is a Python-based project developed to explore and replicate some functionalities of the New York Times' Wordle bot. Over the course of a month, this project aimed to understand the underlying mechanics of Wordle by creating tools that suggest optimal guesses and analyze the effectiveness of initial guesses.

## Features

- **Guess Assistance**: The `wordle_copilot.py` script allows users to input their guesses along with the feedback from the game (correct positions and letters). Based on this information, it suggests the next best guess to help solve the puzzle.

- **Probability Analysis**: The `probability.py` script calculates the Probability Mass Function (PMF) for a given word using the Wordle dictionary. It generates a graph that illustrates the expected effectiveness of a particular starting guess.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/jacksoncdawson/wordle-copilot.git
   cd wordle-copilot
   ```

2. **Install Dependencies**:

   You don't need to worry about dependencies. Selenium was only used initially to scrape a Wordle dictionary that isn't actually used.

## Usage

### Guess Assistance

To use the guess assistance feature:

```bash
python3 main/wordle_copilot.py
```

Follow the on-screen prompts to input your guess and the feedback from the game. The script will suggest the next best guess based on the provided information.

### Probability Analysis

To analyze the effectiveness of a specific starting word, you will need to edit `probability.py` to set the word you want to evaluate. After editing the script:

```bash
python3 main/probability.py
```

The script will calculate the PMF for the given word and display a graph showing its expected effectiveness as a starting guess.

## Project Structure

The repository contains the following files and directories:

- **`main/wordle_copilot.py`**: Main script for assisting with Wordle guesses based on user input and game feedback.

- **`main/probability.py`**: Script for calculating and graphing the Probability Mass Function of a given word using the Wordle dictionary.

- **`main/testing.py`**: Script for testing different functionalities during development.

- **`requirements.txt`**: List of Python dependencies required to run the scripts.

- **`.gitignore`**: Specifies files and directories to be ignored by Git.

- **`.gitattributes`**: Defines attributes for path-specific settings in Git.

- **`README.md`**: This document, providing an overview of the project.

- **`/Library`**: Directory containing helper modules, JSON data files, and functions used by the main scripts.

  - **`__init__.py`**: Initializes the Library module.
  - **`entropy.py`**: Contains functions for calculating the entropy of word guesses, aiding in determining the most informative guesses.
  - **`wordlist.py`**: Manages the list of possible Wordle words and provides functions to filter and process them based on game feedback.
  - **`entropy.json`**: JSON file storing precomputed entropy values for different words.
  - **`ranks.json`**: JSON file storing word rankings based on their effectiveness.
  - **`solutions.json`**: JSON file containing possible solutions for Wordle.
  - **`states.json`**: JSON file managing various game states for use in analysis.
  - **`test_words.json`**: JSON file containing a set of test words for validation purposes.
  - **`words.json`**: JSON file containing the entire list of possible Wordle words.

- **`/tools`**: Directory containing additional tools and scripts for data processing and analysis.

  - **`answers_scrape.py`**: Script for scraping possible Wordle answers from external sources.
  - **`answers_verify.py`**: Script for verifying the validity of scraped answers.
  - **`helpers_tools.py`**: Helper functions used across various scripts for additional processing.
  - **`jsonify.py`**: Script for converting raw data into JSON format for use in other scripts.
  - **`ranks.py`**: Script for generating and managing word rankings.
  - **`states.py`**: Script for handling game state information during analysis.
  - **`entropy_function.py`**: Script for analyzing the entropy function of word guesses.
  - **`new_wordset.py`**: Script for generating and processing new sets of possible Wordle words.

## Future Enhancements

Planned improvements for the project include:

- **Integration**: Merging the functionalities of `wordle_copilot.py` and `probability.py` to provide a comprehensive tool for Wordle analysis and assistance.

- **User Interface**: Developing a more user-friendly interface to enhance the user experience.

- **Algorithm Optimization**: Improving the underlying algorithms to provide more accurate and efficient suggestions.

