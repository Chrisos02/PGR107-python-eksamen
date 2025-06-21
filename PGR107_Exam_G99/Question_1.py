import random
import os

# ===============================================================================
# Question 1 (25 points)
# Word guessing game
# Date: may, 2025
# Author: 21 - 363 - 287 - 41
# ===============================================================================

# ===============================================================================
# This program lets the user guess a randomly chosen word one letter at a time
# The user selects a difficulty level, which affects the word length
# The number of allowed incorrect guesses is equal to the length of the word
# A local win streak is also saved to a text file between played game sessions
# ==============================================================================

class WordGuessGame:
    # Handles a single round of the word guessing game
    def __init__(self, word_file_path, difficulty="medium"):
        self.word_list = self.load_words(word_file_path, difficulty)

        # Stop if no valid words are found
        if not self.word_list:
            raise ValueError("No valid words found for the selected difficulty.")

        # Choose a random word from the list
        self.word_to_guess = random.choice(self.word_list).lower()

        # Display with underscores for unguessed letters
        self.word_display = ['_'] * len(self.word_to_guess)

        # Set to track guessed letters
        self.guessed_letters = set()

        # Number of allowed wrong guesses = word length
        self.remaining_guesses = len(self.word_to_guess)

    def load_words(self, file_path, difficulty):
        # Reads words from a text file and filters by difficulty (word length)
        try:
            with open(file_path, 'r') as file:
                words = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print("The file words.txt was not found.")
            return []

        # Filtering the words based on difficulty chosen
        if difficulty == "easy":
            return [word for word in words if 3 <= len(word) <= 5]
        elif difficulty == "medium":
            return [word for word in words if 6 <= len(word) <= 8]
        elif difficulty == "hard":
            return [word for word in words if len(word) >= 9]
        else:
            return words

    def play(self):
        # Main gameplay loop
        print(f"\nThe word has {len(self.word_to_guess)} letters. You have {self.remaining_guesses} guesses.\n")
        print(" ".join(self.word_display))

        while self.remaining_guesses > 0 and '_' in self.word_display:
            guess = input("Guess a character: ").lower()

            # Check that the input is one alphabetical character
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single alphabetical character.\n")
                continue

            # Check if the letter has already been guessed
            if guess in self.guessed_letters:
                print("You already guessed that letter.\n")
                continue

            self.guessed_letters.add(guess)

            # If the guess is correct, update the display
            if guess in self.word_to_guess:
                for i, char in enumerate(self.word_to_guess):
                    if char == guess:
                        self.word_display[i] = guess
                print("Correct.")
            else:
                # Wrong guess will reduce remaining guesses
                self.remaining_guesses -= 1
                print("Incorrect.")

            # Showing the progress
            print(" ".join(self.word_display))
            print(f"Remaining guesses: {self.remaining_guesses}")
            print("-" * 30)

        # End of game - displaying either win or lose
        if '_' not in self.word_display:
            print(f'\nYou found the word: "{self.word_to_guess}"')
            print("Congratulations! You won the game :).\n")
            update_highscore(won=True)
        else:
            print(f'\nYou lost :( The word was: "{self.word_to_guess}"\n')
            update_highscore(won=False)

def update_highscore(won):
    # Updates the win streak to a file called highscore.txt
    file_path = "highscore.txt"
    score = 0

    # Read the current score from file (if it exists)
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                score = int(file.read().strip())
        except:
            score = 0

    # Update players score, based on game result
    if won:
        score += 1
        print(f"Current win streak: {score}")
    else:
        score = 0
        print("Win streak reset.")

    # Save updated score to file
    with open(file_path, 'w') as file:
        file.write(str(score))

def choose_difficulty():
    # Prompting the user to select a difficulty level
    while True:
        print("\n=====================")
        print(" Select difficulty:")
        print("=====================")
        print("1. Easy (3–5 letter words)")
        print("2. Medium (6–8 letter words)")
        print("3. Hard (9+ letter words)")
        choice = input("Enter choice (1-3): ")

        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid choice. Please try again.")

def show_menu():
    # Displaying the main menu
    while True:
        print("\n=====================")
        print("    MAIN MENU")
        print("=====================")
        print("1. Start New Game")
        print("2. Instructions")
        print("3. View Win Streak")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            difficulty = choose_difficulty()
            try:
                game = WordGuessGame("words.txt", difficulty)
                game.play()
            except ValueError as e:
                print("Game error:", e)
        elif choice == "2":
            # Showing instructions for the game
            print("\n=====================")
            print("    INSTRUCTIONS")
            print("=====================")
            print("A word will be randomly selected based on your difficulty choice.")
            print("You guess one letter at a time.")
            print("You lose if you use up all allowed guesses.")
            print("Your win streak is saved in highscore.txt.")
            print("---------------------\n")
        elif choice == "3":
            # Show the players current win streak
            try:
                with open("highscore.txt", "r") as file:
                    score = file.read().strip()
                    print(f"\nCurrent Win Streak: {score}")
            except:
                print("\nNo win streak found.")
        elif choice == "4":
            print("Exiting the game... \nThank you for playing.")
            break
        else:
            print("That is Invalid input. Please Try again.")

# Start the program
if __name__ == "__main__":
    show_menu()
