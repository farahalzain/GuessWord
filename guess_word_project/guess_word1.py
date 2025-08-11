import random
def choose_word():
    words = ["python", "programming", "computer", "algorithm", "data"]

def display_word(word, guessed_letter):
    display = ""
    for letter in word:
        if letter in guessed_letter:
            display += letter
        else:
            display += "_"
    return display


def guess_word(word):
    guessed_letters = set()  #users trails of guessing
    attempts = 0 # start with 0 trail
    print("Welcome to the word guessing game! Words are jobs and technology")
    while True:
        print(f"\n Word: {display_word(word, guessed_letters)}")
        user_guess = input("Guess a letter: ").lower()
        attempts += 1

        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please enter a single letter.")
            continue

        if user_guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if user_guess in word:
            print("Good guess!")
            guessed_letters.add(user_guess)
        else:
            print("Incorrect guesss. Try again.")

        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word {word} in {attempts} attempts.")
            break
        


def main():
    word = choose_word()
    guess_word(word)
