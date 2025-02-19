# Word Guess Game

This is a simple word guessing game built using Django. The game randomly selects a word from a predefined list and allows the player to guess letters until the full word is revealed. The player wins when all the correct letters have been guessed.

## Features
- A random word is selected from a list of words.
- The player guesses letters to reveal the hidden word.
- A congratulations message with a trumpet sound is played when the player wins.
- The game automatically resets with a new word after a win.

## Installation

1. Clone this repository or download the source code.
2. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

 

3. Open the game in your browser by visiting [http://127.0.0.1:8000](http://127.0.0.1:8000).

## How to Play

1. A word will be displayed with hidden letters represented by underscores (`_`).
2. Enter a letter in the input field and click "Guess" or press the "Enter" key.
3. If the letter is correct, it will be revealed in the word display.
4. If the letter is incorrect, it will not change, and you can try again.
5. Once the player guesses all letters correctly, the game will display a win message, and a trumpet sound will be played.
6. A new word will be generated after the game ends.

