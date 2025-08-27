import random
import time
import os

# Number of Allowed Attempts
ALLOWED_ATTEMPTS = 10

# Words List
WORDS = ["python", "programming", "computer", "algorithm", "data", "apple", "banana", "orange", "grape", "strawberry", "carrot", "tomato"]

def choose_word():
    """Choose Random Word"""
    return random.choice(WORDS)

def rules():
    """View Rules to the User"""
    print(f"""Welcome to Guess the Word! 
You have {ALLOWED_ATTEMPTS} attempts to guess the correct word.
Words are from jobs, technology, and fruits/vegetables.""")

def display_word(word, guessed_letters):
    """Display the word with the guessed letters"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    print(display)

def clear_screen():
    """Screen Wipe (Works on Windows/macOS/Linux)"""
    time.sleep(0.8)
    os.system('cls' if os.name == 'nt' else 'clear')

def guess_word():
    """The main game"""
    rules()
    word = choose_word()
    guessed_letters = set()
    attempts = 0

    while True:
        print("\nWord: ", end="")
        display_word(word, guessed_letters)

        guess = input("Enter a letter: ").lower()
        attempts += 1

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z)!!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!!")
            continue

        if guess in word:
            print("Correct guess!")
            guessed_letters.add(guess)
        else:
            print("Wrong guess!")

        clear_screen()

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word '{word}' in {attempts} attempts.")
            break
        elif attempts >= ALLOWED_ATTEMPTS:
            print(f"Game Over! You used all {ALLOWED_ATTEMPTS} attempts.")
            print(f"The correct word was: {word}")
            break

def main():
    """Play the game"""
    while True:
        guess_word()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye.")
            break
        clear_screen()

if __name__ == "__main__":
    main()
