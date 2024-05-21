# Number Guessing Game

This is a simple number guessing game implemented in Python. The game prompts the user to specify a range, selects a random number within that range, and then challenges the user to guess the number. The game provides hints if the guess is too high or too low and tracks the number of guesses and the time taken to guess correctly.

## How to Play

1. **Start the Game:**
   - Run the script.
   - You will be asked to enter the upper limit for the range of numbers (e.g., if you enter 10, the game will choose a random number between 1 and 10).

2. **Guess the Number:**
   - The game will prompt you to guess the randomly chosen number.
   - After each guess, the game will provide feedback:
     - If the guess is too high, it will tell you that the number is less.
     - If the guess is too low, it will tell you that the number is greater.

3. **Winning the Game:**
   - Once you guess the correct number, the game will display:
     - The correct number.
     - The total number of guesses.
     - The time taken to guess the number correctly.
   - The game will then end.

## Example Gameplay

- How many numbers do you want to include: 10
   - A random number has been chosen between 1 and 10. Try to guess it!
- Guess the number: 5
   -The number is greater than 5
- Guess the number: 8
   - The number is less than 8
- Guess the number: 7
   - The number is less than 7
- Guess the number: 6
   - You guessed correct! 6 was the right number! You guessed 4 times in 12.34 seconds 🤖
