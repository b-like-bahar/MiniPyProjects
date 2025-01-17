# Python Mini Projects Collection

This repository contains a diverse collection of Python mini-projects, including games, utilities, and experiments. These projects range from simple console-based programs to more advanced graphical applications built using Tkinter. The purpose of this repository is to demonstrate my Python programming skills, explore various libraries and concepts, and provide an engaging way for others to learn and experiment with Python. With every project, I aim to challenge myself and expand my knowledge of the language.

## Projects Overview

1. **CalculatorApp**
   - A simple calculator application built in Python.

2. **Guess a Number**
   - A fun game where the user or the computer guesses a number.

3. **Hangman**
   - A classic word-guessing game.

4. **Madlib**
   - A program to create your own Madlib stories.

5. **Rock Paper Scissors**
   - A Python implementation of the classic Rock, Paper, Scissors game.

6. **SnakeGame**
   - A graphical Snake game using Python.

7. **TicTacToe**
   - A graphical Tic Tac Toe game built with Tkinter.

## Purpose

This repository serves as a showcase of my Python programming journey, reflecting my growth as a developer. Through these projects, I aim to:
- Explore and utilize Python's vast libraries and tools.
- Gain hands-on experience with GUI development using Tkinter.
- Build logical and creative problem-solving skills.
- Share interesting and interactive projects for others to use and learn from.

## Instructions for Each Project

Each project folder contains the necessary code files. Some projects are console-based, while others include graphical visualizations. Instructions on how to run each project are provided below:

- **CalculatorApp:** Run `Calculator.py` to start the calculator application. This project uses Tkinter for a graphical user interface. The calculator supports basic operations (addition, subtraction, multiplication, division) and advanced features such as square root (`√`), pi (`π`), power (`^`), and parentheses. Use the following buttons:
  - **Numbers (0-9):** Click to input digits.
  - **Operators:** Perform operations like `+`, `-`, `*`, `/`, `%`, and more.
  - **AC (All Clear):** Clear the entire input field.
  - **<-- (Delete):** Remove the last entered character.
  - **= (Equals):** Calculate the entered expression.
  - **Advanced:** Use `√` for square root, `π` for pi, and `^` for power.

- **Guess a Number:**
  - Run `GAN_Computer.py` to let the computer pick a random number between 1 and 20. You, as the player, guess the number with hints provided after each guess (too high or too low) until you find the correct number.
  - Run `GAN_User.py` to reverse the roles. Here, you think of a number between 1 and 1000, and the computer tries to guess it based on your feedback: "H" (too high), "L" (too low), or "C" (correct). The program uses a binary search-like strategy to minimize the number of guesses.

- **Hangman:** Run `hangman.py` to play the Hangman game. This game selects a random word from the `words.py` file. You have 7 lives to guess the word correctly. Gameplay features include:
  - Input validation to ensure valid guesses.
  - Tracking and displaying letters used so far.
  - Revealing correct guesses in the word while hiding the remaining letters with dashes (`-`).
  - A live counter to display remaining lives.
  - A congratulatory message when you win or the correct word if you lose.

- **Madlib:** Run `main.py` to play the Madlib game. This project offers five different templates: Adventure, Party, Mystery, Superhero Story, and Robot. Steps to play:
  - Select a template by entering its number (1-5) when prompted.
  - Provide inputs for placeholders in the template, such as adjectives, nouns, and verbs, as requested.
  - The program will generate a completed story based on your inputs.

  The template definitions are stored in `SampleMadlibs.py`. Examples of templates include:
  - **Adventure:** A story about a brave character on an exciting journey through forests and castles.
  - **Party:** A lively event featuring music, food, and unexpected surprises.
  - **Mystery:** A detective story set in a mysterious location with intriguing clues.
  - **Superhero Story:** A tale of heroism and saving the day with superpowers.
  - **Robot:** A futuristic story about a robot seeking freedom and adventure.

- **Rock Paper Scissors:** Run `RPS.py` to play the game. Features include:
  - Choose the number of turns to play.
  - Play by entering "r" (rock), "p" (paper), or "s" (scissors).
  - Compete against the computer, which randomly selects its move.
  - The winner of each round is determined based on standard Rock-Paper-Scissors rules:
    - Rock beats Scissors.
    - Scissors beats Paper.
    - Paper beats Rock.
  - Track scores for both the user and the computer.
  - Displays the final winner after all turns are played or if it results in a tie.

- **SnakeGame:** Run `snakegame.py` to play the graphical Snake game. Features include:
  - Use arrow keys to control the snake's movement.
  - Collect food to grow the snake and increase the score.
  - Avoid collisions with the walls or the snake's own body.
  - Displays a "Game Over" screen with the final score when the game ends.
  - Includes a restart button to play again.

- **TicTacToe:** Run `tictactoe.py` to play the graphical Tic Tac Toe game. Features include:
  - Play as "X" or "O" against another player.
  - The game announces the winner or a tie when the match ends.
  - Highlights the winning row, column, or diagonal in yellow.
  - Includes a "Restart" button to reset the game and play again.

## How to Run

1. Clone this repository using:
   ```bash
   git clone https://github.com/b-like-bahar/MiniPyProjects.git
   ```
2. Navigate to the project folder of your choice.
3. Run the corresponding Python file using:
   ```bash
   python <filename.py>
   ```

## Future Plans

This repository is a work in progress. I plan to:
- Add more projects as I explore new ideas and concepts.
- Improve existing projects based on feedback and further learning.
- Include detailed documentation and instructions for all projects.

Feel free to explore, contribute, or share feedback on this repository!
